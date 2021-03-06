@namespace
class SpriteKind:
    ninja = SpriteKind.create()

def on_on_overlap(sprite, otherSprite):
    info.change_life_by(-1)
    otherSprite.destroy(effects.disintegrate)
    scene.camera_shake(4, 500)
    sprite.say(randomsayings._pick_random(), 2000)
sprites.on_overlap(SpriteKind.player, SpriteKind.ninja, on_on_overlap)

def makeEnemy():
    global evilninja
    info.change_score_by(1)
    evilninja = sprites.create(img("""
            ..............ffffff....
                    .............fffffffff..
                    ............fffffffffff.
                    ............fffffffffff.
                    ...........fffffffffffff
                    ...........ffffffffffff.
                    ...........fffeeefffffff
                    ...........fee44fbe44eff
                    ............feccf14d4eef
                    .............fcccc4eeef.
                    .............fe444eccf..
                    .............ccc22eccf..
                    .............cdc22fee...
                    ............cddc4444f...
                    ...........cddcfffff....
                    ..........cddc..fff.....
                    ..........cdc...........
                    ..........cc............
                    ........................
                    ........................
                    ........................
                    ........................
                    ........................
                    ........................
        """),
        SpriteKind.ninja)
    evilninja.vx = 40
    evilninja.vy = 60
    evilninja.y = 0
    evilninja.x = randint(0, 160)
    evilninja.set_bounce_on_wall(True)
evilninja: Sprite = None
randomsayings: List[str] = []
randomsayings = ["yete", "chidori", "bruh", "RASAGEAN !"]
info.set_life(10)
info.set_score(0)
monkeyleftImg = img("""
    . . . . f f f f f . . . . . . . 
        . . . f e e e e e f . . . . . . 
        . . f d d d d e e e f . . . . . 
        . c d f d d f d e e f f . . . . 
        . c d f d d f d e e d d f . . . 
        c d e e d d d d e e b d c . . . 
        c d d d d d d d e e b d c . . . 
        c c c c c d d e e e f c . . . . 
        . f d d d d e e e f f . . . . . 
        . . f f f f f e e e e f . . . . 
        . . . . f f e e e e e e f . f f 
        . . . f e e f e e f e e f . e f 
        . . f e e f e e f e e e f . e f 
        . f b d f d b f b b f e f f e f 
        . f d d f d d f d d b e f f f f 
        . . f f f f f f f f f f f f f .
""")
monkeyRightImg = monkeyleftImg.clone()
monkeyRightImg.flip_x()
monkey = sprites.create(monkeyleftImg, SpriteKind.player)
controller.move_sprite(monkey, 100, 0)
monkey.y = 110
monkey.set_stay_in_screen(True)
makeEnemy()
scene.set_background_color(2)

def on_update_interval():
    makeEnemy()
game.on_update_interval(2500, on_update_interval)
