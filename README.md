Motivational Misty
==================

In this project, Misty transforms into a motivational companion who delivers encouraging messages, delightful visuals, and engaging animations whenever her head is touched. This project uses Misty’s built-in features to create an uplifting interaction, making her the perfect source of inspiration and motivation.

Requirements
------------

*   **Misty Robot**: You will need a Misty robot to interact with the Python code.
    
*   **Python 3.9**: Ensure Python is installed on your system.
    * You can install python using this link: https://www.python.org/downloads/release/python-3913/
    
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
    py -m pip install -q -U requests==2.25.1
    py -m pip install -q -U websocket-client==0.57.0
    py -m pip install -q -U yapf==0.30.0
    ```
    * Mac:
    ```bash
    python3 -m pip install -q -U requests==2.25.1
    python3 -m pip install -q -U websocket-client==0.57.0
    python3 -m pip install -q -U yapf==0.30.0
    ```   
4.  **Configure the Robot and API Keys**:
    *   Replace with the Misty robot's IP address.
        ```python
        #line 6    
        misty = Robot("<YOUR_IP_ADDRESS>")
        ```

        
5.  **Running the Code**:
    
    *   Open a terminal or command prompt in the directory where you placed the files.
        * Windows:
        ```bash    
        py robot.py
        ```
        * Mac:
        ```bash    
        python3 robot.py
        ```
6.  **Interacting with the Robot**:
    
    *   Once the script is running, the Misty robot will perform a series of actions based on touch events. The robot is designed to react to touch by performing different animations and providing encouraging speech.
        

Features
--------

*   **Misty Robot Movements**: The robot's LED color, head position, and arms can be customized for each animation.
    
*   **Voice Interaction**: The robot plays different audio clips and speaks encouraging phrases based on the animation selected.
    
*   **Randomized Responses**: The animations are randomized, providing varied experiences each time the robot is touched.
    
*   **LED Transitions**: The robot's LED colors transition smoothly during animations, enhancing the visual experience.

*   **Touch-Activated Animations**: The robot reacts to touch by performing random animations from a predefined list.
    

Notes
-----

*   Make sure the Misty robot is powered on and connected to the same network as your computer.
    
*   Ensure that the mistypy SDK is installed and configured correctly before running the script.
    

License
-------

This project is licensed under the MIT License - see the LICENSE file for details.

