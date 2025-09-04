"""
- Create a function that takes in 3 parameters(firstname, lastname, age) and
returns a dictionary based on those values
"""

def get_details(first_name, last_name, age):
    return {
        "first_name": first_name,
        "last_name": last_name,
        "age":age
    }

print(get_details("Syed Ibrahim", "T", 28))
