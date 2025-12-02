nilai_siswa = [95, 82, 76, 65, 58, 89, 91]

print("=== HASIL PENILAIAN SISWA ===")

for nilai in nilai_siswa:
    if nilai >= 95:
        grade = "A"
        status = "Lulus"
    elif nilai >= 87:
        grade = "B"
        status = "Lulus"
    elif nilai >= 75:
        grade = "C"
        status = "Lulus"
    elif nilai >= 55:
        grade = "D"
        status = "Tidak Lulus"
    else:
        grade = "E"
        status = "Tidak Lulus"

    print(f"Nilai: {nilai} | Grade: {grade} | Status: {status}") 