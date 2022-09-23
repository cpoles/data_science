import re


def matches(text):
    st_vowel = re.compile(r'^[aeiou]')
    cons_vowel_sound = re.compile(r'([xrty][xrty]+)')
    cons_qus = re.compile(r'(^squ)|(^qu)|(^[^aeiou]+)')
    cons_y = re.compile(r'(^[^aeiou]+)y')
    ay = 'ay'

    if cons_y.match(text):
        if len(text) == 2:
            return text[1:] + text[0] + ay
        result = cons_y.search(text)
        beg = ''.join(list(filter(None, result.groups())))
        end = text[len(beg):]
        return end + beg + ay

    if st_vowel.match(text) or cons_vowel_sound.match(text):
        return text + ay

    if cons_qus.match(text):
        result = cons_qus.search(text)
        beg = list(filter(None, result.groups()))
        end = cons_qus.split(text)[-1]
        return end + ''.join(beg) + ay


def translate(text):
    return ' '.join(list(map(lambda x: matches(x), text.split())))
