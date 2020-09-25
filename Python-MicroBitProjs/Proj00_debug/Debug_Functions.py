import music
import random
from microbit import *

'''
该文件用于
1. 尝试进行"Week 3 - Python and MicroBit Functions"中的函数定义调用传参和获取返回值等尝试
2. 看看为啥music模块不发音
'''

'''
定义主函数 负责loop循环
'''
def main():
    while True:
        music.play(music.JUMP_UP)
        display.clear()
        # 第一段逻辑
        number = random.randint(1, 9)
        display.show(number)
        sleep(2000)
        is_even = is_even_number(number)
        if is_even:
            display.show(Image.YES)
        else:
            display.show(Image.NO)
        sleep(2000)
        display.clear()
        # 第二段逻辑
        full_traffic_light()
        display.show(Image.HAPPY)


'''
业务函数 尝试传参和返回结果
'''
def is_even_number(number):
    is_even = number % 2
    return not is_even


'''
业务函数 封装交通灯
交通灯模块 GND接G12 G接S12 Y接S13 R接S14
'''
def traffic_light(red_on, yellow_on, green_on):
    pin12.write_digital(green_on)
    pin13.write_digital(yellow_on)
    pin14.write_digital(red_on)


'''
业务函数 一次完整的交通灯变灯流程
'''
def full_traffic_light():
    traffic_light(False, False, True)
    sleep(2000)
    traffic_light(False, True, False)
    sleep(500)
    traffic_light(True, False, False)
    sleep(2000)


# Call the main function.
main()
