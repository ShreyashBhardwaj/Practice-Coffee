MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

money=0
#penny = 1 cent = 0.01
#nickel = 5 cent = 0.05
#dime = 10 cent = 0.1
#quarter = 25 cent = 0.25
# coffee in grams and water and milk in ml

#Done TODO:1. Print Report when the user types "report" showcases all the resources it has
#TODO:2. Check if resource sufficient for making the coffee if true then return insufficient
#TODO:3. If not enough money required to get the item then refund it back but if the money is provided then we have to
#   return the change and collect the money

def print_report():
    for key,values in resources.items():
        print(f"{key}:{values}")
    print(f"Money:{money}")

def accept_money():
    print("Please insert Coins")
    quarter=int(input("How many quarters?: "))* 0.25
    dime=int(input("How many dime?: "))* 0.1
    nickel=int(input("How many nickel?: "))* 0.05
    penny=int(input("How many penny?: ")) * 0.01
    return penny+nickel+dime+quarter

def check_money(total_money,coffee_type):
   price=MENU[coffee_type]["cost"]
   global money
   money+=price

   if total_money==price:
       return 0
   elif total_money>price:
       return total_money-price
   else:
       print("Sorry that's not enough money. Money refunded")

def check_ingredient(coffee_type):
    ingredient=MENU[coffee_type]["ingredients"]
    for key in ingredient:
        if resources[key]<ingredient[key]:
            return False
    return True


def make_coffee(coffee_type):
    if coffee_type in MENU:
        ingredient = MENU[coffee_type]["ingredients"]
        total_money = accept_money()
        change= check_money(total_money, coffee_type)
        check=check_ingredient(coffee_type)

        if check==True:
            for key in ingredient:
                resources[key]-=ingredient[key]
            finished(change,coffee_type)
        else:
            print(f"Apologies!!! We do not have the ingredient to make {coffee_type}")
    else:
        print("Wrong Input provided")


def finished(change,coffee_type):
    if change!=0:
        print(f"Here is your change: {round(change,2)}")
    else:
        print("As you have paid exact value. Therefore no change. Thank you for using me!!!")
    print(f"Here is your {coffee_type}. Enjoy")


def main():
    x=True
    while(x):
        coffee=input("What would you like? (espresso/latte/cappuccino): ").lower()
        if coffee=="report":
            print_report()
        elif coffee=="off":
            print("Turning OFF")
            x=False
        elif coffee=="espresso" or coffee=="latte" or coffee=="cappuccino":
            make_coffee(coffee)
        else:
            print("Wrong Input!!Try again!")



if __name__ == "__main__":
    main()