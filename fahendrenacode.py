print("Bonjour !")
name = str(input("Votre nom s'il vous plait : "))
age = int(input("Pouvez-vous entrer votre âge içi : "))
if (age < 18):
    print("Donc {}, vous êtes mineur, car votre âge est {} < 18.".format(name, age))
else:
    print("Donc {}, vous êtes majeur, car votre âge est {} > 18.".format(name, age))
