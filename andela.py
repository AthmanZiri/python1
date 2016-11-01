
def andela():
    list=[]
    a=input("first number: ")
    list.append(a)
    b=input("second number: ")
    list.append(b)
    c=input("third number: ")
    list.append(c)
    d=input("fourth number: ")
    list.append(d)
    e=input("fifth number: ")
    list.append(e)
  
    print list.sort() 
    while list.len():
          prod=[]
          f=list.pop(0)
          l=list.pop()
          fp=f*l
          prod.append(fp)
          print prod
    return list

