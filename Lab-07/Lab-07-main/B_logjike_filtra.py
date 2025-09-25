mosha = int(input("Mosha: "))
karte = input("Ke karte studenti? (po/jo): ").lower().strip()

zbritje_e_lejuar = (mosha < 18) or (mosha >= 65) or (karte == 'po')

buxheti = float(input("Buxheti (Lek): "))
cmimi = float(input("Cmimi (Lek): "))

blerja_e_mundur = buxheti >= cmimi

oferta_speciale = (500 <= cmimi <= 2000) and (16 <= mosha <= 25)

print("Zbritje e lejuar:", "PO" if zbritje_e_lejuar else "JO")
print("Blerja e mundur:", "PO" if blerja_e_mundur else "JO")
print("Oferta speciale:", "PO" if oferta_speciale else "JO")
