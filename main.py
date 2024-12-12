"Program Manajemen Kontak"

def melihat_kontak():
    # melihat semua kontak
    if kontak:
        for num, item in enumerate(kontak, start=1):
            print(f'{num}. {item["nama"]} ({item["HP"]}, {item["email"]})')
    else:
        print("Kontak masih kosong")
        return 1

def menambah_kontak():
    # menambahkan kontak
    nama = input("Masukkan nama kontak yang baru: ")
    HP = input("Masukkan nomor HP kontak yang baru: ")
    email = input("Masukkan alamat email kontak yang baru: ")
    kontak_baru = {'nama': nama, 'HP': HP, 'email': email}
    kontak.append(kontak_baru)
    print("Kontak baru telah berhasil ditambahkan!")

def menghapus_kontak():
    # menghapus kontak
    if melihat_kontak() == 1:
        return
    else:
        i_hapus = int(input("Masukkan nomor kontak yang akan dihapus: "))
        del kontak[i_hapus - 1]
        print("Kontak berhasil dihapus")

kontak1 = {'nama' : 'Andi', 'HP' : '123456789', 'email' : 'andi@python.com'}
kontak2 = {'nama' : 'Ani', 'HP' : '234567891', 'email' : 'ani@python.com'}
kontak = [kontak1, kontak2]

while True:
    print("\nMenu Kontak")
    print("1. Melihat Semua Kontak")
    print("2. Menambahkan Kontak Baru")
    print("3. Menghapus Kontak")
    print("4. Keluar dari Kontak")

    pilihan = input("Masukkan pilihan menu kontak (1, 2, 3 atau 4):")

    if pilihan == "1":
        melihat_kontak()

    elif pilihan == "2":
        menambah_kontak()

    elif pilihan == "3":
        menghapus_kontak()

    elif pilihan == "4":
        # keluar dari kontak
        break
    else:
        print("Anda memasukkan pilihan yang salah!")