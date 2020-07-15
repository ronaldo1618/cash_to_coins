piggyBank = {
    "pennies": 0,
    "nickels": 0,
    "dimes": 0,
    "quarters": 0
}

def convert_to_coins(dollar_amount):
    amount = dollar_amount
    piggyBank["quarters"] = int((amount / 25) * 100)
    amount %= .25
    piggyBank["dimes"] = int((amount / 10) * 100)
    amount %= .10
    piggyBank["nickels"] = int((amount / 5) * 100)
    amount %= .05
    piggyBank["pennies"] = round(amount * 100)
    return print(piggyBank)

convert_to_coins(108.69)