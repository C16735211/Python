import random

health = 50

difficulty = 3

potion_health = int(random.randint(25,50) / difficulty)

print(health)

health = health + potion_health

print('New health',health)
