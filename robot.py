from mistyPy.Robot import Robot
from mistyPy.Events import Events
import random
import time

misty = Robot("<YOUR_IP_ADDRESS>")
misty.change_led(0, 0, 255)
misty.move_head(0, 0, 0)
misty.display_image("e_DefaultContent.jpg")

def goofy():
    misty.play_audio("s_Awe2.wav")
    time.sleep(2)
    misty.display_image("e_JoyGoofy.jpg")
    misty.transition_led(0, 255, 0, 0, 0, 255, "breathe", 1200)  # Transition from green to blue
    misty.move_arms(-40, 40)  # Move left arm up, right arm down
    misty.move_head(-5, 0, 5)  # Head tilt
    misty.speak("Keep going! You're doing great!")
    print("goofy")

def love():
    misty.play_audio("s_Love.wav")
    time.sleep(2)
    misty.display_image("e_Love.jpg")
    misty.transition_led(255, 255, 0, 0, 255, 0, "breathe", 1200)  # Transition from yellow to green
    misty.move_arms(20, -20)  # Move right arm up, left arm down
    misty.move_head(0, 0, -5)  # Nod head down
    misty.speak("Believe in yourself, you can achieve anything!")
    print("love")

def joy():
    misty.play_audio("s_Joy.wav")
    time.sleep(2)
    misty.display_image("e_Joy.jpg")
    misty.transition_led(0, 0, 255, 255, 0, 0, "breathe", 1200)  # Transition from blue to red
    misty.move_arms(-20, -20)  # Both arms down
    misty.move_head(5, 5, 0)  # Head nod to the side
    misty.speak("You’ve got this, keep pushing forward!")
    print("joy")

def ecstacy():
    misty.play_audio("s_Ecstacy2.wav")
    time.sleep(2)
    misty.display_image("e_EcstacyHilarious.jpg")
    misty.transition_led(255, 0, 0, 255, 255, 0, "breathe", 1200)  # Transition from red to yellow
    misty.move_arms(40, 40)  # Both arms up
    misty.move_head(-10, 0, 0)  # Shake head
    misty.speak("Every step you take is progress, don’t stop now!")
    print("ecstacy")

def amazement():
    misty.play_audio("s_Amazement.wav")
    time.sleep(2)
    misty.display_image("e_Amazement.jpg")
    misty.transition_led(255, 165, 0, 0, 255, 255, "breathe", 1200)  # Transition from orange to cyan
    misty.move_arms(-40, 20)  # Left arm down, right arm mid-level
    misty.move_head(0, -5, 5)  # Slight tilt and nod
    misty.speak("Great things never come from comfort zones. Keep it up!")
    print("amazement")

# Store animations in a list
animations = [goofy, love, joy, ecstacy, amazement]

# Function to handle touch events
def touched(data):
    print("Sensor touched!")
    random.choice(animations)()
    unregister_all_events()

# Register touch event
misty.register_event(event_name='touch', event_type=Events.TouchSensor, callback_function=touched, keep_alive=False)

# Keep the program running
misty.keep_alive()
