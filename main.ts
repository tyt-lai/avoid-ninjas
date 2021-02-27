
namespace SpriteKind {
    export const ninja = SpriteKind.create()
}
sprites.onOverlap(SpriteKind.Player, SpriteKind.ninja, function (sprite, otherSprite) {
	
})
function makeEnemy  () {
let evilninja = sprites.create(img`
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
`, SpriteKind.Enemy)
evilninja.vx=40	
evilninja.vy=60
evilninja.y=0
evilninja.x= randint(0,160)
evilninja.setBounceOnWall(true)
}

let monkeyleftImg=img`
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
`
let monkeyRightImg = monkeyleftImg.clone()
monkeyRightImg.flipX()
let monkey = sprites.create(monkeyleftImg, SpriteKind.Player)
controller.moveSprite(monkey, 100, 0)
monkey.y=110

monkey.setStayInScreen(true)
makeEnemy()
scene.setBackgroundColor(2) 