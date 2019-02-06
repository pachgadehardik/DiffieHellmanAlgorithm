    import random
    users =[]
    p_keys = []
    q = int(input("Enter the large prime number: "))
    n = int(input("enter the number of users: "))

    root = q-1
    b=[]
    temp =[]
    #Calculation of primitive roots
    for i in range(0,root):
        a = []
        for j in range(0,root):
            f = (i+1)**(j+1) % q
            if(f in a):
                break
            else:
                a.append(f)
            if(len(a) == root):
                temp.append(a)
                b.append(i+1)
    print(b)        
    prim_root = random.choice(b)
    print("primitive root is : ",prim_root)

    #multiple users
    for i in range(n):
        print("enter the private key for user no. ",i+1)
        key =int(input())
        p_keys.append(key)
    for i in range(n):
        for j in range(i+1,n):
            y1 = prim_root ** p_keys[i] %q
            y2 = prim_root ** p_keys[j] % q
            print('y-%d = ' %(i),y1)
            print("y-%d = " %(j),y2)
            k1 = y2 ** p_keys[i] % q
            k2 = y1 ** p_keys[j] % q
            print("k-%d = " %(i),k1)
            print("k-%d = " %(j),k2)
            if k1 == k2:
                print("Successfull communication b/w users",i,"and",j)

    # OUTPUT-1
    # PS H:\CSS Labs> python .\DH.py
    # Enter the large prime number: 97
    # enter the number of users: 3
    # [5, 7, 10, 13, 14, 15, 17, 21, 23, 26, 29, 37, 38, 39, 40, 41, 56, 57, 58, 59, 60, 68, 71, 74, 76, 80, 82, 83, 84, 87, 90, 92]
    # primitive root is :  23
    # enter teh private key for user no.  1
    # 5
    # enter teh private key for user no.  2
    # 7
    # enter teh private key for user no.  3
    # 13
    # y-0 =  5
    # y-1 =  26
    # k-0 =  40
    # k-1 =  40
    # Successfull communication b/w users 0 and 1
    # y-0 =  5
    # y-2 =  80
    # k-0 =  29
    # k-2 =  29
    # Successfull communication b/w users 0 and 2
    # y-1 =  26
    # y-2 =  80
    # k-1 =  39
    # k-2 =  39
    # Successfull communication b/w users 1 and 2

    # OUTPUT-2
    # PS H:\CSS Labs> python .\DH.py
    # Enter the large prime number: 53
    # enter the number of users: 2
    # [2, 3, 5, 8, 12, 14, 18, 19, 20, 21, 22, 26, 27, 31, 32, 33, 34, 35, 39, 41, 45, 48, 50, 51]
    # primitive root is :  33
    # enter the private key for user no.  1
    # 13
    # enter the private key for user no.  2
    # 19
    # y-0 =  23
    # y-1 =  48
    # k-0 =  30
    # k-1 =  30
    # Successfull communication b/w users 0 and 1

    # OUTPUT-3
    # PS H:\CSS Labs> python .\DH.py
    # Enter the large prime number: 43
    # enter the number of users: 4
    # [3, 5, 12, 18, 19, 20, 26, 28, 29, 30, 33, 34]
    # primitive root is :  19
    # enter the private key for user no.  1
    # 8
    # enter the private key for user no.  2
    # 12
    # enter the private key for user no.  3
    # 13
    # enter the private key for user no.  4
    # 24
    # y-0 =  15
    # y-1 =  35
    # k-0 =  35
    # k-1 =  35
    # Successfull communication b/w users 0 and 1
    # y-0 =  15
    # y-2 =  20
    # k-0 =  9
    # k-2 =  9
    # Successfull communication b/w users 0 and 2
    # y-0 =  15
    # y-3 =  21
    # k-0 =  21
    # k-3 =  21
    # Successfull communication b/w users 0 and 3
    # y-1 =  35
    # y-2 =  20
    # k-1 =  16
    # k-2 =  16
    # Successfull communication b/w users 1 and 2
    # y-1 =  35
    # y-3 =  21
    # k-1 =  4
    # k-3 =  4
    # Successfull communication b/w users 1 and 3
    # y-2 =  20
    # y-3 =  21
    # k-2 =  41
    # k-3 =  41
    # Successfull communication b/w users 2 and 3
    # PS H:\CSS Labs>