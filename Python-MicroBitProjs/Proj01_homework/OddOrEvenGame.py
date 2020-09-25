# Write your code here :-)

from mb_i2c_lcd1602 import *

import random

lcd = LCD1620()

# Introduce the game
lcd.puts('It's game time', 0, 0)
lcd.puts('Odd or even', 1, 1)
sleep(3000)
lcd.clear()
lcd.puts('Pls use the btns', 0, 0)
lcd.puts('A=Odd, B=Even', 1, 1)
sleep(3000)
lcd.clear()
lcd.puts('Here we go!', 0, 0)
sleep(3000)
lcd.clear()

in_game_loop = True

# Game loop
while in_game_loop:
    number = random.randint(1, 9)
    answer_is_a = number % 2
    display.show(number)
    while True:
        if button_a.is_pressed() or button_b.is_pressed():
            if button_a.is_pressed() == answer_is_a:
                display.show(Image.YES)
            else:
                display.show(Image.NO)
            sleep(2000)
            display.clear()

            # Ask the user to restart or not
            lcd.puts('A=restart', 0, 0)
            lcd.puts('B =quit', 1, 1)
            while True:
                if button_a.is_pressed():
                    reset()
                elif button_b.is_pressed():
                    lcd.clear()
                    sleep(1000)
                    in_game_loop = False
                    lcd.puts('Thank you!')
# The end
