# Random Module
# This module provides functions to generate random numbers and perform random selections.
# This module has functions to generate random integers, floats, and to select random elements from a list.

import random

# random() - Returns a random float number between 0.0 and 1.0
print(random.random())

# randint(a, b) - Returns a random integer N such that a <= N <= b
print(random.randint(1, 10))

# choice(seq) - Returns a randomly selected element from a non-empty sequence
items = ['apple', 'banana', 'cherry', 'date']
print(random.choice(items))

# Example: Simulating a coin toss
coin_faces = ("Head", "Tail")
i = 1
while i <= 10:
    print(random.choice(coin_faces))
    i += 1

# uniform(a, b) - Returns a random float number N such that a <= N <= b
print(random.uniform(1.5, 10.5))

# shuffle(x) - Shuffles the sequence x in place
deck = ['ace', 'king', 'queen', 'jack', '10']
random.shuffle(deck)
print(deck)

# sample(population, k) - Returns a list of k unique elements chosen from the population sequence
print(random.sample(items, 2))

# randrange(start, stop[, step]) - Returns a randomly selected element from range(start, stop, step)
print(random.randrange(0, 100, 5))

# seed(a=None) - Initializes the random number generator
random.seed(42)
print(random.random())  # This will produce the same output every time the program is run with the same seed

# gauss(mu, sigma) - Returns a random float number from a Gaussian distribution with mean mu and standard deviation sigma
print(random.gauss(0, 1))

# expovariate(lambd) - Returns a random float number from an exponential distribution with rate lambd
print(random.expovariate(1.5))

# betavariate(alpha, beta) - Returns a random float number from a Beta distribution with parameters alpha and beta
print(random.betavariate(2, 5))

# vonmisesvariate(mu, kappa) - Returns a random float number from a Von Mises distribution
print(random.vonmisesvariate(0, 4))

