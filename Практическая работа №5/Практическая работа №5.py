def open_file(filename: str):
    opened = False
    try:
        file = open(filename, "r")
        opened = True
        count = int(file.readline())
        return [int(x) for x in [file.readline() for _ in range(count)]]

    except ValueError:
        print("В файле есть не только числа")

    except FileNotFoundError:
        print("Файла не существует")

    except Exception as ex:
        return 'Неизвестная ошибка: ' + str(ex)

    finally:
        if opened:
            file.close()


filename = input("Введите имя файла 0_0: ")
print(open_file(filename))