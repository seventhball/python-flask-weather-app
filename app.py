from flask import Flask, render_template,request
	#api = '4f72f589522b286795311f69ddbf95fe'
import requests, json

app = Flask(__name__)
  
@app.route('/', methods =['POST', 'GET'])
def weather():
    if request.method == 'POST':
        CITY = request.form['city']
    else:
        CITY = "Hyderabad"
    BASE_URL = "https://api.openweathermap.org/data/2.5/weather?"
    API_KEY =  '4f72f589522b286795311f69ddbf95fe'
    URL = BASE_URL + "q=" + CITY + "&appid=" + API_KEY
    response = requests.get(URL)
    if response.status_code == 200:     
        data = response.json()
        descp=data['weather']
        required_data={
            "country_code":str(data['sys']['country']),
            "temp":str(data['main']['temp'])+'k',
            "pressure":str(data['main']['pressure']),
            "humidity":str(data['main']['humidity']),
            "name":str(data['name']),
            "desc":str(descp[0]['description'])
        }

    else:
        print("Error in the HTTP request")
        required_data={
        }
   # print(required_data)    
    return render_template('index.html',data=required_data)    

if __name__ == '__main__':
    app.run(debug = True)        