sunny=0
rainy=0
cold=0
weather = str (input("What's the weather like today? (sunny/rainy/cold): "))


if weather < sunny:
    print("Wear a t-shirt and sunglasses.")
elif weather < rainy:
    print("Don't forget your umbrella and a raincoat.")
elif weather < cold:
    print("Make sure to wear a warm coat and a scarf.")
else:
    print("Sorry, I don't have recommendations for this weather.")

print(f"the clothing recommendation based on the weather condition provided by the user", sunny, rainy, cold)