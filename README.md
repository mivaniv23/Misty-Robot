Misty Get Weather
=================

In this project, Misty will use the command send_external request to connect with Weatherstack and request your city's data.

Requirements
------------

*   **Misty Robot**: You will need a Misty robot to interact with the Python code.
    
*   **Python 3.9**: Ensure Python is installed on your system.
    * You can install python using this link: https://www.python.org/downloads/release/python-3913/
    
*   **WeatherStack API Key**: You need an API key from WeatherStack to handle weather responses.
    Weatherstack is an online weather data API service that provides real-time weather information, historical data, and weather forecasts for various locations around the world. It is commonly used by developers to integrate weather data into applications and websites. The service is known for its reliability, ease  of use, and wide coverage, making it popular for various weather-based applications and projects.
    * Navigate in Weatherstack, link: https://weatherstack.com/
    * Click on "START USING THE API"
    * Sign up with your credentials and your plan (we used the free version, which gives only 250 API requests)
    * Click on "VISIT DASHBOARD"
    * and you'll see your API Key with many other information.
    
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
    *   Replace with your Google GenAI API key.
    *   Replace with your path to the Misty-Robot-Main folder.
        ```python
        #line 4     
        misty = Robot("<YOUR_IP_ADDRESS>")
        #line 10
        access_key = "<YOUR_API_KEY>" 
        #line 11
        query = "<YOUR_CITY>"
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
    
    *   After extracting the weather data, the robot verbally informs the user about the current weather conditions in the specified city. Misty will speak the weather update, and you’ll see a printed message in the terminal.
        

Features
--------

*   **Misty Robot Movements**: The robot can change its LED color, move its head, and display images on its screen.
    
*   **Voice Interaction**: The robot can record speech, transcribe it, and interact with you based on the transcription.
    
*   **Weather Information**: The script fetches real-time weather data for a given city using the WeatherStack API and shares this information with the user.
    
*   **Customizable Experience**: You can modify the city and customize the robot's behavior, including changing its image, LED colors, and more.
    

Notes
-----

*   Make sure the Misty robot is powered on and connected to the same network as your computer.
    
*   Ensure that the mistypy SDK is installed and configured correctly before running the script.
    

License
-------

This project is licensed under the MIT License - see the LICENSE file for details.

