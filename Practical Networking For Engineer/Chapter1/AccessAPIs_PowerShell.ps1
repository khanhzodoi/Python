
$city="Ho Chi Minh City, VN"
$urlx="https://api.openweathermap.org/data/2.5/weather?q="+$city+"&appid=f32a7d9f5cd2ad2d05ff48be965fb0c6"

#send the request to URL using GET Method
$stuff = Invoke-RestMethod -Uri $urlx -Method Get

#wirte raw json
$stuff

#fetch and print latitude and longtitude
write-host ("Longtitude: " + $stuff.coord.lon + "  ,  " + "Latitude: "+ $stuff.coord.lat)
write-host ("The weather status: " +$stuff.weather.main)
