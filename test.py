from weasyprint import HTML, CSS
from weasyprint.text.fonts import FontConfiguration
import os

# get the path of the current file
path = os.path.dirname(os.path.realpath(__file__))

TEMPLATE = path + "/stylesheet/page_01.html"

font_config = FontConfiguration()
html = HTML(TEMPLATE)
css = CSS(filename=path + "/stylesheet/styles.css")

html.write_pdf(path + '/tmp/CRE.pdf', font_config=font_config, stylesheets=[css])