'''num=int(input("enter the integer:"))
if((num>99 and num<=999) or (num>=-999 and num<-99)):
    print("three digits number")
else:
    print("not")'''
#four digit number
'''num=int(input("enter the integer:"))
if((num<=999 and num>=9999) or (num<=-9999 and num>=-999)):
    print("four digit")
else:
    print("not")'''
#five digits
num=int(input("enter the integer:"))
if((num>=99999 and num<=10000) or (num<=-99999 and num>=-100000)):
    print("it is a five digit number")
else:
    print("it is not a five digit number")
        
