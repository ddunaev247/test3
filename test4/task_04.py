#Создать строку равную введенной строке без последних двух символов.
st = input("введите строку:", )

if len(st) < 3:
    print("введенная строка меньше 3-х символов")
else:
    pred_s = len(st) -2
    new_str = st[0:pred_s]
    print(new_str)

