
# Пункты задачи:
# Создайте функцию send_email, которая принимает 2 обычных аргумента: message(сообщение),
# recipient(получатель) и 1 обязательно именованный аргумент со значением по умолчанию
# sender = "university.help@gmail.com".
# Если строки recipient и sender не содержит "@" или не оканчивается на ".com"/".ru"/".net",
# то вывести на экран(в консоль) строку: ("Невозможно отправить письмо с адреса <sender>"
#                                         " на адрес <recipient>").
# Если же sender и recipient совпадают, то вывести "Нельзя отправить письмо самому себе!"
# Если же отправитель по умолчанию - university.help@gmail.com,
# то вывести сообщение: "Письмо успешно отправлено с адреса <sender> на адрес <recipient>."
# В противном случае вывести сообщение: ("НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено
#                                        с адреса <sender> на адрес <recipient>.")
# Здесь <sender> и <recipient> - значения хранящиеся в этих переменных.
# За один вызов функции выводится только одно и перечисленных уведомлений!
# Проверки перечислены по мере выполнения.

def send_email (message, recipient, sender='university.help@gmail.com'):
    if "@" not in recipient and "@" not in sender:
         print("Невозможно отправить письмо с адреса", sender, "на адрес", recipient)
         print(recipient.endswith(".com, .ru, .net")) # метод endswith проверяет, заканчивается ли строка на указанное окончаниеbreak

    elif recipient == sender:
              print("Нельзя отправить письмо самому себе")

    elif sender==sender:
        print("Письмо успешно отправлено с адреса", sender, "на адрес", recipient)
    else:
        print("НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ!Письмо отправлено с адреса", sender, "на адрес", recipient)



send_email("Тестовое сообщение","hgfkjhkj",'university.helpgmail.jk')
send_email("Тестовое сообщение","help@gmail.com","help@gmail.com")
send_email("Тестовое сообщение","Jonny@gmail.com","university.help@gmail.com")
send_email("Тестовое сообщение","university@gmail.com","university.fan@gmail.com")
