a,b,v = input().split()
a=int(a)
b=int(b)
v=int(v)
go_time=(v-b)/(a-b)
if go_time%1!=0:
    go_time=int(go_time)+1
else:
    go_time=int(go_time)
print(go_time)