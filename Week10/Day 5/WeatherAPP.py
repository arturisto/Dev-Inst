from pyowm import OWM
from matplotlib import pyplot as plt
from datetime import datetime



def weather_data(city, country_code):
    try:
        owm = OWM("c7944fb01f126e8605540d01be0dc854")
    except:
        print("there was problem with the token")
        return

    registry = owm.city_id_registry()
    list_of_cities = registry.ids_for(city)

    # get the desired city code
    for item in list_of_cities:
        if item[2] == country_code:
            city_code = item[0]
            break
    else:
        print(f"there is no {city} in {country_code} ")
        return
    w_manager = owm.weather_manager()
    try:
        weather = w_manager.weather_at_place(f'{city}, {country_code}').weather
    except:
        print("there was an error retrieving the data ")
    temp = weather.temperature('celsius')["temp"]
    sunrise_time = weather.sunrise_time(timeformat='date')
    sunset_time = weather.sunset_time(timeformat='date')
    wind = weather.wnd  # dict {speed, deg}
    forecast = w_manager.forecast_at_id(city_code, "3h")
    print(f""" Today weather in {city},{country_code} is:
            temp        :{temp} celsius
            sunrise_time:{sunrise_time}
            sunset_time :{sunset_time}
            wind        :{wind["speed"]}kmh, {wind["deg"]} deg' 
            """)

    # polution data

    # first get the coordinates
    city_location = registry.locations_for(city, country=country_code)
    city_lat = city_location[0].lat
    city_lon = city_location[0].lon
    # # coi = owm.coindex_around_coords(city_lat, city_lon)
    # coi = owm.airpollution_manager().coindex_around_coords(city_lat, city_lon)
    #
    # print(coi)

    # calculate data for humidity plot
    forcasted_weather = []
    set_of_dates = []
    # get data from the forecast object
    for item in forecast.forecast.weathers:
        # format date string for printing (DD/MM)
        forecast_date = str(datetime.fromtimestamp(item.ref_time).day) + "/" + str(
            datetime.fromtimestamp(item.ref_time).month)
        # create list of tuple with data (humidity level, date)
        forcasted_weather.append([item.humidity, forecast_date])
        # create set of dates, because the date strings are not sortable, the "set" is created manually
        if not forecast_date in set_of_dates:
            set_of_dates.append(forecast_date)
    print(set_of_dates)

    # calculate average humidity level for each day
    avg_humidty_lvls = []
    for item in set_of_dates:
        list_to_calc_avg = [x[0] for x in forcasted_weather if x[1] == item]
        avg_humidty_lvls.append(round(sum(list_to_calc_avg) / len(list_to_calc_avg), 2))

    print(avg_humidty_lvls)
    for x in forcasted_weather:
        print(x)

    plt.bar(set_of_dates,avg_humidty_lvls,align="center")
    plt.xlabel("Dates")
    plt.ylabel("Humidity Levels (%)")
    plt.title("Humidity Forecast")
    plt.show()

def main():
    # while True:
    #     city = input("Enter a city: ")
    #     if not all(letter.isalpha() or letter.isspace() for letter in city):
    #         print("bad input, try again")
    #         continue
    #     country = input("enter a country: ")
    #     if not country.isalpha() or not 0 < len(country) < 3:
    #         print("bad input, try again")
    #         continue
    #
    #     weather_data(city, country.upper())
    weather_data("Tel Aviv", "IL")


if __name__ == "__main__":
    main()
