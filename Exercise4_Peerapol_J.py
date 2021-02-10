mainPerson = []
mainSubject = ["Foundation English","General Business","Introduction to Computer Systems","Computer Programming"]
mainScore = {}
personAndScore = {}

while True:
    name = input("Your name:")
    if name != "":
        mainPerson.append(name)
        for subject in mainSubject:
            score = input(subject+":")
            mainScore.update({subject: score})
        print(mainScore)
        personAndScore.update({name: mainScore})
        print(personAndScore)
    else:
        break

print(personAndScore)

for name in personAndScore:
    print(name)
    for score in personAndScore[name]:
        print(score, ':', personAndScore[name][score])


