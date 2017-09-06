import tkinter as tk

from moja_projektna import *


okno = tk.Tk()
okno.geometry('500x300')
okno.configure(background = "salmon")

prazna1 = tk.Label(okno, text = "",background = "salmon")
prazna1.grid(row = 0, columnspan = 3)
naslov = tk.Label(okno, text = "ANALIZA PREHRANE", background = "salmon", font = (None, 15))
naslov.grid( row = 1, columnspan = 3)

vprasanje = tk.Label(okno, text = "Kaj ste pojedli danes? (živilo, teža v gramih)", background = "salmon", font = (None, 12))
vprasanje.grid(row = 2, columnspan = 3)

vnos_zivil = tk.Entry(okno)
vnos_zivil.grid(row = 3, columnspan = 3)


prazna2 = tk.Label(okno, text = "",background = "salmon")
prazna2.grid(row = 4, columnspan = 3)

zabelezi_gumb = tk.Button(okno, text = "ZABELEŽI", command = lambda: vnos(lastnosti))
zabelezi_gumb.grid(row = 5, columnspan = 3)


prazna2 = tk.Label(okno, text = "",background = "salmon")
prazna2.grid(row = 6, columnspan = 3)

sport_gumb = tk.Button(okno, text = "ŠPORT", command = lambda : aktivnost(lastnosti))
sport_gumb.grid(row = 7, column = 0)
izpis_sport = tk.Label(okno, text = "",width=20)
izpis_sport.grid(row = 8, column = 0)

hrana_gumb = tk.Button(okno, text = "HRANA", command = lambda : najdi(lastnosti))
hrana_gumb.grid(row = 7, column = 1)

izpis_gumb = tk.Button(okno, text = "IZPIS")
izpis_gumb.grid(row = 7, column = 2)

izpis_kalorije = tk.Label(okno, text = "kalorije : 0",width=20)
izpis_kalorije.grid(row = 8, column = 2)

hrana_kalorije = tk.Label(okno, text = "",width=20)
hrana_kalorije.grid(row = 8, column = 1)

def vnos(L):
    vnos_hrane = vnos_zivil.get()
    vnos_zivil.delete(0, tk.END)
    seznam = vnos_hrane.split(',')
    zivilo = seznam[0].strip().lower()
    teza = int(seznam[1].strip())
    L.dodaj_vrednosti(zivilo, teza) #Lastnosti
    #Spreminjaj izpis
    izpis_kalorije.config(text = "kalorije : "+str(L.lastnosti["kalorije"]))
    
    return 

def aktivnost(L):
    sport = L.aktivnost()
    if sport=="primerno":
        izpis_sport.config(text="Prehrana je primerna.")
    else:
        izpis_sport.config(text="bablabla "+str(sport))
    return

def najdi(L):
    priporocila = L.najdi()
    hrana_kalorije.config(text = priporocila["kalorije"])
    return

lastnosti = Lastnosti()

    

okno.mainloop()

