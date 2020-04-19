import pyxel


class App:
    def __init__(self):
        pyxel.init(160, 120, caption="Hello Pyxel")
        pyxel.load("assets/test000.pyxres")
        self.x = 0
        pyxel.run(self.update, self.draw)

    def update(self):
        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()
        self.x = (self.x  + 1) % pyxel.width

    def draw(self):
        pyxel.cls(0)
        pyxel.text(55, 41, "Hello, Pyxel!", pyxel.frame_count % 16)
        pyxel.rect(self.x, 0, 7, 7, 9)
        pyxel.blt(61, 66, 0, 0, 0, 32, 32)
App()