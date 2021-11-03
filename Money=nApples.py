def MagkanoPeraNaHawakMoNgayon():
    PeraNaMeronkaNgayon = int(input("How much money do you currently have?:"))
    return PeraNaMeronkaNgayon


def GaanoKamahalBaAngMansanas():
    MagkanoBaYungMansanas = int(input("How much does the apple cost?:"))
    return MagkanoBaYungMansanas


def MansanasNaKayaMongMabili():
    ApplesNaMabibiliMo = int(MagkanoHawakMoNgayon) // (MagkanoBaPresyoNgMansanas)
    return ApplesNaMabibiliMo


def ItoLahatNgSukliMo():
    MagkanoMatitiraSaPeraMo = int(MagkanoHawakMoNgayon) % (MagkanoBaPresyoNgMansanas)
    return MagkanoMatitiraSaPeraMo


def MagkanoLahatNgNagastosKo():
    print(f"You can buy {MabibiliMongApple} apples and your change is {SukliMoAy}")


# 1stStep: These lines will ask for the money you possess right now and the price of the apple you want to purchase.
MagkanoHawakMoNgayon = MagkanoPeraNaHawakMoNgayon()
MagkanoBaPresyoNgMansanas = GaanoKamahalBaAngMansanas()

# 2ndStep: Then this will perform the math, and calculate the number of apples that you can buy with your money 
# and consequently it will show the amount of change you will receive from your purchase.
MabibiliMongApple = MansanasNaKayaMongMabili()
SukliMoAy = ItoLahatNgSukliMo()

# Lastly, this will present the total of your expenditures all in all.
MagkanoLahatNgNagastosKo()


# I did not insert any parameters in this program since it was not necessary.
# Throughout the process of learning the fundamentals, I learned that 2 spaces between each line is a tradition.