import random
import matplotlib.pyplot as plt

x = 0
y = 0
durchläufe = 100
odds = [1, 2]
input = []
geldstand = []
wallet = 100
round = []
einsatz = 1

while y <= durchläufe and wallet - einsatz > 0:
    round.append(y)
    rand = random.choice(odds)
    input.append(rand)

    if rand == 1:
        wallet = wallet + einsatz
        einsatz = 1
        geldstand.append(wallet)

    if rand == 2:
        wallet = wallet - einsatz
        einsatz = einsatz * 2
        geldstand.append(wallet)

    y = y + 1
    
print(wallet)
print(input)
print(geldstand)
print(round)

plt.plot(round, geldstand)
plt.xlabel('Runden')
plt.ylabel('Geld')
plt.title('Gambling strat')
plt.show()
