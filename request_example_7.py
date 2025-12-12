print("перший таск:")
matrix = [[19, 62, -45, -1, 84],[23, 54, -4, -2, 68],[36, 39, 96, 94, 97],[-3, -8, -4, -6, -22],[98, -5, -3, 0, 11]]

def sort_matrix(matrix):
    """сортування матриці"""
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

def product_underline(sorted_matrix):
    """добуток членів під головною діагоналю"""
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

def average_underline(product_of_numbers):
    """середнє арефметичне добутків"""
    sum = 0
    for el in product_of_numbers:
        sum += el
    return int(sum/len(product_of_numbers))

sorted_matrix = sort_matrix(matrix)
product_of_numbers = product_underline(sorted_matrix)
    
for i in sorted_matrix:
    print(i)
print(f"Список добутків чисел: {product_of_numbers}")
print(f"Середнє арефметичне добутків чисел: {average_underline(product_of_numbers)}")

print("\n"+"дргуй таск:")

class Passager_Queue:
    def __init__(self):
        self.__queue = []

    def new_passager_in_queue(self, new_passager):
        """додавання нового пасажира"""
        self.__queue.append(new_passager)

    def to_sit(self):
        """функція для провірки чи черга не пуста і розсадки пасажирів"""
        if len(self.__queue) > 0:
            sitting_passager = self.__queue
            return sitting_passager
        return None

    def show_queue(self):
        for i in range(len(self.__queue)):
            print(f"Місце в черзі {i + 1}: {self.__queue[i]}")

bus_station = Passager_Queue()

bus_station.new_passager_in_queue("Енакін Скайвокер")
bus_station.new_passager_in_queue("Шарлотта Вайлтшайр")
bus_station.new_passager_in_queue("Вінстон Уітмен")

print("Черга пасажирів:")
bus_station.show_queue()
bus_station.to_sit()
print("\n"+"Після того, як пасажир сів:")
bus_station.show_queue()


