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


AnoPresyoNgOrange = MagkanoBaLahatNgOrange(25)

AnoPresyoNgApple = MagkanoBaLahatNgMansanas(20)

MagkanoNaNgayon = MagkanoBaLahatNgPrutas()

PakitaAngTotalNgNabili()





