from kivy.lang import Builder
from kivymd.app import MDApp
import components.to_pdf_class as pdf



class App(MDApp):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def build(self):
        kv = Builder.load_file("ui.kv")
        return kv


    def submit(self):
        var_dict = {'licensee': self.root.ids.licensee.text,'start_date': self.root.ids.start_date.text, 'end_date': self.root.ids.end_date.text, 'location': self.root.ids.location.text, 'apartment_city': self.root.ids.apartment_city.text, 'apartment_price': self.root.ids.apartment_price.text, 'licensor': self.root.ids.licensor.text, 'onboarding': self.root.ids.onboarding.text, 'security_MXN': self.root.ids.security_MXN.text, 'wage_MXN': self.root.ids.wage_MXN.text, 'christmas_MXN': self.root.ids.christmas_MXN.text, 'apartment_fee': self.root.ids.apartment_fee.text,}
        try:
            name = var_dict['licensee']
            contract = pdf.Report(vars_dict=var_dict)
            contract.start('CRE_contract.html', f'CRE_{name}.pdf')
        except:
            print('error')



App().run()
