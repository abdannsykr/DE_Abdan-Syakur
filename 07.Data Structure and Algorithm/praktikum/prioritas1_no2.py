def get_breads(breads, flour_stock):
    def sort_by_flour(bread):
        return bread["flour"]

    stock_bread = []
    
    sorted_bread = sorted(breads, key=sort_by_flour)
    for bread in sorted_bread:
        if bread["flour"] <= flour_stock:
            stock_bread.append(bread["Name"])
            flour_stock -= bread["flour"]
    return stock_bread


bread1 = [
    {"Name": "donut", "flour": 25},
    {"Name": "mini puff", "flour": 15},
    {"Name": "baguette", "flour": 75},
    {"Name": "cupcake", "flour": 15},
]

bread2 = [
    {"Name": "pancake", "flour": 15},
    {"Name": "waffle", "flour": 25},
    {"Name": "bagel", "flour": 15},
    {"Name": "cupcake", "flour": 15},
    {"Name": "choco chips", "flour": 10},
    {"Name": "mini puff", "flour": 5},
    {"Name": "bread", "flour": 30},
]

print("Jenis roti yang dapat dibuat :")
print(get_breads(bread1, 100))  # ['mini puff', 'cupcake', 'donut']
print(get_breads(bread2, 75))   # ['mini puff', 'choco chips', 'pancake', 'bagel', 'cupcake']
