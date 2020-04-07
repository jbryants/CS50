import os

from cs50 import SQL
from flask import Flask, flash, jsonify, redirect, render_template, request, session
from flask_session import Session
from tempfile import mkdtemp
from werkzeug.exceptions import default_exceptions, HTTPException, InternalServerError
from werkzeug.security import check_password_hash, generate_password_hash

from helpers import apology, login_required, lookup, usd

# Configure application
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

# Ensure responses aren't cached
@app.after_request
def after_request(response):
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response

# Custom filter
app.jinja_env.filters["usd"] = usd

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_FILE_DIR"] = mkdtemp()
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///finance.db")

# Make sure API key is set
if not os.environ.get("API_KEY"):
    raise RuntimeError("API_KEY not set")


@app.route("/")
@login_required
def index():
    """Show portfolio of stocks"""

    # read symbol, name and shares owned
    rows = db.execute("""
                    SELECT symbol, name, SUM(shares) as shares
                    FROM portfolio
                    WHERE username = :session_user
                    GROUP BY symbol
                    HAVING SUM(shares) > 0
                    """,
                    session_user=session["username"])

    # cash currently owned
    cash = db.execute("SELECT cash FROM users WHERE id = :user_id", user_id=session["user_id"])[0]["cash"]

    # grand total after all transactions so far.
    total = cash

    for row in rows:
        # looking up current price
        row['price'] = lookup(row['symbol'])['price']
        # total price as per current rate and shares owned
        row['total'] = row['price'] * row['shares']
        # stocks' total value plus cash
        total += row['total']

    return render_template("index.html", rows=rows, cash=cash, total=total)


@app.route("/buy", methods=["GET", "POST"])
@login_required
def buy():
    """Buy shares of stock"""
    if request.method == "POST":
        # Ensure symbol was submitted
        if not request.form.get("symbol"):
            return apology("missing symbol", 400)

        # Ensure shares was submitted
        elif not request.form.get("shares"):
            return apology("missing shares", 400)

        # Ensure shares is positive integer
        try:
            if not int(request.form.get("shares")) > 0:
                return apology("shares must be a positive integer", 400)
        except ValueError:
            return apology("shares must be a positive integer", 400)

        response = lookup(request.form.get("symbol"))
        # proceed if valid response is obtained.
        if response:
            # check if enough cash to buy
            # indexing at 0 to select the element in list and key indexing to get value.
            cash = db.execute("SELECT cash FROM users WHERE id = :user_id", user_id=session["user_id"])[0]["cash"]

            # balance amount
            bal = cash - (response["price"] * float(request.form.get("shares")))
            if bal < 0:
                return apology("can't afford", 400)
            else:
                # update cash in users table
                db.execute("UPDATE users SET cash = :bal WHERE id = :user_id", bal=bal, user_id=session["user_id"])
                # insert new transaction record for user
                db.execute("""
                           INSERT INTO portfolio
                           (username, symbol, name, shares, price)
                           VALUES (:username, :symbol, :name, :shares, :price)
                           """,
                           username=session["username"], symbol=response["symbol"], \
                           name=response["name"], shares=request.form.get("shares"), \
                           price=response["price"])
                flash("Bought!")
                return redirect("/")
        else:
            return apology("invalid symbol", 400)

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("buy.html")


@app.route("/check", methods=["GET"])
def check():
    """Return true if username available, else false, in JSON format"""
    print(request.args)
    print(request.args.get('username'))

    # Query database for username
    rows = db.execute("SELECT * FROM users WHERE username = :username",
                          username=request.args.get("username"))

    # Ensure username is available
    if len(rows) == 1:
        return jsonify(False)
    else:
        return jsonify(True)


@app.route("/history")
@login_required
def history():
    """Show history of transactions"""
    rows = db.execute("SELECT symbol, shares, price, datetime FROM portfolio WHERE username = :session_user", session_user=session["username"])

    return render_template("history.html", rows=rows)


@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username", 403)

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password", 403)

        # Query database for username
        rows = db.execute("SELECT * FROM users WHERE username = :username",
                          username=request.form.get("username"))

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(rows[0]["hash"], request.form.get("password")):
            return apology("invalid username and/or password", 403)

        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]
        session["username"] = rows[0]["username"]

        # Redirect user to home page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html")


@app.route("/logout")
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/")


@app.route("/quote", methods=["GET", "POST"])
@login_required
def quote():
    """Get stock quote."""

    if request.method == "POST":
        # Ensure symbol was submitted
        if request.form.get("symbol"):
            response = lookup(request.form.get("symbol"))
            # rendering the response dict data if symbol was valid
            if response:
                return render_template("quoted.html", data=response)
            else:
                return apology("invalid symbol", 400)
        else:
            return apology("missing symbol", 400)
    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("quote.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user"""

    if request.method == "POST":

        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username", 400)

        # Ensure password was submitted
        elif not request.form.get("password") or not request.form.get("confirmation"):
            return apology("must provide password and confirmation", 400)

        # Ensure passwords match
        elif request.form.get("password") != request.form.get("confirmation"):
            return apology("passwords don't match", 400)

        # Query database for username
        rows = db.execute("SELECT * FROM users WHERE username = :username",
                          username=request.form.get("username"))

        # Ensure username is available
        if len(rows) == 1:
            return apology("Username is not available", 400)

        # Insert query on database to register user
        rows = db.execute("""
                           INSERT INTO users(username, hash)
                           values(:username, :hash_val)
                           """,
                           username=request.form.get("username"),
                           hash_val=generate_password_hash(request.form.get("password"))
                           )

        # Query database for username
        rows = db.execute("SELECT * FROM users WHERE username = :username",
                          username=request.form.get("username"))

        # Ensure username exists and password is correct
        if len(rows) == 1:
            # Remember which user has logged in
            session["user_id"] = rows[0]["id"]
            session["username"] = rows[0]["username"]
        else:
            return apology("Unable to register user, please try again.", 400)

        flash("Registered!")
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("register.html")


@app.route("/sell", methods=["GET", "POST"])
@login_required
def sell():
    """Sell shares of stock"""

    if request.method == "POST":
        # fetch sum of shares for given symbol.
        rows = db.execute("""
                    SELECT SUM(shares) as shares_owned
                    FROM portfolio
                    WHERE username = :session_user
                    GROUP BY symbol
                    HAVING symbol = :symbol""",
                    session_user=session["username"], symbol=request.form.get("symbol"))

        # index list and obtain shares owned
        shares_owned = rows[0]['shares_owned']

        # Ensure symbol was submitted
        if not request.form.get('symbol'):
            return apology('missing symbol', 400)

        # Ensure shares was submitted
        if not request.form.get('shares'):
            return apology('missing shares', 400)

        shares = int(request.form.get('shares'))

        # Ensure shares submitted is a positive int
        if not shares > 0:
            return apology('shares must be positive', 400)

        # Ensure shares submitted is not more than shares owned
        if shares > shares_owned:
            return apology('too many shares', 400)

        response = lookup(request.form.get("symbol"))

        # update cash of user for the shares sold.
        db.execute("""
                    UPDATE users
                    SET cash = cash + (:price * :shares)
                    WHERE id = :user_id
                    """,
                    price=response["price"],
                    shares=shares,
                    user_id=session["user_id"])

        # insert new transaction record for user
        db.execute("""
                   INSERT INTO portfolio
                   (username, symbol, name, shares, price)
                   VALUES (:username, :symbol, :name, :shares, :price)
                   """,
                   username=session["username"], symbol=response["symbol"], \
                   name=response["name"], shares=(-shares), \
                   price=response["price"])

        flash("Sold!")
        return redirect("/")
    else:
        rows = db.execute("SELECT DISTINCT symbol FROM portfolio WHERE username = :session_user", session_user=session["username"])
        return render_template("sell.html", rows=rows)


def errorhandler(e):
    """Handle error"""
    if not isinstance(e, HTTPException):
        e = InternalServerError()
    return apology(e.name, e.code)


# Listen for errors
for code in default_exceptions:
    app.errorhandler(code)(errorhandler)
