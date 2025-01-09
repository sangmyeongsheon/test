test_num=int(input())
for i in range(test_num):
    balance=int(input())
    coin_list=[25,10,5,1]
    balance_list=[0,0,0,0]

    for i in range(4):
        if (balance//coin_list[i] !=0):
            balance_list[i]=balance//coin_list[i]
            balance=balance%coin_list[i]

    for i in balance_list:
        print(i,end=" ")

