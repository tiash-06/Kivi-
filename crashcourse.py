from kivy.app import App
from kivy.uix.boxlayout import BoxLayout

class DossierRoot(BoxLayout):
    def press_bouton(self):
        # Manova le texte du Label amn alalan ny  ID any
        self.ids.mon_label.text = "Bravo, le bouton a été cliqué !"

class CrashCourseApp(App):
    def build(self):
        return DossierRoot()

if __name__ == '__main__':
    CrashCourseApp().run()