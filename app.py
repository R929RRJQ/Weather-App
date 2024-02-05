import requests
from flask import Flask, render_template, request

app = Flask(__name__)

def get_weather_data(city):
    base_url = "https://api.weatherbit.io/v2.0/current"
    api_key = "7937beb3dc134701a91c4ac248d42587"
    params = {
            "key": api_key,
            "city": city,
            }
    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status()  # Check for errors
        data = response.json()
        return data
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return None

@app.route('/', methods=['POST', 'GET'])
def index():
    weather_data = None
    if request.method == 'POST':
        city = request.form['city']
        weather_data = get_weather_data(city)
        print(city)
    return render_template('index.html', weather_data=weather_data)

if __name__ == '__main__':
    app.run(debug=True,port=5050)