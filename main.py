from flask import Flask, render_template, request
import requests

app = Flask(__name__)

API_KEY = 'a93aa6c0db6d7e6cb73fdf50eb9926de'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/weather', methods=['POST'])
def weather():
    city = request.form['city']
    url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric'

    print(url)  
    response = requests.get(url)
    data = response.json()
    print(data) 

    if data.get('cod') == 200:
        weather_info = {
            'city': city.title(),
            'temperature': data['main']['temp'],
            'description': data['weather'][0]['description'],
            'humidity': data['main']['humidity']
        }
        return render_template('result.html', weather=weather_info)
    else:
        error = "City not found! Please enter a valid city name."
        return render_template('index.html', error=error)
    city = request.form['city']
    url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric'

    response = requests.get(url)
    data = response.json()

    if data['cod'] == 200:
        weather_info = {
            'city': city.title(),
            'temperature': data['main']['temp'],
            'description': data['weather'][0]['description'],
            'humidity': data['main']['humidity']
        }
        return render_template('result.html', weather=weather_info)
    else:
        error = "City not found! Please enter a valid city name."
        return render_template('index.html', error=error)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=81)