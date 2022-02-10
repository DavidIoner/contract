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
        self.onboard_check = False
        self.apartment_check = False
        self.holiday_check = False
        self.holiday_coin_check = False

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
        
    

    def check_security(self, checkbox, active):
        if active:
            self.security_check = True
            self.root.ids.security.hint_text = 'Security deposit (USD)'
        if not active:
            self.security_check = False     
            self.root.ids.security.hint_text = 'Security deposit (MXN)'  

    def check_onboard(self, checkbox, active):
        if active:
            self.onboard_check = True
            self.root.ids.onboard.hint_text = 'Onboard deposit (USD)'
        if not active:
            self.onboard_check = False     
            self.root.ids.onboard.hint_text = 'Onboard deposit (MXN)'  
    

    def check_apartment(self, checkbox, active):
        if active:
            self.apartment_check = True
            self.root.ids.apartment.hint_text = 'Apartment fee (USD)'
        if not active:
            self.apartment_check = False
            self.root.ids.apartment.hint_text = 'Apartment fee (MXN)'

    def check_holiday(self, checkbox, active):
        if active:
            self.holiday_check = True
            self.root.ids.holiday_label.text = "Holiday fee activated!"
        else:
            self.holiday_check = False
            self.root.ids.holiday_label.text = "Holiday fee deactivated!"      

    def check_holiday_coin(self, checkbox, active):
        if active:
            self.holiday_coin_check = True
            self.root.ids.holiday_label.text = 'Security deposit (USD)'
        if not active:
            self.holiday_coin_check = False
            self.root.ids.holiday_label.text = 'Security deposit (MXN)'

    def submit(self):
        if self.security_check:
            self.security = self.root.ids.security.text + 'USD'
        if not self.security_check:
            self.security = self.root.ids.security.text + 'MXN'
        if self.onboard_check:
            self.onboard = self.root.ids.onboard.text + 'USD'
        if not self.onboard_check:
            self.onboard = self.root.ids.onboard.text + 'MXN'
        if self.apartment_check:
            self.apartment = self.root.ids.apartment.text + 'USD'
        if not self.apartment_check:
            self.apartment = self.root.ids.apartment.text + 'MXN'
        if self.holiday_coin_check:
            self.holiday_coin = 'USD'
        if not self.holiday_coin_check:
            self.holiday_coin = 'MXN'


        try:
            var_dict = {'licensee': self.root.ids.licensee.text, 
            'company': self.root.ids.company.text, 
            'located_at': self.root.ids.located_at.text,
            'phone': self.root.ids.phone.text,
            'email': self.root.ids.email.text,
            'location': self.location, 
            'specific_location': self.specific_location,
            'city': self.city,
            'worker': self.root.ids.worker.text, 
            'licensor': self.root.ids.licensor.text, 
            'apartment': self.apartment, 
            'onboard': self.onboard, 
            'security': self.security, 
            'wage_MXN': self.root.ids.wage_MXN.text, 
            'christmas_MXN': self.root.ids.christmas_MXN.text,
            'desk_fee_USD': self.root.ids.desk_fee_USD.text,
            'holiday_fee': self.holiday_check,
            'holiday_coin': self.holiday_coin}
            self.root.ids.error_label.text = ""
        except:
            print("Error")
            self.root.ids.error_label.text = "please check your inputs"


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
