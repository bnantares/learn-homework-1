"""

Домашнее задание №1

Цикл for: Оценки

* Создать список из словарей с оценками учеников разных классов 
  школы вида [{'school_class': '4a', 'scores': [3,4,4,5,2]}, ...]
* Посчитать и вывести средний балл по всей школе.
* Посчитать и вывести средний балл по каждому классу.
"""

def main():
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    scores_sum = 0
    n_students = 0

    student_grades = [
        {'school_class': '10a', 'scores': [5,4,4,5,4]},
        {'school_class': '10b', 'scores': [4,4,4,5,3]},
        {'school_class': '10c', 'scores': [3,3,4,3,5]},
        {'school_class': '10d', 'scores': [3,4,3,5,2]}
    ]

    # Средний балл по каждому классу 
    for current_class in student_grades:
        class_average = (sum(current_class['scores'])/len(current_class['scores']))
        print(f"Средняя оценка по классу {current_class['school_class']}: {class_average}") 

    # Средний балл по школе
    for avg_class in student_grades:
        scores_sum += (sum(current_class['scores']))
        n_students += (len(current_class['scores']))

    result = scores_sum / n_students
    print(f"Средняя оценка по школе: {result}")
        
if __name__ == "__main__":
    main()
