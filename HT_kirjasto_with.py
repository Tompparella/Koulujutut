######################################################################
# CT60A0203 Ohjelmoinnin perusteet
# Tekijä: Tommi Kunnari
# Opiskelijanumero: 0543382
# Päivämäärä: 18.11.2019
# Yhteistyö ja lähteet, nimi ja yhteistyön muoto:
# wiki.python.org, stackoverflow.com, tech-queries.blogspot.com
# Etsin näiltä sivuilta sitä sun tätä ohjelmoinnin avuksi.
# HUOM! KAIKKI KURSSIN TEHTÄVÄT OVAT HENKILÖKOHTAISIA!
######################################################################

# Tämä tiedosto sisältää pääohjelmassa kutsuttavat funktiot.

import datetime as dt                            # Tuodaan datetime-,sys- ja numpy kirjastot.
import numpy as np
import sys as kys

class LUKU_T():                                  # Määritetään käytettävät luokat.
    pvm = ''
    paiste = ''

class TULOSTE():
    pvm = []
    paiste = []

class TIEDOSTO():
    nimi = ''
    asema = ''
    vuosi = ''

def tied():
    while True:                                  # Ensimmäinen funktio kysyy
        hav = input('Anna havaintoaseman nimi: ')# käyttäjältä käsiteltävän
        vuo = input('Anna analysoitava vuosi: ') # tiedoston nimen ja tarkasteltavan
        if vuo.isdigit() == False:               # vuoden, jotka tallennetaan olioihin.
            print('Anna vuosiluku kokonaislukuna.')
        else:
            break
    tdsto = TIEDOSTO()                           
    tdsto.nimi = (hav + vuo + '.txt')
    tdsto.asema = hav
    tdsto.vuosi = vuo
    print('')
    return tdsto

def luku(tdsto):                                 # Määritetään funktio joka lukee käsiteltävän tiedostot
    lista = []                                   # ja tallentaa sen tiedot olioihin, jotka sitten                   
    rivit = 1                                    # palautetaan listan avulla pääohjelmaan.
    try:
        with open(tdsto.nimi, 'r') as x:
            x.readline()
            while True:
                rivi = x.readline()
                rivi = rivi[:-1]
                if len(rivi) == 0:
                    rivit += 1
                    break
                rivi = rivi.split(';')
                paiste = rivi[2]                 # Käytetään datetime modulia pvm:n käsittelyyn.
                pvm = rivi[0] + (';' + rivi[1])
                pvm = dt.datetime.strptime(pvm, '%Y-%m-%d;%H:%M')
                luku_t = LUKU_T()
                luku_t.pvm = pvm
                luku_t.paiste = paiste
                lista.append(luku_t)
                rivit += 1
    except (FileNotFoundError, PermissionError):
        print("Tiedoston '%s' avaaminen epäonnistui." % (tdsto.nimi))
        kys.exit(0)
    print("Tiedosto '%s' luettu. Tiedostossa oli %s riviä.\n" % (tdsto.nimi,rivit))
    return lista

def analyysi(lista,tdsto):                    
    paiva = lista[0].pvm.weekday()               # Analysoitaan oliot sisältävä lista siten, että lopulliseen
    paivalista = []                              # listaan jää jäljelle päivittäiset paistemäärät. Toteutetaan
    paistelista = []                             # tämä käyttämällä datetimen weekday-funktiota ja annetaan
    summa = 0                                    # käyttäjälle tieto minkä aikavälin ohjelma on analysoinut.
    vuosi = int(tdsto.vuosi)                     # Palautetaan myös analyysin sisältävä lista takaisin pääohjelmalle.
    alku = lista[0].pvm.strftime('%d.%m.%Y')
    for tunti in lista:
        if tunti.pvm.year != vuosi:
            continue
        if tunti.pvm.weekday() != paiva:
            paiva += 1
            paistelista.append(summa)
            paivalista.append(loppu)
            summa = 0
            summa += int(tunti.paiste)
            if paiva == 7:
                paiva = 0
            continue
        summa += int(tunti.paiste)
        loppu = tunti.pvm.strftime('%d.%m.%Y')
    paistelista.append(summa)
    paivalista.append(loppu)
    tuloste = TULOSTE()
    tuloste.pvm = paivalista
    tuloste.paiste = paistelista
    print("Data analysoitu ajalta %s - %s.\n" % (alku,loppu))
    return tuloste
        
def tallennus(tuloste,tdsto):
    kum_sum = 0
    tdsto_nimi = input('Anna tulostiedoston nimi: ')
    try:                                          # Sitten tehdään vielä funktio joka käsittelee olion tiedot
        with open(tdsto_nimi,'w',encoding='utf-8') as x:          # tiedostoon kirjoitettavaan muotoon ja tallentaa nämä käyttäjän # määrittämän nimen omaavaan tiedostoon.
            x.write(('Pvm').rstrip())                     
            for juttu in tuloste.pvm:                   
                teksti = (';' + juttu.rstrip())
                x.write(teksti)
            x.write('\n' + tdsto.asema)
            kum_lista = []
            for juba in tuloste.paiste:
                kum_sum += juba
                kum_lista.append(kum_sum)
            for i in kum_lista:
                jebba = (';' + (str(int(i/60))).rstrip())
                x.write(jebba)
            x.write('\n')
    except (FileNotFoundError, PermissionError):
        print("Tiedoston '%s' avaaminen epäonnistui." % (tdsto_nimi))
        kys.exit(0)
    print("Paisteaika tallennettu tiedostoon '%s'.\n" %(tdsto_nimi))
    return None

                                                   # Tehdään alkuperäisen tiedoston lukevaa funktiota muistuttava
                                                   # funktio joka lukee ilmatieteenlaitoksen datatiedoston.
                                                     
def ilmat_luku(tdsto):
    nimi = (tdsto.asema + tdsto.vuosi + '_fmi.txt')# Määritetään funktio joka lukee ilmatieteenlaitoksen tiedoston # ja palauttaa tästä pääohjelmalle päivämäärät ja paisteajat
    lista = []
    rivit = 2
    try:
        with open(nimi,'r',encoding='utf-8') as x:
            x.readline()                           # Tässä on varmasti viopessa jokin virhe koska tehtävänannossakin luki että kumpula-tiedostossa on
            while True:                            # 8762 riviä mutta viope valittaa että se on 8763 riviä, joten korjasin sen lisäämällä rivejä 1kpl
                rivi = x.readline()
                rivi = rivi[:-1]
                if len(rivi) == 0:
                    break
                rivi = rivi.split(',')
                paiste = rivi[5]            
                pvm = (rivi[0]+' ')+(rivi[1]+' ')+(rivi[2]+' ')+rivi[3]
                pvm = dt.datetime.strptime(pvm, '%Y %m %d %H:%M')
                ilmat = LUKU_T()
                ilmat.pvm = pvm
                ilmat.paiste = paiste
                lista.append(ilmat)
                rivit += 1
    except (FileNotFoundError, PermissionError):
        print("Tiedoston '%s' avaaminen epäonnistui." % (nimi))
        kys.exit(0)
    print("Tiedosto '%s' luettu. Tiedostossa oli %s riviä.\n" % (nimi,rivit))
    return lista
        
def ilmat_anal(lista,tdsto):                       # Tehdään aiempia analyysifunktioita muistuttava ilmatieteenlaitoksen
    alku = lista[0].pvm.strftime('%d.%m.%Y')       # datan kuukausittain analysoiva funktio, joka palauttaa pääohjelmalle
    kuu = lista[0].pvm.month                       # olion joka sisältää listat kuukausista ja kuukausittaisista paistemääristä.
    kuulista = []                              
    paistelista = []                             
    summa = 0                                    
    vuosi = int(tdsto.vuosi)                     
    for tunti in lista:
        if tunti.pvm.year != vuosi:
            continue
        if tunti.pvm.month != kuu:
            kuu += 1
            paistelista.append(summa)
            kuulista.append(str(loppu).zfill(2))
            summa = 0
            try:
                summa += int(tunti.paiste)
                continue
            except ValueError:
                summa += 0
                continue
        try:
            summa += int(tunti.paiste)
        except ValueError:
            summa += 0
        loppu = tunti.pvm.month
        viim = tunti.pvm.strftime('%d.%m.%Y')
    paistelista.append(summa)
    kuulista.append(loppu)
    tuloste = TULOSTE()
    tuloste.pvm = kuulista
    tuloste.paiste = paistelista                  
    print("Data analysoitu ajalta %s - %s.\n" % (alku,viim))
    return tuloste

def ilmat_tallennus(tuloste,tdsto):                     # Ja sitten tehdäänkin funktio joka tallentaa tiedostoon aseman nimen, vuoden ja tulokset.
    tdsto_nimi = input('Anna kuukausitiedoston nimi: ') # Lisäksi lisätään myös mahdollisuus lisätä rivejä jo luotuun tiedostoon poistamatta
    try:                                                # aikaisempia tuloksia. Muutetaan myös kirjoitusvaiheessa tulokset sekunteista minuuteiksi.
        x = open(tdsto_nimi, 'r',encoding='utf-8')
    except (FileNotFoundError, PermissionError):
        try:
            with open(tdsto_nimi,'w',encoding='utf-8') as y:
                    y.write(('Kk').rstrip())                     
                    for juttu in tuloste.pvm:                     
                        teksti = (';' + str(juttu))
                        y.write(teksti)
                    y.write('\n')
        except (FileNotFoundError,PermissionError):
            print("Tiedoston '%s' avaaminen epäonnistui." % (tdsto_nimi))
            kys.exit(0)
    try:
        with open(tdsto_nimi, 'a+') as x:
            x.write(tdsto.asema + ' '+tdsto.vuosi)
            for juba in tuloste.paiste:
                jebba = (';' + str(int(juba/60)).rstrip())
                x.write(jebba)
                loppu = juba
            x.write('\n')
    except (FileNotFoundError,PermissionError):
        print("Tiedoston '%s' avaaminen epäonnistui." % (tdsto_nimi))
        kys.exit(0)
    print("Paisteaika tallennettu tiedostoon '%s'.\n" %(tdsto_nimi))
    return None

def tunti_anal(lista,tdsto):                           # Tehdään ilmatieteenlaitoksen tiedoston datan tuntien mukaan analysoiva funktio.
    alku = lista[0].pvm.strftime('%d.%m.%Y')           # Funktio lisää kuukausittain jokaisen yksittäisen tunnin (1-24) summan kirjastoon
    kuu = lista[0].pvm.month                           # kuukauden toimiessa avaimena ja paisteaika arvona. Lopuksi kaikki 12 kirjastoa
    kuulista = []                                      # lisätään listaan joka palautetaan pääohjelmalle. Käyttäjälle myös esitetään
    kirjasto = {}                                      # analysoitu aikaväli.
    vuosi = int(tdsto.vuosi)                     
    for tunti in lista:
        if tunti.pvm.year != vuosi:
            continue
        if tunti.pvm.month != kuu:
            kuu += 1
            kuulista.append(kirjasto)
            kirjasto = {}
            try:
                if tunti.pvm.hour in kirjasto:
                    kirjasto[tunti.pvm.hour] += int(tunti.paiste)
                else:
                    kirjasto[tunti.pvm.hour] = int(tunti.paiste)
            except ValueError:
                if tunti.pvm.hour in kirjasto:
                    pass
                else:
                    kirjasto[tunti.pvm.hour] = 0
                continue
        try:
            if tunti.pvm.hour in kirjasto:
                kirjasto[tunti.pvm.hour] += int(tunti.paiste)
            else:
                kirjasto[tunti.pvm.hour] = int(tunti.paiste)
        except ValueError:
            if tunti.pvm.hour in kirjasto:
                pass
            else:
                kirjasto[tunti.pvm.hour] = 0
            continue
        loppu = tunti.pvm.month
        viim = tunti.pvm.strftime('%d.%m.%Y')
    kuulista.append(kirjasto)
    print("Data analysoitu ajalta %s - %s.\n" % (alku,viim))
    return kuulista

def tunti_tallennus(lista,tdsto):                                                  # Tässä funktiossa tunti_anal() funktiosta saatujen kirjastojen arvot käydään läpi
    tdsto_nimi = (tdsto.asema+tdsto.vuosi+'tunnit.txt')                            # ja kirjoitetaan tuntinsa ja kuukautensa mukaan tiedostoon minuutteina josta tulokset on helppo
    try:                                                                           # lukea vaikkapa excelillä. Lisäksi lasketaan kaikkien tuntien summat lisäämällä jokaisen
        with open(tdsto_nimi, 'w') as x:                                           # kirjaston arvot omiin listoihinsa kuukausittain (12 listaa joissa 24 paistelukua), jonka
            x.write((tdsto.asema+' '+tdsto.vuosi+' tuntipohjainen paisteaika:\n')) # jälkeen listat summataan yhteen numpyn sum() funktiolla.
            for i in range(24):                                                   
                x.write(';'+str(i))
            for kuu in range(1,13):
                x.write('\n'+str(kuu))
                for i in lista[kuu-1].values():
                    x.write(';'+(str(int(i/60))))
            x.write('\nYht.')
            kaikki = []
            for i in lista:
                arvot=[]
                for tunti in i:
                    arvot.append(i[tunti])
                kaikki.append(arvot)
            yht = np.sum(kaikki,0)
            pyoristettu = []
            for i in yht:
                x.write(';'+str(int(i/60)))
            x.write('\n')
    except (FileNotFoundError,PermissionError):
        print("Tiedoston '%s' avaaminen epäonnistui." % (tdsto_nimi))
        kys.exit(0)
    print("Paisteaika tallennettu tiedostoon '%s'.\n" %(tdsto_nimi))
    return None







    
