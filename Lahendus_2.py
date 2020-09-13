from Laulja import Laulja
from Laul import Laul
from Album import Album
import csv


tabel = []

# loeme faili tabelisse
with open("Albumid", encoding="utf-8") as fail:
    csv_fail = csv.reader(fail, delimiter="\t")
    for rida in csv_fail:
        tabel.append(rida)

albumid = []
lauljad = []
laulud = []

eelmine_laulja = ""
eelmine_album = ""

lauljad_olemas = []
albumid_olemas = []

# laotame tabeli sisu kolme objektiga andmestruktuuri
for rida in tabel:
    laul = Laul(rida[3], rida[0])
    laulud.append(laul)

    if rida[0] not in lauljad_olemas:
        # vajadusel lisame uue laulja
        laulja = Laulja(rida[0])
        lauljad.append(laulja)
        lauljad_olemas.append(laulja.nimi)

    if rida[1] not in albumid_olemas:
        # vajadusel lisame uue albumi
        album = Album(rida[1], rida[2], rida[0])
        laulja.lisa_album(album)
        albumid.append(album)
        albumid_olemas.append(rida[1])

    album.lisa_laul(laul)

kas_jatkata = True
while kas_jatkata:
    print("Tee valik:")
    print("1: väljasta albumid ja laulud")
    print("2: otsing albumi pealkirja või aasta järgi")
    print("3: otsing laulu järgi")
    print("4: otsing laulja järgi")

    valik = input("Valik [1, 2, 3, 4]: ")

    if valik == "1":
        print("Albumid: ")
        for album in albumid:
            album.naita_laulja_ja_nimi()
            album.naita_laulud()
            print("----------------")
    elif valik == "2":
        otsitav = input("Sisesta otsitav album või aasta: ")
        for album in albumid:
            if otsitav.lower() in album.nimetus.lower() or otsitav == album.aasta:
                album.naita_laulja_ja_nimi()
                album.naita_laulud()
    elif valik == "3":
        otsitav = input("Sisesta otsitav laul: ")
        for album in albumid:
            for laul in album.laulud:
                if otsitav.lower() in laul.pealkiri.lower():
                    album.naita_laulja_ja_nimi()
                    laul.naita_pealkiri()
    elif valik == "4":
        otsitav = input("Sisesta otsitav laulja: ")
        for laulja in lauljad:
            if otsitav.lower() in laulja.nimi.lower():
                for album in laulja.albumid:
                    album.naita_laulja_ja_nimi()
    else:
        print("Lõpp")
        kas_jatkata = False
    print("++++++++++++++++++++++++++++++++++++++++")

