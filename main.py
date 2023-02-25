import management

def nav():
    print('+-----------+')
    print('| 1. Login  |')
    print('+-----------+')
    print('| 2. Signup |')
    print('+-----------+')
    print('| 3. Logout |')
    print('+-----------+')

def choiceGender():
    while True:
        print('+-------+-------+')
        print('|  Man  | Woman |')
        print('+-------+-------+')
        gender = input('Gender : ')
        if gender == 'Man' or 'Woman':
            return gender

Login = False

while True:
    nav()
    while True:
        print('Enter a command number.\n> ', end='')
        commandNumber = int(input())
        if commandNumber > 0 and commandNumber < 4:
            break
    if commandNumber == 1:
        print('[ Login ]')
        while True:
            id = input('Id : ')
            if id != '':
                break
        while True:
            password = input('Password : ')
            if password != '':
                break
        login = management.login(id, password)
        if login == 'SUCCESS':
            Login = True
            print('Login success')
        else:
            print('Login failure')
        print(f'Login status : {Login}\n')
    elif commandNumber == 2:
        print('[ Sign up ]')
        while True:
            email = input('Email : ')
            if email != '':
                break
        while True:
            id = input('Id : ')
            if id != '':
                break
        while True:
            password = input('Password : ')
            if password != '':
                break
        while True:
            phone = input('Phone number : ')
            if phone != '':
                break
        gender = choiceGender()
        err = management.signup(email, id, password, phone, gender)
        if err == 'EMAIL_ERROR':
            print('[ERROR] Duplicate email.\n')
        elif err == 'ID_ERROR':
            print('[ERROR] Duplicate id.\n')
        elif err == 'PHONE_ERROR':
            print('[ERROR] Duplicate phone.\n')
        else:
            print('Member registration completed.\n')
    else:
        Login = False
        print('You have logged out...')
        print(f'Login status : {Login}\n')