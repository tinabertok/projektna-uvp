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

izpis_OH = tk.Label(okno, text = "OH : 0",width=20, background = "salmon")
izpis_OH.grid(row = 9, column = 2)

izpis_beljakovine = tk.Label(okno, text = "beljakovine : 0",width=20, background = "salmon")
izpis_beljakovine.grid(row = 10, column = 2)

izpis_vitamini = tk.Label(okno, text = "vitamini : 0",width=20, background = "salmon")
izpis_vitamini.grid(row = 11, column = 2)

izpis_mascobe = tk.Label(okno, text = "maščobe : 0",width=20, background = "salmon")
izpis_mascobe.grid(row = 12, column = 2)



hrana_kalorije = tk.Label(okno, text = "",width=20)
hrana_kalorije.grid(row = 8, column = 1)

hrana_OH = tk.Label(okno, text = "",width=20, background = "salmon")
hrana_OH.grid(row = 9, column = 1)

hrana_beljakovine = tk.Label(okno, text = "",width=20, background = "salmon")
hrana_beljakovine.grid(row = 10, column = 1)

hrana_vitamini = tk.Label(okno, text = "",width=20, background = "salmon")
hrana_vitamini.grid(row = 11, column = 1)

hrana_mascobe = tk.Label(okno, text = "",width=20, background = "salmon")
hrana_mascobe.grid(row = 12, column = 1)



def vnos(L):
    vnos_hrane = vnos_zivil.get()
    vnos_zivil.delete(0, tk.END)
    seznam = vnos_hrane.split(',')
    zivilo = seznam[0].strip().lower()
    teza = int(seznam[1].strip())
    L.dodaj_vrednosti(zivilo, teza) #Lastnosti
    #Spreminjaj izpis
    izpis_kalorije.config(text = "kalorije : "+str(L.lastnosti["kalorije"]))
    izpis_OH.config(text = "OH : "+str(L.lastnosti["OH"]))
    izpis_beljakovine.config(text = "beljakovine : "+str(L.lastnosti["beljakovine"]))
    izpis_vitamini.config(text = "vitamini : "+str(L.lastnosti["vitamini"]))
    izpis_mascobe.config(text = "maščobe : "+str(L.lastnosti["maščobe"]))

    return 

def aktivnost(L):
    sport = L.aktivnost()
    if sport == "primerno":
        izpis_sport.config(text = "Prehrana je primerna.")
    else:
        izpis_sport.config(text = str(sport))
    return

def najdi(L):
    priporocila = L.najdi()
    hrana_kalorije.config(text = priporocila["kalorije"])
    hrana_OH.config(text = priporocila["OH"])
    hrana_beljakovine.config(text = priporocila["beljakovine"])
    hrana_vitamini.config(text = priporocila["vitamini"])
    hrana_mascobe.config(text = priporocila["maščobe"])
    return

lastnosti = Lastnosti()

    

okno.mainloop()

