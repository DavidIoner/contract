
 
from kivy.factory import Factory
from kivy.core.window import Window
from kaki.app import App
from kivymd.app import MDApp

Window.size=(360,640)
class HotReload(App,MDApp):
    CLASSES={
        'Menus':'tests.kv3'
    }
    KV_FILES=[
        'tests/test3.kv'
    ]
    AUTORELOADER_PATHS=[
        ('.',{'recursive':True})
    ]

    def build_app(self, first=False):
        self.title='Menu'
        return Factory.Menus()

if __name__=='__main__':
    HotReload().run()