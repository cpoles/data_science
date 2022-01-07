import re

def abbreviate(words):
    tokens = re.findall(r"[a-zA-Z]+(?:'[a-z]+)?", words)

    return ''.join(list(map(lambda x: x[0].upper(), tokens)))
   
