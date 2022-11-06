import xml
from os import name
import json
import xml.etree.ElementTree as ET


class Dish:
    def __init__(self, name='', price=0, weight=0):
        self.name = name
        self.weight = weight
        self.price = price
        data['Dishes'].append(self.__dict__)

    def setD(self, name, price, weight):
        self.name = name
        self.weight = weight
        self.price = price


class Drink:
    def __init__(self, name='', price=0, portion=0) -> None:
        self.name = name
        self.price = price
        self.portion = portion
        data1['Drinks'].append(self.__dict__)


    def setD(self, name, price, portion):
        self.name = name
        self.price = price
        self.portion = portion


data = {
    "Dishes": []
}

data1 = {
    "Drinks":[]
}

Drinks = []

class restauran:
    def takeASeat():
        try:
            with open('data.json', 'r+') as outfile:
                s = json.load(outfile)
                for i in range(len(s['Dishes'])):
                    data['Dishes'].append(s['Dishes'][i])
        except json.decoder.JSONDecodeError:
           print("No value ")

        payment = 0
        print(
            "1 - Добавление блюда в меню\n2 - Запись позиции из меню в файл\n3 - Добавление напитка в меню\n4 - Добавление напитка в файл")
        print(
            "5 - Удаление позиций\n6 - Просмотр доступных блюд\n7 - Просмотр доступных напитков\n8 - Заказ блюд\n0 - Выход")
        a = 1
        try:
            while (a != 0):
                a = int(input("Введите желаемое действие: "))
                if (a < 0 or a > 9):
                    raise TypeError
                elif a == 1:
                    menu.addDish()
                elif a == 2:
                    menu.jsonDataDdd(data)
                elif a == 3:
                    menu.addDrink()
                elif a == 4:
                    menu.xmlDataAdd(data1)
                elif a == 5:
                    menu.jsonDataRead()
                    m = input("Введите название блюда на удаление: ")
                    menu.removePosition(m)
                    menu.removePositionXml('sample.xml')
                elif a == 6:
                    s = menu.jsonDataRead()
                elif a == 7:
                    menu.xmlDataRead('sample.xml')
                elif a == 8:
                    l = customer.makeAnOrder()
                    payment += l
                elif a == 0:
                    print("Вы заказали на сумму: ", payment)
                    print("Ресторан закрывается")
                    exit(1)
        except TypeError:
            print("A is not a number or there is no valid option")
        except json.decoder.JSONDecodeError:
            print("Вероятно вы пытаетесь прочесть файл в котором ничего нет")


class menu:
    def addDish():
        try:
            x = input("Введите имя блюда: ")
            y = int(input("Цену: "))
            z = int(input("Вес :"))
            position = Dish(x, y, z).__dict__
        except TypeError:
            print("Unrecognizable name or price can not be describe as 0")
        except ValueError:
            print("Wrong value")

    def addDrink():
        try:
            x = input("Введите имя блюда: ")
            y = int(input("Введите цену напитка: "))
            z = int(input("Предпочитаете 0.5 или же литр? "))
            position = Drink(x, y, z).__dict__
            Drinks.append(position)
        except TypeError:
            print("Unrecognizable name or you can`t purchase 5 gallon of beer on once")
        except ValueError:
            print("Wrong value")

    def jsonDataDdd(data):
        with open('data.json', "r+") as outfile:
            json.dump(data, outfile, indent=4)

    def removePosition(m):
        with open('data.json', 'r+') as outfile:
            s = json.load(outfile)
        for i in range(len(s['Dishes']) - 1):
            if s['Dishes'][i]['name'] == m:
                del s['Dishes'][i]
                del data['Dishes'][i]
        with open('data.json', 'w') as outfile:
            json.dump(s, outfile, indent=4)

    def jsonDataRead():
        try:
            with open('data.json', 'r+') as outfile:
                s = json.load(outfile)
                for i in s['Dishes']:
                    print("Name:", i['name'], "Price:", i['price'], "Weight:", i['weight'])
                return s
        except json.decoder.JSONDecodeError:
            print("Пустой файл")

    def xmlDataAdd(data):
        root = ET.Element('Drinks')
        for i in data['Drinks']:
            s = ET.SubElement(root, 'name').set('name', str(i['name']))
            y = ET.SubElement(root, 'price').set('price', str(i['price']))
            h = ET.SubElement(root, 'portion').set('portion', str(i['portion']))
        tree = ET.ElementTree(root)
        tree.write("sample.xml")


    def xmlDataRead(path):
        try:
            tree = ET.parse(path)
            root = tree.getroot()
            for child in root:
                print(child.attrib)
                for pop in child:
                    print(pop.attrib)
        except xml.etree.ElementTree.ParseError:
            print("Здесь ничего нет")

    def removePositionXml(path):
        menu.xmlDataRead('sample.xml')
        s = input("Введите имя напитка, который хотите удалить: ")
        tree = ET.parse(path)
        root = tree.getroot()
        for name in root:
            if name.attrib.get('name') == s:
                root.remove(name)
                tree.write('sample.xml')
                break



class customer:
    def makeAnOrder():
        a = 1
        totalsum = 0
        s = menu.jsonDataRead()
        while a != -1:
            a = int(input("Выберите номер блюда, которое хотите заказать; Для выхода набирите -1  "))
            if a == -1:
                break
            else:
                p = s['Dishes'][a]['price']
                totalsum += p
        a = 1
        menu.xmlDataRead('sample.xml')
        while s != -1:
            s = input('Введите Название напитка; Для выхода введите -1 ')
            if s == "-1":
                return totalsum
            else:
                tree = ET.parse('sample.xml')
                root = tree.getroot()
                for name in root:
                    if name.attrib.get('name') == s:
                        for price in name:
                            if price.attrib.get('price') != None:
                                v = int(price.attrib.get('price'))
                                totalsum += v



restauran.takeASeat()

