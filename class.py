class Dog(object):

    def __init__(self):
        self.legs = 4

    def set_color(self, color):
        self.color = color

    def get_color(self):
        print self.color

zoe = Dog()
zoe.set_color("black")
zoe.get_color()
