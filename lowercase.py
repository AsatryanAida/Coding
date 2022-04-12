import re

def to_underscore(string):
    if type(string) == int:
        string = str(string)
    else:
        string = re.sub( r"([AZ])", r" \1", string).split()
        string = '_'.join(string)
        print(string.lower())      
    return string

to_underscore('TestController')