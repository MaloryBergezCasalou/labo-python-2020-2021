# malorybergezcasalou

from ursina import *
import random

# create a window
app = Ursina()

window.title = "brick shooter mk2"

player = Entity(model='quad', color=color.blue,
                Collision=True, x=-0, y=-3.5, scale=(0.5, 0.5))


class Player:
    global player

    def update(self):
        player.x += held_keys['d'] * time.dt
        player.x -= held_keys['q'] * time.dt

    update()

    # def collision(self):
    #     self.entity = Entity(model='sphere', color=color.orange, x=2)
    #     entity.collider = 'sphere'

    def shoot(self, key):
        if key == 'space':
            player.y += 1
            invoke(setattr, player, 'y', player.y-1, delay=.25)

    shoot()


# start running the game
def main():
    spaceship = Player()


if __name__ == "__main__":
    main()

app.run()
