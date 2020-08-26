def sentence_maker(phrase):
    capitalized = phrase.capitalize()
    interrogatives = ("how","what","why","when","where")

    if phrase.startswith(interrogatives):
        return "{}?".format(capitalized)
    else:
        return "{}.".format(capitalized)

text=[] 

while True:
    user_input = input("Say something: ")
    if user_input == "\end":
        break
    else:
        text.append(sentence_maker(user_input))

print(" ".join(text))