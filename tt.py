def func():
 try:
    l=[4,5,8,3,4]
    i=int(input("enter:"))
    print(l[i])
    return 1
 except:
    print("error")
    return 0
 finally:
    print("cyber devil")
x=func()
print(x)