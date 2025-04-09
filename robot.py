from mistyPy.Robot import Robot
import json

misty = Robot("<YOUR_IP_ADDRESS>")
misty.set_default_volume(20)
misty.change_led(0, 255, 0)
misty.move_head(0, 0, 0)
misty.display_image("e_Joy.jpg")

access_key = "<YOUR_API_KEY>" #follow instructions to get your API key
query = "<YOUR_CITY>" #for example: Stockholm

data = misty.send_external_request("GET", "http://api.weatherstack.com/current?access_key="+ access_key+"&query="+ query+"&units=f")
if data.status_code == 200: # success code
    parsed = json.loads(data.text) # transform the result in json

    #locate your variables
    weather_descriptions = parsed["current"]["weather_descriptions"][0]
    city = parsed["location"]["name"]
    temperature = parsed["current"]["temperature"]

    #create Misty animations with your data!
    print(f"Just letting you know it's {temperature} and {weather_descriptions} in {city}")
    misty.speak(f"Just letting you know it's {temperature} and {weather_descriptions} in {city}")
else:
    print("Failed to get data")
