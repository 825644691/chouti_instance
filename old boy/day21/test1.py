import re



def match(data):
    da = re.findall(r"(\d+\.?\d*|,\d*?)", string=data)
    if "EUR" in data:
        da.pop()

        value = "".join(da)
        value = value.replace(",","")
        value = value.replace(".","")
        print(value)
    elif "€" in data:
        value = "".join(da)
        value = value.replace(",",".")
        print(value)
    else:
        value = "".join(da)
        value = value.replace(",","")
        print(value)



match("EUR 1.409,00")
match("€ 409,05")
match("￥409.50")
match("CNY 1,000")
