# โปรเจกต์ NumPy เล็ก ๆ: "การวิเคราะห์ข้อมูลยอดขายสินค้าเบื้องต้น"

#สถานการณ์:
#สมมติว่าลูกเป็น Data Analyst ที่ได้รับข้อมูลยอดขายสินค้า 3 ชนิด (Product A, Product B, Product C) ในแต่ละไตรมาสของปี 2024 ครับ

#ข้อมูล (สมมติ):
'''
ยอดขายไตรมาส 1 (ล้านบาท): Product A=10, Product B=12, Product C=8

ยอดขายไตรมาส 2 (ล้านบาท): Product A=15, Product B=10, Product C=11

ยอดขายไตรมาส 3 (ล้านบาท): Product A=13, Product B=14, Product C=9

ยอดขายไตรมาส 4 (ล้านบาท): Product A=18, Product B=11, Product C=12
'''
import numpy as np


#สร้าง NumPy Array 2 มิติ:
#สร้าง NumPy Array ชื่อ sales_data ที่เก็บข้อมูลยอดขายข้างต้น โดยให้แต่ละ แถว แทน ไตรมาส และแต่ละ คอลัมน์ แทน สินค้าแต่ละชนิด (Product A, B, C)
sales = np.array([(10,12,8),(15,10,11),(13,14,9),(18,11,12)])
sales_data = sales.reshape(4,3)
print("ข้อมูล sales_data: ",sales_data)
print("ข้อมูล sales_data.shape: ",sales_data.shape)

#การเข้าถึงและเลือกข้อมูล:
#แสดงยอดขายทั้งหมดของ Product B (คอลัมน์ที่ 2)
print("ยอดขายทั้งหมดของ Product B",sales_data[:,1])

#แสดงยอดขายทั้งหมดใน ไตรมาสที่ 3 (แถวที่ 3)
print("ยอดขายทั้งหมดใน Q3",sales_data[2,:])

#แสดงยอดขายของ Product A ในไตรมาสที่ 4
print("ยอดขาย Product A ใน Q4",sales_data[-1,0])

#การคำนวณเบื้องต้น:
#คำนวณหา ยอดขายรวม (Total Sales) ของแต่ละสินค้า (Product A, Product B, Product C) ตลอดทั้งปี
total_sales = np.sum(sales_data, axis=0) #ถ้าผมใช้เป็น total_sales = sum(sales_data) เลยจะได้ไหมนะ? outputออกมาได้เท่ากันนะ
print("ยอดขายรวม ของแต่ละสินค้า: ",total_sales, "ตลอดทั้งปี")

#คำนวณหา ยอดขายเฉลี่ย (Average Sales) ของแต่ละสินค้า ตลอดทั้งปี
average_sales = np.mean(sales_data, axis=0) #ใช้เป็น np.average(sales_data, axis= 0) ได้ไหม? outputออกมาได้เท่ากันนะ
print("ยอดขายเฉลี่ย ของแต่ละสินค้า ตลอดทั้งปี: ", average_sales)

#คำนวณหา ยอดขายรวมทั้งหมด (Grand Total Sales) 
grand_total_sales = np.sum(sales_data)
print("ยอดขายรวมทั้งหมด: ",grand_total_sales)

#การใช้ Broadcasting (เพิ่มโบนัส/ส่วนลด):
#สมมติว่าในไตรมาสที่ 4 มีการจัดโปรโมชั่น ทำให้ยอดขายของทุกสินค้า เพิ่มขึ้น 5 ล้านบาท
bonus_q4 = np.array([5,5,5])

#สร้าง Array ใหม่ชื่อ sales_q4_adjusted ที่ปรับยอดขายไตรมาส 4 โดยการบวก bonus_q4 เข้าไป (ใช้ Broadcasting)
sales_q4_adjusted = sales_data[3:,:] + bonus_q4
print(sales_q4_adjusted)

#การใช้ Logical Indexing (วิเคราะห์ยอดขายต่ำ):
#เลือกและแสดงผลเฉพาะยอดขายที่ น้อยกว่า 10 ล้านบาท จาก sales_data ทั้งหมด
lower_10 = sales_data[sales_data < 10]
print("ยอดขายที่ น้อยกว่า 10 ล้านบาท จาก sales_data ทั้งหมด: " ,lower_10)

