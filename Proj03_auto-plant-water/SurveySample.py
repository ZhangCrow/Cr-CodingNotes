import music
from microbit import *

'''
————————————————————

Target

* 尝试同时接入多个硬件使其都可以正常工作(土壤湿度传感器, 水流传感器, 环境光传感器, 蜂鸣器, 红灯(表示水泵))
* 实现对土壤，水流以及环境光进行样本数值采样，用来进行区间划分
* 尝试函数的声明和调用
ToDo:
* 业务逻辑
* 场景测试、细节调整及优化

————————————————————

Note
pins 5, 11 default used for buttons.
pins 3, 4, 6, 7, 9, 10 default used for LED display.
pins 19, 20 default used for I2C.
other pins
pins 0, 1, 2 support read-write
pins 8, 12, 13, 14, 15, 16 support write only

————————————————————

Input/Output Pins
— — —
Water Sensor
-:G0 +:V0 S:S0
— — —
Ambient Light Sensor
-:G1 +:V1 S:S1
— — —
Soil Humidity Sensor
-:G2 +:V2 S:S2
— — —
Digital Buzzer Module
-:G12 +:V12 S:S12
- - -
Red LED Module
-:G13 +:V13 S:S13

————————————————————
'''


# 声明变量 为硬件模块或传感器分配引脚
water_sensor = pin0
ambient_light_sensor = pin1
soil_humidity_sensor = pin2
buzzer = pin12
relay = pin13 # 用Red LED Module 表示“Single Relay Module+电池+水泵”组合，因为没有水泵


# 定义主函数 loop循环
def main():
    while True:
        display.clear()
        # 测试输出指令
        debug_output_module()
        # 传感器读取样本
        w_level = get_sensor_analog(water_sensor, 'W')
        l_level = get_sensor_analog(ambient_light_sensor, 'L')
        h_level = get_sensor_analog(soil_humidity_sensor, 'H')
        msg = w_level + ',' + l_level + ',' + h_level
        display.scroll(msg)


def debug_output_module():
    # 开关水泵
    relay.write_digital(True)
    sleep(1000*5)
    relay.write_digital(False)
    # 蜂鸣器
    music.play('f4:2', pin = buzzer, wait = True, loop = False)


# 获取传感器度数的文本内容
def get_sensor_analog(sensor, title):
    display.scroll(title)
    value = sensor.read_analog()
    content = title + ':' + str(value)
    return content

# Call the main function.
main()
