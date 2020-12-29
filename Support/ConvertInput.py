def convert_input_to_int(user_input: str):
    try:
        val = int(user_input)
        return val
    except ValueError:
        print("Нет... вы ввели не целое число ( ´•︵•` )")