# First Capstone Project (Yellow Page - Data Kontak Petugas Emergency Gedung DSP)

database = [
    {'ID': 1901, 'nama': 'Yoga Permana', 'lantai': '9', 'jabatan': 'Staf pemadam kebakaran', 'telepon': '081287659807'},
    {'ID': 1201, 'nama': 'Iip Dharmawan', 'lantai': '12', 'jabatan': 'kepala staf first AID', 'telepon': '085476895430'}
]

def tampilkan():
    '''
    FUNGSI UNTUK FITUR MENAMPILKAN DATA KONTAK PETUGAS
    '''
    list_menu_1 = [
    'Tampilkan Data Kontak Seluruh Petugas',
    'Tampilkan Data Kontak Petugas di lantai tertentu',
    'Kembali ke Menu Utama'
    ]
    while True:
        # Cetak menu dalam fitur tampilkan data dan inputan user untuk memilih menu
        print('''\n===== DATA KONTAK PETUGAS EMERGENCY =====''')
        for i, j in enumerate(list_menu_1):
            print(f'{i + 1}. {j}')
        perintah = input('Silahkan Pilih Menu [1 - 3]: ')

        # Code untuk menjalankan "Tampilkan Kontak Seluruh Petugas"
        if perintah == '1':
            if len(database) > 0:
                for i, j in enumerate(database):
                    print(f"\n{i + 1}. ID: {j['ID']}, nama: {j['nama']}, lantai: {j['lantai']}, jabatan: {j['jabatan']}, no tlpn: {j['telepon']}")
            else:
                print('\nooooo Tidak Ada Data Kontak Petugas ooooo')

        # Code untuk menjalankan "Tampilkan Kontak Petugas di lantai tertentu"
        elif perintah == '2':
            if len(database) > 0:
                input_id = input('\nMasukkan Nomor Lantai: ')
                jumlah = 0
                for i, j in enumerate(database):
                    if j['lantai'] == input_id:
                        print(f'\nBerikut Adalah Kontak Petugas Di Lantai {input_id}:')
                        print(f"ID: {j['ID']}, nama: {j['nama']}, lantai: {j['lantai']}, jabatan: {j['jabatan']}, no tlpn: {j['telepon']}")
                        jumlah += 1
                if jumlah == 0:
                    print(f'\nooooo Tidak Ada Data Kontak Petugas Di Lantai {input_id} atau Lantai {input_id} Tidak Ada ooooo')
            else:
                print('\nooooo Tidak Ada Data Kontak Petugas ooooo')

        # Code untuk menjalankan "Kembali ke Menu Utama"
        elif perintah == '3':
            return menu_utama()


def tambahkan():
    '''
    FUNGSI UNTUK FITUR MENAMBAH DATA KONTAK PETUGAS
    '''
    list_menu_2 = [
    'Tambah Data Petugas',
    'Kembali Ke Menu Utama'
    ]

    while True:
        # Cetak menu dalam fitur menambah data dan inputan user untuk memilih menu
        print('\n+++++ MENAMBAH DATA KONTAK PETUGAS EMERGENCY +++++')
        for i, j in enumerate(list_menu_2):
            print(f'{i + 1}. {j}') 
        perintah = input('Silahkan Pilih Menu [1 - 2]: ')

        # Code untuk menjalankan "Tambah Data Petugas"
        if perintah == '1':
            while True:
                input_id = input('\nMasukkan nomor ID (*4 digit angka, dengan 1 sebagai digit pertama): ')
                if input_id.isnumeric() == False:
                    continue
                else:
                    if int(input_id) < 1000 or int(input_id) > 1999:
                        continue
                    else:
                        jumlah = 0
                        for i in database:
                            if i['ID'] == input_id:
                                jumlah += 1

                        if jumlah != 0:
                            print('\n===== ID Sudah Ada Dalam Database =====')
                        else:
                            database.append({})
                            for i in database:
                                if len(i) == 0:
                                    i['ID'] = input_id
                                    i['nama'] = input('Masukkan Nama: ')
                                    i['lantai'] = input('Masukkan Nomor Lantai: ')
                                    i['jabatan'] = input('Masukkan Jabatan: ')
                                    i['telepon'] = input('Masukkan Nomor Telepon: ')
                            
                            while True:
                                konfirmasi_simpan = input('\nSimpan Data [Y/N]: ')
                                if konfirmasi_simpan == 'N':
                                    print('\nooooo Data Tidak di Simpan ooooo')
                                    database.pop()
                                    break
                                elif konfirmasi_simpan == 'Y':
                                    print('\n+++++ Data Tersimpan +++++')
                                    break
                        break

        # Code untuk menjalankan "Kembali Ke Menu Utama"
        elif perintah == '2':
            return menu_utama()


def rubah():
    '''
    FUNGSI UNTUK MERUBAH/ UPDATE DATA KONTAK PETUGAS EMERGENCY
    '''
    list_menu_3 = [
    'Ubah Data Petugas',
    'Kembali Ke Menu Utama'
    ]

    while True:
        # Cetak menu dalam fitur rubah data dan inputan user untuk memilih menu
        print('\n>>>>> MENGUBAH DATA KONTAK PETUGAS EMERGENCY <<<<<')
        for i, j in enumerate(list_menu_3):
            print(f'{i + 1}. {j}')
        perintah = input('Silahkan Pilih Menu [1 - 2]: ')

        # Code untuk menjalankan "Ubah Data Petugas"
        if perintah == '1':
            input_id = input('\nMasukkan ID: ')
            jumlah = 0
            for j in database:
                if j['ID'] == input_id:
                    jumlah += 1
                    print(f"ID: {j['ID']}, nama: {j['nama']}, lantai: {j['lantai']}, jabatan: {j['jabatan']}, nomor telepon: {j['telepon']}")
                    while True:
                        konfirmasi_rubah_awal = input('\nRubah Data [Y / N]: ')
                        if konfirmasi_rubah_awal == 'Y':
                            while True:
                                field_rubah = input('\nMasukkan Field Yang Akan Dirubah (nama, lantai, jabatan, atau telepon): ')
                                if field_rubah == 'nama' or field_rubah == 'lantai' or field_rubah == 'jabatan' or field_rubah == 'telepon':
                                    perubahan = input(f'\nMasukkan {field_rubah} Baru: ')
                                    while True:
                                        konfirmasi_rubah = input('\nRubah Data [Y / N]: ')
                                        if konfirmasi_rubah == 'Y':
                                            j[f'{field_rubah}'] = perubahan
                                            print('\n>>>>> Perubahan Berhasil Disimpan <<<<<')
                                            break
                                        elif konfirmasi_rubah == 'N':
                                            print('\n===== Perubahan Tidak Disimpan =====')
                                            break
                                    break
                                else:
                                    print('\nxxxxx Field Yang Anda Masukkan Salah xxxxx')
                            break
                        elif konfirmasi_rubah_awal == 'N':
                            break

            if jumlah == 0:
                print(f'\nxxxxx Data Untuk ID {input_id} Tidak Ada xxxxx')

        # Code untuk menjalankan "Kembali Ke Menu Utama"
        elif perintah == '2':
            return menu_utama()


def hapus():
    '''
    FUNGSI UNTUK MENGHAPUS DATA KONTAK PETUGAS EMERGENCY
    '''
    list_menu_4 = [
    'Hapus Data Kontak Petugas',
    'Kembali Ke Menu Utama'
    ]

    while True:
        # Cetak menu dalam fitur menghapus data dan inputan user untuk memilih menu
        print('\n----- MENGHAPUS DATA KONTAK PETUGAS EMERGENCY -----')
        for i, j in enumerate(list_menu_4):
            print(f'{i + 1}. {j}')
        perintah = input('Silahkan Pilih Menu [1 - 2]: ')

        # Code untuk menjalankan "Hapus Data Kontak Petugas"
        if perintah == '1':
            input_id = input('\nMasukkan ID Yang Ingin Dihapus: ')
            if len(database) > 0:
                jumlah = 0
                for j in database:
                    if j['ID'] == input_id:
                        jumlah += 1
                        while True:
                            konfirmasi_hapus = input('\nHapus Data [Y / N]: ')
                            if konfirmasi_hapus == 'Y':
                                database.remove(j)
                                print('\nxxxxx Data Berhasil Terhapus xxxxx')
                                break
                            elif konfirmasi_hapus == 'N':
                                print('\n===== Data Tidak Jadi Dihapus =====')
                                break
                if jumlah == 0:
                    print(f'\nxxxxx Data untuk ID {input_id} Tidak Ditemukan Di Database xxxxx')
            else:
                print(f'\nxxxxx Data untuk ID {input_id} Tidak Ditemukan Di Database xxxxx')
                    
        # Code untuk menjalankan "Kembali Ke Menu Utama"
        elif perintah == '2':
            return menu_utama()


def menu_utama():
    list_menu_utama = [                                         # Membuat list yang berisi list menu utama
'Tampilkan Data Kontak Petugas Emergency',
'Tambahkan Data Kontak Petugas Emergency',
'Rubah Data Kontak Petugas Emergency',
'Hapus Data Kontak Petugas Emergency',
'Exit'
]
    while True: # Membuat while loop untuk menampilkan menu utama apabila input untuk variabel perintah salah
        print('\n***** DATA KONTAK DARURAT GEDUNG DSP *****')
        for i, j in enumerate(list_menu_utama):
            print(f'{i + 1}. {j}')
 
        perintah = input('Silahkan Pilih Menu [1 - 5]: ')

        if perintah == '1': # Membuat conditional statement untuk menentukan "menu" yang akan di jalankan berdasar "perintah"
            return tampilkan()
        elif perintah == '2':
            return tambahkan()
        elif perintah == '3':
            return rubah()
        elif perintah == '4':
            return hapus()
        elif perintah == '5':
            break
        else:
            print('xxxxx Pilihan Anda Tidak Ditemukan Dalam Program xxxxx')

menu_utama()
