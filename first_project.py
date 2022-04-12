def split(s):
    return [char for char in s]

def last_survivor(letters, coords): 
    l=len(letters)
    new=split(letters)
    for n in range(0,l-2):
        m=coords[n]
        new.pop[m]
    return ''.join(new)

last_survivor('abs', [0, 1])