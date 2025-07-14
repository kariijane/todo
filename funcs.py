import json

savedActions = None

def controller(valid, actions):
    match valid:
        case 1:
            task_list()
        case 2:
            edit_tasks()
        case 3:
            main_menu(actions)
        case 4:
            print("До новых встреч!")
            actions[3][0]()

def main_menu(actions):
    print("\033[H\033[J")
    global savedActions
    savedActions = actions
    print("##### Главное меню #####")
    print("Выберете действие:")
    
    c = 0
    for i in actions:
        print(c + 1, " - ", i[1])
        c = c + 1

    controller(validator(len(actions)), actions)
    
def task_list():
    print("\033[H\033[J") 
    print("##### Список задач #####")

    with open("tasks.json", "r") as f:
        readed = json.load(f)
        for i in readed:
            status = None
            if i['status']:
                status = "Active"
            else:
                status = "Inactive"
            print(readed.index(i), " - ", i['name'], " - ", status)
        f.close()
    input('\nНажмите Enter, чтобы вернуться в меню')
    main_menu(savedActions)
        
def edit_tasks():
    print("\033[H\033[J") 
    print("##### Редактор задач #####")
    def change_task():
        print("\033[H\033[J") 
        print("--- Изменение задачи ---")
        index = int(input("Введите id задачи: "))
        with open("tasks.json", "r") as f:
            tasks = json.load(f)
            task = tasks[index]
            print(task['name'], " - ", task['status'])
            task['name'] = input("Введите новое название задачи: ")
            tasks[index] = task
            f.close()
            with open("tasks.json", "w") as wf:
                wf.write(json.dumps(tasks))
                wf.close()
        
        print("Имя сохранено")
        edit_tasks()

    def change_task_status():
        print("\033[H\033[J") 
        print("--- Изменение статуса задачи ---")
        index = int(input("Введите id задачи: "))
        with open("tasks.json", "r") as f:
            tasks = json.load(f)
            task = tasks[index]
            print(task['name'], " - ", task['status'])
            oldStatus = task['status']
            if oldStatus:
                task['status'] = False
            else:
                task['status'] = True
            tasks[index] = task
            f.close()
            with open("tasks.json", "w") as wf:
                wf.write(json.dumps(tasks))
                wf.close()

        print("Статус сохранен")
        edit_tasks()

    def add_task():
        print("\033[H\033[J") 
        print("--- Создание задачи ---")
        name = input("Введите название задачи: ")
        with open("tasks.json", "r") as f:
            tasks = json.load(f)
            tasks.append({'name': name, 'status': True})
            f.close()
            with open("tasks.json", "w") as wf:
                wf.write(json.dumps(tasks))
                wf.close()
        print("Задача создана")
        edit_tasks()
    
    def delete_task():
        print("\033[H\033[J") 
        print("--- Удаление задачи ---")
        index = int(input("Введите id задачи: "))
        match input("Вы уверены? (д/н): "):
            case "д":
                with open("tasks.json", "r") as f:
                    tasks = json.load(f)
                    tasks.pop(index)
                    f.close()
                    with open("tasks.json", "w") as wf:
                        wf.write(json.dumps(tasks))
                        wf.close()
                print("Задача удалена")
                edit_tasks()
            case "н":
                edit_tasks()

    print("Выберите действие:")
    print("1 - Изменить название задачи")
    print("2 - Изменить статус задачи")
    print("3 - Добавить задачу")
    print("4 - Удалить задачу")
    print("5 - Главное меню")

    valid = validator(5)
    match valid:
        case 1:
            change_task()
        case 2:
            change_task_status()
        case 3:
            add_task()
        case 4:
            delete_task()
        case 5:
            main_menu(savedActions)

def validator(length):
    while True:
        choose = input()
        if choose.isdigit():
            choose = int(choose)
            if choose <= length and choose > 0:
                return choose
            else:
                print("Такого действия не существует")
        else:
            print("Введите число")
      