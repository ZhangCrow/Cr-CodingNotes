from microbit import *
import music

in_traffic_light_loop = True

'''
该文件用于
1. 确保多个sensor可以同时work, 而不涉及具体的业务逻辑
2. 尝试进行"Week 3 - Python and MicroBit Functions"中的Functions Definition and call
'''

'''
极限情况下引脚需求：土壤湿度传感器1个，交通灯3个，水泵1个，水流传感器1个，环境光传感器1个

根据以下2个文档
https://tech.microbit.org/hardware/edgeconnector/
https://microbit-micropython.readthedocs.io/en/latest/pin.html
得知pins 5, 11, 3, 4, 6, 7, 9, 10, 19 and 20 已经被预设用于按钮或LED或I2C
所以可用pins 0, 1, 2, 8, 12, 13, 14, 15, 16 共9个引脚

根据MakeCode editor 中的提示
https://makecode.microbit.org/#editor
得知 pins 0, 1, 2, 3, 4, 10 attribute 支持 readwrite
其他pins attribute 只支持 writeOnly

所以
交通灯模块 GND接G12 G接S12 Y接S13 R接S14
土壤湿度检测器 G接G0 V接V0 S接S0
'''

# Traffic Light Module Loop
while in_traffic_light_loop:
    music.play(music.JUMP_UP)
    display.clear()
    # 读取并展示土壤湿度
    humidity = pin0.read_analog()
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
