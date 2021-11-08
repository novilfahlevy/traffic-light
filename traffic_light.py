import time
import os

lampu = 'Merah', 'Kuning', 'Hijau'
warna = '\033[0;30;41m', '\033[0;30;43m', '\033[0;30;42m', '\x1b[0m'
index_lampu = 0
detik = 5

while True :
  # Jika detik habis, print lampunya sesuai index_lampu
  if detik == 0 :
    os.system('cls')
    print(f'\n| - - - |')
    print(f'|{warna[index_lampu]}{" " * 7}{warna[3]}|' if index_lampu == 0 else (f'|{" " * 7}|'))
    print(f'|{warna[index_lampu]}{" " * 7}{warna[3]}|' if index_lampu == 0 else (f'|{" " * 7}|'))
    print(f'| - - - |')
    print(f'|{warna[index_lampu]}{" " * 7}{warna[3]}|' if index_lampu == 1 else (f'|{" " * 7}|'))
    print(f'|{warna[index_lampu]}{" " * 7}{warna[3]}|' if index_lampu == 1 else (f'|{" " * 7}|'))
    print(f'| - - - |')
    print(f'|{warna[index_lampu]}{" " * 7}{warna[3]}|' if index_lampu == 2 else (f'|{" " * 7}|'))
    print(f'|{warna[index_lampu]}{" " * 7}{warna[3]}|' if index_lampu == 2 else (f'|{" " * 7}|'))
    print(f'| - - - |')
    print(f'| - |')
    print(f'| - |')
    print(f'| - |\n')

    # kembalikan detik menjadi 5
    detik = 5 + 1

    # index_lampu kembali ke 0 (awal) jika sudah sama dengan panjang lampu
    if index_lampu == (len(lampu) - 1) :
      index_lampu = 0
    else :
      # jika tidak, index_lampu ditambah 1
      index_lampu = index_lampu + 1

  # kurangi 1 detik setiap berjalan
  detik = detik - 1
  
  # module time dari python untuk mengskip 1 detik program
  time.sleep(1)
