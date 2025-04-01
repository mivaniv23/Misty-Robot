Misty Intruder Alert
====================

In this project you can learn how to have Misty follow a human. 

Requirements
------------

*   **Misty Robot**: You will need a Misty robot to interact with the Python code.
    
*   **Python 3.9**: Ensure Python is installed on your system.
    
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
    pip install -q -U requests==2.25.1
    pip install -q -U websocket-client==0.57.0
    pip install -q -U yapf==0.30.0
    ```    
4.  **Configure the Robot and API Keys**:
    *   Replace with the Misty robot's IP address.
    *  Set up the modes. Read about modes in section Modes lower.
        ```python    
        misty = Robot("<YOUR_IP_ADDRESS>")
        turn_in_place = (True or False)
        follow_human = (True or False)
        ```

        
6.  **Running the Code**:
    
    *   Open a terminal or command prompt in the directory where you placed the files.
    ```bash    
    py robot.py
    ```    
        

Modes
--------

There are three different modes that you can use in this Python code (Misty's head will always move): 

* Mode 1: No driving ("turnInPlace" : false, "followHuman" : false)
  
* AMode 2: Allow turning in place, but not driving forward/backward ("turnInPlace" : true, "followHuman" : false) 

* Mode 3: Allow full driving ("turnInPlace" : true, "followHuman" : true)
      

Notes
-----

*   Make sure the Misty robot is powered on and connected to the same network as your computer.
    
*   Ensure that the mistypy SDK is installed and configured correctly before running the script.
    

License
-------

This project is licensed under the MIT License - see the LICENSE file for details.

