def tree(cycle):
    height=1
    for i in range (1,cycle+1):
        if i%2!=0:
            height*=2
        else:
            height+=1
    print("height of tree after",cycle,"growth cycles is",height)
list=[]
test=int(input("Enter the number of test cases : "))
for i in range (test):
    print(i+1)
