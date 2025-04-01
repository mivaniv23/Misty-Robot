from mistyPy.Robot import Robot
from mistyPy.Events import Events
import pyautogui
import time

misty = Robot("YOUR_ROBOT_IP_ADDRESS") #your Robot IP Address

time.sleep(2)
def bumped(event):
    if(event["message"]["sensorId"] == "brr" and event["message"]["isContacted"] == True):
        misty.change_led(0, 255, 255)
        pyautogui.press("right")
        print("next")

    if(event["message"]["sensorId"] == "brl" and event["message"]["isContacted"] == True):
        misty.change_led(255, 0, 255)
        pyautogui.press('left')
        print("previous")

    if(event["message"]["sensorId"] == "bfl" and event["message"]["isContacted"] == True):
        misty.unregister_all_events()
        print("finished")

misty.register_event(event_name='bump_event', event_type=Events.BumpSensor, callback_function=bumped, keep_alive=True)
misty.keep_alive()
