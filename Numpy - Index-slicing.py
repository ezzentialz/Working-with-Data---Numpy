#ลองใช้ความรู้เรื่อง Indexing, Slicing และการคำนวณเบื้องต้นกับโจทย์นี้ดูนะครับ:
import numpy as np

#สร้าง 2D NumPy Array ขนาด 4x4 ที่มีค่าตั้งแต่ 1 ถึง 16 (เรียงตามลำดับ) ชื่อ matrix_data
#(Hint: สร้าง 1D array ด้วย np.arange(1, 17) แล้วใช้ reshape((4, 4)) ครับ)
matrix_data = np.arange(1, 17).reshape((4, 4))
print(matrix_data)

#เข้าถึงและแสดงผล:

#สมาชิกที่อยู่แถวที่ 2 คอลัมน์ที่ 3 (index 1, 2)
print(f"สมาชิกที่อยู่แถวที่ 2 คอลัมน์ที่ 3 (index 1, 2): {matrix_data[1, 2]}")

#ทุกสมาชิกในคอลัมน์สุดท้าย
print(f"ทุกสมาชิกในคอลัมน์สุดท้าย: {matrix_data[:, -1]}")

#สองแถวแรกทั้งหมด
print(f"สองแถวแรกทั้งหมด: {matrix_data[0:2, ]}")

#Sub-matrix (เมทริกซ์ย่อย) ที่ประกอบด้วยสมาชิกในแถวที่ 2 และ 3 (index 1, 2) และคอลัมน์ที่ 2 และ 3 (index 1, 2)
print(f"Sub-matrix: {matrix_data[1:3, 1:3]}")

##สร้าง Array scores_a = np.array([85, 90, 78]) และ scores_b = np.array([92, 88, 80])
scores_a = np.array([85, 90, 78])
scores_b = np.array([92, 88, 80])

result = scores_a + scores_b

print(f"คำนวนผลรวมของคะแนน A แบบ Element-wise {np.sum(scores_a)}")
print(f"คำนวนผลรวมของคะแนน B แบบ Element-wise {np.sum(scores_b)}")
print(f"ผลรวมคะแนนทั้งหมด {np.sum(result)}")

#หาค่าเฉลี่ยของ scores_a
print(f"หาค่าเฉลี่ยของ scores_a: {np.average(scores_a)}")

#หาค่าสูงสุดของ scores_b
print(f"หาค่าสูงสุดของ scores_b: {np.max(scores_b)}")