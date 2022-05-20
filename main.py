class Pracownik:
	def __init__(self, imie, brutto):
		self.imie = imie
		self.brutto = brutto
		
	def skladki_pracownika(self):
		emerytalna = round(self.brutto * 0.0976,2)
		rentowa = round(self.brutto * 0.015,2)
		chorobowa = round(self.brutto * 0.0245,2)
		skladka = round(emerytalna+rentowa+chorobowa,2)
		
	
		podstawa=round(self.brutto-skladka,2)
	
	#ubezpieczenia
		zdrowotne = round(podstawa * 0.09,2)
		odliczenie = round(podstawa * 0.0775,2)

		koszt=111.25
		zaliczka = round(self.brutto - koszt -skladka)

		zaliczka_przed = round((zaliczka *0.18)-46.33,2)
		zaliczka_na_podatek = round(zaliczka_przed - odliczenie)


		kwota = round(self.brutto - skladka - zdrowotne - zaliczka_na_podatek, 2)
		return float(kwota)
		
	def skladki_pracodawcy(self):
		emerytalna = round(self.brutto * 0.0976,2)
		rentowa = round(self.brutto * 0.065,2)
		wypadkowa = round(self.brutto * 0.0193,2)
		fp = round(self.brutto * 0.0245,2)
		fgsp = round(self.brutto * 0.001,2)

		skladka2 = round(emerytalna+rentowa+wypadkowa+fp+fgsp,2)
		return float(skladka2)
		
		
l_pracownicy = int(input())
pracownicy = {}

laczny_koszt = 0

for x in range(l_pracownicy):
	imie, wynagrodzenie = input().split()
	pracownicy[x] = {'imie': imie, 'wynagrodzenie': int(wynagrodzenie)}

for id in pracownicy:
	pracownik = Pracownik(pracownicy[id]['imie'], pracownicy[id]['wynagrodzenie'])
	laczny_koszt += pracownicy[id]['wynagrodzenie'] + pracownik.skladki_pracodawcy()
	print(f"{pracownicy[id]['imie']} {pracownik.skladki_pracownika():.2f} {pracownik.skladki_pracodawcy()} {round(pracownicy[id]['wynagrodzenie']+ pracownik.skladki_pracodawcy(), 2)}")


print(round(laczny_koszt, 2))