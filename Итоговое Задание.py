import csv

print("Выберете что хотите сделать: \n1.График отпусков \n2.Прмеия к 13 сентбяря \n3.Премия к 8 марта \n4.Премия к 23 февраля \n5.Индексация зарплат")
a = input()


#График отпусков
if (int)(a) == 1: 
    print('введите текущую датy в формате 31.01.20004')
    data1 = input()
    year = (str)(data1[-4:])
    month = (str)(data1[3:5])
    print(year, month)


    with open('machine_learning_2.csv', newline='') as addresses_csv:
        address_reader = csv.DictReader(addresses_csv, delimiter=';')
        for row in address_reader:
            data = row['Date_of_Employment']
            if ((int)(year) - ((int)(data[-4:])) >= 1) or ((int)(month) - (int)(data[3:5]) >= 6):
                print(row['Full_Name'], ' Имеет отпуск')
            else:
                print(row['Full_Name'], 'Не имеет отпуск')


elif (int)(a) == 2:
    print("Прмеия к 13 сентбяря")
    with open('machine_learning_2.csv', newline='') as addresses_csv:
        address_reader = csv.DictReader(addresses_csv, delimiter=';')
        for row in address_reader:
            Salary = (int)(row['Salary'])
            Position = row['Position']
            full_name = row['Full_Name']
            if Position == 'Senior programmer' or Position == 'Lead programmer' or Position == 'Junior programmer':
                Salary = Salary + Salary * 0.03
            print(full_name,' ', Salary)
            


elif (int)(a) == 3:
    print("Премия к 8 марта")
    with open('machine_learning_2.csv', newline='') as addresses_csv:
        address_reader = csv.DictReader(addresses_csv, delimiter=';')
        for row in address_reader:
            Sex =row['Sex']
            full_name = row['Full_Name']
            if Sex == 'F':
                print(full_name, '- премия 2000')



elif (int)(a) == 4:
    print("Премия к 23 февраля")
    with open('machine_learning_2.csv', newline='') as addresses_csv:
        address_reader = csv.DictReader(addresses_csv, delimiter=';')
        for row in address_reader:
            Sex =row['Sex']
            full_name = row['Full_Name']
            if Sex == 'M':
                print(full_name, '- премия 2000')

elif (int)(a) == 5:
    print("Индексация зарплат")
    print('введите текущий год')
    data1 = input()
    year = (str)(data1)

    with open('machine_learning_2.csv', newline='') as addresses_csv:
        address_reader = csv.DictReader(addresses_csv, delimiter=';')
        for row in address_reader:
            data = row['Date_of_Employment']
            Salary = (int)(row['Salary'])
            full_name = row['Full_Name']
            if (int)(year) - (int)(data[-4:]) >= 10:
                Salary = Salary + Salary * 0.07
            else:
                Salary = Salary + Salary * 0.05
            print(full_name, Salary)



