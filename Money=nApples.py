def MagkanoPeraNaHawakMoNgayon():
    PeraNaMeronkaNgayon = int(input("How much money do you currently have?:"))
    return PeraNaMeronkaNgayon


def GaanoKamahalBaAngMansanas():
    MagkanoBaYungMansanas = int(input("How much does the apple cost?:"))
    return MagkanoBaYungMansanas


def MansanasNaKayaMongMabili():
    ApplesNaMabibiliMo = int(TotalNgPeraNaKayaMoGastusin) // (TotalNgMansanasNaGustoMo)
    return ApplesNaMabibiliMo


def ItoLahatNgSukliMo():
    MagkanoMatitiraSaPeraMo = int(TotalNgPeraNaKayaMoGastusin) % (TotalNgMansanasNaGustoMo)
    return MagkanoMatitiraSaPeraMo


def MagkanoLahatNgNagastosKo():
    print(f"You can buy {MabibiliMongApple} apples and your change is {SukliMoAy}")


TotalNgPeraNaKayaMoGastusin = MagkanoPeraNaHawakMoNgayon()
TotalNgMansanasNaGustoMo = GaanoKamahalBaAngMansanas()


MabibiliMongApple = MansanasNaKayaMongMabili()
SukliMoAy = ItoLahatNgSukliMo()


MagkanoLahatNgNagastosKo()