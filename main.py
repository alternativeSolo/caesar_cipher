def encode_decode():
    frst = False
    keey = False
    mylist = []
    while frst == False:
        x = input("выберите вариант,если вы хотите зашифровать сообщение то напишите 1,если хотите расшифровать то 2: ")
        if x == '1':
            var = 1
            frst = True
        if x == '2':
            var = 2
            frst = True
        if x != '1' and x != '2':
            print("вы ввели не то что я у вас просил ")
            
    if var == 1:
        mess = input("введите сообщение которое хотите зашифровать: ")
        while keey == False:
            key = int(input("введите ключ шифрования: "))
            if key < 1 or key > 25 :
                print("ключ должен быть больше 1, и по прикольчику меньше 26")
            else:
                keey = True
        for i in mess:
            i = i.lower()
            if ord(i) + key > ord("я"):
                mylist.append(((chr(ord("а") + (key - (ord("я") - ord(i))) - 1))).upper())

            elif ord(i) == 32:
                mylist.append(i)

            else:
                mylist.append(((chr(ord(i) + key))).upper())
        mylist = "".join(mylist)
        print(mylist)
    if var == 2:
        mess = input("введите сообщение которое хотите расшифровать: ")
        while keey == False:
            key = int(input("введите ключ шифрования: "))
            if key < 1 or key > 25 :
                print("ключ должен быть больше 1, и по прикольчику меньше 26")
            else:
                keey = True
        for i in mess:
            
                i = i.lower()
                deviation = ord(i) - 1071
                if ord(i) - key < ord("а") and ord(i) != 32:
                    mylist.append(((chr(ord("я") - key + deviation))).upper())

                elif ord(i) == 32:
                    mylist.append(i)

                else:
                    mylist.append(((chr(ord(i) - key))).upper())
        mylist = "".join(mylist)
        print(mylist)

encode_decode()