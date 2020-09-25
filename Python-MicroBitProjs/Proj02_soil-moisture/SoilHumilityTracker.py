import music
from microbit import *

'''
————————————————————

代码进度安排
本次完成:
* 尝试同时接入多个硬件使其都可以正常工作(土壤湿度传感器, 交通灯, 蜂鸣器)
* 尝试进行方法的声明和调用
ToDo:
* 业务逻辑
* 细节调整与优化

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
Soil Humidity Sensor
-:G0 +:V0 S:S0
— — —
Digital Buzzer Module
-:G8 +:V8 S:S8
— — —
Traffic Light Module
GND:G12 G:S12 Y:S13 R:S14

————————————————————
'''


# 声明变量分配引脚
soil_humidity_sensor = pin0
buzzer = pin8
traffic_light_g = pin12
traffic_light_y = pin13
traffic_light_r = pin14


# 定义主函数 loop循环
def main():
    while True:
        # 蜂鸣清屏 本轮循环开始
        music.play('f4:2', pin = buzzer, wait = True, loop = False)
        display.clear()
        # 读取并展示土壤湿度
        humidity = soil_humidity_sensor.read_analog()
        display.scroll(humidity)
        sleep(2000)
        expression_humidity(humidity)
        # 播放一次交通灯变灯流程
        full_traffic_light()


# 调试函数 表情化输出湿度(太干, 有点干, 舒适)
# param value: 土壤湿度值(0~1023)
def expression_humidity(value):
    severe_dry = 50
    mild_dry = 150
    if value < severe_dry:
        display.show(Image.SAD)
    elif value < mild_dry:
        display.show(Image.ASLEEP)
    else:
        display.show(Image.HAPPY)


# 调试函数 一次完整的交通灯变灯流程
# param red_on:     红灯开关 bool
# param yellow_on:  黄灯开关 bool
# param green_on:   绿灯开关 bool
# param duration:   持续时长(ms) int
def traffic_light(red_on, yellow_on, green_on, duration):
    traffic_light_g.write_digital(green_on)
    traffic_light_y.write_digital(yellow_on)
    traffic_light_r.write_digital(red_on)
    if duration > 0:
        sleep(duration)


# 调试函数 一次完整的交通灯变灯流程
def full_traffic_light():
    traffic_light(False, False, True, 2000)
    traffic_light(False, True, False, 500)
    traffic_light(True, False, False, 2000)


# Call the main function.
main()
