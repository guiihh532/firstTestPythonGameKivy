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
    def update(self, jump, collided):
        #Gravity Logic
        if self.vel > 0 and collided:
            onGround = False
        elif self.vel <= 0 and collided:
            onGround = True
        else:
            onGround = False
        if onGround and jump:
            self.vel = 400
            self.y += self.vel * 1/60
            onGround = False
        elif onGround:
            self.vel = 0
        else:
            self.vel += self.ac * 1/60
            self.y += self.vel* 1/60

        #Movement Logic
        if move:                 
            if move == 'right':
                 self.x += 1
            elif move == 'left':
               self.x -= 1


class Bloco(Image):
    px = NumericProperty(0)
    py = NumericProperty(0)


class Tela(Screen):
    blocos=[]
    jump = False
    move = 'right'
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        Clock.schedule_once(self.desenhaTela)
        Window.bind(on_keyboard=self.keyDown, on_key_up=self.keyUp)


    def keyUp(self, *args):
        print(args)

    def keyDown(self, a,b, keycode, *args):
        if keycode == 27:
            print('jump')
        if keycode == 79:
            self.move = 'right'
        elif keycode == 80:
            self.move = 'left'
        else:
            self.move = ''

    def collision(self):
        px = self.player.x
        py = self.player.y
        for block in self.blocos:
            if block.x <= px < block.x + block.width:
                if block.y <= py < block.y + block.width:
                    
                    return True
        return False

    def update(self, *args):
        collided = self.collision()
        self.player.update(self.jump, self.move, collided)
        self.jump = False

    def desenhaTela(self, *args):
        self.player= Player()
        self.add_widget(self.player)
        for i in range(40):
            self.blocos.append(Bloco(px=i))
            self.add_widget(self.blocos[-1])
        Clock.schedule_interval(self.update, 1/60)
    


class Mario(App):
    pass

Mario().run()


