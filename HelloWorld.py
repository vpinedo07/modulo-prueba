def calculate_pet_ages(humanYears):
    if humanYears == 1:
        catYears = 15
        dogYears = 15
    elif humanYears == 2:
        catYears = 24  # 15 + 9
        dogYears = 24  # 15 + 9
    else:
        catYears = 24 + (humanYears - 2) * 4
        dogYears = 24 + (humanYears - 2) * 5

    return [humanYears, catYears, dogYears]


# Ejemplo de uso
humanYears = 5
ages = calculate_pet_ages(humanYears)
print(ages)  # Debería imprimir: [5, 37, 39]
