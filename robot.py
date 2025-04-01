from mistyPy.Robot import Robot
from mistyPy.Events import Events
import time
import pywhatkit
from datetime import datetime

misty = Robot("YOUR_ROBOT_IP_ADDRESS") #your Robot IP Address

def send_whatsapp_message(MyNumber, MyTextMessage): #function to send a message on WhatsApp
    myobj = datetime.now()
    pywhatkit.sendwhatmsg(MyNumber, MyTextMessage, myobj.hour, myobj.minute + 1, 10, True)

MyNumber = "___" #your phone number (don't forget to include the country code)

misty.start_face_recognition()

def recognized(data):
    print(data)  
    if data["message"]["label"] == 'unknown person': #intruder
        misty.display_image("e_Anger.jpg")
        misty.transition_led(255, 0, 0, 0, 0, 255, "Blink", 100)
        misty.move_arms(-80, -80)
        misty.speak("Intruder! Intruder!")
        misty.play_audio("Police Siren Sound Effect.mp3", 50)
        MyTextMessage = "Intruder!"
        send_whatsapp_message(MyNumber, MyTextMessage)
    else :
        misty.display_image("e_Joy2.jpg") #familiar face
        misty.change_led(0, 255, 0)
        for i in range (2):
            misty.move_arms(80, -80, 50, 50)
            time.sleep(1)
            misty.move_arms(80, 0, 50, 50)
            time.sleep(1)
        MyTextMessage = data["message"]["label"] + " is home!"
        send_whatsapp_message(MyNumber, MyTextMessage)


misty.register_event(event_name='face_recognition_event', event_type=Events.FaceRecognition, callback_function=recognized, keep_alive=False)
misty.keep_alive()
