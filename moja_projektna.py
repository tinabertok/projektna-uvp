def slovar_kalorij(ime_datoteke):
    '''Naredili bomo slovar kalorij.'''
    with open(ime_datoteke) as f:
        zivila = dict()
        for vrstica in f:
            vrstica_v_slovarju = vrstica.strip().split(',')
            zivilo = vrstica_v_slovarju[0]
            hranilne_vrednosti = dict()
            for vsebnosti in vrstica_v_slovarju[1:]:
                hranilna_vrednost, stevilo = vsebnosti.split(':')
                hranilne_vrednosti[hranilna_vrednost] = int(stevilo)
            
            zivila[zivilo] = hranilne_vrednosti
        return zivila

def slovar_primerjav(ime_datoteke):
    '''Naredili bomo slovar priporocenih vrednosti.'''
    with open(ime_datoteke) as f:
        priporocene_vrednosti = dict()
        for vrstica in f:
            lastnost, vrednost = vrstica.split(',')
            vrednost = int(vrednost)
            
            priporocene_vrednosti[lastnost] = vrednost
    return priporocene_vrednosti


              
            


def vnos(): 
    vnos_hrane = input('Kaj ste danes pojedli? (živilo, teža): ')
    seznam = vnos_hrane.split(',')
    zivilo = seznam[0].strip().lower()
    teza = int(seznam[1].strip())
    return zivilo, teza
    

    
class Lastnosti:
    '''Lastnosti nam seštejejo vse dnevne kalorije in vnose hranilnih vrednosti.'''

    def __init__(self):
        self.lastnosti = {'beljakovine' : 0,
                          'maščobe' : 0,
                          'OH' : 0,
                          'kalorije' : 0,
                          'vitamini' : 0}

        self.slovar_zivil = slovar_kalorij(r'vsebnost_hranil.txt')
        self.primerjalne_vrednosti = slovar_primerjav(r'priporocen_vnos.txt')
        

    def dodaj_vrednosti(self, zivilo, teza):
        '''Preračunamo hranilne vrednosti in kalorije glede na količino vnosa.'''
##        if zivilo not in self.slovar_zivil:
##            novo_zivilo = input('Dodaj ime novega živila, njegove kalorije na 100g ter ostale hranilne vrednosti.') 
##            with open(r'vsebnost_hranil.txt', 'a') as f: # Zapišemo novo živilo v datoteko
##                print('\n' + novo_zivilo, file=f, sep='') # Napisali smo še \n da gre v novo vrstico in sep, da ni presledkov
##            self.slovar_zivil = slovar_kalorij(r'vsebnost_hranil.txt')# Dodamo novo živilo in posodobimo slovar
##            
        for kljuc, vrednost in self.slovar_zivil[zivilo].items():
            self.lastnosti[kljuc] = round(self.lastnosti.get(kljuc, 0) + teza * (vrednost / 100),2)

    def __str__(self):
        '''Prikaz objekta, vrne mi natačno število hranilnih vrednosti, ki se sproti seštevajo.'''
        niz = ''
        for kljuc,vrednost in self.lastnosti.items():
            niz += kljuc + ' ' + str(vrednost) + '\n'
            
        return niz


    def aktivnost(self):
        '''Funkcija nam pove s katero aktivnostjo se moramo ukvarjati.'''
        kalorije = self.lastnosti['kalorije']


        if kalorije >= 3000:
            aktivnost = "ROLANJE"
            
        elif kalorije >= 2500:
            aktivnost = "TEK"
            
        elif kalorije >= 2000:
            aktivnost = "KOLESARJENJE"
        else:
            #return 'Vaš dnevni vnos kalorij je primeren.'
            return "primerno"

        return aktivnost    
        #return 'Priporočamo vam, da se vsaj trikrat tedensko po 30 minut ukvarjate {}.'.format(aktivnost)




    def slovar_razlik(self):
        '''Primerjamo priporocene vrednosti z našim vnosom.'''
        
        razlika = dict()
        
        for lastnost_x, vrednost_x in self.lastnosti.items():
            priporocena_vrednost = self.primerjalne_vrednosti[lastnost_x]
            razlika[lastnost_x] = vrednost_x - priporocena_vrednost

        return razlika
    

    def najdi(self):
        
        '''Najde zivilo z največjo vsebnostjo lastnosti, ki nam je primanjkuje. Vrne nam slovar teh zivil.'''
        slovar_razlik = self.slovar_razlik()
        slovar_priporocil = {}
        for lastnost in slovar_razlik.keys():
            if slovar_razlik[lastnost] < -50:
                #Poiščemo najprimernejše živilo
                kandidati = []
                for zivilo in self.slovar_zivil.keys():
                    vrednost = self.slovar_zivil[zivilo].get(lastnost,0)
                    if vrednost>0:
                        kandidati.append([vrednost,zivilo])
                #print(kandidati)
                slovar_priporocil[lastnost] = max(kandidati)[1]                
            else:
                slovar_priporocil[lastnost] = ""
        #print(slovar_priporocil)
        return slovar_priporocil




##    def primerjava(self):
##        slovar_razlik = self.slovar_razlik()
##        return slovar_razlik
##        
##            





##            if vrednost_x < priporocena_vrednost:
##                print (lastnost_x, round(vrednost_x,2)) #hočemo da prikaže BOLD
            
    
    
               
                           

                     
        

##
##
##    
##lastnosti = Lastnosti()
##
##
##
##
##
##for _ in range(3):
##    zivilo, teza = vnos()
##    lastnosti.dodaj_vrednosti(zivilo, teza)
##    print(lastnosti)
##
##print(lastnosti.slovar_razlik())
##
##print(lastnosti.najdi())        
