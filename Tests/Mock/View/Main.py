from Tests.Mock.Controller.Support import convert_input_to_int


def delete_group_logic(cmd_input: str, groups_count: int, groups):
    if cmd_input == "":
        raise Exception("Нет... вы ввели пустую строчку ( ´•︵•` )")
    cmd_input = convert_input_to_int(cmd_input)
    if cmd_input == 0:
        print("0 - Выход\n",
              "1 - Студент\n",
              "2 - Группа\n",
              "3 - Предмет\n",
              "4 - БРС", sep="")
    elif cmd_input <= groups_count:
        print("Успешно удален\n",
              "0. Назад")
    else:
        raise Exception("Выход за пределы массива ( ´•︵•` )")