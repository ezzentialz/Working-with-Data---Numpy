# Working-with-Data---Numpy
NumPy (Numerical Python) เป็น Library พื้นฐานที่ทรงพลังมากสำหรับ:

การทำงานกับ Numerical Data (ข้อมูลตัวเลข)

การคำนวณทางคณิตศาสตร์และวิทยาศาสตร์ที่ซับซ้อนและมีประสิทธิภาพสูง

เป็นรากฐานสำหรับ Library อื่น ๆ ที่ใช้ใน Machine Learning เช่น Pandas, Matplotlib, Scikit-learn, TensorFlow, PyTorch

ทำไมต้องใช้ NumPy ใน ML?
ใน Machine Learning เรามักจะต้องจัดการกับข้อมูลจำนวนมหาศาลที่อยู่ในรูปของ Array (อาร์เรย์) หรือ Matrix (เมทริกซ์) ซึ่ง NumPy ถูกออกแบบมาเพื่อจัดการกับข้อมูลประเภทนี้ได้อย่างรวดเร็วและมีประสิทธิภาพมากกว่า Python List ทั่วไปหลายเท่าตัวครับ!

แนวคิดหลัก: ndarray (N-dimensional Array)
แกนกลางของ NumPy คือ Object ที่เรียกว่า ndarray (N-dimensional Array)

ndarray เป็นเหมือน List ที่สามารถมีได้หลายมิติ (1 มิติ, 2 มิติ, 3 มิติ หรือมากกว่า) และเก็บข้อมูลประเภทเดียวกันเท่านั้น (เช่น ทั้งหมดเป็นจำนวนเต็ม, ทั้งหมดเป็นทศนิยม)

การคำนวณบน ndarray จะทำได้เร็วกว่า Python List มาก เพราะมันถูกเขียนขึ้นด้วยภาษา C/Fortran ที่เร็วกว่าครับ

การสร้าง NumPy Array:
เราสามารถสร้าง ndarray ได้หลายวิธีครับ:

จาก Python List หรือ Tuple:

Python

import numpy as np

# 1 มิติ (Vector)
my_list = [1, 2, 3, 4, 5]
np_array_1d = np.array(my_list)
print("1D Array:", np_array_1d)
print("Type:", type(np_array_1d)) # Output: <class 'numpy.ndarray'>

# 2 มิติ (Matrix)
my_list_of_lists = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
np_array_2d = np.array(my_list_of_lists)
print("\n2D Array:\n", np_array_2d)
print("Shape (รูปร่าง/ขนาด):", np_array_2d.shape) # Output: (3, 3) คือ 3 แถว 3 คอลัมน์
print("Dimension (มิติ):", np_array_2d.ndim)     # Output: 2
print("Data Type (ชนิดข้อมูล):", np_array_2d.dtype) # Output: int64 (หรือตามข้อมูล)
การสร้าง Array ด้วยฟังก์ชันของ NumPy:

np.zeros(shape): สร้าง Array ที่มีค่าเป็น 0 ทั้งหมด

np.ones(shape): สร้าง Array ที่มีค่าเป็น 1 ทั้งหมด

np.full(shape, value): สร้าง Array ที่มีค่าเป็น value ทั้งหมด

print("\n--- สร้าง Array ด้วยฟังก์ชัน NumPy ---")
zeros_array = np.zeros((2, 3)) # 2 แถว 3 คอลัมน์ ของ 0
print("Zeros Array:\n", zeros_array)

ones_array = np.ones(4) # 1 มิติ 4 ตัว ของ 1
print("\nOnes Array:", ones_array)

full_array = np.full((2, 2), 7) # 2 แถว 2 คอลัมน์ ของ 7
print("\nFull Array (ค่า 7):\n", full_array)

arange_array = np.arange(0, 10, 2) # เริ่ม 0, ไม่เกิน 10, ทีละ 2
print("\nArange Array:", arange_array) # Output: [0 2 4 6 8]

linspace_array = np.linspace(0, 1, 5) # 5 ตัวเลข กระจายเท่ากันระหว่าง 0 ถึง 1
print("\nLinspace Array:", linspace_array) # Output: [0.   0.25 0.5  0.75 1.  ]

random_array = np.random.rand(2, 2) # Array สุ่ม 2x2
print("\nRandom Array (0-1):\n", random_array)

np.arange(start, stop, step): คล้ายกับ range() แต่สร้างเป็น NumPy Array (ที่เราเคยใช้แล้ว!)

np.linspace(start, stop, num): สร้าง Array ที่มีค่ากระจายเท่ากันในช่วงที่กำหนด

np.random.rand(shape): สร้าง Array ของตัวเลขสุ่มระหว่าง 0-1

np.eye(n): สร้าง Identity Matrix (เมทริกซ์เอกลักษณ์)



การเข้าถึงข้อมูล (Indexing & Slicing) และการคำนวณเบื้องต้น
เมื่อเราสร้าง Array ขึ้นมาแล้ว สิ่งต่อไปที่สำคัญคือการที่เราจะ เข้าถึงข้อมูล (Indexing) หรือ เลือกช่วงข้อมูล (Slicing) ที่เราต้องการ เพื่อนำไปวิเคราะห์หรือคำนวณต่อครับ

1. การเข้าถึงข้อมูล (Indexing):
การเข้าถึงข้อมูลใน NumPy Array คล้ายกับการเข้าถึงสมาชิกใน Python List แต่มีความยืดหยุ่นและทรงพลังกว่า โดยเฉพาะกับ Array หลายมิติครับ

1 มิติ (1D Array): เหมือน List ทั่วไป ใช้ [] และ index
import numpy as np
arr_1d = np.array([10, 20, 30, 40, 50])

print("Array 1D:", arr_1d)
print("สมาชิกตัวแรก (index 0):", arr_1d[0])    # Output: 10
print("สมาชิกตัวสุดท้าย (index -1):", arr_1d[-1]) # Output: 50

2 มิติ (2D Array / Matrix): ใช้ [row_index, col_index] หรือ [row_index][col_index] (แต่วิธีแรกจะนิยมกว่าและเร็วกว่า)
print("\n--- Slicing 1D Array ---")
arr_1d = np.array([10, 20, 30, 40, 50, 60, 70])
print("Array 1D:", arr_1d)
print("ตั้งแต่ index 2 ถึง 4 (ไม่รวม 5):", arr_1d[2:5])   # Output: [30 40 50]
print("ตั้งแต่ต้นจนถึง index 3 (ไม่รวม 4):", arr_1d[:4])  # Output: [10 20 30 40]
print("ตั้งแต่ index 3 เป็นต้นไป:", arr_1d[3:])        # Output: [40 50 60 70]
print("ทุกตัวเว้น 2 (ตั้งแต่ต้น):", arr_1d[::2])     # Output: [10 30 50 70]



2. การเลือกช่วงข้อมูล (Slicing):
การ Slicing ใช้ start:end:step เหมือน List ทั่วไป แต่สามารถใช้ได้กับหลายมิติพร้อมกัน!

1 มิติ:

Python

print("\n--- Slicing 1D Array ---")
arr_1d = np.array([10, 20, 30, 40, 50, 60, 70])
print("Array 1D:", arr_1d)
print("ตั้งแต่ index 2 ถึง 4 (ไม่รวม 5):", arr_1d[2:5])   # Output: [30 40 50]
print("ตั้งแต่ต้นจนถึง index 3 (ไม่รวม 4):", arr_1d[:4])  # Output: [10 20 30 40]
print("ตั้งแต่ index 3 เป็นต้นไป:", arr_1d[3:])        # Output: [40 50 60 70]
print("ทุกตัวเว้น 2 (ตั้งแต่ต้น):", arr_1d[::2])     # Output: [10 30 50 70]
2 มิติ: นี่คือจุดที่ NumPy ทรงพลังมาก! เราสามารถ Slice ได้ทั้งแถวและคอลัมน์พร้อมกัน

รูปแบบ: [row_start:row_end, col_start:col_end]

ถ้าเว้นว่างหมายถึงทั้งหมด เช่น : หมายถึงทั้งหมดในมิตินั้น

Python

print("\n--- Slicing 2D Array ---")
arr_2d = np.array([[1, 2, 3, 10],
                   [4, 5, 6, 11],
                   [7, 8, 9, 12],
                   [13, 14, 15, 16]])
print("Array 2D:\n", arr_2d)

print("\nแถวแรกทั้งหมด:", arr_2d[0, :])     # Output: [ 1  2  3 10]
print("คอลัมน์สุดท้ายทั้งหมด:", arr_2d[:, -1])  # Output: [10 11 12 16]
print("สองแถวแรก สองคอลัมน์แรก:\n", arr_2d[0:2, 0:2])
# Output:
# [[1 2]
#  [4 5]]
print("แถวสุดท้าย (ทั้งแถว):", arr_2d[-1, :])   # Output: [13 14 15 16]
print("ทุกแถว คอลัมน์ที่ 1 และ 2 (index 0, 1):\n", arr_2d[:, 0:2])
# Output:
# [[ 1  2]
#  [ 4  5]
#  [ 7  8]
#  [13 14]]
3. การคำนวณเบื้องต้นบน NumPy Array:
นี่คือจุดเด่นที่ทำให้ NumPy แตกต่างจาก Python List อย่างชัดเจน! เราสามารถทำการคำนวณทางคณิตศาสตร์ได้โดยตรงบน Array ทั้ง Array โดยไม่จำเป็นต้องใช้ Loop! ซึ่งเรียกว่า Vectorization และมันเร็วกว่ามาก ๆ ครับ!

การดำเนินการแบบ Element-wise (สมาชิกต่อสมาชิก):

บวก, ลบ, คูณ, หาร, ยกกำลัง, Modulo

Python

print("\n--- การคำนวณเบื้องต้น ---")
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])

print("Array 1:", arr1)
print("Array 2:", arr2)
print("บวกกัน (Element-wise):", arr1 + arr2) # Output: [5 7 9]
print("คูณด้วย scalar (สมาชิกทุกตัวคูณด้วย 2):", arr1 * 2) # Output: [2 4 6]
print("ยกกำลัง 2 (ทุกตัว):", arr2 ** 2) # Output: [16 25 36]
ฟังก์ชันทางคณิตศาสตร์ทั่วไป: np.sqrt(), np.exp(), np.log(), np.sin(), np.cos()

Python

print("Square Root ของ Array 2:", np.sqrt(arr2)) # Output: [2.         2.23606798 2.44948974]
ฟังก์ชันทางสถิติ: np.sum(), np.mean(), np.min(), np.max(), np.std() (Standard Deviation)

Python

data_points = np.array([10, 20, 30, 40, 50])
print("\nData Points:", data_points)
print("ผลรวม:", np.sum(data_points))      # Output: 150
print("ค่าเฉลี่ย:", np.mean(data_points))    # Output: 30.0
print("ค่าน้อยสุด:", np.min(data_points))     # Output: 10
print("ค่ามากสุด:", np.max(data_points))     # Output: 50
print("ส่วนเบี่ยงเบนมาตรฐาน (Standard Deviation):", np.std(data_points)) # Output: 14.1421...



