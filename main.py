#
#
# API, IMPORT, FILE CALLS
import re
import requests
#
#
# CLASS ROI


class ROI_Estimator():
    user_data = {}
    home_inv = {}
    stock_inv = {}
#
#
# INTERFACE WELCOME

    def main_menu(self):

        #   DIPLAY WELCOME MESSAGE
        print('\n')
        print('\n')
        print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
        print(' Welcome to Bigger Pockets ROI Calculator ')
        print(f'         Let\'s get you started...       ')
        print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
        self.input_firstname = input("What is your first name?\n")
        self.driver()
#
#
# INTERFACE DRIVER

    def driver(self):
        # Print statement menu
        print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
        print('       Bigger Pockets ROI Calculator      ')
        print(f'            Welcome {self.input_firstname.title()}!   ')
        print('                                          ')
        print('        1: Investment - Home ROI          ')
        print('        2: Investment - Stocks ROI        ')
        print('        3: View Available Homes (beta)    ')
        print('        4: QUIT                           ')
        print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
        res = input('Please choose an item /# from the list above:\n')
        while True:
            if res == '1':
                self.add_home_investment()
            elif res == '2':
                self.add_stock_investment()
            elif res == '3':
                self.call_zillow()
            elif res == '4':
                break
            else:
                print('Please enter a valid response, 1-7')
#
#
# API CALL

    def call_zillow(self):
        # BEEN WAITING FOR AN ACTUAL ZILLOW API KEY TO IMPROVE QUERY ABILITY
        # INSTEAD, USED THE MOST FUNCTIONAL/FREE SERVICE I COULD FIND (with only 30 uses per month)
        # API INFORMATION
        url = "https://zillow56.p.rapidapi.com/search"
        querystring = {"location": "city, st"}
        headers = {
            "X-RapidAPI-Key": "41a38c8cd6mshbe9044313920e31p1441a7jsnb4993ea108d2",
            "X-RapidAPI-Host": "zillow56.p.rapidapi.com"
        }
        file2 = open('./property_data.txt', 'w+')
#
#
# API QUERY
        print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
        print('       Bigger Pockets ROI Calculator      ')
        print(f'            Property Search              ')
        print('       Warning: Results are raw data      ')
        print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
        loc_input = input(
            f"Please enter a City and State to search: (city, st)\n")
        user_search = {"location": loc_input}
        querystring.update(user_search)
        print(querystring)
        response = requests.request(
            "GET", url, headers=headers, params=querystring)
        properties = response.text
# WRITE TO PROPERTIES FILE
        file2.writelines(properties)
        file2.close
        with open("./property_data.txt")as f:
            view_prop = f.readlines()
            for line in view_prop:
                print(line)
        print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
        print('      RESULTS HAVE BEEN SAVED TO:         ')
        print('          "property_data.txt"             ')
        print('~~~~~~~~~~~~~~END RESULTS~~~~~~~~~~~~~~~~~\n')
        self.driver
#
#
# ADD HOME INVESTMENT

    def add_home_investment(self):
        inv_home = input(
            'What would you like to call this home?\nType "exit" to return to the main menu\n').lower()
        if inv_home == 'exit':
            self.driver()
        inv_home_quantity = 1
# GET HOME COST
        while True:
            try:
                home_price = float(
                    input(f"What is the expected or actual sale price of {inv_home.title()}?:\n"))
                break
            except:
                print('Please enter price in digits\n')
        while True:
            try:
                home_mort_payment = float(
                    input(f"What is the expected monthly mortgage payment for {inv_home.title()}?:\n (If none, enter 0)"))
                break
            except:
                print('Please enter price in digits\n')
# GET HOME FEES/TAXES
        while True:
            try:
                home_fees = float(
                    input(f"Please enter the initial down payment, fees, taxes\netc- due at purchase for {inv_home.title()}: (If none, enter 0)\n"))
                break
            except:
                print('Please enter fees/taxes in digits\n')
# GET HOME RENOVATION COSTS
        while True:
            try:
                inv_reno = float(
                    input(f"Please enter the estimated amount you will\nspend for renovation of {inv_home.title()}: (If none, enter 0)\n"))
                break
            except:
                print('Please enter renovation costs in digits\n')
# GET HOME MONTHLY EXPENSES
        while True:
            try:
                home_upkeep = float(
                    input(f"Please enter the estimated amount of recurring monthly\nexpenses/upkeep (if any) \nfor {inv_home.title()}: (If none, enter 0)\n"))
                break
            except:
                print('Please enter expenses/upkeep in digits\n')
# GET HOME REVENUE
        while True:
            try:
                home_revenue = float(
                    input(
                        f"Please enter the estimated gross monthly revenue\n you expect to receive from {inv_home.title()}: (If none, enter 0)\n"))
                break
            except:
                print('Please enter revenue in digits\n')
# GET MARKET VALUE
        while True:
            try:
                home_market_value = float(
                    input(
                        f"What is the estimated current value, or expected future\nsale price of {inv_home.title()}: (If unknown, enter purchase price)\n"))
                break
            except:
                print('Please enter revenue in digits\n')
# CALCULATE HOME DATA
        cash_home_inv = home_price + home_fees + inv_reno
        mortgage_home_inv = home_fees + inv_reno
        monthly_home_inv = home_upkeep
        mort_monthly_home_inv = home_upkeep + home_mort_payment
        annual_home_inv = home_upkeep * 12
        mort_monthly_home_net_revenue = home_revenue - mort_monthly_home_inv
        cash_monthly_home_net_revenue = home_revenue - monthly_home_inv
        mort_annual_home_net_revenue = mort_monthly_home_net_revenue * 12
        cash_annual_home_net_revenue = cash_monthly_home_net_revenue * 12
        home_net_value = home_market_value - cash_home_inv
# ADD HOME TO home_inv DICT
        print(f"You have updated '{inv_home.title()}' in your portfolio!\n")
        self.home_inv.update({
            'nickname': inv_home,
            'quantity': inv_home_quantity,
            'price': home_price,
            'renovation': inv_reno,
            'fees': home_fees,
            'upkeep': home_upkeep,
            'revenue': home_revenue,
            'annual_costs': annual_home_inv,
            'annual_revenue': mort_annual_home_net_revenue,
            'home_value': home_net_value,
        })
# WRITE TO USER FILE
        file1 = open('./userdata.txt', 'w+')
        file1.writelines(self.home_inv)
        file1.close
# OUPTUT HOME ROI
        print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
        print('                Estimated Return on Investment               ')
        print(
            f'                        for {inv_home.title()}                      ')
        print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n')
        print(
            f'          You have added {inv_home.title()}, at the                  ')
        print(f'           purchese price of ${home_price}.               \n ')
        print(f'    CASH PURCHASE DETAILS:                                   ')
        print(
            f'        Initial Investment Total: ${cash_home_inv}            ')
        print(
            f'        Monthly Expenses: ${monthly_home_inv}                 ')
        print(
            f'        Monthly Net Revenue: ${cash_monthly_home_net_revenue}      ')
        print(
            f'        Annual Net Revenue: ${cash_annual_home_net_revenue}      \n')
        print(f'    MORTGAGE PURCHASE DETAILS:                               ')
        print(
            f'        Initial Investment Total: ${mortgage_home_inv}        ')
        print(
            f'        Monthly Expenses: ${mort_monthly_home_inv}                 ')
        print(
            f'        Monthly Net Revenue: ${mort_monthly_home_net_revenue}              ')
        print(
            f'        Annual Net Revenue: ${mort_annual_home_net_revenue}      \n')
        print(
            f'    ESTIMATED NET VALUE OF {inv_home.title()}:                       ')
        print(f'                    ${home_net_value}')
        print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
        response = input(
            'Would you like to calculate ROI for another property? (Y/N)').lower()
        print('Type "exit" to return to the main menu\n')
        if response == 'y':
            self.add_home_investment
        if response == 'n':
            self.driver
        if response == 'exit':
            self.driver
        else:
            print(
                'Please enter "y" to recalculate, "n" to return to the menu,\nor "exit" to quit.\n')
#
#
# ADD STOCK INVESTEMENT

    def add_stock_investment(self):
        #  GET INV NAME
        inv_item = input(
            'Please enter a name or ticker ID for the stock you are calculating:\nOr type "exit" to return to the menu\n').lower()
        if inv_item == 'exit':
            self.driver()
        while True:
            inv_quantity = input(
                f"How many '{inv_item}' are you going to purchase?:\n")
            if inv_quantity.isdigit():
                inv_quantity = int(inv_quantity)
                break
            else:
                print('Please enter quantity in digits\n')
# GET PRICE PER STOCK
        while True:
            try:
                inv_price = float(
                    input(f"How much does EACH '{inv_item}' cost?:\n"))
                break
            except:
                print('Please enter price in digits\n')
# GET STOCK FEES
        while True:
            try:
                fees_taxes = float(
                    input(f"Total amount of fees and/or taxes:\n"))
                break
            except:
                print('Please enter price in digits\n')
# CALCULATE STOCK TOTAL
        total_inv = inv_quantity * inv_price + fees_taxes
        # AVERAGE RETURN CALCULATIONS
        # 10 YEAR AVERAGE Annualized Real Return 14.8% (Adjusted for Inflation 12.4%)
        ten_average = (total_inv - fees_taxes) / 100 * 14.8 * 10
        ten_av_value = (ten_average + total_inv - fees_taxes)
        ten_average_adj = (total_inv - fees_taxes) / 100 * 12.4 * 10
        ten_adj_value = (ten_average_adj + total_inv - fees_taxes)
        # 30 YEAR AVERAGE Annualized Real Return 9.9% (Adjusted for Inflation 7.3%)
        thirty_average = (total_inv - fees_taxes) / 100 * 9.9 * 30
        thirty_av_value = (thirty_average + total_inv - fees_taxes)
        thirty_average_adj = (total_inv - fees_taxes) / 100 * 7.3 * 30
        thirty_adj_value = (thirty_average_adj + total_inv - fees_taxes)
        # 50 YEAR AVERAGE Annualized Real Return 9.4% (Adjusted for Inflation 5.4%)
        fifty_average = (total_inv - fees_taxes) / 100 * 9.4 * 50
        fifty_av_value = (fifty_average + total_inv - fees_taxes)
        fifty_average_adj = (total_inv - fees_taxes) / 100 * 5.4 * 50
        fifty_adj_value = (fifty_average_adj + total_inv - fees_taxes)
# SAVE STOCK DATA TO stock_inv DICT
        self.stock_inv.update({
            'name': inv_item,
            'price': inv_price,
            'quantity': inv_quantity,
            'fees_taxes': fees_taxes,
            'total_cost': total_inv,
            'ten_year_value': ten_adj_value,
            'thirty_year_value': thirty_adj_value,
            'fifty_year_value': fifty_adj_value,
        })
# OUTPUT STOCK ROI
        print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
        print('                Estimated Return on Investment               ')
        print(f'                        for {inv_item}                      ')
        print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n')
        print(f'           You have added {inv_quantity} {inv_item},        ')
        print(f'           at the price of ${inv_price} each                ')
        print(f'           TOTAL EXPENSE: {total_inv}                     \n')
        print(f'   10 Year Annualized Return:                               ')
        print(f'   ${ten_average} Net Return                                ')
        print(f'   ${ten_average_adj} Net Return, Adjusted for Inflation    ')
        print(f'   Estimated Nominal Total Value: ${ten_av_value}            ')
        print(
            f'   Estimated Inflation Adjusted Total Value: ${ten_adj_value }\n')
        print(f'   30 Year Annualized Return:                 ')
        print(f'   ${thirty_average} Net Return             ')
        print(
            f'   ${thirty_average_adj} Net Return, Adjusted for Inflation')
        print(
            f'   Estimated Nominal Total Value: ${thirty_av_value}            ')
        print(
            f'   Estimated Inflation Adjusted Total Value: ${thirty_adj_value }\n')
        print(f'   50 Year Annualized Return:                 ')
        print(f'   ${fifty_average} Net Return             ')
        print(
            f'   ${fifty_average_adj} Net Return, Adjusted for Inflation')
        print(
            f'   Estimated Nominal Total Value: ${fifty_av_value}            ')
        print(
            f'   Estimated Inflation Adjusted Total Value: ${fifty_adj_value }\n')
        print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')

    def view_stocks_api():
        pass

    def compare_roi():
        pass

    def view_portfolio():
        pass
