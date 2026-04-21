bal = 1000

try:
    amt = int(input())
    if amt > bal:
        raise Exception("Overdraft")
    bal -= amt
except Exception as e:
    print(e)
