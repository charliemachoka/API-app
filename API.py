import requests

def weather_search(query):
    api_key = '&appid=f990fe84509fde267d7f0707e52b3e33'
    url = "http://api.openweathermap.org/data/2.5/weather?q="
    city = query
    result = requests.get(url+city+api_key)
    data = result.json()
    return data 

def main():
    while True:
        try:
            query = str(input("Enter the Name of the city"))
            break
        except:
            print("enter a valid city of name")

    return weather_search(query)

if __name__ == "__main__":
    print (main())
    


print(weather_search())


