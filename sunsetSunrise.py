import requests
url = "https://api.sunrise-sunset.org/json?lat=40.4167&lng=-3.70325"
json = requests.get(url).json()
print ("La latitud en Madid es: 40.4167")
print ("La longitud en Madid es: -3.70325")
print ("La hora del amanecer en Madid es:", json['results']['sunrise'])
print ("La hora de la puesta de sol en Madrid es:", json['results']['sunset'])