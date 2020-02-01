# Savelyev Sergey ncsot@ya.ru

d = [{"name":"Atlantic Castle Hotel","star":"3 stars","cost":45000},
     {"name":"Oriental Tide Hotel & Spa", "star":"5 stars", "cost":92000},
     {"name":"Parallel Harbor Hotel", "star":"5 stars", "cost":84000},
     {"name":"Obsidian Vertex Hotel", "star":"5 stars", "cost":80000},
     {"name":"Noble Memorial Hotel", "star":"5 stars", "cost":120000},
     {"name":"Mirth Hotel", "star":"5 stars", "cost":59000},
     {"name":"Felicity Motel", "star":"5 stars", "cost":64000},
     {"name":"Renaissance Hotel ", "star":"5 stars", "cost":29000},
     {"name":"Rainbow Hotel & Spa", "star":"5 stars", "cost":154000}]



def main(userInp,dataset):
    filteredCost = sorted(filter(lambda x: x["cost"]<=userInp,dataset),key=lambda x:x["cost"])
    lenMatch = len(filteredCost)
    selectCost = filteredCost[lenMatch:lenMatch-4:-1] if (lenMatch >3) else filteredCost[lenMatch::-1]
    if lenMatch:
        print("\nВсего найдено: {}".format(len(selectCost)))
        for hotel in selectCost:
            print("Отель: {}, Cтатус: {}, Cтоимость: {}".format(*hotel.values()))
    else:
        print("Ничего не найдено :(")


def cli():
    # интерфейс пользователя
    print("Мы подберем отель, просто введите желаемую стоимость. "
          "Или нажмите 'q' и 'Enter' для выхода")
    while True:
        try:
            userInput = input("\nВведите стоимость: ")
            if not userInput:
                print("Вы ввели пустую строку\nДля выхода нажмите 'q'")
                continue
            elif userInput == "q":
                raise KeyboardInterrupt
            userInputInt = int(userInput)
        except ValueError:
            print("Введите стоимость цифрами")
        except KeyboardInterrupt:
            print("\nДо свидания")
            break
        else:
            main(userInputInt,d)


if __name__ == '__main__':
    cli()
