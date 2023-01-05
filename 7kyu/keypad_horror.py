def computer_to_phone(numbers):
    keyboard = ["7", "8", "9", "4", "5", "6", "1", "2", "3", "0"]
    tel = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
    word = ""
    for x in numbers:
        index = keyboard.index(x)
        word = word + tel[index]
    return word