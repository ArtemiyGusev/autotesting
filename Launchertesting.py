#from autotesting.insertpribor import *
print('Введите:\n "1" - для добавления приборов\n "2" - для добавления группы приборов\n "3" - для чистке всех приборов\n Команда "exit" - Выйти\n Ввод:')
nomertesta = input()

if nomertesta == "1":
    try:
        from autotesting.insertpribor import *
    except:
        print("Тест добавления приборов не выполненен")
if nomertesta == "2":
    try:
        from autotesting.insertpriborgrup import *
    except:
        print("Тест добавления группы приборов не выполненен"+e)
        pass
if nomertesta == "3":
    try:
        from autotesting.chistkapriborov import *
    except:
        print("Тест чистки всех приборов не выполненен")
if nomertesta == "4":
    try:
        from autotesting.pesok import *
    except:
        print("Тест чистки всех приборов не выполненен")
if nomertesta == "exit":
    exit()
