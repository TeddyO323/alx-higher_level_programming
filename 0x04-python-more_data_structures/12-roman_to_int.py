#!/usr/bin/python3
def roman_to_int(roman_string):
    if isinstance(roman_string, str) is False:
        return 0
    else:
        romanNumber = 0
        valuesRoman = {'I': 1, 'V': 5, 'X': 10, 'L': 50,
                       'C': 100, 'D': 500, 'M': 1000}
        for i in range(len(roman_string)):
            valueTemp = valuesRoman.get(roman_string[i])
            if (i == (len(roman_string) - 1)):
                romanNumber += valueTemp
            else:
                if valuesRoman.get(roman_string[i + 1]) > valueTemp:
                    romanNumber -= valueTemp
                else:
                    romanNumber += valueTemp
        return romanNumber
