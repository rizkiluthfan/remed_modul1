email = input('Input Email : ')

def cek_email(x):                                # pertama saya membuat list angka dan huruf
    angka = ['0','1','2','3','4','5','6','7','8','9']
    huruf = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

    u = x.lower()                                # untuk merubah huruf kapital menjadi lowercase
    a = u.split('@')                             # untuk membagi email berdasarkan @ (split @)
    status = []                                  # membuat list untuk mengisi status email
    if len(a)==2:                                # melakukan check line a sama dengan 2 (hasil dari splitnya 2), jadi kalau terpenuhi maka akan lanjut ke proses berikutnya
        for i in a[0]:                           # for loop yg pertama untuk cek kondisi nama user  
            if i in angka or i in huruf:         # melakukan check apakah yang di input masih dalam list angka dan huruf
                status.append(True)              # jika benar maka akan lanjut ke proses check nama hosting
            else:
                status.append(False)             # jika tidak dalam list maka dianggap False

        b = a[1].split('.')                      # setelah berhasil check kondisi nama user maka lanjut ke proses for loop yg kedua untuk cek kondisi nama hosting
        if len(b)==2:                            # melakukan check line b (setelah @) sama dengan 2 (ex @purwadhika.com), jadi kalau terpenuhi maka akan lanjut ke proses berikutnya
            for j in b[0]:                       # for loop yg kedua untuk cek kondisi nama hosting 
                if j in angka or j in huruf:     # melakukan check apakah yang di input masih dalam list angka dan huruf
                    status.append(True)          # jika benar maka akan lanjut ke proses check nama ekstensi
                else:
                    status.append(False)         # jika tidak dalam list list angka dan huruf maka diangap False

            if len(b[1])<=5:                    # melakukan check ekstensi apakah yang di input tidak lebih dari 5, jadi kalau terpenuhi maka akan lanjut ke proses berikutnya
                for k in b[1]:                  # for loop yg ketiga untuk cek kondisi nama ekstensi
                    if k in huruf:              # melakukan check apakah yang di input masih dalam list huruf 
                        status.append(True)     # jika benar jika semua proses benar maka di anggap True
                    else:
                        status.append(False)    # jika tidak dalam list maka diangap False
            else:
                status.append(False)            # jika ekstensi lebih dari 5 maka di anggap False
        else:                                   
            status.append(False)                # jika check line b tidak terpenuhin (ex @purwadhika tanpa .com) maka statusnya False
    else:
        status.append(False)                    # jika line tidak sama maka di anggap False

    if False in status:                         # jika hasilnya false maka output email yang di input adalah "EMAIL TIDAK VALID"
        return 'EMAIL TIDAK VALID'
    else:
        return 'EMAIL VALID'                    # jika hasilnya true maka output email yang di input adalah "EMAIL VALID"

print(cek_email(email))                         # melakukan print untuk menjalankan proses yang telah dibuat



