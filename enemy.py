from pico2d import *
import game_world
import game_framework
import background
import play_state


class Mushroom:
    def __init__(self , x , y):
        self.mx = x
        self.my = y
        self.frame = 0
        self.image = load_image('monster1.png')
        self.state = 0
        self.dir = 1
        self.mdx = 2
        self.moving_x = 0
        self.moving = 0
        #self.cx = self.mx - background.Background.window_left

    def update(self):
        # self.frame = (self.frame + 1) % 3

        if play_state.char.x > 400 and play_state.char.dir == 1:
            self.mx -= self.dir * self.mdx + play_state.char.dx
            self.moving += play_state.char.dx
        elif play_state.char.x > 400 and play_state.char.dir < 0:
            self.mx += self.dir * self.mdx + play_state.char.dx
            self.moving += play_state.char.dx
        # if play_state.char.x > 400:
        #     self.mx -= self.dir * self.mdx
        #     self.mx -= play_state.char.dx
            if self.mx < self.moving:
                self.dir = -1
            elif self.mx > self.moving:
                self.dir = 1

        else:
            self.mx -= self.dir * 2

            if self.mx < 300:
                self.dir = -1

            elif self.mx > 500:
                self.dir = 1


    def draw(self):
        self.image.clip_draw(0, 0, 48, 58, self.mx, self.my)
        draw_rectangle(*self.get_bb())

    def get_bb(self):
        return self.mx - 25, self.my - 25, self.mx + 25, self.my + 25