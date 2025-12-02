# 1. Tentukan Kriteria Penilaian dan Kelulusan
BATAS_LULUS = 75 # Nilai rata-rata minimal untuk LULUS
GRADE_A = 90
GRADE_B = 80
GRADE_C = 70
# Grade D adalah di bawah 70 hingga BATAS_LULUS
# Grade E adalah di bawah BATAS_LULUS

# 2. Data Siswa
# Setiap elemen adalah dictionary dengan nama dan list nilai (Tugas, UTS, UAS)
data_siswa = [
    {
        "nama": "Andi Pratama", 
        "nilai": [95, 90, 92] 
        # Rata-rata: 92.33 -> Grade A, LULUS (Uji Grade A)
    },
    {
        "nama": "Budi Santoso", 
        "nilai": [82, 85, 78] 
        # Rata-rata: 81.67 -> Grade B, LULUS (Uji Grade B)
    },
    {
        "nama": "Citra Dewi", 
        "nilai": [75, 70, 75] 
        # Rata-rata: 73.33 -> Grade D, GAGAL (Uji GAGAL/di bawah 75)
    },
    {
        "nama": "Dian Sari", 
        "nilai": [78, 77, 79] 
        # Rata-rata: 78.00 -> Grade C, LULUS (Uji Grade C dan LULUS)
    },
    {
        "nama": "Eko Murti", 
        "nilai": [60, 65, 60] 
        # Rata-rata: 61.67 -> Grade E, GAGAL (Uji Grade E/paling rendah)
    }
]

# 3. Proses Perhitungan dan Penentuan Grade
print("="*50)
print("             LAPORAN NILAI AKHIR SISWA")
print("="*50)

# Gunakan perulangan 'for' untuk memproses setiap siswa dalam list data_siswa
for siswa in data_siswa:
    # a. Hitung Rata-Rata
    total_nilai = sum(siswa["nilai"])
    jumlah_mapel = len(siswa["nilai"])
    rata_rata = total_nilai / jumlah_mapel
    
    # b. Tentukan Grade (Grade A jika 90, Grade B jika 80, dst.)
    if rata_rata >= GRADE_A:
        grade = 'A'
    elif rata_rata >= GRADE_B:
        grade = 'B'
    elif rata_rata >= GRADE_C:
        grade = 'C'
    elif rata_rata >= BATAS_LULUS:
        grade = 'D' # LULUS tapi nilai pas-pasan
    else:
        grade = 'E' # GAGAL
        
    # c. Tentukan Kelulusan (Kelulusan jika 75)
    if rata_rata >= BATAS_LULUS:
        kelulusan = "LULUS"
    else:
        kelulusan = "GAGAL"
        
    # d. Simpan hasil ke dictionary siswa
    siswa["rata_rata"] = rata_rata
    siswa["grade"] = grade
    siswa["kelulusan"] = kelulusan
    
    # 4. Output Hasil ke Konsol
    print(f"Nama Siswa: {siswa['nama']}")
    print(f"  Nilai (T,U,A): {siswa['nilai']}")
    print(f"  Rata-Rata: {rata_rata:.2f}")
    print(f"  Grade Akhir: **{grade}**")
    print(f"  Status: **{kelulusan}**")
    print("-" * 50)

# Opsional: Tampilkan semua data yang sudah diperbarui
# print("\nDATA AKHIR SEMUA SISWA:")
# for siswa in data_siswa:
#     print(siswa)