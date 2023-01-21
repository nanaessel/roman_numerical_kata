def roman_number(num):
    roman_numerals = {
        1000: 'M',
        900: 'CM',
        500: 'D',
        400: 'CD',
        100: 'C',
        90: 'XC',
        50: 'L',
        40: 'XL',
        10: 'X',
        9: 'IX',
        5: 'V',
        4: 'IV',
        1: 'I'
    }
    result = ''
    for key in roman_numerals:
        while num >= key:
            result += roman_numerals[key]
            num -= key
    return result

print(roman_number(1))    
print(roman_number(4))    
print(roman_number(9))    
print(roman_number(40))   
print(roman_number(99))   
print(roman_number(2018)) 