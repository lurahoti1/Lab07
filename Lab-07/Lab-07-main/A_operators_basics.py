a = float(input("A: "))
b = float(input("B: "))

shuma = round(a + b, 2)
diferenca = round(a - b, 2)
prodhimi = round(a * b, 2)

if b != 0:
    pjesetimi = round(a / b, 2)
    pjesetimi_i_plote = a // b
    mbetja = round(a % b, 2)
else:
    pjesetimi = "Mos shkruaj zero."
    pjesetimi_i_plote = "Mos shkruaj zero."
    mbetja = "Mos shkruaj zero."

fuqi_a = round(a ** 2, 2)
fuqi_b = round(b ** 3, 2)

print("Shuma:", shuma)
print("Diferenca:", diferenca)
print("Produkti:", prodhimi)
print("Pjesetimi:", pjesetimi)
print("Pjesetimi_i_plote:", pjesetimi_i_plote)
print("Mbetja:", mbetja)
print("Fuqi a^2:", fuqi_a)
print("Fuqi b^3:", fuqi_b)
