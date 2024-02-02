def to_roman(num):

    rom_nums = {
        "M": 1000, "CM": 900, "D": 500, "CD": 400, "C": 100, "XC": 90,
        "L": 50, "XL": 40, "X": 10, "IX": 9, "V": 5, "IV": 4, "I": 1,
    }

    result = ""
    
    for k, v in rom_nums.items():
        if num >= v:
            qty = int(num/v)
            result += k*qty
            # print(num, (k*qty))
            num -= v*qty
            
    return result