def balikPosisi(a):                                  
    new = []                                         # pertama membuat list kosong sebagai list tujuan    
    for i in range(len(a)-1,-1,-1):                  # untuk mengambil index a dimulai dari index terbesar sampai index ke 0
        new.append(a[i])                             # pada setiap pengulangan list new di append dengan list a pada index sesuai dengan pengulangan i
    return new                                       # untuk mendapatkan hasil dari fungsi yang berupa list inputan yang sudah di reverse

print(balikPosisi([1, 2, 3, 4, 5, 6, 7, 8, 9]))
print(balikPosisi(['A', 'B', 'C', 'D', 'E', 'F', 'G']))
print(balikPosisi(['Messi', 'Suarez', 'Coutinho', 'Dembele', 'Rakitic']))