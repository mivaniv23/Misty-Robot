Misty Robot Assistant for Catawba College Digital Learning Lab
==============================================================

This project allows interaction with the Misty robot for Catawba College's Digital Learning Lab. The robot provides information about the lab's equipment, policies, and hours of operation, while also allowing users to have general conversations. Additionally, the robot can process voice commands for signing in or engaging in a conversation, leveraging Google GenAI for conversational responses.

Requirements
------------

*   **Misty Robot**: You will need a Misty robot to interact with the Python code.
    
*   **Python 3.9**: Ensure Python is installed on your system.
    * You can install python using this link: https://www.python.org/downloads/release/python-3913/
    
*   **Google GenAI API Key**: You need an API key from Google GenAI to handle conversational responses.
    
*   **Misty Python SDK**: The Misty Python SDK must be downloaded and set up on your local machine.
    

Project Setup
-------------

Follow these steps to get the project up and running:

1.  **Download Necessary Files**:
    
    *   Download the robot.py file.
        
    *   Download the Python-SDK-main.zip folder, which contains the necessary SDK files.
        
2.  **Extract and Set Up the SDK**:
    
    *   Extract the Python-SDK-main.zip file to a directory on your system.
        
    *   Place the robot.py file in the same directory as the extracted SDK files.
        
3.  **Install Dependencies**:
        * Windows:
        ```bash
        py -m pip install -q -U google-genai
        py -m pip install -q -U requests==2.25.1
        py -m pip install -q -U websocket-client==0.57.0
        py -m pip install -q -U yapf==0.30.0
        ```
        * Mac:
        ```bash
        pythpn3 -m pip install -q -U google-genai
        pythpn3 -m pip install -q -U requests==2.25.1
        pythpn3 -m pip install -q -U websocket-client==0.57.0
        pythpn3 -m pip install -q -U yapf==0.30.0
        ```   
5.  **Configure the Robot and API Keys**:
    *   Replace with the Misty robot's IP address.
    *   Replace with your Google GenAI API key.
        ```python    
        line 10 misty = Robot("<YOUR_IP_ADDRESS>")
        line 21 client = genai.Client(api\_key="<YOUR_API_KEY>")
        line 103 myfile = client.files.upload(file='/Users/makerspace/Desktop/Misty-Robot-main/' + file_name)
        ```

        
6.  **Running the Code**:
    
    *   Open a terminal or command prompt in the directory where you placed the files.
        * Windows:
        ```bash    
        py robot.py
        ```
        * Mac:
        ```bash    
        python3 robot.py
        ```
7.  **Interacting with the Robot**:
    
    *   Once the script is running, the robot will start its face recognition.
        
    *   When a face is recognized as "unknown," it will ask whether you want to sign in or start a conversation.
        
    *   If you choose a conversation, the robot will transcribe your speech, process it using Google GenAI, and respond accordingly.
        
    *   If you choose to sign in, the robot will display a QR code for you to scan.
        

Features
--------

*   **Misty Robot Movements**: The robot's LED color, head position, and arms can be customized.
    
*   **Voice Interaction**: The robot can record speech, transcribe it, and interact with you based on the transcription.
    
*   **Google GenAI Integration**: The robot uses Google GenAI to provide conversational responses and interact intelligently with users.
    
*   **Sign-In Feature**: Users can sign in using a QR code displayed by the robot.
    

Notes
-----

*   Make sure the Misty robot is powered on and connected to the same network as your computer.
    
*   Ensure that the mistypy SDK is installed and configured correctly before running the script.
    

License
-------

This project is licensed under the MIT License - see the LICENSE file for details.

