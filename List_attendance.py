n,k=map(int,input().split())
l=list(map(int,input().split()))
c=0
for i in l:
	if i==k:
		print("yes")
		c+=1
if c==0:
	print("no")
