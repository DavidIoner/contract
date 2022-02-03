from weasyprint import HTML, CSS
from weasyprint.text.fonts import FontConfiguration
import os
from jinja2 import Environment, FileSystemLoader

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

        
        if not output_name:
            #output_name = template_file - '.html' + '.pdf'
            pass
        
        # rendering to html string
        self.vars_dict['template_src'] = 'file://' + self.TEMPLATE_SRC
        rendered_string = template.render(self.vars_dict)
        html = HTML(string=rendered_string)
        report = os.path.join(self.DEST_DIR, output_name)
        html.write_pdf(report, stylesheets=[css])
        print(f'file is generated successfully and under {self.DEST_DIR}')
 



