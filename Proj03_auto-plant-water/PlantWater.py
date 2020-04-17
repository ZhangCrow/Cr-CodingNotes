import music
from microbit import *

'''
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
Single Relay Module
-:G13 +:V13 S:S13
# # #
if has not water pump, use red LED module
Red LED Module
-:G13 +:V13 S:S13

————————————————————
'''


# 声明变量 为硬件模块或传感器分配引脚
water_sensor = pin0
ambient_light_sensor = pin1
soil_humidity_sensor = pin2
buzzer = pin12
relay = pin13


low_water_level = 80    # ProductionValue:  80, TestingValue: 120
low_light_level = 50    # ProductionValue:  50, TestingValue: 100
low_humidity = 330      # ProductionValue: 330, TestingValue: 420


# 定义主函数 loop循环
def main():
    while True:
        # 初始化/重置状态(蜂鸣器, LED)
        display.clear()
        switch_buzzer(False)
        # 获取感应器实时状态(水箱水位、光照亮度)
        is_enough_water = water_sensor.read_analog() > low_water_level
        is_still_up = ambient_light_sensor.read_analog() > low_light_level
        # 环境判断
        if is_enough_water:
            # 高水位 -> 停止蜂鸣 监测土壤 如有必要执行浇水
            soil_need_water = track_soil_humility()
            if soil_need_water:
                watering()
        elif is_still_up:
            # 低水位&(高光照:白天/未熄灯) -> 蜂鸣提醒加水
            switch_buzzer(True)
        else:
            # 低水位&(低光照:夜里&已熄灯) -> 停止蜂鸣 休眠一段时间
            # display.show(Image.ASLEEP)    # debug code
            # sleep(1000*10)                # debug code 调试时睡10秒够了
            sleep(1000*60*60*4)


# 这个函数来读取土壤湿度 显示表情 返回是否需要浇水
# return is_need_water
def track_soil_humility():
    value = soil_humidity_sensor.read_analog()
    need_water = value < low_humidity
    # display.clear()             # debug code
    # display.scroll(value)       # debug code
    # sleep(1000*2)               # debug code
    if need_water:
        display.show(Image.SAD)
    else:
        display.show(Image.HAPPY)
    return need_water


# 控制硬件设备提醒用户水箱缺水
# param switch_on: 开关蜂鸣器 bool
def switch_buzzer(switch_on):
    if switch_on:
        music.play('f4:2', pin = buzzer, wait = True, loop = False)
    else:
        music.stop(buzzer)


# 控制硬件设备进行浇水
def watering():
    relay.write_digital(True)
    # 浇水数秒后停止
    sleep(1000*20)
    relay.write_digital(False)


# Call the main function.
main()
