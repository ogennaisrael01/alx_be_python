# Ask the user for the current weather condition 
check_weather = input("What's the weather like today? (sunny/rainy/cold): ")

 
if check_weather == "sunny":
    print(" Wear a t-shirt and sunglasses.")
elif check_weather == "rainy":
    print(" Don't forget your umbrella and a raincoat.")
elif check_weather == "cold":
    print(" Make sure to wear a warm coat and a scarf.")
else:
    print("Sorry, I don't have recommendations for this weather.") #display default message if dosent match user input