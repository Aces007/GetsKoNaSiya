def AnoPangalanMo():
    PangalanMoPo = input("What's your name?: ")
    return PangalanMoPo


def AnongEdadMoNa():
    WhatsYourAge = input("What is your Age?: ")
    return WhatsYourAge


def SaanKaPoNakatira():
    WhereDoYouLive = input("What's your Address?: ")
    return WhereDoYouLive


def GaanoKaKatangkad():
    AnoPoHeightMoMeters = float(input("How tall are you?: "))
    return AnoPoHeightMoMeters
    

def GaanoKaKabigat():
    AnoNamanWeightMoKg = int(input("What is your weight?: "))
    return AnoNamanWeightMoKg


def WhatIsYourBMI():
    YourBMI = WeightInKg / (HeightInMeters ** 2)
    print("BMI: ")
    print(YourBMI)
    if YourBMI < 25:
        return "normal"
    else: 
        return "overweight"


def BioSummary():
    print(f"Hi, my name is {PangalanMo}. I am {EdadMo} and I live in {SaanKaNakatira}.")


def BMIResult():
    print(f"I am {HeightInMeters}m tall, I weigh {WeightInKg}kg and my classfication is {BMIMo}.")


# The first step is the program asking for your name.
PangalanMo = AnoPangalanMo()

# The second step is for you to provide your age.
EdadMo = AnongEdadMoNa()

# The third step now is providing your address. 
SaanKaNakatira = SaanKaPoNakatira()

# Now for the next step is providing your height in meters.
HeightInMeters = GaanoKaKatangkad()

# Then for the 5th step is you provide your weight in kg.
WeightInKg = GaanoKaKabigat()

# And then in orderly fashion the program will provide you your BMI results.
BMIMo = WhatIsYourBMI()

# This will summarize all the information you provided the program.
PakitaNaAngSummary = BioSummary()

# The program will also provide you with your BMI classification.
Results = BMIResult()


# I tried this program initially on my youngest brother since we are trying to lower his weight so
# we needed to know his BMI classification as a start. 
# We found out that he is overweight hahahahaha lol.

# When I was revising this program I could not push the changes through git bash so I got frustrated a little
# I found out that changing the name of the file and pushing it again is a mistake but I was too late since 
# I deleted the file on account of my frustration so I reverted my commits and recovered the file then
# learned to use git reset --mixed origin/master so I could upload my file sucessfully.
