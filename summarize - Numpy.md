สรุปบทเรียน NumPy
NumPy (Numerical Python) เป็น Library พื้นฐานที่ทรงพลังสำหรับการทำงานกับข้อมูลเชิงตัวเลข (Numerical Data) และการคำนวณทางคณิตศาสตร์และวิทยาศาสตร์ใน Python มันเป็นรากฐานสำหรับ Library ยอดนิยมอื่น ๆ ที่ใช้ใน Machine Learning เช่น Pandas, Matplotlib, Scikit-learn, TensorFlow และ PyTorch

1. แนวคิดหลัก: ndarray (N-dimensional Array)
แกนกลางของ NumPy คือ Object ที่เรียกว่า ndarray ซึ่งเป็นโครงสร้างข้อมูลที่มีประสิทธิภาพสูงสำหรับเก็บข้อมูลตัวเลข

ndarray สามารถมีได้หลายมิติ (1D, 2D, 3D, ... N-dimensional)

สมาชิกทั้งหมดใน ndarray ต้องเป็นข้อมูลประเภทเดียวกัน (homogeneous)

การคำนวณบน ndarray ทำได้เร็วกว่า Python List มาก เนื่องจากถูก optimize มาอย่างดี

2. การสร้าง NumPy Array
2.1 จาก Python List หรือ Tuple
Python

import numpy as np

# 1 มิติ (Vector)
my_list_1d = [1, 2, 3, 4, 5]
arr_1d = np.array(my_list_1d)
print("1D Array:", arr_1d)
print("Type:", type(arr_1d)) # Output: <class 'numpy.ndarray'>

# 2 มิติ (Matrix)
my_list_2d = [[1, 2, 3], [4, 5, 6]]
arr_2d = np.array(my_list_2d)
print("\n2D Array:\n", arr_2d)
print("Shape (รูปร่าง/ขนาด):", arr_2d.shape) # (จำนวนแถว, จำนวนคอลัมน์)
print("Dimension (มิติ):", arr_2d.ndim)
print("Data Type (ชนิดข้อมูล):", arr_2d.dtype)
2.2 การสร้างด้วยฟังก์ชันของ NumPy
ฟังก์ชัน              

คำอธิบาย                                                            

ตัวอย่าง                                                                              

np.zeros(shape)    

สร้าง Array ที่มีค่าเป็น 0 ทั้งหมด                                

np.zeros((2, 3))                                                                  

np.ones(shape)      

สร้าง Array ที่มีค่าเป็น 1 ทั้งหมด                                

np.ones(4)                                                                        

np.full(shape, value)

สร้าง Array ที่มีค่าเป็น value ทั้งหมด                            

np.full((2, 2), 7)                                                                

np.arange(start, stop, step)

คล้ายกับ range() แต่สร้างเป็น NumPy Array                              

np.arange(0, 10, 2)                                                                

np.linspace(start, stop, num)

สร้าง Array ที่มีค่ากระจายเท่ากันในช่วงที่กำหนด (num คือจำนวนตัวเลข)

np.linspace(0, 1, 5)                                                              

np.random.rand(shape)

สร้าง Array ของตัวเลขสุ่มระหว่าง 0-1                                

np.random.rand(2, 2)                                                              

arr.reshape(new_shape)

เปลี่ยนรูปร่างของ Array โดยไม่เปลี่ยนข้อมูล                              

np.arange(1, 10).reshape((3, 3))                                                  


ส่งออกไปยังชีต
3. การเข้าถึงข้อมูล (Indexing) และการเลือกช่วงข้อมูล (Slicing)
Indexing: เข้าถึงสมาชิกแต่ละตัว

1 มิติ: arr[index]

2 มิติ: arr[row_index, col_index]

Slicing: เลือกช่วงข้อมูล (Sub-array)

1 มิติ: arr[start:end:step]

2 มิติ: arr[row_start:row_end:row_step, col_start:col_end:col_step]

Python

arr_1d = np.array([10, 20, 30, 40, 50, 60])
print("1D Array:", arr_1d)
print("Index 0:", arr_1d[0]) # 10
print("Slice [1:4]:", arr_1d[1:4]) # [20 30 40]

arr_2d = np.array([[1, 2, 3],
                   [4, 5, 6],
                   [7, 8, 9]])
print("\n2D Array:\n", arr_2d)
print("arr_2d[1, 2]:", arr_2d[1, 2]) # 6
print("แถวแรกทั้งหมด:", arr_2d[0, :]) # [1 2 3]
print("คอลัมน์สุดท้ายทั้งหมด:\n", arr_2d[:, -1]) # [3 6 9]
print("Sub-matrix (แถว 1-2, คอลัมน์ 1-2):\n", arr_2d[0:2, 0:2])
# [[1 2]
#  [4 5]]
4. การคำนวณบน NumPy Array (Vectorization)
NumPy สามารถทำการคำนวณทางคณิตศาสตร์ได้โดยตรงบน Array ทั้งหมดแบบ Element-wise ซึ่งเร็วกว่า Python List มาก

การดำเนินการแบบ Element-wise:

Python

arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
print("arr1 + arr2:", arr1 + arr2) # [5 7 9]
print("arr1 * 2:", arr1 * 2) # [2 4 6]
ฟังก์ชันทางคณิตศาสตร์ทั่วไป: np.sqrt(), np.exp(), np.log(), np.sin() ฯลฯ

Python

print("np.sqrt(arr2):", np.sqrt(arr2))
ฟังก์ชันทางสถิติ:

Python

data = np.array([10, 20, 30, 40, 50])
print("Sum:", np.sum(data)) # 150
print("Mean:", np.mean(data)) # 30.0
print("Max:", np.max(data)) # 50
print("Min:", np.min(data)) # 10
print("Standard Deviation:", np.std(data))
# การคำนวณตามแกน (axis)
matrix_sum = np.array([[1,2],[3,4]])
print("Sum ตามคอลัมน์ (axis=0):", np.sum(matrix_sum, axis=0)) # [4 6]
print("Mean ตามแถว (axis=1):", np.mean(matrix_sum, axis=1)) # [1.5 3.5]
5. Broadcasting (การกระจายค่า)
กลไกที่ NumPy ใช้ในการคำนวณทางคณิตศาสตร์ระหว่าง Array ที่มีรูปร่าง (shape) ไม่เท่ากัน โดยจะพยายาม "ยืด" หรือ "กระจาย" Array ที่มีขนาดเล็กกว่าให้มีขนาดเท่ากับ Array ที่ใหญ่กว่า

เป็นไปตามกฎบางอย่าง (เปรียบเทียบมิติจากขวาไปซ้าย)

Python

matrix = np.array([[1, 2, 3], [4, 5, 6]]) # Shape (2, 3)
scalar = 10
row_vec = np.array([10, 20, 30]) # Shape (3,)
col_vec = np.array([[10], [20]]) # Shape (2, 1)

print("\nMatrix + Scalar:\n", matrix + scalar)
# [[11 12 13]
#  [14 15 16]]
print("\nMatrix + Row Vector:\n", matrix + row_vec)
# [[11 22 33]
#  [14 25 36]]
print("\nMatrix + Column Vector (ต้องเป็น (2,1) หรือ (3,1) ถ้าอีกตัวเป็น (X,3)):\n", np.array([[1,2],[3,4]]) + np.array([[10],[20]]))
# [[11 12]
#  [23 24]]
6. Logical (Boolean) Indexing (การเลือกข้อมูลด้วยเงื่อนไข)
การเลือกสมาชิกของ Array โดยใช้ Array ของค่า True/False (Boolean Array)

มีประโยชน์มากในการกรองข้อมูลตามเงื่อนไขที่ซับซ้อน

Python

data_values = np.array([5, 12, 8, 20, 3, 15, 7])
print("\nOriginal Data:", data_values)

# เลือกค่าที่มากกว่า 10
filter_condition = (data_values > 10)
print("Boolean Condition:", filter_condition) # [False True False True False True False]
filtered_data = data_values[filter_condition]
print("Values > 10:", filtered_data) # [12 20 15]

# เลือกค่าที่อยู่ระหว่าง 5 ถึง 15 (รวม 5 และ 15)
filtered_range = data_values[(data_values >= 5) & (data_values <= 15)]
print("Values between 5 and 15:", filtered_range) # [ 5 12  8 15  7]
