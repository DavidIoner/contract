from kivy.lang import Builder
from kivymd.app import MDApp
import components.to_pdf_class as pdf

from kivy.metrics import dp
from kivymd.uix.menu import MDDropdownMenu


class App(MDApp):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.kv = Builder.load_file("components/ui.kv")
        menu_items = [
            {
                "viewclass": "OneLineIconListItem",
                "text": f"local 1",
                "height": dp(56),
                "on_release": lambda x=f"#1 2DA CERRADA LAGO BOLSENA": self.set_item(x),
            },
            {
                "viewclass": "OneLineIconListItem",
                "text": f"local 2 (not available)",
                "height": dp(56),
                "on_release": lambda x=f"#2": self.set_item(x),
            }, 
            {
                "viewclass": "OneLineIconListItem",
                "text": f"local 3 (not available)",
                "height": dp(56),
                "on_release": lambda x=f"#3": self.set_item(x),
            } 
        ]
        self.menu = MDDropdownMenu(
            caller=self.kv.ids.drop_local,
            items=menu_items,
            position="center",
            width_mult=4,
        )
        self.menu.bind()

        # to avoid bugs
        self.security_check = False

    def set_item(self, text_item):
        self.kv.ids.drop_local.set_item(text_item)
        self.menu.dismiss()
        print(text_item)
        if "#1" in text_item:
            self.specific_location = "2DA CERRADA LAGO BOLSENA #54, LAGO NORTE DF, MIGUEL HIDALGO, DF. MX"
            self.location = "Mexico City, Mexico"
            self.city = "Mexico City"
        else:
            self.specific_location = text_item
    
    
    def check(self, checkbox, active):
        print(active)
        if active:
            self.security_check = True
            self.root.ids.security.hint_text = 'Security deposit (USD)'
        if not active:
            self.security_check = False     
            self.root.ids.security.hint_text = 'Security deposit (MXN)'   

        


    def submit(self):
        if self.security_check:
            self.security = self.root.ids.security.text + 'USD'
        if not self.security_check:
            self.security = self.root.ids.security.text + 'MXN'
        var_dict = {'licensee': self.root.ids.licensee.text,'start_date': self.root.ids.start_date.text, 'company': self.root.ids.company.text,'located_at': self.root.ids.located_at.text,'phone': self.root.ids.phone.text, 'location': self.location, 'specific_location': self.specific_location,'city': self.city, 'apartment_price_USD': self.root.ids.apartment_price_USD.text, 'licensor': self.root.ids.licensor.text, 'onboarding': self.root.ids.onboarding.text, 'security': self.security, 'wage_MXN': self.root.ids.wage_MXN.text, 'christmas_MXN': self.root.ids.christmas_MXN.text, 'federal_holiday_MXN': self.root.ids.federal_holiday_MXN.text}
        try:
            name = var_dict['licensee']
            contract = pdf.Report(vars_dict=var_dict)
            contract.start('CRE_contract.html', f'CRE_{name}.pdf')
            self.root.ids.label.text = f'Contract for {name} is generated successfully'
        except:
            print('error')
            self.root.ids.label.text = 'Error'


    def build(self):
        return self.kv

App().run()
