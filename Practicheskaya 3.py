def zadanie1():
    s1 = input("Ваши фамилия, имя")
    s2 = input("Ваш возраст")
    s3 = input("Вы живете в")

    print(s1, s2, s3)


def zadanie2():
    a1 = int(input("Первое число"))
    a2 = int(input("Второе число"))
    a3 = int(input("Третье число"))

    if a1 >= 1 and a1 <= 3:
        print("a1 принадлежит интервалу")
    else:
        print("Число не находится в интервале")
    if a2 >= 1 and a2 <= 3:
        print("a2 принадлежит интервалу")
    else:
        print("Число не находится в интервале")
    if a3 >= 1 and a3 <= 3:
        print("a3 принадлежит интервалу")

    else:
        print("Число не находится в интервале")
zadanie2()
