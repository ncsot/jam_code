<<<<<<< HEAD
# Savelyev Sergey ncsot@ya.ru

rawData = '''Atlantic Castle Hotel  3 stars  45 000
Oriental Tide Hotel & Spa  5 stars  92 000
Bronze Mansion Resort  4 stars  84 000
Parallel Harbor Hotel  4 stars  80 000
Obsidian Vertex Hotel  5 stars  120 000
Noble Memorial Hotel  4 stars  59 000
Mirth Hotel  4 stars  64 000
Felicity Motel  3 stars  29 000
Renaissance Hotel  3 stars  49 000
Rainbow Hotel & Spa  5 stars  154 000'''


def sortedByCost(rawData):
    # парсим в отсортированый по ценам список
    listData = [i.split("  ") for i in rawData.split("\n")]
    parseCostList = [[hotel[0], 
                     hotel[1], 
                     int(hotel[2].replace(" ", ""))] for hotel in listData]
    parseCostList.sort(key=lambda x: x[2])
    return parseCostList


def searchMaxIndex(userInput, dataset):
    # простой линейный поиск в dataset
    matchIndex = -1
    for index, hotel in enumerate(dataset):
        cost = hotel[2]
        if cost >= userInput:
            matchIndex = index if cost == userInput else index - 1
            break
    if userInput > dataset[len(dataset) - 1][2]:
        matchIndex = len(dataset) - 1
    return matchIndex


def matchingSelection(ind, dataset, n=3):
    # вернет слайс подходящих по цене
    sliceSelect = []
    if ind >= 0:
        sliceSelect = dataset[ind:ind - n:-1] if (ind >= 3) else dataset[ind::-1]
    return sliceSelect

def main(userInp,dataset):
    listMatch = matchingSelection(
                searchMaxIndex(userInp,dataset),
                                dataset)
    lenMatch = len(listMatch)
    if lenMatch:
        print("\nВсего найдено: {}".format(lenMatch))
        for hotel in listMatch:
            print("Отель: {}, Cтатус: {}, Cтоимость: {}".format(*hotel))
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
            main(userInputInt,hotelList)


if __name__ == '__main__':
    hotelList = sortedByCost(rawData)
    cli()
=======
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
>>>>>>> dictData
