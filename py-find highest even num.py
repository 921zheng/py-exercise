


def highest_even(li):
    highest=0
    for num in li:
        if num%2==0:
           if num>highest:
               highest=num
               print (highest)

highest_even([10,2,4,3,5,3,1,8])