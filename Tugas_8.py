from os import getpid
from time import time, sleep
from multiprocessing import cpu_count, Pool, Process

def angka (i):
   if i % 2 == 0:
      print(i+1, "Ganjil - ID Proses", getpid())
   else:
      print(i+1, "Genap - ID Proses", getpid())
   sleep(1)


lim = int(input("Masukkan input: "))


#Sequential
sequential_first = time()
print("\n Sekuensial")
for i in range(lim):
  angka(i)
sequential_last = time()


#multiprocessing.Process
print("\n multiprocessing.Process")
array_process = []
first_process = time()
for i in range(lim):
    multiproses = Process(target=angka, args=(i, ))
    array_process.append(multiproses)
    multiproses.start() 
for i in array_process:
    multiproses.join()
last_process = time()


#multiprocessing.Pool
print("\n multiprocessing.Pool")
first_pool = time()
pool = Pool()
pool.map(angka, range(0, lim))
pool.close()
last_pool = time()


#Perbandingan.waktu
total_sequential = sequential_last - sequential_first
total_process = last_process - first_process
total_pool = last_pool - first_pool

print("\nWaktu eksekusi sequential: ", total_sequential, "detik")
print("Waktu eksekusi multiprocessing.Process: ", total_process, "detik")
print("Waktu eksekusi multiprocessing.Pool:" , total_pool, "detik")
