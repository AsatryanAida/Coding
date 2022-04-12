def spin_words(sentence):
    accumulator = ""
    phrases=sentence.split()
    for phrase in phrases:
        if len(phrase)>4:
            a=list(phrase)
            a.reverse()
            accumulator += "".join(a) + " "
        else:
            accumulator += phrase + " "
    return accumulator.strip()

print(spin_words('Hello world'))