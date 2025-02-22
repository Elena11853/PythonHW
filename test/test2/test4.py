#Логические операторы
#Проверка соответствия логина и пароля (логическое "и" (and))
#user_login = "adam"
#user_password = "Qwerty123456"

#login = input("Login: ")
#password = input("Password: ")

#if (login == user_login) and (password == user_password):
#print('Добро пожаловать')

#else:
    #print("Неверный логин или пароль")

    #Оператор or (или)
crit1 = "red"
crit2 = "lock"
colour = input("Colour: ")
feature = input("Featyre: ")
if (colour == crit1) or (feature == crit2):
        print("Покупаю рюкзак")
else:
        print("Ничего не подошло")