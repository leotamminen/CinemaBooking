import random
import csv

def tarkastele_tiedostoja(avattava_tiedosto):
    rivit_tiedostossa = []
    with open(avattava_tiedosto, 'r') as avattu_tiedosto:
        for rivi in avattu_tiedosto:
                rivi = rivi.strip()
                if rivi != "":
                    rivit_tiedostossa.append(rivi)

    for rivi in rivit_tiedostossa:
                
        if rivi[0].isdigit():
            rivi = rivi.replace("_sali", "")
            rivi = "Sali " + rivi
            rivi = rivi.split(",")
            rivi[2] = "Ikäraja: " + rivi[2]
            salin_numero = rivi[0]
            elokuvan_nimi = rivi[1]
            elokuvan_ikaraja = rivi[2]

                
        if rivi[0] == "[":
            rivi = rivi.replace(",", ", ")
            rivi = rivi.replace("[", "")
            rivi = rivi.replace("]", "")
            rivi = f"{salin_numero}, {elokuvan_nimi} ({elokuvan_ikaraja}), vapaat paikat: " + rivi
            print(rivi)

#Tiedostojen ikärajojen perusteella annetaan lukijalle palautetta.
elokuvanimet = {}
elokuvanimet["18"] = "HUOM. TÄMÄ ELOKUVA ON VAIN TÄYSI-IKÄISILLE!"
elokuvanimet["16"] = "Hyvä valinta! Huom. Sinun on oltava yli 15 v katsoaksesi tämän elokuvan."
elokuvanimet["12"] = "Hyvä valinta! Huom. Sinun on oltava yli 12 v katsoaksesi tämän elokuvan."
elokuvanimet["10"] = "Hyvä valinta! Tämä elokuva soveltuu koko perheen katsottavaksi."

#Funktio selvittämään mikä ikäraja elokuvalla on.
def elokuva_ikäraja(tiedosto):
    with open(tiedosto, "r") as tietokanta:
        for rivi in tietokanta:
            if rivi[0] == "1" or rivi[0] == "2" or rivi[0] == "3":
                rivi = rivi.strip().split(",")
                if rivi[1] == elokuva_nimi:
                    if int(rivi[2]) >= 18:
                        return "18"
                        break
                    elif int(rivi[2]) >= 16 and int(rivi[2]) < 18:
                        return "16"
                        break
                    elif int(rivi[2]) >= 12 and int(rivi[2]) < 16:
                        return "12"
                        break
                    elif int(rivi[2]) <= 11:
                        return "10"
                        break

#Funktio jolla tehdään lista elokuvien nimistä.
def uusi(tiedosto):
    lista = []
    with open(tiedosto,) as kova:
        for i in kova:
            if i[0] == "1" or i[0] == "2" or i[0] == "3":
                i = i.strip().split(",")
                lista.append(i[1])
    return lista

#Funktio, joka etsii oikeasta tiedostosta oikean elokuvan paikat aina seuraavalta riviltä.
def Paikat_tiedostosta(tiedosto):
    with open(tiedosto, "r") as tiedosto2:
        laskuri = 0
        for rivi in tiedosto2:
            if laskuri == 1:
                return(rivi)
                break
            if rivi[0] == "1" or rivi[0] == "2" or rivi[0] == "3":
                rivi = rivi.strip().split(",")
                if rivi[1] == elokuva_nimi:
                    laskuri = 1

# Käyttäjän versio paikan varaus. Käytännössä poistetaan paikat tiedostosta. 
print("Tervetuloa käyttämään elokuvateatterin uutta varausjärjestelmää!")
print("Huomioithan, että tämä on pieni elokuvateatteri ja näytösaikoja on vallitsevan koronatilanteen vuoksi vain vähän.")
print("Tällä hetkellä ainoat käytössä olevat näytösajat ovat klo 12.00, 14.00, sekä 16.00. Kiitos ymmärryksestänne.")
print("Valitse mitä haluat tehdä syöttämällä luvun kenttään.")

mita_tehdaan = input("Syötä \"1\" varataksesi paikan yhteen elokuvistamme. Syötä \"2\" jos haluat vain tarkastella varauksia: ")

# Elokuvien nimet
elokuvat_klo_12_nimet = uusi("varaukset_klo_12.csv")
elokuvat_klo_14_nimet = uusi("varaukset_klo_14.csv")
elokuvat_klo_16_nimet = uusi("varaukset_klo_16.csv")

#Varaaminen alkaa tästä
if mita_tehdaan == "1":

    avattava_tiedosto = input("Mihin aikaan haluat mennä katsomaan elokuvaa? (12, 14 tai 16): ")
    kelpaavat = ["12", "14", "16"]
    if avattava_tiedosto not in kelpaavat:
        print("virheellinen syöte")


    print("\n" + f"Kello {avattava_tiedosto} saatavilla olevat näytökset ja varaukset:" + "\n")

    if avattava_tiedosto == "12":
        tarkastele_tiedostoja("varaukset_klo_12.csv")
    elif avattava_tiedosto == "14":
        tarkastele_tiedostoja("varaukset_klo_14.csv")
    elif avattava_tiedosto == "16":
        tarkastele_tiedostoja("varaukset_klo_16.csv")
    else:
        print("Virheellinen syöte.")

    #Käyttäjän elokuvan ja ajan varmistaminen 
    while True:
        elokuva_aika = avattava_tiedosto
        elokuva_nimi =input("Valitse, mihin elokuvaan haluat varata paikan (Ole tarkkana oikeinkirjoituksen kanssa): ")

        if elokuva_aika == "12" or elokuva_aika == "12.00":
            if elokuva_nimi in elokuvat_klo_12_nimet:
                tiedosto ="varaukset_klo_12.csv"
                break
        if elokuva_aika == "14" or elokuva_aika == "14.00":
            if elokuva_nimi in elokuvat_klo_14_nimet:
                tiedosto ="varaukset_klo_14.csv"
                break
        if elokuva_aika == "16" or elokuva_aika == "16.00":
            if elokuva_nimi in elokuvat_klo_16_nimet:
                tiedosto ="varaukset_klo_16.csv"
                break
        else:
            print("En saanut selvää minkä ajan tai elokuvan halusit voitko vastata uudelleen")
    #Ikäraja 
    print(elokuvanimet[elokuva_ikäraja(tiedosto)])

# Varaus: korvataan tiedosto ilman varattua paikkaa, sillä se ei ole enää vapaa.
    while True:

        paikat = Paikat_tiedostosta(tiedosto)
        vanhat_paikat = Paikat_tiedostosta(tiedosto)
        paikat = paikat.replace("\n", "")
        paikat = paikat.replace("]", "")
        paikat = paikat.replace("[", "")
        paikat = paikat.replace("'", "")
        paikat_stringina = paikat.replace(",", ", ")
        paikat_listana = paikat.split(",")
        
        print("Vapaana olevat paikat:", paikat_stringina)

        poistettava_paikka = input("Anna yksi (1) paikan numero, jonka haluat varata (tyhjä lopettaa) ")

        
        if poistettava_paikka == "":
            print("Paikkaa ei varattu.")
            break
        
        elif poistettava_paikka in paikat_listana:
            paikat_listana.remove(poistettava_paikka)

            # Avataan tiedosto lukutilassa ensin.
            lukutila = open(tiedosto, "r")
            korvaus = ""
            # Käytetään for-looppia ja muuttujaa vanhat_paikat, jota tarvirtaan myöhemmin korvaamiseen.
            vanhat_paikat = vanhat_paikat.replace(" ", "")
            vanhat_paikat = vanhat_paikat.strip()
            
            for line in lukutila:
                line = line.strip()
                paikat_listana = str(paikat_listana)
                paikat_listana = paikat_listana.replace("'", "")
                paikat_listana = paikat_listana.replace(" ", "")

                muutokset = line.replace(vanhat_paikat, str(paikat_listana))
                korvaus = korvaus + muutokset + "\n"

            lukutila.close()
            
            # Avataan tiedosto kirjoitustilassa ja kirjoitetaan nyt kaikki edelliset rivit + paikat_listana, josta poistettu paikka.
            kirjoitustila = open(tiedosto, "w")
            kirjoitustila.write(korvaus)
            kirjoitustila.close()

            print(f"Varasit paikan {poistettava_paikka} onnistuneesti.")
            print("Kiitos kun käytit elokuvan varausjärjestelmää! Sinut on nyt kirjattu ulos automaattisesti.")
            break

        else:
            print("Paikkaa ei löytynyt")

if mita_tehdaan == "2":
    print("Olet nyt tarkastelemassa elokuvien varauksia.")
    avattava_tiedosto = input("Minkä kellonajan varauksia haluat tarkastella (12, 14 tai 16): ")

    print("\n" + f"Kello {avattava_tiedosto} saatavilla olevat näytökset ja varaukset:" + "\n")

    if avattava_tiedosto == "12":
        tarkastele_tiedostoja("varaukset_klo_12.csv")
    elif avattava_tiedosto == "14":
        tarkastele_tiedostoja("varaukset_klo_14.csv")
    elif avattava_tiedosto == "16":
        tarkastele_tiedostoja("varaukset_klo_16.csv")
    else:
        print("Virheellinen syöte.")


if mita_tehdaan != "1" and mita_tehdaan != "2":
    print("Virheellinen syöte!")