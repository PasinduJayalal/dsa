import csv
class NYCWeather:
    def __init__(self):
        self.data = {}
    
    def add(self, date, temperature):
        self.data[date] = temperature
        
    def average_temperature(self):
        return sum(self.data.values()) / len(self.data)
    
    def max_temperature(self):
        return max(self.data.values())
    
    def print_temp_by_date(self, date):
        if date in self.data:
            print(f"Temperature on {date}: {self.data[date]}")
        else:
            print(f"No data for {date}")
    
if __name__ == "__main__": 
    weather = NYCWeather()
    with open("nyc_weather.csv", newline="") as f:
        reader = csv.DictReader(f)  
        for row in reader:
            date = row["date"].strip()
            temp = float(row["temperature(F)"])
            weather.add(date, temp)
            print(f"Date: {date}, Temperature: {temp}")

    print(f"Average Temperature: {weather.average_temperature()}")
    print(f"Max Temperature: {weather.max_temperature()}")
    weather.print_temp_by_date("Jan 9")
    

            
        
       

  
    

   