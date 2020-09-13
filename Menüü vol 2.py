class Album():

    def __init__(self, albumi_nimi):
        self.albumi_nimi = albumi_nimi
#Teen objekti album, kus on tema põhiomadus - tema nimi


class Laul():
    def __init__(self, laulu_nimi):
        self.laulu_nimi = laulu_nimi
#Teen objekti Laul, kus on tema põhiomadus - tema nimi

class lauljad():

    def __init__(self, laulja_nimi):
        self.laulja_nimi = laulja_nimi
#Teen objekti lauljad, nende omadusega - laulja nimi

fail = open("albumid.txt", encoding="UTF-8")
kogu_tabel = []
#Avan faili ja loen selle järjendisse.
x = input("Kas soovid otsida albumi nime järgi? jah/ei")


def album_otsi():
     otsi = input("Sisesta albumi nimi:")
     for rida in fail:
         elemendid = rida.split("\t")
         esineja = lauljad(elemendid[0])
         album = Album(elemendid[1])
         kogu_tabel.append(elemendid[1])
         aasta = elemendid[2]
         laul = Laul(elemendid[3])
         if otsi == elemendid[1]:
             print(esineja.laulja_nimi, album.albumi_nimi, aasta, laul.laulu_nimi)
#Kasutan funktsiooni album_otsi, mis otsib järjendist albumi nime ja väljastab ekraanile selle omadused.



def esitaja_otsi():

    Juhan = []
    otsi = input("Sisesta esitaja nimi:")
    for rida in fail:
        elemendid = rida.split("\t")
        esineja = lauljad(elemendid[0])
        album = Album(elemendid[1])
        kogu_tabel.append(elemendid[1])
        aasta = elemendid[2]
        laul = Laul(elemendid[3])
        if otsi == elemendid[0] and otsi not in Juhan:
            print(album.albumi_nimi, aasta)
            Juhan.append(elemendid[0])
#Kasutan funktsiooni esitaja_otsi, mis otsib järjendist  esitaja nime ja väljastab ekraanile selle omadused.

def aasta_otsi():
    Kaarel = []
    otsi = input("Sisesta aasta number:")
    for rida in fail:
        elemendid = rida.split("\t")
        esineja = lauljad(elemendid[0])
        album = Album(elemendid[1])
        kogu_tabel.append(elemendid[1])
        aasta = elemendid[2]
        laul = Laul(elemendid[3])
        if otsi == elemendid[2]:
            if elemendid[1] not in Kaarel:
                print(esineja.laulja_nimi, album.albumi_nimi)
                Kaarel.append(elemendid[1])
#Kasutan funktsiooni aasta_otsi, mis otsib järjendist aasta ja väljastab ekraanile selle omadused.

def laulu_nimi_otsi():
    otsi = input("Sisesta laulu nimi:")
    for rida in fail:
        kogu_tabel.append(rida)
        elemendid = rida.split("\t")
        esineja = lauljad(elemendid[0])
        album = Album(elemendid[1])
        aasta = elemendid[2]
        laul = Laul(elemendid[3])
        if otsi in elemendid[3]:
            print(esineja.laulja_nimi, album.albumi_nimi, aasta)
#Kasutan funktsiooni laulu_nimi_otsi, mis otsib järjendist laulu nimeja väljastab ekraanile selle omadused.

if x == "jah":
    album_otsi()
else:
    xx = input("Kas soovid otsida albumi esitaja järgi? jah/ei")


    if xx == "jah":
        esitaja_otsi()
    else:
        yyy = input("Kas soovid otsida albumi aasta järgi? jah/ei")
        if yyy == "jah":
            aasta_otsi()
        else:
            yxy = input("Kas soovid otsida albumi laulu nime järgi? jah/ei")
            if yxy == "jah":
                laulu_nimi_otsi()
            else:
                print("Nüüd on jama majas")
#Tingimus laused, mis määravad teksi kuvamise järjekorra ekraanile.













