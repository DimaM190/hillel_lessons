from pywebio.input import slider, FLOAT
from pywebio.output import put_html


# HEADER
put_html("<hi>Welcom to our shop</h1>")

# INPUT SECTION

put_html("<hi>Cheese</h1>")

cheese_weight = slider("Cheese", type=FLOAT, min_value=0, max_value=0.15, required=True)
