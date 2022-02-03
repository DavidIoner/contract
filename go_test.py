import to_pdf_class as pdf
from datetime import datetime
import components.exchange as exchange
import json
import os


def get_dict():
    print('Use "." instead "," in decimal numbers!')
    MXN = round(exchange.get_rate("MXN-USD"), 2)
    COP = round(exchange.get_rate("COP-USD"), 2)
    BRL = round(exchange.get_rate("BRL-USD"), 2)

    date = datetime.now().strftime("%Y-%m-%d")
    start_date = input("Enter start date (YYYY-MM-DD): ")
    end_date = input("Enter end date (YYYY-MM-DD): ")
    location = input("Enter location (city, country): ")
    licensee = input("Enter licensee: ")
    located_at = input("Enter located at: ")
    apartment_city = input("Enter apartment city: ")
    apartment_price = input("Enter apartment price: ")
    licensor = input("Enter licensor: ")
    onboarding = input("Enter onboarding fee: ")
    security_MXN = input("Enter security deposit MXN: ")
    security_USD = round(float(security_MXN) * MXN, 2)
    wage_MXN = input("Enter wage MXN: ")
    wage_USD = round(float(wage_MXN) * MXN, 2)
    christmas_MXN = input("Enter christmas bonus MXN: ")
    christmas_USD = round(float(christmas_MXN) * MXN, 2)
    apartment_fee = input("Enter apartment fee USD: ")
    dict = {'MXN': MXN, 'COP': COP, 'BRL': BRL, 'date': date, 'start_date': start_date, 'end_date': end_date, 'location': location, 'licensee': licensee, 'located_at': located_at, 'apartment_city': apartment_city, 'apartment_price': apartment_price, 'licensor': licensor, 'onboarding': onboarding, 'security_MXN': security_MXN, 'security_USD': security_USD, 'wage_MXN': wage_MXN, 'wage_USD': wage_USD, 'christmas_MXN': christmas_MXN, 'christmas_USD': christmas_USD, 'apartment_fee': apartment_fee,}
    return dict


if os.path.exists('output/var_dict.json'):
    x = input('Do you want to use the saved variables? (y/n): ')
    if x in 'Yy':
        with open('output/var_dict.json', 'r') as f:
            var_dict = json.load(f)
    else:
        var_dict = get_dict()
else:
    var_dict = get_dict()

contract = pdf.Report(vars_dict=var_dict)
contract.start('CRE_contract.html', 'page_merge.pdf')

#save the dict into a json file
with open('output/var_dict.json', 'w') as f:
    json.dump(var_dict, f)





