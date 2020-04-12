from microbit import *
import music

in_traffic_light_loop = True

# 交通灯模块 R接S5 Y接S6 G接S7 GND接G5
# Traffic Light Module Loop
while in_traffic_light_loop:
    music.play(music.JUMP_UP)
    display.clear()
    pin5.write_digital(0)
    pin6.write_digital(0)
    pin7.write_digital(0)
    sleep(1000)
    # 绿灯亮
    display.show('G')
    pin7.write_digital(1)
    sleep(2000)
    # 黄灯亮
    display.show('Y')
    pin6.write_digital(1)
    sleep(2000)
    # 红灯亮
    display.show('R')
    pin5.write_digital(1)
    sleep(2000)

# The end
