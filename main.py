def on_button_pressed_a():
    basic.show_string("HI PRESS BUTTON B TO CONTINUE...")
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_ab():
    basic.clear_screen()
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_button_pressed_b():
    basic.show_leds("""
        . # # # #
        . # . . .
        . . # . .
        . . . # .
        # # # # .
        """)
    basic.pause(1000)
    basic.show_leds("""
        # . . . #
        # . . . #
        # # # # #
        # . . . #
        # . . . #
        """)
    basic.pause(1000)
    basic.show_leds("""
        . . # . .
        . # . # .
        # . . . #
        # # # # #
        # . . . #
        """)
    basic.pause(1000)
    basic.show_leds("""
        . # . # .
        . # # . .
        . # . . .
        . # # . .
        . # . # .
        """)
    basic.pause(1000)
    basic.show_leds("""
        # # # # .
        # . . . .
        # # # # .
        # . . . .
        # # # # .
        """)
input.on_button_pressed(Button.B, on_button_pressed_b)

def on_gesture_shake():
    pass
input.on_gesture(Gesture.SHAKE, on_gesture_shake)

def on_forever():
    pass
basic.forever(on_forever)
