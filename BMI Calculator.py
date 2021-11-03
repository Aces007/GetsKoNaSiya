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

HeightInMeters = GaanoKaKatangkad()

WeightInKg = GaanoKaKabigat()

BMIMo = WhatIsYourBMI()

PakitaNaAngSummary = BioSummary()

Results = BMIResult()