# malorybergezcasalou

from ursina import *
import random

# create a window
app = Ursina()

window.title = "brick shooter mk2"

startPositionX = 0
startPositionY = -3.5

player = Entity(model='quad', color=color.blue,
                Collision=False, x=startPositionX, y=startPositionY, scale=(0.5, 0.5))

bullet = Entity(model=Circle(1, mode='line', thickness=0.25),
                color=color.orange, Collision=True, x=player.x, y=-3.15)


def shoot(key):
    if key == 'space':
        bullet.y += 1 * time.dt


def update():
    player.x += held_keys['d'] * time.dt
    player.x -= held_keys['q'] * time.dt
#    bullet.y += held_keys['space'] * time.dt


# def collision():
#    entity = Entity(model='sphere', color=color.orange, x=2)
#    entity.collider = 'sphere'


# start running the game
app.run()
