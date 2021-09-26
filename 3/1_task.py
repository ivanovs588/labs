with open('Упражнение_1.txt' , 'w') as file:
    file.write('   qwertyui')
    file.write(' iuytrewwq \n')
file.close()
Filik = input()
try:
    with open(Filik, 'r') as file:
        for line in file:
            print(line.strip())
    file.close()

except FileNotFoundError:
    print("Введите другое имя!")
except Exception:
    print("ERROR")
