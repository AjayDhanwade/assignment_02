no=int(input())
if no>1:
    for i in range(2,int(no/2)+1):
        if no%i==0:
            print("Not Prime")
            break
        
    else:
        print("Prime")
else:
    print("Not Prime")