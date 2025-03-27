Misty Robot Interactive Assistant Documentation
This repository provides an implementation of an interactive assistant using the Misty Robot integrated with Google GenAI for speech recognition, transcription, and conversational responses. The robot can interact with users through voice commands, face recognition, and perform specific tasks related to a Digital Learning Lab (DLL).

Table of Contents
Introduction

Prerequisites

Setup

Features

Usage

Code Explanation

Contributing

License

Introduction
The Misty Robot Interactive Assistant allows users to interact with a Misty robot for a variety of tasks. The robot uses voice input to determine user requests and provides responses based on preconfigured system instructions stored in Google GenAI. The robot is designed for use in a Digital Learning Lab (DLL), where it can assist with general lab-related questions or provide a conversational interface.

Prerequisites
Before using this system, make sure you have the following installed and configured:

Python 3.x

MistyPy SDK: Python library to interact with Misty robots.

Google GenAI API Key: For handling transcription and chatbot interaction.

Misty Robot: Misty robot (version 2.0 or later) connected to the same network as your development environment.

Setup
Install MistyPy: The MistyPy SDK is used to interact with the Misty robot.

bash
Copy
pip install mistyPy
Install Google GenAI:

To use Google's GenAI API, install the required package.

bash
Copy
pip install google-genai
API Key Configuration:

Obtain a Google GenAI API key from the Google Cloud platform.

Replace the placeholder YOUR_API_KEY in the script with your API key to authenticate with Google GenAI.

Misty Robot Configuration:

Ensure that the Misty robot's IP address is configured correctly in the script. Replace "10.100.2.20" with your Misty robot’s IP address.

Features
Face Recognition: The robot uses face recognition to identify whether the person is known or unknown and provides a personalized response.

Speech-to-Text: Misty captures voice input, processes the speech into text, and interacts with the Google GenAI model to generate a response.

Voice Interaction: Misty speaks responses to users based on the transcription from voice input.

Customizable Responses: The system is preconfigured with details about the Digital Learning Lab, and the robot can answer specific questions related to the lab's schedule, equipment, policies, and more.

Conversation Flow: The system maintains a conversational flow that allows continuous interaction until the user says "Bye Misty".

Usage
Starting the Robot
To begin the interactive assistant, execute the Python script. The robot will:

Connect to the Misty robot.

Begin face recognition and wait for a user to approach.

If an unknown person is detected, the robot will prompt the user with a choice: to have a conversation or sign in.

Speech Interaction
When the user opts for a conversation:

The robot listens for voice commands.

It records the speech and sends it for transcription.

Based on the transcribed text, the robot generates a response using the Google GenAI model.

The robot speaks out the generated response.

The conversation continues until the user says "Bye Misty".

Sign-In Option
If the user selects the sign-in option, the robot will display a QR code for signing in, then proceed with the lab's check-in process.

Code Explanation
Key Functions
transcribe(file_name):

Uploads the audio file to Google GenAI for transcription.

Returns the transcribed text.

chat_with_gemini(transcription):

Sends the transcribed text to Google GenAI for generating a response.

Prints the response and chat history for debugging purposes.

estimate_speaking_time(text):

Estimates how long it will take to speak the transcribed text based on average words-per-minute (185 words/minute by default).

download_audio(file_name):

Downloads the audio file recorded by the Misty robot and saves it in the local environment for transcription.

talk(callback_function):

Starts the process of capturing speech and invokes the callback function with the transcription result.

options():

Asks the user for options (Conversation or Sign In) and waits for a voice input.

conversation():

A loop to handle continuous conversation between the robot and the user until "Bye Misty" is said.

recognized(data):

Handles face recognition events and initiates conversation or sign-in options when an unknown person is detected.

Contributing
If you'd like to contribute to this project, feel free to fork the repository and submit pull requests with improvements, bug fixes, or new features. Be sure to include relevant tests for any new functionality.

License
This project is licensed under the MIT License - see the LICENSE file for details.

Acknowledgments
Misty Robotics for providing the SDK and hardware to enable this project.

Google GenAI for enabling advanced speech-to-text and chatbot capabilities.
