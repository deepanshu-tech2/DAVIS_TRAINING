def netbill(consumedunit):
    return (consumedunit*7.25)


def bill(consumedunit):
    result = netbill(consumedunit)
    return result


consumedunit = int(input("enter the consumed unit => "))
print("your bill amout is ",bill(consumedunit))