s=input()
l=s.split()
n = int(l[0])
k = int(l[1])
s1=input()
marks=s1.split()
for i in range(len(marks)):
    marks[i] = int(marks[i])
c=0
for i in range(len(marks)):
    for j in range(len(marks)):
        if j==i:
            continue
        if marks[j]>=(marks[i]-k) and marks[j]<=(marks[i]+k):
            c+=1
c=int(c/2)
print(c,"students need to worry!")
print(n-c,"students should relax!")
