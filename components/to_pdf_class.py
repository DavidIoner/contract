from weasyprint import HTML
import os
from jinja2 import Environment, FileSystemLoader
import requests
from datetime import datetime
from components.send_pdf import send_email

# come back one directory
def get_rate(id="MXN-BRL"):
    url = "https://economia.awesomeapi.com.br/last/" + id
    response = requests.get(url)
    data = response.json()
    data_id = id.replace("-", "")
    rate = data[data_id]["bid"]
    return float(rate)

class Report:
    def __init__(self, vars_dict={}):
        self.vars_dict = vars_dict
        self.ROOT = os.path.dirname(os.path.abspath(__file__))
        self.TEMPLATE_SRC = os.path.join(self.ROOT, 'templates')
        self.DEST_DIR = os.path.join(self.ROOT, 'output')
       

    def start(self, template_file, output_name=False):
        print('start generate report...')
        env = Environment(loader=FileSystemLoader(self.TEMPLATE_SRC))
        template = env.get_template(template_file)
        css = os.path.join(self.TEMPLATE_SRC, 'styles.css')
        
        print('setting variables')
        # variables
        BRL = get_rate('BRL-USD')
        MXN = get_rate('MXN-USD')
        COP = get_rate('COP-USD')
        if 'USD' in self.vars_dict['security']:
            security_temp = self.vars_dict['security'].replace('USD', '')
            security_USD = float(security_temp)
            security_MXN = security_USD / MXN
        else:
            security_temp = self.vars_dict['security'].replace('MXN', '')
            security_MXN = float(security_temp)
            security_USD = security_MXN * MXN
        if 'USD' in self.vars_dict['onboard']:
            onboard_temp = self.vars_dict['onboard'].replace('USD', '')
            onboard_cash = float(onboard_temp)
            onboard_coin = 'USD'
            affiliate_onboard = '5CRE'
        else:
            onboard_temp = self.vars_dict['onboard'].replace('MXN', '')
            onboard_cash = float(onboard_temp)
            onboard_coin = 'MXN'
            affiliate_onboard = '5CRE’s LATAM affiliate'

        wage_USD = float(self.vars_dict['wage_MXN']) * MXN
        christmas_USD = float(self.vars_dict['christmas_MXN']) * MXN
        apartment_price_USD = float(self.vars_dict['apartment_price_USD'])
        apartment_price_USD_year = apartment_price_USD * 12
        biwage = float(self.vars_dict['wage_MXN']) / 2
        biwage_USD = biwage * MXN
        federal_holiday_MXN = float(self.vars_dict['wage_MXN']) * 12 * 0.023 
        federal_holiday_USD = federal_holiday_MXN * MXN

        
        # setting variables into the template
        self.vars_dict.update({'date': datetime.now().strftime('%d/%m/%Y')})
        self.vars_dict.update({'MXN': f'{MXN:.2f}', 'BRL': f'{BRL:.2f}', 'COP': f'{COP:.2f}'})
        self.vars_dict.update({'security_USD': f'{security_USD:.2f}', 'security_MXN': f'{security_MXN:.2f}','onboard_affiliate': affiliate_onboard, 'onboard_coin': onboard_coin,'onboard_cash': f'{onboard_cash:.2f}', 'wage_USD': f'{wage_USD:.2f}', 'biwage': f'{biwage:.2f}','biwage_USD': f'{biwage_USD:.2f}', 'christmas_USD': f'{christmas_USD:.2f}', 'apartment_price_USD': f'{apartment_price_USD:.2f}','apartment_price_USD_year': apartment_price_USD_year, 'federal_holiday_USD': f'{federal_holiday_USD:.2f}', 'federal_holiday_MXN': f'{federal_holiday_MXN:.2f}'})
        print('rendering')
        # rendering to html string
        self.vars_dict['template_src'] = 'file://' + self.TEMPLATE_SRC
        rendered_string = template.render(self.vars_dict)
        html = HTML(string=rendered_string)
        report = os.path.join(self.DEST_DIR, output_name)
        print('generating pdf')
        html.write_pdf(report, stylesheets=[css])
        print(f'file is generated successfully and under {self.DEST_DIR}')
        print('sending email')
        #send_email(report)
        
 



