# create by Pyroseza a.k.a. Engineer Pyro

from math import sqrt, floor
import logging, sys

# create proper logging because printing everywhere is overrated
logging.basicConfig(stream=sys.stderr, level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# remove all multiples of a given number
def ClearMultiples(number_to_check, test_list):
    # move back one space because of 0 index list, then add then next multiple
    # i.e. if we are checking 2 then skip 2 and check 4 and onwards
    element = (number_to_check - 1) + number_to_check
    while element < len(test_list):
        test_list[element] = "0"
        element += number_to_check
    return test_list

# generate a list of prime numbers up to a given number
def PrimeGen(up_to):
    primes = []
    # create a list the size of our limit
    test_list = ["1" for _ in range(up_to)]
    # minus 1 to account for 0 indexed list
    #up_to -= 1
    # get the square root to check up until, no point checking further
    limit = floor(sqrt(up_to))
    logging.info(f"checking limited to {limit}, which is the floored square root of {up_to}")
    # set 1st element to zero as 1 cannot be a prime
    test_list[0] = "0"
    # start checking from 2nd element, the number 2
    element = 1
    # loop from the 2 element to the last element
    while element < up_to:
        number_to_check = element + 1
        # if element is alreday "0" then skip it
        if (test_list[element] == "0"):
            element += 1
            continue
        # if we are going beyond the square root then skip
        if element > limit:
            element += 1
            continue
        logging.info(f"Checking for multiples of: {number_to_check}")
        # set all mulitples of this number to "0"
        test_list = ClearMultiples(number_to_check, test_list)
        logging.debug(f"result list after clearing multiples of {number_to_check}: {test_list}")
        element += 1
    for index in range(len(test_list)):
        logging.debug(f"Item: {index}, {test_list[index]}")
        if test_list[index] == "1":
            # add 1 to index because of 0 based index
            primes.append(index+1)
    logging.debug(primes)
    return primes

limit = 3001
logging.info(f"getting primes up to {limit}")
primes = PrimeGen(limit)
logging.info(f"Done! Primes found = {len(primes)}")
for i in range(len(primes)):
    logging.info(f"prime: {i+1} -> {primes[i]}")
