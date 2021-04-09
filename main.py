from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.image import Image
from kivy.clock import Clock
from kivy.properties import NumericProperty
from kivy.core.window import Window

class Gerenciador(ScreenManager):
    pass

class Player(Image):
    vel=0
    ac = -1000
    def update(self):
        if not collided:
            self.vel += self.ac * 1/60
            self.y += self.vel* 1/60
        else:
            self.vel = 0

class Bloco(Image):
    px = NumericProperty(0)
    py = NumericProperty(0)


class Tela(Screen):
    blocos=[]
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        Clock.schedule_once(self.desenhaTela)
        Window.bind(on_keyboard=self.keyDown)

    def keyDown(self, a,b, keycode, *args):
        if keycode == 27:
            print('jump')
        elif keycode == 79:
            print('direita')
        elif keycode == 80:
            print('esquerda')

    def collision(self):
        px = self.player.x
        py = self.player.y
        for block in self.blocos:
            if block.x <= px < block.x + block.width:
                if block.y <= py < block.y + block.width:
                    
                    
                    return true
        return False

    def update(self, *args):
        collided = self.collision()
        self.player.update(col)

    def desenhaTela(self, *args):
        self.player= Player()
        self.add_widget(self.player)
        for i in range(15):
            self.blocos.append(Bloco(px=i))
            self.add_widget(self.blocos[-1])
        Clock.schedule_interval(self.)


class Mario(App):
    pass

Mario().run()


