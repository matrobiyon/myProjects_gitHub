import sys
import json

dic = {}
class actions():
    # def __init__(self, dobavit,izmenit,udalit,summa):
    #     self.dobavit = dobavit
    #     self.izmenit = izmenit
    #     self.udalit = udalit
    #     self.summa = summa
    
    def dobavit(self):
        try:
            with open("actions.json", "r") as f:
                data = json.load(f)
            with open("actions.json", "w") as f:
                naimenovanie = input("Наименование: ").lower()
                z = True
                while z:
                    try:
                        cena = int(input("Цена: "))
                        z = False
                    except:
                        z = True
                data2 = {}
                data2[naimenovanie] = cena
                data.update(data2)
                # f.seek(0)
                x = json.dumps(data)
                # x = json.dumps(data,separators=(",","-"))
                f.write(x)
                # f.truncate()
        except:
            with open("actions.json", "w") as f:
                naimenovanie = input("Наименование: ").lower()
                z = True
                while z:
                    try:
                        cena = int(input("Цена: "))
                        z = False
                    except:
                        z = True
                data2 = {}
                data2[naimenovanie] = cena
                x = json.dumps(data2)
                f.write(x)
    def izmenit(self):
        with open("actions.json", "r+") as f:
            data = json.load(f)
            key = input("Введите имю продукта для изменения: ").lower().strip()
            try:
                if data[key]:
                    naimenovanie = input("Наименование: ").lower()
                    z = True
                    while z:
                        try:
                            cena = int(input("Цена: "))
                            z = False
                        except:
                            z = True
                    del data[key]
                    print(data)
                    data2 = {}
                    data2[naimenovanie] = cena
                    data.update(data2)
                    f.seek(0)
                    x = json.dumps(data)
                    f.seek(0)
                    # x = json.dumps(data,separators=(",","-"))
                    f.write(x)
                    f.truncate()
            except:
                print("Такого продукта не существует( ")
    def udalit(self):
        with open("actions.json", "r+") as f:
            data = json.load(f)
            key = input("Введите имю продукта для удаления: ").lower().strip()
            try:
                if data[key]:
                    del data[key]
                    f.seek(0)
                    x = json.dumps(data)
                    # x = json.dumps(data,separators=(",","-"))
                    f.write(x)
                    f.truncate()
            except:
                print("Такого продукта не существует( ")
    def summa(self):
        with open("actions.json", "r") as f:
            x = json.load(f)
            print(sum(x.values()))
if len(sys.argv) == 2:
    command = sys.argv[1]
    
    if command == "dobavit":
        call_class = actions()
        call_class.dobavit()
    elif command == "izmenit":
        call_class = actions()
        call_class.izmenit()
    elif command == "udalit":
        call_class = actions()
        call_class.udalit()
    elif command == "summa":
        call_class = actions()
        call_class.summa()
    else:
        print("Вы ввели неправильную команду!")
else:
    print("Пожалуйса, ввелите команду!")


