t = int(input())
for z in range(t):
    s = input()
    l1 = s.split()
    no_of_friends = int(l1[0])
    remove_friends = int(l1[1])
    popularity=[]
    s1 = input()
    popularity = s1.split()
    for i in range(len(popularity)):
        popularity[i] = int(popularity[i])
    for i in range(remove_friends):
        flag=0
        for j in range(len(popularity)-1):
            if(popularity[j]<popularity[j+1]):
                popularity.pop(j)
                flag=1
                break
        if flag==0:
            popularity.pop()
    op=""
    for i in popularity:
        op+=str(i)+" "
    print(op)
