# В заданной строке расположить в обратном порядке все слова. Разделителями слов считаются пробелы.
s = input('введите строку: ')
print(*reversed(s.split()))
