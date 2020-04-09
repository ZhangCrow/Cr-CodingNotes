from microbit import *
import music

in_traffic_light_loop = True

# 交通灯模块 R接S5 Y接S6 G接S7 GND接G5
# Traffic Light Module Loop
while in_traffic_light_loop:
    music.play(music.JUMP_UP)
    pin5.write_digital(0)
    pin6.write_digital(0)
    pin7.write_digital(0)
    while True:
        display.show('G')
        pin5.write_digital(0)
        pin6.write_digital(0)
        pin7.write_digital(1)
        if button_a.is_pressed() or button_b.is_pressed():
            pin7.write_digital(0)
            if button_a.is_pressed() == answer_is_a:
                display.show('R')
                pin5.write_digital(1)
            else:
                display.show('Y')
                pin6.write_digital(1)
            sleep(1000)
            pin5.write_digital(0)
            pin6.write_digital(0)
            pin7.write_digital(0)
            display.clear()

# The end
