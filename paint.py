from random import random
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.graphics import Color, Ellipse, Line

class MyPaintWidget(Widget):

    def on_touch_down(self, touch):
        # Utilisation de la palette HSV pour garantir des couleurs vives et lumineuses
        color = (random(), 1, 1)
        with self.canvas:
            Color(*color, mode='hsv')
            d = 30.
            # Dessine un cercle au point de contact initial
            Ellipse(pos=(touch.x - d / 2, touch.y - d / 2), size=(d, d))
            # Crée une ligne liée au dictionnaire 'ud' (user data) du tactile
            touch.ud['line'] = Line(points=(touch.x, touch.y), width=2)

    def on_touch_move(self, touch):
        # Met à jour les points de la ligne lorsque le toucher/la souris se déplace
        if 'line' in touch.ud:
            touch.ud['line'].points += [touch.x, touch.y]


class MyPaintApp(App):

    def build(self):
        # Conteneur principal (Widget racine)
        parent = Widget()
        
        # Instance du widget de dessin
        self.painter = MyPaintWidget()
        parent.add_widget(self.painter)
        
        # Bouton pour effacer le dessin
        clearbtn = Button(text='Clear', size_hint=(None, None), size=(100, 50), pos=(10, 10))
        clearbtn.bind(on_release=self.clear_canvas)
        parent.add_widget(clearbtn)
        
        return parent

    def clear_canvas(self, obj):
        # Efface toutes les instructions graphiques du canevas
        self.painter.canvas.clear()


if __name__ == '__main__':
    MyPaintApp().run()