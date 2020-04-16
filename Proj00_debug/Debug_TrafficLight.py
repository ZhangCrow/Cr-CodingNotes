from microbit import *
import music

in_traffic_light_loop = True

# 交通灯模块 R接S14 Y接S13 G接S12 GND接G12
# 土壤湿度检测器 S接S1 V接V1 G接G1
# Traffic Light Module Loop
while in_traffic_light_loop:
    music.play(music.JUMP_UP)
    display.clear()
    # 读取并展示土壤湿度
    humidity = pin1.read_analog()
    display.show(humidity)
    # 初始化交通灯
    pin12.write_digital(0)
    pin13.write_digital(0)
    pin14.write_digital(0)
    sleep(1000)
    # 绿灯亮
    pin12.write_digital(1)
    pin13.write_digital(0)
    pin14.write_digital(0)
    sleep(2000)
    # 黄灯亮
    pin12.write_digital(0)
    pin13.write_digital(1)
    pin14.write_digital(0)
    sleep(2000)
    # 红灯亮
    pin12.write_digital(0)
    pin13.write_digital(0)
    pin14.write_digital(1)
    sleep(2000)

# The end
