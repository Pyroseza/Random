def is_prime(candidate):
    if candidate in (2, 3):
        return True
    if not candidate % 2 or candidate < 2 or candidate % 6 == 3:
        return False
    is_prime = True
    for d in range(3, int(candidate**0.5) + 1, 2):
        if candidate % d == 0:
            is_prime = False
            break
    return is_prime

primes = []
import time
start = time.time()
for x in range(1000000):
    if is_prime(x): primes.append(x)
print(len(primes), 'primes calculated')
print('in', time.time() - start, 'Seconds')
