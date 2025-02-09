import math
import random
import string
from itertools import count
from operator import index

# FizzBuzz uzduotis

fzsarasas = []
for z in range(1,101):
    fzsarasas.append(z)
print(fzsarasas)
for fz in fzsarasas:
    if fz % 3 == 0 and fz % 5 == 0:
        print('FizzBuzz')
    elif fz % 3 == 0:
        print('Fizz')
    elif fz % 5 == 0:
        print('Buzz')
    else:
        print(fz)

# Veiksmai su dviem kintamaisiais

while True:
    print('Iveskite pirma skaiciu:')
    sk = int(input())
    print('Iveskite antra skaiciu:')
    sk2 = int(input())
    print('Irasykite norima veiksma - sudetis, atimtis, daugyba ar dalyba:')
    veiksmas = input()
    if veiksmas == 'sudetis':
        print(sk, '+', sk2, '=', sk + sk2)
    if veiksmas == 'atimtis':
        print(sk, '-', sk2, '=', sk - sk2)
    if veiksmas == 'daugyba':
        print(sk, '*', sk2, '=', sk * sk2)
    if veiksmas == 'dalyba':
        print(sk, '/', sk2, '=', sk / sk2)
    user_input = input('Ar norite pakartoti is naujo? (taip/ne): ')
    if user_input.lower() in ["taip", "t"]:
        continue
    elif user_input.lower() in ["ne", "n"]:
        break

# Random skaiciai ir ju vidurkiai

skaiciai = []
for a in range(50):
    skaiciai.append(random.randint(1, 10000))
print(skaiciai)
print('Vidurkis:', sum(skaiciai)/len(skaiciai))
print('Didziausias skaicius:', max(skaiciai))
print('Maziausias skaicius:', min(skaiciai))
mazesni = []
for sk in skaiciai:
    if sk < sum(skaiciai)/len(skaiciai):
        mazesni.append(sk)
mazesni.sort(reverse=True)
print('Mazesni skaiciai uz vidurki:', mazesni)
print('Bei ju vidurkis:', round(sum(mazesni)/len(mazesni), 2))
didesni = []
for sk2 in skaiciai:
    if sk2 > sum(skaiciai)/len(skaiciai):
        didesni.append(sk2)
didesni.sort()
print('Didesni skaiciai uz vidurki:', didesni)
print('Bei ju vidurkis:', round(sum(didesni)/len(didesni), 2))

# fukcijos - max reiksmes paieska bei sarasu uzpildymas random skaiciais

def didz(listas):
    maxi = listas[0]
    for sk in listas:
        if sk > maxi:
            maxi = sk
    print('didziausias rastas skaicius:', maxi)

def skaic(listukas):
        listukas.append(random.randint(1,100))
        listukas.append(random.randint(1, 100))
        listukas.append(random.randint(1, 100))
        listukas.append(random.randint(1, 100))
        listukas.append(random.randint(1, 100))
        print(listukas)

pirmas = []
antras = []
trecias = []

skaic(pirmas)
skaic(antras)
skaic(trecias)

didz(pirmas)
didz(antras)
didz(trecias)