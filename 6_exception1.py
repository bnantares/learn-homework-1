"""

Домашнее задание №1

Исключения: KeyboardInterrupt

* Перепишите функцию hello_user() из задания while1, чтобы она 
  перехватывала KeyboardInterrupt, писала пользователю "Пока!" 
  и завершала работу при помощи оператора break
    
"""

def hello_user():
    """
    Замените pass на ваш код
    """
    howdy = {
        "Как дела?":"Хорошо!",
        "Что делаешь?":"Программирую",
        "Как погода?":"Дождь",
        "Что читаешь?":"Лавкрафта",
        "Пока!":"Счастливо!"
    }
    
    while True:
        try:
            user_say = input("Задай вопрос: ")
            print(howdy[user_say])
        except KeyError: 
            print("Я таких слов не знаю")
        except KeyboardInterrupt:
            print("\nПока!")
            break    
        if user_say == "Пока!":
            break
    
if __name__ == "__main__":
    hello_user()
