def get_vat(price, vat_rate):
    if isinstance(price, (int, float)) and price > 0 :
        vat = price / 100 * vat_rate
        print(vat)
    else:
        print("Вася ввел фигню")


price1 = -1
vat_rate1 = 18
get_vat(price1, vat_rate1)

#