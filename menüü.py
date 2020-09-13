import csv
#Failide lugemine tabelisse
kogu_tabel = []

#Avan faili Albumid csv tööriistaga
with open("Albumid", encoding="utf-8") as fail:
    csv_fail = csv.reader(fail, delimiter="\t")
    for rida in csv_fail:
        kogu_tabel.append(rida)


#Teen funktsiooni otsi album, mis ostib failist sisestaud albumi nime ja prindib selle ekraanile
def otsi_Album():
    otsing = input("Sisesta albumi nimi:\n").lower()

    for rida in kogu_tabel:
        if otsing ==rida[1].lower():
            print(rida)

#Teen funktsiooni otsi esitaja, mis ostib failist sisestaud esitaja  nime koos albumitega aasta numbritega
def otsi_esitaja():
    otsing_2 = input("Sisesta esitaja nimi:").lower()
    Juhan = []

    for rida in kogu_tabel:
        if otsing_2 in rida[0].lower() and rida[1].lower() not in Juhan:
            print(rida[1], rida[2])
            Juhan.append(rida[1].lower())

#Teen funktsiooni otsi aasta järgi, mis ostib failist sisestaud aasta numbri ja prindib ekraanile Albumid, mis on sellel aastal ilmunud

def otsi_aasta_järgi():
    otsing_3 = input("Sisesta aasta:").lower()
    Kaarel = []

    for rida in kogu_tabel:
        if otsing_3 in rida[2].lower() and rida[1].lower() not in Kaarel:
            print(rida[1])
            Kaarel.append(rida[1].lower())

#Teen funktsiooni otsi laulu nime järgi, mis ostib failist sisestatud laulu nime ja prindib ekraanile selle loo esitaja, albumi, kust lugu pärit on, ja ilmumis aasta
def osti_laulu_nime_järgi():
    otsing_4 = input("Sisesta loo nimi:").lower()

    for rida in kogu_tabel:
        if otsing_4 in rida[3].lower():
            print(rida[0], rida[1], rida[2])


print("Sisesta 1 kui tahad ostida Albumi nime järgi")
print("Sisesta 2 kui tahad ostida Esitaja järgi")
print("Sisesta 3 kui tahad otsida aasta järgi")
print("Sisesta 4 kui tahad ostida laulu nime järgi")

scr = int(input("Sisesta siia:"))

if scr ==1:
    otsi_Album()
elif scr==2:
    otsi_esitaja()
elif scr==3:
    otsi_aasta_järgi()
elif scr==4:
    osti_laulu_nime_järgi()

else:
    print("Nüüd on jama majas")