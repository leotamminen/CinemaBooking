
print("Tervetuloa käyttämään elokuvateatterin varausjärjestelmää." + '\n' + "Olet käyttämässä ylläpitäjän versiota. Aloita syöttämällä luku.")

# Kysytään ensimmäiseksi käyttäjältä, mitä tehdään.
# Jos käyttäjä syöttää "1", päästään lisäämään elokuvia
# Jos "2", listataan elokuvat ja niiden näytökset.


def valittu_kellonaika(tiedosto):
    with open(tiedosto, 'r') as file:
        data = file.readlines()

    for rivi in data:
        if rivi[0] == "1":
            sali1_varaustila = True
        elif rivi[0] == "2":
            sali2_varaustila = True
        elif rivi[0] == "3":
            sali3_varaustila = True

    uusi_elokuva = input("Anna uuden elokuvan nimi: ")
    ikaraja = input("Anna ikäraja elokuvalle: ")


    valitse_sali = input("Anna salin numero 1, 2 tai 3: ")

    if valitse_sali == "1":
        paikat = sali1_paikkamaara

    elif valitse_sali == "2":
        paikat = sali2_paikkamaara

    elif valitse_sali == "3":
        paikat = sali3_paikkamaara
    else:
        print("Virheellinen syöte!")
        
        
    paikat = str(paikat)
    paikat = paikat.replace("'", "")
    paikat = paikat.replace(" ", "")

    

    h = [x[0] for x in data]
    if valitse_sali in h:
        print("Tämä sali on varattu varattu tähän aikaan, ei lisätty mitään.")

    else:
        data[1] =  "\n" + valitse_sali + "_sali" + "," + uusi_elokuva + "," + ikaraja + '\n' + str(paikat) + '\n' + '\n'

        with open(tiedosto, 'w') as file:
            file.writelines(data)
            print(f"Lisättiin elokuva \"{uusi_elokuva}\" saliin {valitse_sali} klo {kellon_aika} onnistuneesti!")

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

        
        if rivi[0] == "[":
            rivi = rivi.replace(",", ", ")
            rivi = rivi.replace("[", "")
            rivi = rivi.replace("]", "")
            rivi = f"{salin_numero}, {elokuvan_nimi}, vapaat paikat: " + rivi
            print(rivi)

sali1_paikkamaara = list(range(1,36))
sali2_paikkamaara = list(range(1,31))
sali3_paikkamaara = list(range(1,21))
sali1_varaustila = False
sali2_varaustila = False
sali3_varaustila = False

while True:
    mita_tehdaan = input("Syötä luku \"1\" lisätäksesi elokuvia ja \"2\" selataksesi varauksia: ")

    if mita_tehdaan == "1":
            
        print('\n' + "Valitse kellonaika, jolle haluat lisätä näytöksen." + '\n' + "Mahdolliset näytösajat ovat kello 12.00, 14.00 ja 16.00")

        kellon_aika = input("Anna kellonaika 12, 14 tai 16: ")

        if kellon_aika == "12":
            tarkastele_tiedostoja("varaukset_klo_12.csv")
        elif kellon_aika == "14":
            tarkastele_tiedostoja("varaukset_klo_14.csv")
        elif kellon_aika == "16":
            tarkastele_tiedostoja("varaukset_klo_16.csv")
        else:
            print("Virheellinen syöte.")        

        def salien_vapaustila(tiedosto):
            with open(tiedosto, 'r') as file:
                data = file.readlines()

            for rivi in data:
                if rivi[0] == "1":
                    sali1_varaustila = True
                elif rivi[0] == "2":
                    sali2_varaustila = True
                elif rivi[0] == "3":
                    sali3_varaustila = True

            if sali1_varaustila == True and sali2_varaustila == True and sali3_varaustila == True:
                print("Kaikki salit varattu!")
            elif sali1_varaustila == True and sali2_varaustila == True:
                print("Vain sali 3 vapaa!")
            elif sali1_varaustila == True and sali3_varaustila == True:
                print("Vain sali 2 vapaa!")
            elif sali2_varaustila == True and sali3_varaustila == True:
                print("Vain sali 1 vapaa!")
            elif sali1_varaustila == True:
                print("Salit 2 ja 3 vapaita!")
            elif sali2_varaustila == True:
                print("Salit 1 ja 3 vapaita!")
            elif sali3_varaustila == True:
                print("Salit 1 ja 2 vapaita!")




        if kellon_aika == "12":
            valittu_kellonaika("varaukset_klo_12.csv")
        elif kellon_aika == "14":
            valittu_kellonaika("varaukset_klo_14.csv")
        elif kellon_aika == "16":
            valittu_kellonaika("varaukset_klo_16.csv")
        else:
            print("Virheellinen syöte.")
        break

    if mita_tehdaan == "2":

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


    elif mita_tehdaan == "":
        print("Kiitos kun käytit ohjelmaa ylläpitäjänä! Sinut on nyt kirjattu ulos.")
        break

    else:
        print("Virheellinen syöte! Yritä uudelleen.")