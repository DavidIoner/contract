from kivy.lang import Builder
from kivymd.app import MDApp
import components.to_pdf_class as pdf



class App(MDApp):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def build(self):
        kv = Builder.load_file("components/ui.kv")
        return kv


    def submit(self):
        var_dict = {'licensee': self.root.ids.licensee.text,'start_date': self.root.ids.start_date.text, 'end_date': self.root.ids.end_date.text,'company': self.root.ids.company.text,'located_at': self.root.ids.located_at.text,'phone': self.root.ids.phone.text, 'location': self.root.ids.location.text, 'apartment_price_MXN': self.root.ids.apartment_price_MXN.text, 'licensor': self.root.ids.licensor.text, 'onboarding': self.root.ids.onboarding.text, 'security_MXN': self.root.ids.security_MXN.text, 'wage_MXN': self.root.ids.wage_MXN.text, 'christmas_MXN': self.root.ids.christmas_MXN.text,}
        try:
            name = var_dict['licensee']
            contract = pdf.Report(vars_dict=var_dict)
            contract.start('CRE_contract.html', f'CRE_{name}.pdf')
            self.root.ids.label.text = f'Contract for {name} is generated successfully'
        except:
            print('error')
            self.root.ids.label.text = 'Error'



App().run()
