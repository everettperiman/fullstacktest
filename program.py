import urllib
import json
import time


class location_loader(object):
    
    weather_api_url = "https://api.weather.gov/points/"
    
    def __init__(self, latitude, longitude):
         self.api_url = self.weather_api_url + latitude + "," + longitude
        
    def get_current_info(self):
        daily_forecast_url = self.get_hourly_url(self.api_url)
        forecast_data = self.get_api_info(daily_forecast_url)
        daily_forecast = forecast_data["properties"]["periods"][:24]
        self.daily_forecast = daily_forecast
        print(daily_forecast)
        print(forecast_data["properties"]["generatedAt"])
        print(forecast_data["properties"]["elevation"]["value"])

    def get_hourly_url(self, url):
        response_json = self.get_api_info(url)
        hourly_url = response_json["properties"]["forecastHourly"]
        return hourly_url
        
    def get_api_info(self, url):
        response = urllib.request.urlopen(url)
        response_string = response.read()
        response_jsonified = response_string.decode('utf8').replace("'", '"')
        response_json = json.loads(response_jsonified)
        return response_json
    
        
if __name__ =="__main__":
    detroit_lat = "42.331429"
    detroit_lon = "-83.045753"
    seattle_lat = "47.6062"
    seattle_lon = "-122.3321"
    
    detroit = location_loader(detroit_lat, detroit_lon)
    detroit.get_current_info()
    
    seattle = location_loader(seattle_lat, seattle_lon)
    seattle.get_current_info()