import sys
from funcs import *

main_action_list = [
    [task_list, "Список задач"],
    [edit_tasks, "Редактировать задачи"],
    [main_menu, "Главное меню"],
    [sys.exit, "Выход"]
]

    

print("Добро пожаловать в ToDo!")
main_menu(main_action_list)