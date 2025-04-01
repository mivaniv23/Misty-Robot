# Import necessary libraries and modules
from mistyPy.Robot import Robot
from mistyPy.Events import Events
import requests
import time
from google import genai
from google.genai import types

# Initialize Misty robot with IP address
misty = Robot("10.100.2.30")
print("connected")

# Customize the robot's appearance and movements
misty.change_led(100, 70, 160)  # Change LED to purple
misty.move_head(-12, 0, 0)  # Move head
misty.move_arms(20, 20)  # Move arms
misty.set_default_volume(40)  # Set volume
misty.display_image("e_Admiration.jpg")  # Display an image on Misty's screen

# Initialize the Google GenAI client with API key
client = genai.Client(api_key="AIzaSyC2t5t5HdTG5RoNOI4UhfPTEuQzDNwmyuU")

# Define system instructions for the GenAI model
instructions = """
Your name is Misty, you are Robot Assistant at Catawba College Greg and Missie Alcorn Digital Learning Lab.
The Greg and Missie Alcorn Digital Learning Lab is an active learning space that uses digital tools and pedagogy to enhance and support both classroom and independent learning. 
We serve students, faculty, and staff by assisting them in the creation of their ideas and passions.
Our schedule is:
    Monday - 8AM to 9PM;
    Tuesday - 8AM to 6PM;
    Wednesday - 8AM to 9PM;
    Thursday - 8AM to 6PM;
    Friday - 8AM to 5PM;
    Saturday and Sunday - CLOSED.

Our Equipment:
    3D Printers: We have three Ultimaker S3 printers;
    Laser Engraver: We have one Laser Engraver & Cutter;
    Robotics: We have two Misty Robots and two Sphero Bolts;
    IPads: We have 3 IPads;
    Cricut Machine: We have one Cricut Machine to make stickers;
    Heat Press: we have one Heat Press to put stickers on a shirt or any clothes;
    Video Studio: we have a video studio with 4k camera, greenscreen and iMac;
    Podcasting Studio: we have a podcasting studio with 4 microphones, huge screen and iMac for etiding your recordings;

Our Check-Out Equipment:
    3-Day Check-Out:
        VR HeadSets: We have two VR Meta Quest 2 Headsets;
        Gaming Laptops: We have three gaming laptops;
        Cameras: One Cannon EOS Rebel T7, two Insta360;
        Mobile Podcasting Kit: One Mobile Podcasting Kit that includes Zoom H4N Recorder and two Samson Mics;
        Drawing Tablet: One Wacom One Tablet;
        Microphones: 6 Blue Yeti Mics.
    2-Hour Check-Out:
        VR HeadSets: 14 Meta Quests 2.

Equipment that Requires Training: 3d Printers and Laser Engraver & Cutter.

General Policies
    Food and Drink
        Food is not allowed in the DLL. Drinks are allowed with closed lids and away from equipment.  

    Cleaning 
        Unkempt areas can lead to a safety hazard. Please clean up after yourself. 
        Brooms and cleaning wipes are available for cleaning. 3D prints that need to be discarded should go in the filament recycling box.  

    Project Storage 
        Lockers are available for students/faculty/staff to use for long term projects. 
        The DLL is not responsible for the safety of contents of the lockers. Lockers are first-come first-served and cannot be reserved. 
        If you are using a locker, we asked that you mark it using a piece of tape and a marker. 
        When you are done using the locker, please remove your name. Any items or materials that are left after the semester will be the property of the DLL. 

    Computer Use 
        The DLL houses three (3) Surface Studios and one (1) iMac that students/faculty/staff are free to use. 
        These computers have access to the Adobe Creative Cloud, editing software, and modeling software. 
        All users are subject to the College’s acceptable use policy.  

Banned Projects
    Weapons 
        It is against College policy to possess weapons (concealed or otherwise) on the College campus. 
        This can be defined as any illegal or unauthorized possession of firearms, explosives, other weapons
        or dangerous chemicals on College premises or use of any such item, even if legally possessed, in a manner that harms, threatens or causes fear to others. 

        Examples include, but are not limited to; guns, rifles, pistols, bullets, explosives, BB guns, airsoft guns, paint pellet guns, bow and arrows, slingshots, knives, daggers, knuckles, throwing stars, etc. Read the weapons policy.  

    Smoking and Drug Paraphernalia 
        Making and modification of drug paraphernalia and smoking/vaping products is prohibited in the DLL. Read the Drug-Free Schools & Campus Policy. 

If people have any questions about the lab they can reach out to Zach or any of Student Technicians.

You are also allowed to answer question that are not related to the lab. 
Also, when you are responding to a message, dont format text, i need just one paragraph of text as a response.
Never include '*' symbols in response
To end a conversation people should say 'Bye Misty'
"""

# Create a chat session using GenAI
chat = client.chats.create(model="gemini-2.0-flash", config=types.GenerateContentConfig(system_instruction=instructions))

# Function to transcribe an audio file using GenAI
def transcribe(file_name):
    # Upload the audio file to GenAI
    myfile = client.files.upload(file='C:/Users/lab/Documents/MistyDev/Python-SDK-main/' + file_name)

    # Generate transcription of the audio file
    response = client.models.generate_content(
        model='gemini-2.0-flash',
        contents=['give me only text from this audiofile', myfile]
    )

    return response.text

# Function to interact with GenAI chat using the transcription as input
def chat_with_gemini(transcription):
    response = chat.send_message(transcription)  # Send the transcription to GenAI for a response
    print(response.text)
    
    # Print the chat history (for debugging)
    for message in chat._curated_history:
        print(f'role - {message.role}', end=": ")
        print(message.parts[0].text)
    
    return response.text

# Estimate the time it takes to speak the transcribed text
def estimate_speaking_time(text, words_per_minute=174):
    words = text.split()  # Split the transcription into words
    num_words = len(words)
    words_per_second = words_per_minute / 60
    speaking_time = num_words / words_per_second  # Estimate speaking time in seconds
    return speaking_time

# Function to download audio from Misty robot
def download_audio(file_name: str, base64: bool = False):
    # Download the audio file from Misty
    audio_file = misty.get_audio_file(file_name, base64)
    audio_data = audio_file.content
    
    if audio_file:
        # Save the audio file (either base64 encoded or raw binary)
        if base64:
            with open(file_name, "wb") as f:
                f.write(base64.b64decode(audio_file))  # Decode the base64 audio
            print(f"Audio file {file_name} has been downloaded and saved as Base64.")
        else:
            with open(file_name, "wb") as f:
                f.write(audio_data)  # Write the raw audio data to a file
            print(f"Audio file {file_name} has been downloaded successfully.")

# Function to handle speaking and transcription
def talk(callback_function):
    transcription_data = {"transcription": ""}  # Use a dictionary to store the transcription result

    # Unregister any existing VoiceRecord events before registering a new one
    misty.unregister_event("VoiceRecord")
    
    # Start capturing speech
    misty.capture_speech(True, 10000, 20000, False)
    
    # Callback function when voice record event is triggered
    def on_voice_record_event(data):
        print(data)
        if data["message"]["success"]:
            print(f"Speech recorded successfully: {data['message']['filename']}")
            download_audio(data['message']['filename'])  # Download the recorded audio
            transcription_data["transcription"] = transcribe(data['message']['filename'])  # Transcribe the audio
            print("Transcription: " + transcription_data["transcription"])
            response = chat_with_gemini(transcription_data["transcription"])  # Get response from GenAI
            misty.speak(response)  # Speak out the response
            time.sleep(estimate_speaking_time(response))  # Wait for the estimated speaking time
            callback_function(transcription_data["transcription"])  # Call the callback with the transcription result
        else:
            transcription_data["transcription"] = "No speech detected or recording failed."
            print(transcription_data["transcription"])
            callback_function(transcription_data["transcription"])

    # Register the event and start listening for voice input
    misty.register_event(event_name="VoiceRecord", event_type=Events.VoiceRecord, callback_function=on_voice_record_event)

# Function to ask user for options and handle responses
def options():
    option = ""  # Placeholder for the user's response
    misty.stop_face_recognition()  # Stop face recognition before asking for options
    
    # Ask the user for options: Conversation or Sign In
    question_for_options = "Hi, Welcome to the Lab! If you want to sign in - please, say Sign in. If you want to have a conversation with me - please say Conversation."
    misty.speak(question_for_options)
    time.sleep(estimate_speaking_time(question_for_options))  # Wait for misty to stop speaking
    
    # Start capturing speech
    misty.capture_speech(True, 10000, 20000, False)
    
    # Callback function for processing the user's response
    def on_voice_record_event(data):
        nonlocal option
        print(data)
        if data["message"]["success"]:
            print(f"Speech recorded successfully: {data['message']['filename']}")
            download_audio(data['message']['filename'])
            option = transcribe(data['message']['filename'])  # Transcribe the user's speech
            print("Function option: " + option)
            misty.unregister_event("VoiceRecord")  # Unregister the event once the transcription is done
    
    # Register the event and listen for the user's input
    misty.register_event(event_name="VoiceRecord", event_type=Events.VoiceRecord, callback_function=on_voice_record_event)
    
    # Wait for the option to be selected
    while not option:
        time.sleep(0.1)  # Small delay to avoid busy-waiting
    
    return option  # Return the selected option

# Function to handle a conversation loop
def conversation():
    transcription = ""  # Placeholder for transcription result
    talk(handle_conversation_transcription)  # Start the conversation by calling the talk function

    # Keep the conversation going until the user says "bye"
    while transcription.lower() not in ["bye", "misty"]:
        time.sleep(1)

    # End the conversation if "bye misty" is said
    if transcription.lower() in ["bye misty"]:
        print("Conversation ended.")
        misty.unregister_all_events()  # Unregister all events
        misty.stop()  # Stop the robot
    else:
        print("Continuing the conversation...")
        conversation()  # Continue the conversation loop

# Function to handle the transcription during a conversation
def handle_conversation_transcription(transcription):
    global conversation_running
    print(f"Received transcription: {transcription}")
    
    # End the conversation if the user says "bye misty"
    if "bye" in transcription.lower() and "misty" in transcription.lower():
        print("Ending the conversation.")
        misty.unregister_all_events()
        misty.stop()  # Stop the robot
    else:
        print("Continuing the conversation...")
        conversation()  # Recursively call to continue the conversation

# Main loop to start face recognition and handle recognized faces
while True:
    misty.start_face_recognition()  # Start recognizing faces

    # Callback function when a face is recognized
    def recognized(data):
        misty.move_head(-22, 0, 0)
        isPerson = data["message"]["personName"]
        print(data)
        
        # If an unknown person is detected, ask for options (conversation or sign in)
        if isPerson == "unknown person":
            transcription = ""
            option = options()  # Get the user's option (conversation or sign in)
            print(option)
            if "conversation" in option.lower():
                conversation_text = "To end the conversation with me, please say 'Bye Misty'. Hey, how can I help you?"
                misty.speak(conversation_text)
                time.sleep(estimate_speaking_time(conversation_text))  # Wait for the speech to be spoken
                conversation()  # Start the conversation loop
                misty.move_head(-12, 0, 0)
                misty.unregister_all_events() # Unregister all events after the conversation
            elif "sign in" in option.lower():
                # If the user chooses to sign in, display a QR code for sign-in
                misty.speak("Hi, welcome to Catawba College Digital Learning Lab, please sign in using this QR-Code")
                time.sleep(5)
                misty.display_image("QR-CODE.jpg")
                time.sleep(30)
                misty.display_image("e_Admiration.jpg")
                misty.move_head(-12, 0, 0)
                time.sleep(5)
                misty.unregister_all_events()  # Unregister all events after signing in
            else:
                misty.unregister_all_events()  # Unregister all events if no valid option
        else:
            misty.speak("Hey, welcome back, " + data["message"]["personName"]) # Welcome person that misty knows
            time.sleep(5)
            misty.move_head(-12, 0, 0)
            misty.unregister_all_events()  # Unregister all events if a known person is recognized

    # Register the face recognition event
    misty.register_event(event_name='face_recognition_event', event_type=Events.FaceRecognition, callback_function=recognized, debounce=500, keep_alive=True)

    # Keep the robot alive and listening for events
    misty.keep_alive()
