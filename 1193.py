# 1 ,1 2, 3 2 1, 1,2,3,4
# 1, 2, 3, 4, 5, 6
# n(n+1)/2
# i=n(n+1)/2
# n^2+n-2i=0
#n=(-1 + (1 - 4 * (-2i))**(1/2)) / 2

print()
i= int(input())
n=(-1 + (1 - 4 * (-2*(i-1)))**(1/2)) / 2
total_num=int(n)+1
count_num=int(i-(total_num-1)*(total_num)/2)
count_num_2=int(total_num-i+(total_num-1)*(total_num)/2)+1
if total_num%2==0:
    print(count_num,"/",count_num_2,sep="",end="")
    print("freshman")
else:
    print(count_num_2,"/",count_num,sep="",end="")