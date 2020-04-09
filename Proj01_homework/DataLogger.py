from microbit import *
import os

# Set compass
if not compass.is_calibrated():
    compass.calibrate()

while True:
    # Collect data
    comp = compass.heading()
    temp = temperature()
    log_content = str(comp) + ',' + str(temp) + '\n'
    # Display recent data
    display.scroll(log_content, wait=False, loop=True)
    # Check if the file exist
    file_list = os.listdir()
    file_name = 'data_env.csv'

    # If the file exist, history data append with new data
    if file_name in file_list:
        log_file = open(file_name, 'r')
        log_content = log_file.read() + log_content
        log_file.close()
    # Add all data to file
    log_file = open(file_name, 'w')
    log_file.write(log_content)
    log_file.close()

    sleep(60000)
