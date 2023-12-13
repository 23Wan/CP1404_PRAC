from datetime import datetime
from copy import deepcopy

def load_file(file):
    file_content = list()

    f = open(file, 'r')

    for line in f.readlines():
        data = line.strip().split()

        file_content.append(data)

    f.close()

    return file_content


def write_to_file(file_name, content):
    f = open(file_name, 'w')

    for data in content:
        f.write('{}\n'.format(' '.join(data)))

    f.close()


while True:

    print("(L)oad projects")

    print("(S)ave projects")

    print("(D)isplay projects")

    print("(F)ilter projects by date")

    print("(A)dd new project")

    print("(U)pdate project")

    print("(Q)uit")

    ch = input("Enter choice")

    file_content = list()

    if ch == 'L' or ch == 'l':

        filename = input("Enter file name: ")

        file_content = load_file(filename)

    elif ch == 'S' or ch == 's':

        filename = input("Enter file name: ")

        write_to_file(filename, file_content)

    elif ch == 'D' or ch == 'd':

        print("Incomplete projects: ")

        for data in file_content:

            if data[-1] != '100%':
                print('{}'.format(' '.join(data)))

        print("Complete projects: ")

        for data in file_content:

            if data[-1] == '100%':
                print('{}'.format(' '.join(data)))

    elif ch == 'F' or ch == 'f':

        user_date = input("Enter date in format DD/MM/YYYY: ")

        filtered_data = list()

        for data in file_content:

            data_date = datetime.strptime(data[1], 'DD/MM/YYYY')

            user_date = datetime.strptime(user_date, 'DD/MM/YYYY')

            if data_date > user_date:
                temp = deepcopy(data)

                temp[1] = datetime.strptime(temp[1], 'DD/MM/YYYY')

                filtered_data.append(temp)

        filtered_data.sort(key=lambda x: x[1])

        for data in filtered_data:
            print('{}'.format(' '.join(data)))

    elif ch == 'A' or ch == 'a':

        print('Lets add a new project')

        name = input('Name: ')

        start_date = input('Start date (dd/mm/yy): ')

        priority = input('Priority: ')

        cost = input('Cost estimate: ')
        percent_complete = input('Percent complete: ')

        file_content.append([name, start_date, priority, cost, percent_complete])

    elif ch == 'U' or ch == 'u':

        for index, data in enumerate(file_content):
            print(index, data)

        op = input('select project: ')

        priority = input('Enter priority: ')

        completion = input('Enter completion: ')

        if priority:
            file_content[op][2] = priority

        if completion:

            file_content[op][4] = completion

    elif ch == 'Q' or ch == 'q':

      break
    else:
       print('Invalid input please try again')