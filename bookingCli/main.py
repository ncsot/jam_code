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
            listMatch = matchingSelection(
                        searchMaxIndex(userInputInt,hotelList),
                                          hotelList)
            lenMatch = len(listMatch)
            if lenMatch:
                print("\nВсего найдено: {}".format(lenMatch))
                for hotel in listMatch:
                    print("Отель: {}, Cтатус: {}, Cтоимость: {}".format(*hotel))
            else:
                print("Ничего не найдено :(")


if __name__ == '__main__':
    hotelList = sortedByCost(rawData)
    cli()
