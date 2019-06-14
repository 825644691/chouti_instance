product_list = [
    ('MAC',9000),
    ('kindle',900),
    ('tesla',90000),
    ('python_book',105),
    ('bike',2000),
]

saving = input("please input your money:")
shopping_car=[]

if saving.isdigit():
    saving=int(saving)
    while True:
        for i,v in enumerate(product_list):
            print(i,v)
        #for i in product_list:
        #    print(product_list.index(i),i)
        choice=input('选择购买商品编号[退出：q]')
        if choice.isdigit():
            choice=int(choice)
            if 0<choice<=len(product_list):
                p_item=product_list[choice-1]
                if p_item[1]<saving:
                    saving-=p_item[1]
                    shopping_car.append(p_item)
                else:
                    print("余额不足，还剩%s"%saving)
            else:
                print("编码不存在")
            print(shopping_car)
        elif choice=='q':
            print("--------您已经购买如下商品---------")
            for i in shopping_car:
                print(i)
            print("您还剩钱%s元钱"%saving)
            break
        else:
            print("wrong")
