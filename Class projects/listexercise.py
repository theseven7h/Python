def access_third_element(numbers):
    return numbers[2]

def change_last_item(colours):
    colours[len(colours)-1] = "yellow"

def append_element(colours):
    colours.append("purple")

def remove_element_3(numbers):
    numbers.remove(3)
    return numbers

def return_list_of_lengths(names):
    lengths = []
    for name in names:
        lengths.append(len(name))
    return lengths

def sort_list_in_ascending_order(numbers):
    for i in range(len(numbers)):
        for j in range(i, len(numbers)):
            if numbers[i] > numbers[j]:
                numbers[i], numbers[j] = numbers[j], numbers[i]
    return numbers

def obtain_even_numbers(numbers):
    even_numbers = []
    for number in numbers:
        if number % 2 == 0:
            even_numbers.append(number)
    return even_numbers

def combine_two_lists(list1, list2):
    combined_list = list1 + list2
    return combined_list

def obtain_strings_with_more_than_3_characters(words):
    strings = []
    for word in words:
        if len(word) > 3:
            strings.append(word)
    return strings

def is_even(number):
    return number % 2 == 0

def is_odd(number):
    return number % 2 == 1

def filter_even_numbers(numbers):
    return list(filter(is_even, numbers))

def filter_odd_numbers(numbers):
    return list(filter(lambda gdgd: gdgd % 2 == 1, numbers))

# print(filter_even_numbers([1,2,3,4,5,6,7,8,9,9,12]))
# print(filter_odd_numbers([1,2,3,4,5,6,7,8,9,9,12]))

print(list(filter(lambda number: remove_element_3(number), [[3,4,5,6],[1,2,3,6,3,1]])))