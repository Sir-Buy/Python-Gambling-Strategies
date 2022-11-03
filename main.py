import random
import matplotlib.pyplot as plt
x = 0
y = 0
rounds = 100
odds = [1, 2]
input = []
balance = []
wallet = 100
round = []
bet = 1
print(input)
while y <= rounds and wallet - bet > 0:
    round.append(y)
    rand = random.choice(odds)
    input.append(rand)
    if rand == 1:
        wallet = wallet + bet
        bet = 1
        balance.append(wallet)
    if rand == 2:
        wallet = wallet - bet
        bet = bet * 2
        balance.append(wallet)
    y = y + 1
print(wallet)
print(input)
print(balance)
print(round)
plt.plot(round, balance)
plt.xlabel('Round')
plt.ylabel('Money')
plt.title('Gambling strat')
plt.show()
