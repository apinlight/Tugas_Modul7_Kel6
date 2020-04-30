from collections import deque
pilihan1 = 0
pilihan2 = 0
data = 0
count = 0
queue1 = deque()
queue2 = deque()
while count == 0:
    print("\n~~~~~~~~~~~~~~ Selamat Datang! ~~~~~~~~~~~~~~~~~")
    print("~~~~~~~~ Queue Ganjil-Genap Kelompok 06 ~~~~~~~~")
    print("Bilangan yang anda ingin Queue itu bilangan apa?")
    print("1. Ganjil")
    print("2. Genap")
    print("3. Keluar Program")
    count +=1
    pilihan1 = int(input("\nMasukkan Pilihan : "))
    if pilihan1 == 1:
        print("\n~~~~~~~~~~ Ini Queue Ganjil ~~~~~~~~~~")
        print("1. Enqueue Item")
        print("2. Dequeue Item")
        print("3. Lihat Daftar Data")
        print("4. Lihat Data Teratas")
        pilihan2 = int(input("\nMasukkan Pilihan : "))
        count +=1
        if pilihan2 == 1:
            data = int(input("\nInput Data : "))
            if data %2 == 1 :
                queue1.append(data)
                print ("")
                count = 0
            elif data %2 == 0 :
                print("Data Bilangan Genap!")
                count = 0
            else :
                print("Data bukan Bilangan Bulat!")
                count = 0
        elif pilihan2 == 2:
            queue1.popleft()
            count = 0
            print ("")
        elif pilihan2 == 3:
            print(queue1)
            count = 0
            print ("")
        elif pilihan2 == 4:
            print(queue1[0])
            count = 0
            print ("")
        else :
            print ("\nPilihan tidak tersedia\n")
            count = 0
    elif pilihan1 == 2:
        print("\n~~~~~~~~~~ Ini Queue Genap ~~~~~~~~~~")
        print("1. Enqueue Item")
        print("2. Dequeue Item")
        print("3. Lihat Daftar Data")
        print("4. Lihat Data Teratas")
        pilihan2 = int(input("\nMasukkan Pilihan : "))
        count +=1
        if pilihan2 == 1:
            data = int(input("\nInput Data : "))
            if data %2 == 0 :
                queue2.append(data)
                print ("")
                count = 0
            elif data %2 == 1 :
                print("Data Bilangan Ganjil!")
                count = 0
            else :
                print("Data bukan Bilangan Bulat!")
                count = 0
        elif pilihan2 == 2:
            queue2.popleft()
            count = 0
            print ("")
        elif pilihan2 == 3:
            print(queue2)
            count = 0
            print ("")
        elif pilihan2 == 4:
            print(queue2[0])
            count = 0
            print ("")
        else:
            print ("\nPilihan tidak tersedia\n")
            count = 0
    elif pilihan1 == 3 :
        print("\nTerimakasih telah menggunakan program! ^_^\n")
    else:
        print ("\nPilihan tidak tersedia\n")
        count = 0
