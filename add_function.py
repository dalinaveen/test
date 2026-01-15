def add(n1,n2):
    c=n1+n2
    return c

if __name__=='__main__':
    n1=int(input('Enter first value :'))
    n2=int(input("Enter second value :"))
    result = add(n1,n2)
    print('sum =',result)