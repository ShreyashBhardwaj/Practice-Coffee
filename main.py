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


    def check_money(totalmoney,coffeetype):
       price=MENU[coffeetype]["cost"]
       if totalmoney==price:
           return 0
       elif totalmoney>price:
           return totalmoney-price
       else:
           print("Sorry that's not enough money. Money refunded")
           main()

    def check_ingrident(coffeetype):
        pass


    def make_coffee(coffee_type):
        if coffee_type in MENU:
            total_money = accept_money()
            change=check_money(total_money,coffee_type)
            check_ingrident(coffee_type)
        else:
            print("Wrong Input provided")

    def accept_money():
        print("Please insert Coins")
        quarter=int(input("How many quarters?: "))* 0.25
        dime=int(input("How many dime?: "))* 0.1
        nickel=int(input("How many nickel?: "))* 0.05
        penny=int(input("How many penny?: ")) * 0.01


        return penny+nickel+dime+quarter


    def main():
        while(True):
            pass

    print_report()
    check_money(2)