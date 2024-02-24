number = int(input("Напишіть 5-ти значне число: "))
r_number = (number % 10) * 10000 + ((number % 100) // 10) * 1000 + ((number % 1000) // 100) * 100 + ((number % 10000) // 1000) * 10 + (number // 10000)
print("результат:", r_number)