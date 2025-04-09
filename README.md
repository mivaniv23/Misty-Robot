Misty Conference Assistant
==========================

This project aims to make Misty a conference assistant.

This is a basic interpretation but her code can be enriched with many actions and sentences that can assist the speaker at a conference. This code will allow the speaker to control the presentation triggering Misty's bump sensors. If the rear right sensor is triggered Misty will move to the next slide, if the rear left sensor is triggered Misty will move to the previous slide. After you run the Python code from your computer open your presentation and wait for the magic to happen.

We have also added another command: if you press the front left sensor all the events will be stopped and your program can finish under your control. 

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
    
    *   Extract all files from the Python-SDK-main.zip file to a directory on your system.
        
    *   Place the robot.py file in the same directory as the extracted SDK files.
        
3.  **Install Dependencies**:
    * Windows:
    ```bash
    py -m pip install -q -U pyautogui
    py -m pip install -q -U requests==2.25.1
    py -m pip install -q -U websocket-client==0.57.0
    py -m pip install -q -U yapf==0.30.0
    ```
    * Mac:
    ```bash
    python3 -m pip install -q -U pyautogui
    python3 -m pip install -q -U requests==2.25.1
    python3 -m pip install -q -U websocket-client==0.57.0
    python3 -m pip install -q -U yapf==0.30.0
    ```      
4.  **Configure the Robot and API Keys**:
    *   Replace with the Misty robot's IP address.
        ```python    
        misty = Robot("<YOUR_IP_ADDRESS>")
        ```

        
6.  **Running the Code**:
    
    *   Open a terminal or command prompt in the directory where you placed the files.
    ```bash    
    py robot.py
    ```    
        

Description
--------

*We will utilize the Python pyautogui library for this purpose, which enables our code to control the keyboard. To install pyautogui, use the following command line in your terminal: "pip install pyautogui". Press enter and wait for the installation of all the required packages.

*It can only be used in a desktop environment and is not compatible with the Misty Studio Python Interface, so ensure you have all the necessary resources for the task before initiating.

Notes
-----

*   Make sure the Misty robot is powered on and connected to the same network as your computer.
    
*   Ensure that the mistypy SDK is installed and configured correctly before running the script.
    

License
-------

This project is licensed under the MIT License - see the LICENSE file for details.

