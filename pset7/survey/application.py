import cs50
import csv

from flask import Flask, jsonify, redirect, render_template, request

# Configure application
app = Flask(__name__)

# Reload templates when they are changed
app.config["TEMPLATES_AUTO_RELOAD"] = True


@app.after_request
def after_request(response):
    """Disable caching"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


@app.route("/", methods=["GET"])
def get_index():
    return redirect("/form")


@app.route("/form", methods=["GET"])
def get_form():
    return render_template("form.html")


@app.route("/form", methods=["POST"])
def post_form():
    # data got from the form submitted.
    data = request.form.to_dict()

    # if form data not present.
    if not data:
        return render_template("error.html", message="Form data not complete.")

    # open csvfile and write to it taking fieldnames as keys and data as values.
    with open('survey.csv', 'a', newline='') as csvfile:
        fieldnames = ['Name', 'DOB', 'Gender', 'Django', 'Flask', 'Pyramid', 'Web2py', 'Continent', 'Fav_color', 'Sleep']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames, restval='0')

        writer.writerow(data)

    return redirect("/sheet")


@app.route("/sheet", methods=["GET"])
def get_sheet():

    # open csvfile to read the data in order to be rendered.
    with open('survey.csv', newline='') as csvfile:
        reader = csv.reader(csvfile)
        data = tuple(reader)

    return render_template("sheet.html", header=data[0], rows=data[1:])