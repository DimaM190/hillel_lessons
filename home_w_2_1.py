from pywebio.input import NUMBER

from pywebio.input import input as pw_input

from pywebio.output import put_html, put_success

# HEADER
put_html("<hi>Enter a 4-digit number</h1>")

# INPUT SECTION
user_input = pw_input(type="text", required=True, minlength=4, maxlength=4)

# # CHECK and OUTPUT SECTION
# if user_input.isdigit():
#     user_input = list(user_input)
#     put_success(
#         f"Your number:\n{user_input[0]}\n{user_input[1]}\n{user_input[2]}\n{user_input[3]}"
#     )
# else:
#     put_success("Error: You have extraneous characters")
if user_input.isdigit():
    user_input = int(user_input)
    value_1 = user_input // 1000
    number_1 = user_input - value_1 * 1000
    value_2 = number_1 // 100
    number_2 = number_1 - value_2 * 100
    value_3 = number_2 // 10
    value_4 = number_2 - value_3 * 10

    put_success(f"Your number:\n{value_1}\n{value_2}\n{value_3}\n{value_4}")
else:
    put_success("Error: You have extraneous characters")
