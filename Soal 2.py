import math
nilai_a= int(input("Masukan nilai mapel A: "))
nilai_b= int(input("Masukan nilai mapel B: "))
nilai_c= int(input("Masukan nilai mapel C: "))
nilai= (nilai_a, nilai_b, nilai_c)
print("Nilai kamu semuanya adalah: ",nilai)
print("Nilai tertinggi kamu adalah: ", max(nilai_a,nilai_b,nilai_c))
print("Nilai terendah kamu adalah: ", min(nilai_a,nilai_b,nilai_c))
rata2 = (nilai_a + nilai_b + nilai_c)/3
print(rata2)
print("Nilai rata-rata kamu adalah(dibulatkan ke atas): ", math.ceil(rata2))
print("Nilai rata-rata kamu adalah(dibulatkan ke bawah): ", math.floor(rata2))
