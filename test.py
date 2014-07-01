import sphero
import pyglet
from pyglet.window import key

window = pyglet.window.Window(360, 360)
s = sphero.Sphero()


@window.event
def on_key_press(symbol, modifiers):
    if symbol == key.SPACE:
        print("space")
        s.set_rotation_rate(0x00)
    elif symbol == key.UP:
        print("UP")
        s.roll(0xFF, 0)
    elif symbol == key.RIGHT:
        print("RIGHT")
        s.roll(0xFF, 90)
    elif symbol == key.DOWN:
        print("DOWN")
        s.roll(0xFF, 180)
    elif symbol == key.LEFT:
        print("LEFT")
        s.roll(0xFF, 270)
    elif symbol == key.R:
        print("R")
        s.set_rgb(255, 0, 0)
    elif symbol == key.G:
        print("G")
        s.set_rgb(0, 255, 0)
    elif symbol == key.B:
        print("B")
        s.set_rgb(0, 0, 255)


@window.event
def on_key_release(symbol, modifiers):
    if symbol == key.UP:
        print("RELEASE")
        s.stop()
    elif symbol == key.RIGHT:
        print("RELEASE")
        s.stop()
    elif symbol == key.DOWN:
        print("RELEASE")
        s.stop()
    elif symbol == key.LEFT:
        print("RELEASE")
        s.stop()


# @window.event
# def on_mouse_motion(x, y, dx, dy):
# print(x, y, dx, dy)
#     pass
# s.roll(0x80, abs(x - y))

# @window.event
# def on_mouse_press(x, y, button, modifiers):
# print(x, y)
# @window.event
# def on_mouse_release(x, y, button, modifiers):
# print(x, y)


@window.event
def on_activate():
    print("connect sphero")
    try:
        s.connect()
    except:
        print("err!")
        s.close()

    print( """Bluetooth info:name: %s \nbta: %s """ %
           (s.get_bluetooth_info().name, s.get_bluetooth_info().bta))


@window.event
def on_close():
    s.stop()
    window.close()
    pyglet.app.exit()


@window.event
def on_draw():
    window.clear()


if __name__ == '__main__':
    pyglet.app.run()
