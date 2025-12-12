print("перший таск:")
matrix = [[19, 62, -45, -1, 84],[23, 54, -4, -2, 68],[36, 39, 96, 94, 97],[-3, -8, -4, -6, -22],[98, -5, -3, 0, 11]]

"""сортування матриці"""
def sort_matrix(matrix):
    for rows in matrix: 
        for i in range(len(rows)):
            not_swapped = True
            for j in range(0, len(rows) - i - 1):
                if rows[j] < rows[j + 1]:
                    rows[j], rows[j + 1] = rows[j + 1], rows[j]
                    not_swapped = False
            if not_swapped:
                break
    return matrix

"""добуток членів під головною діагоналю"""
def product_underline(sorted_matrix):
    list_of_products = []
    i = 1
    for rows in sorted_matrix:
        if i > 1:
            j = 0
            product = 1
            while j < i-1:
                product *= rows[j]
                j+=1
            list_of_products.append(product)
        i += 1
    return list_of_products

"""середнє арефметичне добутків"""
def average_underline(product_of_numbers):
    sum = 0
    for el in product_of_numbers:
        sum += el
    return int(sum/len(product_of_numbers))

"""виклики функцій"""
sorted_matrix = sort_matrix(matrix)
product_of_numbers = product_underline(sorted_matrix)
    
"""вивід результатів в консоль"""
for i in sorted_matrix:
    print(i)
print(f"Список добутків чисел: {product_of_numbers}")
print(f"Середнє арефметичне добутків чисел: {average_underline(product_of_numbers)}")

print("\n"+"дргуй таск:")

"""клас для створення пасажира"""
class Pasanger:
    def __init__(self, name, age, time_when_came):
        self.name = name
        self.age = age
        self.time_when_came = time_when_came

    def get_info(self):
        return f"Ім'я і прізвище: {self.name}, Вік: {self.age}"
    
    def get_time_when_came(self):
        return self.time_when_came

"""функція для створення списку з пасажирів"""
def main():
    passenger1 = Pasanger("Енакін Скайвокер", 45, "10.00")
    passenger2 = Pasanger("Астольфо Аргалій", 195, "10.30")
    passenger3 = Pasanger("Вінстон Уітмен ", 30, "9.45")
    passenger4 = Pasanger("Шарлотта Вайлтшайр ", 15, "00.00")

    return passenger1, passenger2, passenger3, passenger4

"""запис всіх пасажирів в список"""
list_of_passengers = main()

"""функція для розсадки пасажирів в порядку їх прибутя"""
def seating_arrangement(list_of_passengers):
    passengers = list(list_of_passengers)  
    n = len(passengers)
    
    for i in range(n):
        for j in range(0, n - i - 1):
            if float(passengers[j].get_time_when_came()) > float(passengers[j + 1].get_time_when_came()):
                passengers[j], passengers[j + 1] = passengers[j + 1], passengers[j]
    
    return passengers
                
"""запис відсортованих пасажирів в список"""
seating_list = seating_arrangement(list_of_passengers)

"""присвоєння номера місця, і вивід пасажирів в консоль"""
sit_number = 1
for i in seating_list:
    print(i.get_info() + f" прийшов о: {i.get_time_when_came()}" + f" місце: {sit_number}")
    sit_number+=1



