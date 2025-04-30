from pywebio.input import NUMBER

from pywebio.input import input as pw_input

from pywebio.output import put_html, put_success

# HEADER
put_html("<hi>Enter a 4-digit number</h1>")

# INPUT SECTION
user_input = pw_input(type="text", required=True, minlength=4, maxlength=4)

# CHECK and OUTPUT SECTION
if user_input.isdigit():
    user_input = list(user_input)
    put_success(
        f"Your inverted number:\n{user_input[3]}\n{user_input[2]}\n{user_input[1]}\n{user_input[0]}"
    )
else:
    put_success("Error: You have extraneous characters")
