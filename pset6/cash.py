# import cs50

def main():
    while True:
        # dollars = get_float("Change owed: ")
        dollars = float(input("Change owed: "))
        if dollars > 0:
            break
        
    cents = round(dollars * 100)
    print(get_coins(cents))

def get_coins(cents):
    coins = 0
    denom = {25, 10, 5, 1}

    for d in denom:
        # integer division
        coins += (cents // d)
        # mod operation to return remainder
        cents %= d
    
    return int(coins)

if __name__ == '__main__':
    main()