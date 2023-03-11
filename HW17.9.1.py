def sort(array):
    for i in range(len(array)):
        for j in range(len(array) - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]

    return array


def bin_search(sort_arr, element, left, right):
    if left > right:
        return False

    middle = (right + left) // 2
    if sort_arr[middle] == element:
        return middle
    elif element < sort_arr[middle]:
        return bin_search(sort_arr, element, left, middle - 1)
    else:
        return bin_search(sort_arr, element, middle + 1, right)


try:
    array = list(map(int, input('Введите последовательность уникальных чисел через пробел:').split()))
    if len(set(array)) != len(array):
        array = list(set(array))
        print('У Вас есть повторяющиеся числа, но мы их исключили!')
    element = int(input('Введите любое число: '))
    if element not in array:
        array.append(element)
    sort_arr = sort(array)
    print('Сортированный по возрастанию список:', sort_arr)
    if element is sort_arr[0]:
        print('Элемент, меньший, чем введенное число, отсутствует')
        print('Номер позиции элемента, большего, чем введенное число:',
              bin_search(sort_arr, element, 0, len(sort_arr) - 1) + 1)
    elif element is sort_arr[-1]:
        print('Номер позиции элемента, меньшего, чем введенное число:',
              bin_search(sort_arr, element, 0, len(sort_arr) - 1) - 1)
        print('Элемент, больший, чем введенное число, отсутствует')
    else:
        print('Номер позиции элемента, меньшего, чем введенное число:',
              bin_search(sort_arr, element, 0, len(sort_arr) - 1) - 1)
        print('Номер позиции элемента, большего, чем введенное число:',
              bin_search(sort_arr, element, 0, len(sort_arr) - 1) + 1)
except ValueError:
    print('Вы ввели букву или символ!')
