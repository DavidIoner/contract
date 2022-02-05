from weasyprint import HTML
import os
from jinja2 import Environment, FileSystemLoader
import requests
from datetime import datetime

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
    # get the path of the current file
        self.vars_dict = vars_dict
        #self.template_name = template_name
        self.ROOT = os.path.dirname(os.path.abspath(__file__))
        self.TEMPLATE_SRC = os.path.join(self.ROOT, 'templates')
        self.DEST_DIR = os.path.join(self.ROOT, 'output')
       
        print(self.vars_dict)

    def start(self, template_file, output_name=False):
        print('start generate report...')
        env = Environment(loader=FileSystemLoader(self.TEMPLATE_SRC))
        template = env.get_template(template_file)
        css = os.path.join(self.TEMPLATE_SRC, 'styles.css')
        # variables
        print('carregou template')
        BRL = get_rate('BRL-USD')
        MXN = get_rate('MXN-USD')
        COP = get_rate('COP-USD')
        security_USD = float(self.vars_dict['security_MXN']) * MXN
        wage_USD = float(self.vars_dict['wage_MXN']) * MXN
        christmas_USD = float(self.vars_dict['christmas_MXN']) * MXN
        apartment_fee_USD = float(self.vars_dict['apartment_fee']) * MXN
        self.vars_dict.update({'date': datetime.now().strftime('%d/%m/%Y')})
        self.vars_dict.update({'MXN': f'{MXN:.2f}', 'BRL': f'{BRL:.2f}', 'COP': f'{COP:.2f}'})
        self.vars_dict.update({'security_USD': f'{security_USD:.2f}', 'wage_USD': f'{wage_USD:.2f}', 'christmas_USD': f'{christmas_USD:.2f}', 'apartment_fee_USD': f'{apartment_fee_USD:.2f}'})

        print("fase 1")
        # rendering to html string
        self.vars_dict['template_src'] = 'file://' + self.TEMPLATE_SRC
        rendered_string = template.render(self.vars_dict)
        html = HTML(string=rendered_string)
        report = os.path.join(self.DEST_DIR, output_name)
        print("fase 2")
        html.write_pdf(report, stylesheets=[css])
        print(f'file is generated successfully and under {self.DEST_DIR}')
 



