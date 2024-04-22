from pygame import *

class Gamesprite():
    def __init__(picture, x, y, h, w):
        self.image = transform.scale(image.load(picture), (h,w))
        self.rect.x = x
        self.rect.y = y
    def bliting(self):
        wind.blit(self.image, (self.rect.x, self.rect.y))


class Scene(sprite.Sprite, Gamesprite):
    def __init__(self, picture, x, y, h, w):
        super().__init__(picture, x, y, h, w)
# class Man()

# class Blocks()

