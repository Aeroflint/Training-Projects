import pyowm

owm = pyowm.OWM('6d00d1d4e704068d70191bad2673e0cc', language = "ru")


place = input("Укажите Ваш город: ")
# Search for current weather in London (Great Britain)
observation = owm.weather_at_place(place)
w = observation.get_weather()

temp = w.get_temperature('celsius')["temp"]

print( "В городе " + place + " около " + w.get_detailed_status())

print("Температура на улице примерно " + str(temp))


if temp < 10:
    print("На улице холодно, Бррр")
elif temp < 20:
    print("Хорошоая погода, только одевайся, чтобы не замерзнуть")
else:
    print("Сейчас жаришка, самое время принять солнечные ванны! :)")