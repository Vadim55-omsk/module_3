def send_email (message, recipient, sender='university.help@gmail.com'):
    if "@" not in recipient and "@" not in sender:
         print("Невозможно отправить письмо с адреса", sender, "на адрес", recipient)
         print(recipient.endswith(".com, .ru, .net")) # метод endswith проверяет, заканчивается ли строка на указанное окончаниеbreak

    elif recipient == sender:
              print("Нельзя отправить письмо самому себе")

    elif sender=='university.help@gmail.com':
        print("Письмо успешно отправлено с адреса", sender, "на адрес", recipient)
    else:
        print("НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ!Письмо отправлено с адреса", sender, "на адрес", recipient)



send_email("Тестовое сообщение","hgfkjhkj",'university.helpgmail.jk')
send_email("Тестовое сообщение","help@gmail.com","help@gmail.com")
send_email("Тестовое сообщение","Jonny@gmail.com","university.help@gmail.com")
send_email("Тестовое сообщение","university@gmail.com","university.fan@gmail.com")

