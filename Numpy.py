import numpy as np

# สร้าง NumPy Array จาก Python List
my_list = [1, 2, 3, 4, 5]
my_array = np.array(my_list)
print(f"My List: {my_list}")
print(f"My NumPy Array: {my_array}")
print(f"Type of my_array: {type(my_array)}")

# สร้าง Array ที่มีหลายมิติ (เหมือนตาราง)
# List ของ List
two_d_list = [[1, 2, 3], [4, 5, 6]]
two_d_array = np.array(two_d_list)
print(f"\n2D List:\n{two_d_list}")
print(f"2D NumPy Array:\n{two_d_array}")
print(f"Shape of 2D Array (แถว, คอลัมน์): {two_d_array.shape}")

import numpy as np

arr1 = np.array([1, 2, 3])
arr2 = np.array([10, 20, 30])

# การบวก
sum_array = arr1 + arr2
print(f"\n{arr1} + {arr2} = {sum_array}") # Output: [11 22 33]

# การคูณ (แต่ละตัว)
product_array = arr1 * arr2
print(f"{arr1} * {arr2} = {product_array}") # Output: [10 40 90]

# การคูณ Array ด้วยตัวเลข
scaled_array = arr1 * 5
print(f"{arr1} * 5 = {scaled_array}") # Output: [ 5 10 15]

# การยกกำลัง
power_array = arr1 ** 2
print(f"{arr1} ** 2 = {power_array}") # Output: [1 4 9]



import numpy as np

my_array = np.array([10, 20, 30, 40, 50])
print(f"\nMy Array: {my_array}")
print(f"First element: {my_array[0]}") # Output: 10
print(f"Elements from index 1 to 3 (exclusive): {my_array[1:4]}") # Output: [20 30 40]

# สำหรับ 2D Array
two_d_array = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])
print(f"\n2D Array:\n{two_d_array}")
print(f"Element at row 0, column 1: {two_d_array[0, 1]}") # Output: 2 (ค่าที่ตำแหน่งแถวที่ 0, คอลัมน์ที่ 1)
print(f"First row: {two_d_array[0, :]}") # Output: [1 2 3] (เลือกแถวที่ 0 ทั้งหมด)
print(f"First column: {two_d_array[:, 0]}") # Output: [1 4 7] (เลือกทุกแถวในคอลัมน์ที่ 0)


'''
โจทย์:

สร้าง NumPy Array 2 อัน:
array_a ให้มีค่าเป็น [5, 10, 15, 20]
array_b ให้มีค่าเป็น [1, 2, 3, 4]
นำ array_a และ array_b มาบวกกัน แล้วเก็บผลลัพธ์ไว้ในตัวแปรชื่อ sum_array
พิมพ์ค่าของ sum_array ออกมาดูผลลัพธ์ครับ'''

import numpy as np
array_a = np.array([5, 10, 15, 20])
array_b = np.array([1, 2, 3, 4])

sum_array = array_a + array_b
print(sum_array)
print(type(sum_array))