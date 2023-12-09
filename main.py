import pearl

# pearl.speak("Hello sir! How can I help you today?")
pearl.speak("Good Morning !")
date = pearl.get_date()
time = pearl.get_time()
weather_report_today = pearl.get_weather_report()
pearl.speak(date)
pearl.speak(time)
pearl.speak(weather_report_today)
