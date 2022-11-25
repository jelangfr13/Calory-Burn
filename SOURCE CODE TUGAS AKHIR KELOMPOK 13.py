import json
import os

namaFile = 'dataOlahraga.json'
namaAkun = 'dataAkun.json'

def tampilan_awal():
    print('='*100)
    print('{:^100}'.format('Selamat Datang Diaplikasi Calory Burn'))
    print('{:^100}'.format('Silahkan Pilih Menu Dibawah Ini'))
    print('='*100)
    print(' ')
    print('1. Register')
    print('2. Login')
    print('3. Keluar')
    print()
    x = input('==> ')

    if x == '1':
        os.system('cls')
        register()
    elif x == '2':
        os.system('cls')
        login()
    elif x == '3':
        print()
        a = input('Apakah Anda Yakin Ingin Keluar? [y/t] :')
        if a == 'y':
            print(' ')
            print('{:^100}'.format('Terimakasih Sudah Menggunakan Aplikasi Calory Burn'))
            print('{:^100}'.format('=== APLIKASI KELUAR ==='))
            exit
        else:
            os.system('cls')
            tampilan_awal()
    else:
        os.system('cls')
        print(' ')
        print('{:^100}'.format('!!! Menu Tidak Tersedia !!!'))
        tampilan_awal()


def register():
    data = []

    print('='*100)
    print('{:^100}'.format('Selamat Datang Diaplikasi Calory Burn'))
    print('{:^100}'.format('Silahkan Register Terlebih Dahulu'))
    print('='*100)
    print(' ')
    username = input('Username             : ')
    password = input('Password             : ')
    confirm_password = input('Confirm Password     : ')

    data_input = dict()
    data_input['username'] = username
    data_input['password'] = password
    data.append(data_input)
    with open(namaAkun, 'w') as file:
        x = json.dump(data, file, indent=3)

    def lanjut_login():
        print()
        print('Lanjut Login / Keluar Aplikasi')
        x = input('[y/t] ==> ')
        if x == 'y':
            os.system('cls')
            login()
        elif x == 't':
            print()
            print('{:^100}'.format('Terimakasih Sudah Menggunakan Aplikasi Calory Burn'))
            print('{:^100}'.format('=== APLIKASI KELUAR ==='))
            exit
        else:
            os.system('cls')
            print(' ')
            print('{:^100}'.format('!!! Menu Tidak Tersedia !!!'))
            lanjut_login()
    
    lanjut_login()


def login():
    with open(namaAkun, "r") as json_file:
        data = json.load(json_file)
        x = data[0]['username']
        y = data[0]['password']

    print('='*100)
    print('{:^100}'.format('Selamat Datang Diaplikasi Calory Burn'))
    print('{:^100}'.format('Silahkan Login Terlebih Dahulu'))
    print('='*100)
    print()
    id = input('Username   : ')
    pw = input('Password   : ')

    if id == x and pw == y:
        os.system('cls')
        print('='*100)
        print('{:^100}'.format('~ Login Berhasil ~'))
        print('='*100)
        print()
        print('{:^100}'.format('Selamat Datang Di Aplikasi Calory Burn'))
        print('{:^100}'.format('Silahkan Pilih Menu Yang Tersedia'))
        print()
        menu_utama()
    else:
        os.system('cls')
        login_salah()


def login_salah():
    print('{:^100}'.format('!!!!! PERHATIAN !!!!!'))
    print('{:^100}'.format('Username Atau Password Yang Anda Masukkan Salah'))
    print('{:^100}'.format('Silahkan Masukkan Kembali Username Atau Password Yang Benar'))
    print()
    login()


def info_aplikasi():
    print('{:^100}'.format('Selamat Datang Diaplikasi Calory Burn'))
    print('{:^100}'.format('Aplikasi Ini Dapat Membantu Anda Dalam Berolahraga'))
    print('{:^100}'.format(' '))
    print('{:^100}'.format('Aplikasi Ini Dapat Menghitung Jumlah Kalori Yang Terbakar Ketika Anda Sedang Berolahraga'))
    print('{:^100}'.format('Terdapat Menu Dengan Berbagai Macam Jenis Olahraga Yang Dapat Dipilih'))
    print('{:^100}'.format(' '))
    print('{:^100}'.format('Aplikasi Ini Mudah Digunakan'))
    print('{:^100}'.format('Dan Juga Dilengkapi Berbagai Macam Fitur Menarik'))
    print(' ')  


def menu_utama():
    print('Silahkan Pilih Menu :')
    print('1. Olahraga')
    print('2. History')
    print('3. Pengaturan')
    print('4. Keluar')
    print(' ')
    x = input('==> ')

    if x == '1':
        os.system('cls')
        menu_olahraga()
    elif x == '2':
        menu_history()
    elif x == '3':
        os.system('cls')
        menu_pengaturan()
    elif x == '4':
        a = input('Apakah Anda Yakin Ingin Keluar? [y/t] :')
        if a == 'y':
            print(' ')
            print('Terimakasih Sudah Menggunakan Aplikasi Calory Burn')
            print('{:^50}'.format('=== APLIKASI KELUAR ==='))
            exit
        else:
            os.system('cls')
            menu_utama()
    else:
        os.system('cls')
        print(' ')
        print('{:^100}'.format('!!! Menu Tidak Tersedia !!!'))
        menu_utama()


def menu_olahraga():
    data = []
    with open(namaFile, "r") as json_file:
        data = json.load(json_file)

    print('='*100)
    print('{:^100}'.format('~ Olahraga ~'))
    print('='*100)
    print(' ')
    print('1.  Jogging')
    print('2.  Treadmill')
    print('3.  Bersepeda')
    print('4.  Sepeda Statis')
    print('5.  Sepak Bola')
    print('6.  Futsal')
    print('7.  Basket')
    print('8.  Volly')
    print('9.  Bulu Tangkis')
    print('10. Berenang')
    print('11. <== Kembali')
    print(' ')
    x = input('==> ')


    def jogging():
        os.system('cls')
        print('='*100)
        print('{:^100}'.format('~ Jogging ~'))
        print('='*100)
        print(' ')
        print('Silahkan Isi Data Berikut Untuk Mengetahui Jumlah Kalori Yang Terbakar')
        print(' ')
        berat = int(input('Berat Badan    [kg]      : '))
        waktu = int(input('Waktu          [menit]   : '))
        hasil = 7 * berat * (waktu / 60)
        print(' ')
        print('='*43)
        print('Kalori Yang Anda Bakar Adalah', hasil, 'kalori')
        print('='*43, '\n')
        print('Catatan :')
        print('Data diatas tidak benar - benar 100 %', 'akurat')
        print('\n')

        data_input = dict()
        data_input['olahraga'] = 'Jogging'
        data_input['berat'] = berat
        data_input['waktu'] = waktu
        data_input['kalori'] = hasil
        data.append(data_input)
        with open(namaFile, 'w') as file:
            x = json.dump(data, file, indent=3)

        x = input('Lanjut / Keluar? [y/t]  : ')
        if x == 'y':
            os.system('cls')
            menu_olahraga()
        else:
            print(' ')
            print('{:^100}'.format('Terimakasih Sudah Menggunakan Aplikasi Calory Burn'))
            print('{:^100}'.format('=== APLIKASI KELUAR ==='))
            exit        

    def treadmill():
        os.system('cls')
        print('='*100)
        print('{:^100}'.format('~ Treadmill ~'))
        print('='*100)
        print(' ')
        print('Silahkan Isi Data Berikut Untuk Mengetahui Jumlah Kalori Yang Terbakar')
        print(' ')
        berat = int(input('Berat Badan    [kg]      : '))
        waktu = int(input('Waktu          [menit]   : '))
        hasil = 8 * berat * (waktu / 60)
        print(' ')
        print('='*43)
        print('Kalori Yang Anda Bakar Adalah', hasil, 'kalori')
        print('='*43)
        print(' ')
        print('Catatan :')
        print('Data diatas tidak benar - benar 100 %', 'akurat')
        print('\n')

        data_input = dict()
        data_input['olahraga'] = 'Treadmill'
        data_input['berat'] = berat
        data_input['waktu'] = waktu
        data_input['kalori'] = hasil
        data.append(data_input)
        with open(namaFile, 'w') as file:
            x = json.dump(data, file, indent=3)

        x = input('Lanjut / Keluar? [y/t]  : ')
        if x == 'y':
            os.system('cls')
            menu_olahraga()
        else:
            print(' ')
            print('{:^100}'.format('Terimakasih Sudah Menggunakan Aplikasi Calory Burn'))
            print('{:^100}'.format('=== APLIKASI KELUAR ==='))
            exit  

    def sepeda():
        os.system('cls')
        print('='*100)
        print('{:^100}'.format('~ Bersepeda ~'))
        print('='*100)
        print(' ')
        print('Silahkan Isi Data Berikut Untuk Mengetahui Jumlah Kalori Yang Terbakar')
        print(' ')
        berat = int(input('Berat Badan    [kg]      : '))
        waktu = int(input('Waktu          [menit]   : '))
        hasil = 8 * berat * (waktu / 60)
        print(' ')
        print('='*43)
        print('Kalori Yang Anda Bakar Adalah', hasil, 'kalori')
        print('='*43)
        print(' ')
        print('Catatan :')
        print('Data diatas tidak benar - benar 100 %', 'akurat')
        print('\n')

        data_input = dict()
        data_input['olahraga'] = 'Bersepeda'
        data_input['berat'] = berat
        data_input['waktu'] = waktu
        data_input['kalori'] = hasil
        data.append(data_input)
        with open(namaFile, 'w') as file:
            x = json.dump(data, file, indent=3)

        x = input('Lanjut / Keluar? [y/t]  : ')
        if x == 'y':
            os.system('cls')
            menu_olahraga()
        else:
            print(' ')
            print('{:^100}'.format('Terimakasih Sudah Menggunakan Aplikasi Calory Burn'))
            print('{:^100}'.format('=== APLIKASI KELUAR ==='))
            exit

    def sepeda_statis():
        os.system('cls')
        print('='*100)
        print('{:^100}'.format('~ Sepeda Statis ~'))
        print('='*100)
        print(' ')
        print('Silahkan Isi Data Berikut Untuk Mengetahui Jumlah Kalori Yang Terbakar')
        print(' ')
        berat = int(input('Berat Badan    [kg]      : '))
        waktu = int(input('Waktu          [menit]   : '))
        hasil = 7 * berat * (waktu / 60)
        print(' ')
        print('='*43)
        print('Kalori Yang Anda Bakar Adalah', hasil, 'kalori')
        print('='*43)
        print(' ')
        print('Catatan :')
        print('Data diatas tidak benar - benar 100 %', 'akurat')
        print('\n')

        data_input = dict()
        data_input['olahraga'] = 'Sepeda Statis'
        data_input['berat'] = berat
        data_input['waktu'] = waktu
        data_input['kalori'] = hasil
        data.append(data_input)
        with open(namaFile, 'w') as file:
            x = json.dump(data, file, indent=3)

        x = input('Lanjut / Keluar? [y/t]  : ')
        if x == 'y':
            os.system('cls')
            menu_olahraga()
        else:
            print(' ')
            print('{:^100}'.format('Terimakasih Sudah Menggunakan Aplikasi Calory Burn'))
            print('{:^100}'.format('=== APLIKASI KELUAR ==='))
            exit

    def sepak_bola():
        os.system('cls')
        print('='*100)
        print('{:^100}'.format('~ Sepak Bola ~'))
        print('='*100)
        print(' ')
        print('Silahkan Isi Data Berikut Untuk Mengetahui Jumlah Kalori Yang Terbakar')
        print(' ')
        berat = int(input('Berat Badan    [kg]      : '))
        waktu = int(input('Waktu          [menit]   : '))
        hasil = 8 * berat * (waktu / 60)
        print(' ')
        print('='*43)
        print('Kalori Yang Anda Bakar Adalah', hasil, 'kalori')
        print('='*43)
        print(' ')
        print('Catatan :')
        print('Data diatas tidak benar - benar 100 %', 'akurat')
        print('\n')

        data_input = dict()
        data_input['olahraga'] = 'Sepak Bola'
        data_input['berat'] = berat
        data_input['waktu'] = waktu
        data_input['kalori'] = hasil
        data.append(data_input)
        with open(namaFile, 'w') as file:
            x = json.dump(data, file, indent=3)

        x = input('Lanjut / Keluar? [y/t]  : ')
        if x == 'y':
            os.system('cls')
            menu_olahraga()
        else:
            print(' ')
            print('{:^100}'.format('Terimakasih Sudah Menggunakan Aplikasi Calory Burn'))
            print('{:^100}'.format('=== APLIKASI KELUAR ==='))
            exit

    def futsal():
        os.system('cls')
        print('='*100)
        print('{:^100}'.format('~ Futsal ~'))
        print('='*100)
        print(' ')
        print('Silahkan Isi Data Berikut Untuk Mengetahui Jumlah Kalori Yang Terbakar')
        print(' ')
        berat = int(input('Berat Badan    [kg]      : '))
        waktu = int(input('Waktu          [menit]   : '))
        hasil = 9 * berat * (waktu / 60)
        print(' ')
        print('='*43)
        print('Kalori Yang Anda Bakar Adalah', hasil, 'kalori')
        print('='*43)
        print(' ')
        print('Catatan :')
        print('Data diatas tidak benar - benar 100 %', 'akurat')
        print('\n')

        data_input = dict()
        data_input['olahraga'] = 'Futsal'
        data_input['berat'] = berat
        data_input['waktu'] = waktu
        data_input['kalori'] = hasil
        data.append(data_input)
        with open(namaFile, 'w') as file:
            x = json.dump(data, file, indent=3)

        x = input('Lanjut / Keluar? [y/t]  : ')
        if x == 'y':
            os.system('cls')
            menu_olahraga()
        else:
            print(' ')
            print('{:^100}'.format('Terimakasih Sudah Menggunakan Aplikasi Calory Burn'))
            print('{:^100}'.format('=== APLIKASI KELUAR ==='))
            exit

    def basket():
        os.system('cls')
        print('='*100)
        print('{:^100}'.format('~ Basket ~'))
        print('='*100)
        print(' ')
        print('Silahkan Isi Data Berikut Untuk Mengetahui Jumlah Kalori Yang Terbakar')
        print(' ')
        berat = int(input('Berat Badan    [kg]      : '))
        waktu = int(input('Waktu          [menit]   : '))
        hasil = 6 * berat * (waktu / 60)
        print(' ')
        print('='*43)
        print('Kalori Yang Anda Bakar Adalah', hasil, 'kalori')
        print('='*43)
        print(' ')
        print('Catatan :')
        print('Data diatas tidak benar - benar 100 %', 'akurat')
        print('\n')

        data_input = dict()
        data_input['olahraga'] = 'Basket'
        data_input['berat'] = berat
        data_input['waktu'] = waktu
        data_input['kalori'] = hasil
        data.append(data_input)
        with open(namaFile, 'w') as file:
            x = json.dump(data, file, indent=3)

        x = input('Lanjut / Keluar? [y/t]  : ')
        if x == 'y':
            os.system('cls')
            menu_olahraga()
        else:
            print(' ')
            print('{:^100}'.format('Terimakasih Sudah Menggunakan Aplikasi Calory Burn'))
            print('{:^100}'.format('=== APLIKASI KELUAR ==='))
            exit

    def voly():
        os.system('cls')
        print('='*100)
        print('{:^100}'.format('~ Volly ~'))
        print('='*100)
        print(' ')
        print('Silahkan Isi Data Berikut Untuk Mengetahui Jumlah Kalori Yang Terbakar')
        print(' ')
        berat = int(input('Berat Badan    [kg]      : '))
        waktu = int(input('Waktu          [menit]   : '))
        hasil = 4 * berat * (waktu / 60)
        print(' ')
        print('='*43)
        print('Kalori Yang Anda Bakar Adalah', hasil, 'kalori')
        print('='*43)
        print(' ')
        print('Catatan :')
        print('Data diatas tidak benar - benar 100 %', 'akurat')
        print('\n')

        data_input = dict()
        data_input['olahraga'] = 'Volly'
        data_input['berat'] = berat
        data_input['waktu'] = waktu
        data_input['kalori'] = hasil
        data.append(data_input)
        with open(namaFile, 'w') as file:
            x = json.dump(data, file, indent=3)

        x = input('Lanjut / Keluar? [y/t]  : ')
        if x == 'y':
            os.system('cls')
            menu_olahraga()
        else:
            print(' ')
            print('{:^100}'.format('Terimakasih Sudah Menggunakan Aplikasi Calory Burn'))
            print('{:^100}'.format('=== APLIKASI KELUAR ==='))
            exit

    def bulutangkis():
        os.system('cls')
        print('='*100)
        print('{:^100}'.format('~ Bulutangkis ~'))
        print('='*100)
        print(' ')
        print('Silahkan Isi Data Berikut Untuk Mengetahui Jumlah Kalori Yang Terbakar')
        print(' ')
        berat = int(input('Berat Badan    [kg]      : '))
        waktu = int(input('Waktu          [menit]   : '))
        hasil = 4.5 * berat * (waktu / 60)
        print(' ')
        print('='*43)
        print('Kalori Yang Anda Bakar Adalah', hasil, 'kalori')
        print('='*43)
        print(' ')
        print('Catatan :')
        print('Data diatas tidak benar - benar 100 %', 'akurat')
        print('\n')

        data_input = dict()
        data_input['olahraga'] = 'Bulutangkis'
        data_input['berat'] = berat
        data_input['waktu'] = waktu
        data_input['kalori'] = hasil
        data.append(data_input)
        with open(namaFile, 'w') as file:
            x = json.dump(data, file, indent=3)

        x = input('Lanjut / Keluar? [y/t]  : ')
        if x == 'y':
            os.system('cls')
            menu_olahraga()
        else:
            print(' ')
            print('{:^100}'.format('Terimakasih Sudah Menggunakan Aplikasi Calory Burn'))
            print('{:^100}'.format('=== APLIKASI KELUAR ==='))
            exit

    def berenang():
        os.system('cls')
        print('='*100)
        print('{:^100}'.format('~ Berenang ~'))
        print('='*100)
        print(' ')
        print('Silahkan Isi Data Berikut Untuk Mengetahui Jumlah Kalori Yang Terbakar')
        print(' ')
        berat = int(input('Berat Badan    [kg]      : '))
        waktu = int(input('Waktu          [menit]   : '))
        hasil = 9 * berat * (waktu / 60)
        print(' ')
        print('='*43)
        print('Kalori Yang Anda Bakar Adalah', hasil, 'kalori')
        print('='*43)
        print(' ')
        print('Catatan :')
        print('Data diatas tidak benar - benar 100 %', 'akurat')
        print('\n')

        data_input = dict()
        data_input['olahraga'] = 'Berenang'
        data_input['berat'] = berat
        data_input['waktu'] = waktu
        data_input['kalori'] = hasil
        data.append(data_input)
        with open(namaFile, 'w') as file:
            x = json.dump(data, file, indent=3)

        x = input('Lanjut / Keluar? [y/t]  : ')
        if x == 'y':
            os.system('cls')
            menu_olahraga()
        else:
            print(' ')
            print('{:^100}'.format('Terimakasih Sudah Menggunakan Aplikasi Calory Burn'))
            print('{:^100}'.format('=== APLIKASI KELUAR ==='))
            exit

    if x == '1':
        jogging()
    elif x == '2':
        treadmill()
    elif x == '3':
        sepeda()
    elif x == '4':
        sepeda_statis()
    elif x == '5':
        sepak_bola()
    elif x == '6':
        futsal()
    elif x == '7':
        basket()
    elif x == '8':
        voly()
    elif x == '9':
        bulutangkis()
    elif x == '10':
        berenang()
    elif x == '11':
        os.system('cls')
        menu_utama()
    else:
        os.system('cls')
        print(' ')
        print('{:^100}'.format('!!! Menu Tidak Tersedia !!!'))
        print(' ')
        menu_olahraga()


def menu_history():
    os.system('cls')
    print('{:^80}'.format('~ HISTORY ~'))
    print(' ')
    print('='*80)
    print('{0:2s} \t {1:15s} \t  {2:5s} \t {3:3s} Menit \t {4:10}'.format('No', 'Jenis Olahraga', 'Berat', 'Waktu', 'Kalori Terbakar'))
    print('='*80)

    with open(namaFile, "r") as json_file:
        data = json.load(json_file)
        for i in range(len(data)):
            print('{0:2d} \t {1:15s} \t {2:3d} Kg \t {3:3d} Menit \t {4:10}'.format(i+1, data[i]['olahraga'], data[i]['berat'], data[i]['waktu'], data[i]['kalori']))
    print('\n')

    x = input('Lanjut / Keluar? [y/t]  : ')
    if x == 'y':
        os.system('cls')
        menu_utama()
    else:
        print(' ')
        print('{:^100}'.format('Terimakasih Sudah Menggunakan Aplikasi Calory Burn'))
        print('{:^100}'.format('=== APLIKASI KELUAR ==='))
        exit


def menu_pengaturan():
    print('='*80)
    print('{:^80}'.format('~ PENGATURAN ~'))
    print('='*80)
    print('1. Hapus History')
    print('2. Info Aplikasi')
    print('3. Kembali')
    print(' ')
    x = input('==> ')

    def hapus_history():
        confirm = input('Apakah Anda Yakin Ingin Menghapus History? [y/t] : ')
        if confirm == 'y':
            data = []
            with open(namaFile, 'w') as file:
                data = json.dump(data, file)
            os.system('cls')
            print()
            print('{:^80}'.format('=== History Berhasil Dihapus ==='))
            print()
            menu_pengaturan()
        else:
            os.system('cls')
            menu_pengaturan()
        

    if x == '1':
        print('\n')
        hapus_history()
    elif x == '2':
        os.system('cls')
        info_aplikasi()
        x = input('Lanjut / Keluar? [y/t]  : ')
        if x == 'y':
            os.system('cls')
            menu_pengaturan()
        else:
            print(' ')
            print('{:^100}'.format('Terimakasih Sudah Menggunakan Aplikasi Calory Burn'))
            print('{:^100}'.format('=== APLIKASI KELUAR ==='))
            exit
    elif x == '3':
        os.system('cls')
        menu_utama()
    else:
        os.system('cls')
        print(' ')
        print('{:^80}'.format('!!! Menu Tidak Tersedia !!!'))
        print(' ')
        menu_pengaturan()

os.system('cls')
tampilan_awal()