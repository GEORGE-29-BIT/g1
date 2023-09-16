input.onButtonPressed(Button.A, function () {
    basic.showString("HI PRESS BUTTON B TO CONTINUE...")
})
input.onButtonPressed(Button.AB, function () {
    basic.clearScreen()
})
input.onButtonPressed(Button.B, function () {
    basic.showLeds(`
        . # # # #
        . # . . .
        . . # . .
        . . . # .
        # # # # .
        `)
    basic.pause(1000)
    basic.showLeds(`
        # . . . #
        # . . . #
        # # # # #
        # . . . #
        # . . . #
        `)
    basic.pause(1000)
    basic.showLeds(`
        . . # . .
        . # . # .
        # . . . #
        # # # # #
        # . . . #
        `)
    basic.pause(1000)
    basic.showLeds(`
        . # . # .
        . # # . .
        . # . . .
        . # # . .
        . # . # .
        `)
    basic.pause(1000)
    basic.showLeds(`
        # # # # .
        # . . . .
        # # # # .
        # . . . .
        # # # # .
        `)
})
input.onGesture(Gesture.Shake, function () {
    basic.showString("GO HOME, YA FILTHY FARM ANIMAL")
})
basic.forever(function () {
	
})
