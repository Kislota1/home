def to_uppercase():
    input_string = input("Введите текст: ")
    output_string = input_string.upper()
    return output_string

def capitalize_words():
    """
    Меняет пеырвые две буквы в словеasdasd на заглавные.
    """
    input_string = input("Введите текст: ")
    words = input_string.split()
    capitalized_words = [word.capitalize() for word in words]
    return ' '.join(capitalized_words)
