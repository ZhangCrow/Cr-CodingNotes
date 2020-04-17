from microbit import *

'''
————————————————————

本文件用以测量土壤，水流以及环境光样本
以对其进行区间划分

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

————————————————————
'''


# 声明变量 为硬件模块或传感器分配引脚
water_sensor = pin0
ambient_light_sensor = pin1
soil_humidity_sensor = pin2


# 定义主函数 loop循环
def main():
    while True:
        display.clear()
        get_sensor_analog(water_sensor, 'W')
        # get_sensor_analog(ambient_light_sensor, 'L')
        # get_sensor_analog(soil_humidity_sensor, 'H')


def get_sensor_analog(sensor, title):
    display.show(title)
    sleep(1000)
    value = sensor.read_analog()
    display.show(value)
    sleep(2000)
    return value


# Call the main function.
main()
