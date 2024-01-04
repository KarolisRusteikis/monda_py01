""" Komandinio darbo užduotis
===[ Šaldytuvas ]===

Reikalavimai:

* Šaldytuvo turinys - žodynas, kurio raktas yra produkto pavadinimas, reikšmė - kiekis (float).
* Pridėti produktą į šaldytuvą. Pridedant egzistuojantį produktą, kiekiai sudedami su esančiais.
* Išimti produktą iš šaldytuvo. Išimant egzistuojantį produktą, kiekis atitinkamai sumažinamas.
* Patikrinti, ar reikiamas produkto kiekis yra šaldytuve.
* Išspausdinti visą šaldytuvo turinį su kiekiais.

BONUS:

* Patikrinti, ar receptas išeina. 
** Recepto įvedimas vyksta viena eilute, kuri po to išdalinama. Pva.: Sūris: 0.5, Pomidoras: 2, Duona: 0.4
** Jeigu receptas neišeina, išvardinti kiek ir kokių produktų trūksta.

"""

class Saldytuvas:
    def __init__(self):
        self.turinys = {}

    def prideti_produktus(self, produktai):
        for produktas, kiekis in produktai.items():
            if produktas in self.turinys:
                self.turinys[produktas] += kiekis
            else:
                self.turinys[produktas] = kiekis

    def isimti_produktus(self, produktai):
        for produktas, kiekis in produktai.items():
            if produktas in self.turinys:
                self.turinys[produktas] -= kiekis
                if self.turinys[produktas] <= 0:
                    del self.turinys[produktas]
            else:
                print(f"{produktas} nėra šaldytuve.")

    def patikrinti_kieki(self, produktas, reikalingas_kiekis):
        if produktas in self.turinys and self.turinys[produktas] >= reikalingas_kiekis:
            return True
        else:
            return False

    def spausdinti_turini(self):
        print("Šaldytuvo turinys:")
        for produktas, kiekis in self.turinys.items():
            print(f"{produktas}: {kiekis}")

    def patikrinti_recepta(self, receptas):
        reikalingi_produktai = dict(item.split(": ") for item in receptas.split(", "))
        truksta_produktu = {}
        
        for produktas, kiekis in reikalingi_produktai.items():
            kiekis = float(kiekis)
            if not self.patikrinti_kieki(produktas, kiekis):
                truksta_produktu[produktas] = kiekis - self.turinys.get(produktas, 0)
        
        if truksta_produktu:
            print("Receptas neišeina. Trūksta šių produktų:")
            for produktas, truksta_kiekis in truksta_produktu.items():
                print(f"{produktas}: {truksta_kiekis}")
        else:
            print("Receptas išeina! Visi produktai yra šaldytuve.")

# Pavyzdys naudojimo:
saldytuvas = Saldytuvas()

saldytuvas.prideti_produktus({"Pomidoras": 5, "Sūris": 1, "Kiaušiniai": 10})
saldytuvas.spausdinti_turini()

saldytuvas.isimti_produktus({"Pomidoras": 2, "Sūris": 0.5})
saldytuvas.spausdinti_turini()

if saldytuvas.patikrinti_kieki("Kiaušiniai", 5):
    print("Yra pakankamai kiaušinių šaldytuve.")
else:
    print("Trūksta kiaušinių šaldytuve.")

saldytuvas.prideti_produktus({"Kiaušiniai": 7, "Pomidoras": 1})
saldytuvas.spausdinti_turini()

receptas = "Sūris: 0.5, Pomidoras: 2, Duona: 0.4"
saldytuvas.patikrinti_recepta(receptas)
