# connect to an apis
my_api_key = "GLFivnWdB0XDVbAXau07ZQg4RJNTioZv"
# curl --request GET --url 
url= 'https://api.tomorrow.io/v4/weather/forecast?location=42.3478,-71.0466&apikey=GLFivnWdB0XDVbAXau07ZQg4RJNTioZv'
from tkinter  import *
from PIL import ImageTk, Image
import requests, json

root = Tk()
root.title("Weather app")
root.geometry("1500x600")
root.configure(background="lime")
data = dict()
try:
    api_req = requests.get(url)
    api =  json.loads(api_req.content)
    data = api
    print("data.keys: ",data.keys())
    location = data["location"]
    print("Location: ", location)
    print("timelines keys: ", data["timelines"].keys())
    timeline = data["timelines"]["hourly"]
    #print("Timeline hourly: ", timeline)
    timeline_day = data["timelines"]["daily"]
    print("Timeline daily. keys: ", timeline_day.keys())
except Exception as e:
    api = e #print("Error:" e)

print(data.keys())
print(data.values())

js2 = json.dumps(data, indent=4, sort_keys=True)
with open("data.json", "w") as f:
    f.write( js2)

long = location["lon"]
lat = location["lat"]
location_text = f"Location has logitude {str(long)} and latitude {str(lat)} \n"
print(location_text )
myLabel = Label(root, text=location_text)
myLabel.grid(row=0, column=0 , columnspan=2, padx=0, pady=(20, 0))

daily = timeline_day
string = ""
for item in daily:
    string +=  "\n"
    string += str( item["time"])  + "\n"
    string += str(item["values"])+ "\n"
    
text = "Daily forecast is: "+  string
myLabel2 = Label(root, text=text)
myLabel2.grid(row=2, column=0 , padx=2, pady=(40, 0))




root.mainloop()