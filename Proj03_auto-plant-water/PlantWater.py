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


low_water_level = 80    # 正式环境 80
low_light_level = 50    # 正式环境 50
low_humidity = 330      # 正式环境 330


# 定义主函数 loop循环
def main():
    while True:
        is_enough_water = water_sensor.read_analog() > low_water_level
        is_still_up = ambient_light_sensor.read_analog() > low_light_level
        if is_enough_water:
            # 水量充足 停止蜂鸣 监测土壤
            music.stop(buzzer)
            display.clear()
            need_water = track_soil_humility()
            if need_water:
                watering()
        elif is_still_up:
            # 水量不足&两脚兽还没睡 蜂鸣提醒加水
            music.play('f4:2', pin = buzzer, wait = True, loop = False)
        else:
            # 水量不足&两脚兽熄灯了 休眠4h
            music.stop(buzzer)
            # display.show(Image.ASLEEP) # 这行是调试代码
            # sleep(1000*10) # 这行是调试代码 调试时睡10秒够了
            sleep(1000*60*60*4)


# 这个函数来读取土壤湿度 如有必要控制继电器通电浇水
def track_soil_humility():
    value = soil_humidity_sensor.read_analog()
    display.clear()
    display.scroll(value)
    sleep(1000*2)
    need_water = value < low_humidity
    if need_water:
        display.show(Image.SAD)
    else:
        display.show(Image.HAPPY)
    return need_water

# 浇水
def watering():
    relay.write_digital(True)
    # 浇水20s
    sleep(1000*20)
    relay.write_digital(False)


# Call the main function.
main()
