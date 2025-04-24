from importlib.metadata import pass_none

some_string = "m\n5     my name is iGor tyh66666666624545     "

upper = some_string.upper()
lower = some_string.lower()
title = some_string.title()
capitalize = some_string.capitalize()
chain = some_string.lower().upper().capitalize()

clear_string_spaces = some_string.strip()
clear_string_symbols_left = some_string.lstrip(" 54name")
clear_string_symbols_right = some_string.rstrip(" 54name")

change_inner_text = some_string.replace("name", "surname")

table = str.maketrans("65", "56", "\n")
result_smart_change = some_string.translate(table)

slices1 = some_string[:]
slices2 = some_string[1:10]
slices3 = some_string[::2]  # каждый второй символ
slices4 = some_string[1:25:2]  # каждый второй символ до 25 символа
slices5 = some_string[::-1]  # реверс
slices6 = some_string[-3:-20:-1]  # реверс


pass
