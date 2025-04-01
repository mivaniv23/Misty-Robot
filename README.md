Misty Intruder Alert
====================

In this project you can learn how to have Misty trigger an intruder alert if she doesn't recognize a person and send a message to your phone. 

If Misty detects a face that's not stored in her memory, she will access your WhatsApp web and send a text message to your phone number saying: "Intruder!". If she does recognize the person, she will send the message "person_name is home!". Before executing the code, open https://web.whatsapp.com/ and log in with your phone number. 

Requirements
------------

*   **Misty Robot**: You will need a Misty robot to interact with the Python code.
    
*   **Python 3.9**: Ensure Python is installed on your system.
    
*   **WhatsApp Account*: You need an account to be able to send messages.
    
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
    ```bash
    pip install pywhatkit
    pip install -q -U requests==2.25.1
    pip install -q -U websocket-client==0.57.0
    pip install -q -U yapf==0.30.0
    ```    
4.  **Configure the Robot and API Keys**:
    *   Replace with the Misty robot's IP address.
    *   Replace with your WhatsApp Account number.
        ```python    
        misty = Robot("<YOUR_IP_ADDRESS>")
        MyNumber = "___"
        ```

        
6.  **Running the Code**:
    
    *   Open a terminal or command prompt in the directory where you placed the files.
    ```bash    
    py robot.py
    ```    
        

Description
--------

* We will utilize the Python pywhatkit library for this purpose, which enables message sending on WhatsApp in a semi-automatic way. To install pywhatkit, use the following command line in your terminal: "pip install pywhatkit". Press enter and wait for the installation of all the required packages.

* Another required action prior to using Whatsapp is to train Misty on the faces you want her to recognize as friends (misty studio Explore>Vision>Train faces) and upload all the files you'll run in the code, both images and audio files (misty studio Explore>Expressions>Upload audio files or Upload images or videos). 

* Note: Sometimes the WhatsApp message might not be sent before the website closes. In that case, try running the code again.

* To reset Misty after running the code, you can access its Misty Studio and in the wizard section, click on the "Body Reset" action.

* It can only be used in a desktop environment and is not compatible with the Misty Studio Python Interface, so before initiating, ensure you have all the necessary resources for the task.
    

Notes
-----

*   Make sure the Misty robot is powered on and connected to the same network as your computer.
    
*   Ensure that the mistypy SDK is installed and configured correctly before running the script.
    

License
-------

This project is licensed under the MIT License - see the LICENSE file for details.

