star_num=int(input())
star_list=[]
for i in range(star_num):
    star_list.append([" "]*star_num)
def star(x,y,star_lenth):
    if star_lenth==3:
        for j in range(3):
            for i in range(3):
                star_list[y+j][x+i]='*'
        star_list[y+1][x+1]=' '
    else:
        for j in range(3):
            for i in range(3):
                if j!=1 or i!=1:
                    star(int(x+i*star_lenth/3),int(y+j*star_lenth/3),int(star_lenth/3))      
    return star_list
    
result=star(0,0,star_num)

for i in range(len(result)):
    if i!=len(result)-1:
        for j in range(len(result[i])):
            print(result[i][j],end='')
        print()
    else:
        for j in range(len(result[i])):
            print(result[i][j],end='')
