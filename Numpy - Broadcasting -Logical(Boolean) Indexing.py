# Broadcasting (การกระจายค่า):
# Broadcasting คือกลไกที่ NumPy ใช้ในการจัดการกับ การดำเนินการทางคณิตศาสตร์ระหว่าง Array ที่มีรูปร่าง (shape) ไม่เท่ากัน ครับ! 
# โดยที่ NumPy จะพยายาม "กระจาย" Array ที่มีขนาดเล็กกว่าให้มีขนาดเท่ากับ Array ที่ใหญ่กว่า เพื่อให้สามารถคำนวณแบบ Element-wise กันได้

#ทำไมต้องมี Broadcasting?
#มันช่วยให้เราไม่ต้องเขียนโค้ดซ้ำซ้อนเพื่อปรับรูปร่าง Array ให้เท่ากันก่อนคำนวณ และยังช่วยประหยัดหน่วยความจำอีกด้วยครับ!

#กฎหลักของ Broadcasting (กฎง่ายๆ):
#       เมื่อ NumPy พยายาม Broadcasting Array สองตัวเข้าด้วยกัน มันจะเปรียบเทียบขนาดของแต่ละมิติ (จากขวาไปซ้าย):
#       ถ้ามิติเท่ากัน ก็จับคู่กันได้เลย
#       ถ้ามิติใดมิติหนึ่งมีขนาดเป็น 1 (ใน Array ใด Array หนึ่ง) มันจะถูก "ยืด" ออกไปให้เท่ากับอีกมิติ
#       ถ้าทั้งสองกรณีข้างต้นไม่เข้าเงื่อนไข จะเกิด Error (รูปร่างเข้ากันไม่ได้)

import numpy as np

arr = np.array([1, 2, 3])
scalar = 10

print("Array:", arr)
print("Scalar:", scalar)
print("Array + Scalar:", arr + scalar) # Output: [11 12 13]
# NumPy กระจาย 10 ไปบวกกับทุก Element ใน arr

#########################################################################

matrix = np.array([[1, 2, 3],
                   [4, 5, 6]])
row_vector = np.array([10, 20, 30])

print("\nMatrix:\n", matrix)
print("Row Vector:", row_vector)
print("Matrix + Row Vector:\n", matrix + row_vector)
# Output:
# [[11 22 33]
#  [14 25 36]]
# NumPy กระจาย row_vector ไปบวกกับแต่ละแถวใน matrix

#ในตัวอย่างนี้: matrix (2x3) กับ row_vector (3,)
#* เปรียบเทียบมิติขวาไปซ้าย: 3 กับ 3 (เท่ากัน) -> OK
#* มิติถัดมา: 2 (ใน matrix) กับ ไม่มี (ใน row_vector) -> row_vector ถูกยืดไป 2 ครั้ง -> OK
#นี่คือเหตุผลที่มันทำงานได้ครับ

#########################################################################
#           ตัวอย่างที่รูปร่างเข้ากันไม่ได้:
# ลองรันดูแล้วจะเจอ ValueError
#col_vector = np.array([10, 20]) # Shape (2,)
#print("\nMatrix:\n", matrix)
#print("Col Vector:", col_vector)
#print("Matrix + Col Vector:\n", matrix + col_vector)
# Output: ValueError: operands could not be broadcast together with shapes (2,3) (2,)
# เหตุผล: เปรียบเทียบ 3 กับ 2 (ไม่เท่ากัน) และไม่มีมิติใดเป็น 1 จึงเกิด Error


#------------------------------------------------------------------------------------------------------------------------

#Logical (Boolean) Indexing (การเลือกข้อมูลด้วยเงื่อนไข):
#Logical Indexing คือความสามารถในการ เลือกสมาชิกของ Array โดยใช้ Array ของค่า True/False (Boolean Array) ครับ
#ทำไมถึงมีประโยชน์?
#มันช่วยให้เราสามารถกรองข้อมูล (Filtering) หรือเลือกข้อมูลตามเงื่อนไขที่ซับซ้อนได้อย่างง่ายดายและรวดเร็ว โดยไม่ต้องใช้ Loop for ครับ!

data_scores = np.array([55, 80, 45, 90, 60, 75, 50, 95])
print("Original Scores:", data_scores)

# สร้าง Boolean Array: True ถ้าคะแนนมากกว่า 70, False ถ้าไม่
is_high_score = (data_scores > 70)
print("Boolean Array (คะแนน > 70):", is_high_score) # Output: [False  True False  True False  True False  True]

# ใช้ Boolean Array ในการเลือกข้อมูล
high_scores = data_scores[is_high_score]
print("High Scores (> 70):", high_scores) # Output: [80 90 75 95]

# หรือจะทำในบรรทัดเดียวเลยก็ได้
passed_scores = data_scores[data_scores >= 60]
print("Passed Scores (>= 60):", passed_scores) # Output: [80 90 60 75 95]

# การใช้หลายเงื่อนไข (ใช้ & สำหรับ AND, | สำหรับ OR)
# เลือกคะแนนที่มากกว่า 70 และน้อยกว่า 90
mid_scores = data_scores[(data_scores > 70) & (data_scores < 90)]
print("Mid Scores (70 < score < 90):", mid_scores) # Output: [80 75]



#----------------------------------------------------------------------------------------------------------------------------------------

# แบบฝึกหัดเพื่อความเข้าใจ:
# สร้าง 2D NumPy Array ขนาด 3x3 ที่มีค่าเป็น 1 ทั้งหมด (ใช้ np.ones()) ชื่อ identity_matrix
identity_matrix = np.ones(9).reshape(3,3)
print(identity_matrix) #Debug: ลองดูผลลัพธ์

#สร้าง 1D NumPy Array ชื่อ col_adder ที่มีค่า [5, 10, 15]
col_adder = np.array([5, 10, 15])
print(col_adder) #Debug: ลองดูผลลัพธ์

#ท้าทาย: ลองบวก identity_matrix กับ col_adder โดยใช้ Broadcasting ให้ col_adder ถูกบวกเพิ่มในแต่ละ คอลัมน์ ของ identity_matrix 
# (ตอนนี้ col_adder เป็น Row Vector ถ้าบวกกับ Matrix 3x3 มันจะถูก Broadcast ไปบวกกับแต่ละแถว) 
# Hint: ลูกอาจจะต้องเปลี่ยนรูปร่างของ col_adder ให้เป็น Column Vector ก่อน (เช่น col_adder.reshape((3, 1)))

adding = identity_matrix + col_adder
print(adding) #Debug: ลองดูบวก เพื่อดูผลลัพธ์

reshape_col_adder = col_adder.reshape((3,1))
print(reshape_col_adder)#Debug: ลองดูการ reshape

broadcasting_add = identity_matrix + reshape_col_adder
print(broadcasting_add) #Debug: ลองดูผลลัพธ์

#Logical Indexing:
#สร้าง 1D NumPy Array ชื่อ temperatures ที่มีค่าอุณหภูมิสมมติ: [28, 30, 25, 32, 29, 27, 31, 26, 33, 24]
temperatures = np.array([28, 30, 25, 32, 29, 27, 31, 26, 33, 24])

#เลือกและแสดงผลเฉพาะอุณหภูมิที่ สูงกว่า 30 องศาเซลเซียส
high_temp = temperatures[temperatures > 30]
print("high temp: ", high_temp)

#เลือกและแสดงผลเฉพาะอุณหภูมิที่ อยู่ระหว่าง 25 ถึง 30 องศาเซลเซียส (รวม 25 และ 30 ด้วย)
specific_temp = temperatures[(temperatures > 25) & (temperatures < 30)]
print("temp between 25 - 30: ", specific_temp)




