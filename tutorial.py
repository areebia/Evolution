import pyglet

window = pyglet.window.Window(800, 600, "Evolution")
window.set_caption("abcdefghijlmoo")
window.set_mouse_visible(True)

#pic = pyglet.resource.image('pop.png')

pic = pyglet.image.load("pop.png")


@window.event
def on_draw():
    window.clear()
    pic.blit(0,0)
 


pyglet.app.run()
