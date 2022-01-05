def convert(number):
    raindrops = {3: 'Pling', 5: 'Plang', 7:'Plong'}
    sound = ''

    for key in raindrops:
        if number % key == 0:
            sound += raindrops[key]
    
    if sound == '':
        return str(number)

    return sound


    