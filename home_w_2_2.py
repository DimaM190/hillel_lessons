from pywebio.input import input as pw_input

from pywebio.output import put_html, put_success

# HEADER
put_html("<hi>Enter a 5-digit number</h1>")

# INPUT SECTION
user_input = pw_input(type="text", required=True, minlength=5, maxlength=5)

# CHECK and OUTPUT SECTION

if user_input.isdigit():
    user_input = int(user_input)
    value_1 = user_input % 10
    number_1 = user_input // 10
    value_2 = number_1 % 10
    number_2 = number_1 // 10
    value_3 = number_2 % 10
    number_3 = number_2 // 10
    value_4 = number_3 % 10
    value_5 = number_3 // 10
    reversed_number = int(f"{value_1}{value_2}{value_3}{value_4}{value_5}")
    put_success(f"Your reserved number:\t{reversed_number}")
else:
    put_success("Error: You have extraneous characters")
