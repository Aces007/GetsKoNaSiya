# I learned some of these from CJ Dojo and Geek Tutotials
def MagkanoBaLahatNgOrange(x):
    OrangesFunc = int(input("Oranges you wish to buy?:" ))
    return x*OrangesFunc


def MagkanoBaLahatNgMansanas(x2):
    MansanasFunc = int(input("Apples you wish to buy?:"))
    return x2*MansanasFunc


def MagkanoBaLahatNgPrutas():
    return AnoPresyoNgOrange + AnoPresyoNgApple


def PakitaAngTotalNgNabili():
    print(f"The total amount is {MagkanoNaNgayon}")


# For the first step, the program will ask for the price of the orange.
AnoPresyoNgOrange = MagkanoBaLahatNgOrange(25)

# Then it will ask for the price of the apples.
AnoPresyoNgApple = MagkanoBaLahatNgMansanas(20)

# Then this variable will add the total amount of your expenditures.
MagkanoNaNgayon = MagkanoBaLahatNgPrutas()

# Lastly, it will then present the total of the expenditures.
PakitaAngTotalNgNabili()

