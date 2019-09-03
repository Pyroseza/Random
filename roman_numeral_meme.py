#!/usr/bin/env python3
def convert_roman_numerals(numeral):
    numeral = numeral.replace('M','DD')
    numeral = numeral.replace('CD','CCCC')
    numeral = numeral.replace('D','CCCCC')
    numeral = numeral.replace('C','LL')
    numeral = numeral.replace('XL','XXXX')
    numeral = numeral.replace('L','XXXXX')
    numeral = numeral.replace('X','VV')
    numeral = numeral.replace('IV','IIII')
    numeral = numeral.replace('V','IIIII')
    return len(numeral)

r_in = ["CXIII", "CCCLXIV", "XLI", "MMMDCCCXXXVII", "IVLXXXIX", "IVDCCCLXXXVIII", "IVCMXCIX", "MMXIX"]
for _ in r_in:
    out = convert_roman_numerals(_)
    print(f"before: {_}, \tafter: {out}")
