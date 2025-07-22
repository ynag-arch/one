def shopping_cart():
    """简易购物车系统"""
    cart = []
    while True:
        print("\n=====购物车系统=====")
        print("1.添加商品")
        print("2.删除商品")
        print("3.查看购物车")
        print("4.结账")
        print("5.退出")
        choice = input("选择1~5")

        if choice == "5":
            print("谢谢使用")
            break

        elif choice == "1":
            name = input("请输入商品名")
            price = float(input("请输入商品价格"))
            quantity = int(input("请输入数量"))

            found = False
            for item in cart:
                if item["name"] == name:
                    item["quantity"] += quantity
                    found = True
                    break
            if not found:
                cart.append({"name": name,
                                "price": price,
                                 "quantity": quantity})
                print(f"已添加{name}到购物车")

        elif choice == "2":
            if not cart:
                print("购物车为空无法删除商品")
                continue
            name = input("请输入需要删除的商品名")
            found = False
            for i, item in enumerate(cart):
                if item["name"] == name:
                    del cart[i]
                    found = True
                    break
            if found:
                print(f"已经从购物车{name}删除")
            else:
                print(f"没有从购物车找到{name}")

        elif choice == "3":
            if not cart:
                print("购物车为空")
                continue

            print("\n<<<<<购物车内容>>>>>>")
            print(f"{'商品名称':<15} {'单价':<10} {'数量':<10} {'小计':<10}")
            print("-" * 45)


            total = 0
            for item in cart:
                subtotal = item["price"] * item["quantity"]
                total += subtotal

                print(f"{item['name']:<15}  ${item["price"]:<9.2f}  ${item["quantity"]:<10} ${subtotal:<9.2f}")
                print("-" * 45)
                print(f"总共: ${total:.2f}")

        elif choice == "4":
            if not cart:
                print("购物车为空无法结算")
                continue

            print("\n<<<<<购物车内容>>>>>>")
            print(f"{'商品名称':<15} {'单价':<10} {'数量':<10} {'小计':<10}")
            print("-" * 45)

            total = 0
            for item in cart:
                subtotal = item["price"] * item["quantity"]
                total += subtotal

                print(f"{item['name']:<15}  ${item["price"]:<9.25}  ${item["quantity"]:<10} ${subtotal:<10}")
            print("-" * 45)
            print(f"总共: ${total:.2f}")
            print("付款成功谢谢你的惠顾")

            cart.clear()


        else:
            print("无效的输入，请你在1~5之间输入")


if __name__ == '__main__':
    shopping_cart()
