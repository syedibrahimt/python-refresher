def calculate_income(income: int, tax_percent: int):
    take_home = round(income - (income * (tax_percent/100)))
    print(f"take home is {take_home}")
    return take_home