import requests
city="Ho Chi Minh City, VN "
#this would give a sample data of the city that was used in the variable
urlx="https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid=f32a7d9f5cd2ad2d05ff48be965fb0c6"

#send the request to URL using GET Method
r = requests.get(url = urlx)
output=r.json()

#parse the valuable information from the return JSON
print("Raw JSON \n")
# Reformat json file to be more clear
output = json.dumps(output, indent=4, separators=(". ", " = "))
print(output)
print("\n")

#fetch and print latitude and longtitude
citylongtitude=output['coord']['lon']
citylatitude=output['coord']['lat']
print("Longtitude: " + str(citylongtitude) + " , " + "Latitude: "
      + str(citylatitude))
print("The weather status: " + str(output['weather'][0]['main']))
