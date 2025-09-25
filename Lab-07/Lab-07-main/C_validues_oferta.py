emri = input("Emri: ").strip()
if len(emri) < 2:
    print("Gabim: Emri duhet të ketë të paktën 2 karaktere pas pastrimit.")
    exit()

try:
    mosha = int(input("Mosha: "))
    if mosha < 10 or mosha > 99:
        print("Gabim: Mosha duhet të jet ne intervalin [10, 99].")
        exit()
except ValueError:
    print("Gabim: Mosha duhet të jete numer i plote.")
    exit()

try:
    cmimi_baze = float(input("Cmimi baze (Lek): "))
    if cmimi_baze <= 0:
        print("Gabim: Cmimi duhet të jete me i madh se 0.")
        exit()
except ValueError:
    print("Gabim: Cmimi duhet të jete numer.")
    exit()

kupon = input("Ke kupon? (po/jo): ").lower().strip()
if kupon not in ['po', 'jo']:
    print("Gabim: Kuponi duhet të jete 'po' ose 'jo'.")
    exit()

zbritje_moshe = 0.10 if mosha < 18 or mosha >= 65 else 0
zbritje_kupon = 0.05 if kupon == 'po' else 0
zbritje_totale = zbritje_moshe + zbritje_kupon
vlere_zbritje = round(cmimi_baze * zbritje_totale, 2)
pas_zbritjes = round(cmimi_baze - vlere_zbritje, 2)
tvsh = round(pas_zbritjes * 0.15, 2)
totali = round(pas_zbritjes + tvsh, 2)

print("-" * 30)
print(f"Klient: {emri} (mosha {mosha})")
print(f"Cmimi baze: {round(cmimi_baze, 2)} Lek")
print(f"Zbritje totale: {int(zbritje_totale * 100)}% (vlere: {vlere_zbritje} Lek)")
print(f"Pas zbritjes: {pas_zbritjes} Lek")
print(f"TVSH (15%): {tvsh} Lek")
print(f"Totali: {totali} Lek")
