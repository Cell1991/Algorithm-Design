# Bubble Sort

## 1. Concept
**Bubble Sort** เป็นอัลกอริทึมการจัดเรียงแบบง่าย (Simple Sorting Algorithm)  
ทำงานโดยการ **เปรียบเทียบ** องค์ประกอบที่อยู่ติดกัน (Adjacent Elements) และ **สลับตำแหน่ง** ถ้าลำดับไม่ถูกต้อง  
ทำซ้ำหลายรอบจนกว่าลิสต์จะเรียงสมบูรณ์

- ลักษณะ: เปรียบเทียบทีละคู่เหมือนฟองอากาศลอยขึ้นไปด้านบน
- ประเภท: **Comparison-based Sorting**
- ความเสถียร: **Stable** (ค่าที่เท่ากันจะไม่สลับลำดับเดิม)

---

## 2. Algorithm Steps
1. เริ่มจากตำแหน่งแรกของลิสต์
2. เปรียบเทียบคู่ของค่าที่อยู่ติดกัน
3. ถ้าค่าด้านซ้าย > ค่าด้านขวา → สลับตำแหน่ง
4. เลื่อนไปยังคู่ถัดไป
5. หลังจากรอบแรก ค่ามากที่สุดจะอยู่ท้ายสุด
6. ทำซ้ำขั้นตอน 1–5 โดย **ลดจำนวนการเปรียบเทียบลงทีละ 1** ในแต่ละรอบ
7. หยุดเมื่อไม่มีการสลับตำแหน่งเกิดขึ้นในรอบหนึ่ง

---

## 3. Pseudocode
```
procedure bubbleSort(A)
    n ← length(A)
    repeat
        swapped ← false
        for i ← 0 to n-2 do
            if A[i] > A[i+1] then
                swap A[i], A[i+1]
                swapped ← true
        n ← n - 1
    until swapped = false
end procedure
```

---

## 4. Python Example
```python
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:  # ถ้าไม่มีการสลับ → หยุด
            break
    return arr

# Example usage
data = [5, 3, 8, 4, 2]
sorted_data = bubble_sort(data)
print(sorted_data)  # Output: [2, 3, 4, 5, 8]
```

---

## 5. Complexity Analysis
| Case       | Time Complexity | Explanation                              |
|------------|----------------|------------------------------------------|
| Best       | O(n)           | ลิสต์เรียงอยู่แล้ว → หยุดทันที          |
| Average    | O(n²)          | ต้องเปรียบเทียบและสลับหลายรอบ           |
| Worst      | O(n²)          | ลิสต์เรียงแบบตรงข้ามทั้งหมด              |
| Space      | O(1)           | ใช้การสลับตำแหน่งในที่เดิม (In-place)   |

---

## 6. Use Cases
- เหมาะกับ **ข้อมูลขนาดเล็ก** ที่ไม่ต้องการประสิทธิภาพสูง
- ใช้สอนพื้นฐานการคิดเชิงอัลกอริทึม
- ใช้ในระบบที่ความง่ายสำคัญกว่าความเร็ว

---

## 7. Visualization (Colored Steps)

### Initial
[5, 3, 8, 4, 2]

---

### Pass 1
- <span style="background-color: #ffcccc">Step 1: Compare 5 & 3 → swap → [3, 5, 8, 4, 2]</span>

- <span style="background-color: #ccffcc">Step 2: Compare 5 & 8 → no swap → [3, 5, 8, 4, 2]</span>
- <span style="background-color: #ffcccc">Step 3: Compare 8 & 4 → swap → [3, 5, 4, 8, 2]</span>
- <span style="background-color: #ffcccc">Step 4: Compare 8 & 2 → swap → [3, 5, 4, 2, 8]</span>

---

### Pass 2
- <span style="background-color: #ccffcc">Step 1: Compare 3 & 5 → no swap → [3, 5, 4, 2, 8]</span>
- <span style="background-color: #ffcccc">Step 2: Compare 5 & 4 → swap → [3, 4, 5, 2, 8]</span>
- <span style="background-color: #ffcccc">Step 3: Compare 5 & 2 → swap → [3, 4, 2, 5, 8]</span>

---

### Pass 3
- <span style="background-color: #ccffcc">Step 1: Compare 3 & 4 → no swap → [3, 4, 2, 5, 8]</span>
- <span style="background-color: #ffcccc">Step 2: Compare 4 & 2 → swap → [3, 2, 4, 5, 8]</span>

---

### Pass 4
- <span style="background-color: #ffcccc">Step 1: Compare 3 & 2 → swap → [2, 3, 4, 5, 8]</span>

---

✅ **Sorted Result:** [2, 3, 4, 5, 8]

