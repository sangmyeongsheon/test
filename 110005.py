a, b = input().split()
a=int(a)
b=int(b)
result_list=[]
while a>=b:
    if a%b==0:
        result_list.append(0)
    else:
        result_list.append(a%b)
    a=a//b



result_list.append(a)
result_list.reverse()
for i in range(len(result_list)):
    if result_list[i]>9:
        result_list[i]=chr(65+result_list[i]-10)


for i in result_list:
    print (i,end='')
    print()
    #바뀐부분

# 8 4 2 1
# 1 0 0 0