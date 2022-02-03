from weasyprint import HTML
import os
from jinja2 import Environment, FileSystemLoader
import components.exchange as exchange

# get the path of the current file
ROOT = os.path.dirname(os.path.abspath(__file__))

#TEMPLATE = ROOT + "/stylesheet/page_02.html"
ASSETS_DIR = os.path.join(ROOT, 'assets')

TEMPLATE_SRC = os.path.join(ROOT, 'templates/test')
CSS_SRC = os.path.join(ROOT, 'static/css')
DEST_DIR = os.path.join(ROOT, 'output')


def start(template_file, output_name=False):
    print('start generate report...')
    env = Environment(loader=FileSystemLoader(TEMPLATE_SRC))
    template = env.get_template(template_file)
    css = os.path.join(TEMPLATE_SRC, 'styles.css')

    # variables
    template_vars = { 'template_src': 'file://' + TEMPLATE_SRC ,}

    if not output_name:
        #output_name = template_file - '.html' + '.pdf'
        pass

    # rendering to html string

    rendered_string = template.render(template_vars)
    html = HTML(string=rendered_string)
    report = os.path.join(DEST_DIR, output_name)
    html.write_pdf(report, stylesheets=[css])
    print('file is generated successfully and under {}', DEST_DIR)


if __name__ == '__main__':
    start('page_01.html', 'page_merge.pdf')


