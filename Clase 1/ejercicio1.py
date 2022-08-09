num_dias = int(input("Digite el numero de dias que desea hacer la conversion : "))

year = num_dias // 365
r = num_dias % 365
m = r // 30
d = r % 30


# print("Años : " + str(int(year)) + ", Meses : " + str(int(m)) +", Dias : " + str(int(d)))
print(f"Años : {year}, Meses {m}, Dias, {d}")


