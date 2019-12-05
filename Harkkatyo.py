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

# Tämä ohjelma lukee ilmatieteenlaitoksen dataa sisältäviä tiedostoja ja   #
# suorittaa analyysin käyttäjän tarpeen mukaan joko päivä-, kuukausi-, tai #
# tuntikohtaisesti ja kirjoittaa kyseisen analyysin käyttäjän määrittämään #
# tiedostoon (poislukien tuntikohtaiset tiedot, tällä on ennaltamääritetty #
# tiedostonimi). Kirjoitettu tieto on sellaisessa muodossa että sen avulla #
# on helppo luoda graafisia mallinnuksia analysoiduista tiedoista esim.    #
# Microsoft Excel:in avulla. Ohjelman päätasolle on laitettu vain ali-     #
# ohjelmat kutsuva valikko sekä pääohjelma, joka suorittaa valikko-        #
# ohjelman. Aliohjelmat löytyvät samasta tiedostosijainnista nimellä       #
# 'HT_kirjasto.py'. Tämä kirjasto tuodaan pääohjelmaan heti alussa.        #

############################################################################

import HT_kirjasto_with as ali

def paaohjelma():                                                          # Ohjelman pääohjelma kutsuu ainoastaan valikko-ohjelman joka
    valikko()                                                              # toistuu käyttäjän haluaman määrän kertoja ja josta
                                                                           # varsinaiset aliohjelmakutsut suoritetaan syötteen perusteella.
    
def valikko():
    while True:
        print('Mitä haluat tehdä:')
        valinta = input("""1) Anna havaintoasema ja vuosi
2) Lue säätilatiedosto
3) Analysoi päivittäiset säätilatiedot
4) Tallenna päivittäiset säätilatiedot
5) Lue Ilmatieteen laitoksen tiedosto
6) Analysoi kuukausittaiset säätilatiedot
7) Tallenna kuukausittaiset säätilatiedot
8) Analysoi tuntikohtaiset säätilatiedot
9) Tallenna tuntikohtaiset säätilatiedot
0) Lopeta
Valintasi: """)
        if valinta == '1':
            tdsto = ali.tied()
        elif valinta == '2':
            try:
                lista = ali.luku(tdsto)
            except UnboundLocalError:
                print('Lista on tyhjä. Analysoi data ennen tallennusta.\n')
        elif valinta == '3':
            try:
                analyysi = ali.analyysi(lista,tdsto)
            except UnboundLocalError:
                print('Lista on tyhjä. Analysoi data ennen tallennusta.\n')
        elif valinta == '4':
            try:
                ali.tallennus(analyysi,tdsto)
            except UnboundLocalError:
                print('Lista on tyhjä. Analysoi data ennen tallennusta.\n')
        elif valinta == '5':
            try:
                ilmat_lista = ali.ilmat_luku(tdsto)
            except UnboundLocalError:
                print('Lista on tyhjä. Analysoi data ennen tallennusta.\n')
        elif valinta == '6':
            try:
                ilmat_analyysi = ali.ilmat_anal(ilmat_lista,tdsto)
            except:
                print('Lista on tyhjä. Lue ensin tiedosto.\n')
        elif valinta == '7':
            try:
                ali.ilmat_tallennus(ilmat_analyysi,tdsto)
            except UnboundLocalError:
                print('Lista on tyhjä. Analysoi data ennen tallennusta.\n')
        elif valinta == '8':
            try:
                tuntipohja = ali.tunti_anal(ilmat_lista,tdsto)
            except UnboundLocalError:
                print('Lista on tyhjä. Analysoi data ennen tallennusta.\n')
        elif valinta == '9':
            try:
                ali.tunti_tallennus(tuntipohja,tdsto)
            except UnboundLocalError:
                print('Lista on tyhjä. Analysoi data ennen tallennusta.\n')
        elif valinta == '0':
            print('Kiitos ohjelman käytöstä.')
            break
        else:
            print('Valintaa ei tunnistettu, yritä uudestaan.\n')

paaohjelma()
