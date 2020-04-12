from microbit import *
import music

in_traffic_light_loop = True

# 交通灯模块 R接S2 Y接S1 G接S0 GND接G0
# Traffic Light Module Loop
while in_traffic_light_loop:
    music.play(music.JUMP_UP)
    display.clear()
    # 读取并展示土壤湿度
    humidity = pin3.read_analog()
    display.show(humidity)
    # 初始化交通灯
    pin0.write_digital(0)
    pin1.write_digital(0)
    pin2.write_digital(0)
    sleep(1000)
    # 绿灯亮
    pin0.write_digital(1)
    pin1.write_digital(0)
    pin2.write_digital(0)
    sleep(2000)
    # 黄灯亮
    pin0.write_digital(0)
    pin1.write_digital(1)
    pin2.write_digital(0)
    sleep(2000)
    # 红灯亮
    pin0.write_digital(0)
    pin1.write_digital(0)
    pin2.write_digital(1)
    sleep(2000)

# The end
