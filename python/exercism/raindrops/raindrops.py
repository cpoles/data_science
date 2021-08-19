def convert(number):
    raindrops = str()

    if number % 3 == 0:
        raindrops += "Pling"
    if number % 5 == 0:
        raindrops += "Plang"
    if number % 7 == 0:
        raindrops += "Plong"

    if len(raindrops) == 0:
        return str(number)
    else:
        return raindrops
