# Insertion Sort

## 1. Concept
**Insertion Sort** เป็นอัลกอริทึมการจัดเรียงที่ทำงานโดยการแทรกค่าทีละตัวเข้าไปในตำแหน่งที่เหมาะสมในลิสต์ที่เรียงแล้ว
เริ่มจากสมาชิกที่สอง และขยับค่าทางซ้ายไปเรื่อย ๆ เพื่อหาตำแหน่งที่ควรแทรก

- ลักษณะ: คล้ายการเรียงไพ่ในมือ
- ประเภท: **Comparison-based Sorting**
- ความเสถียร: **Stable** (ค่าที่เท่ากันจะไม่สลับลำดับเดิม)

---

## 2. Algorithm Steps
1. เริ่มจากตำแหน่งที่ 1 (ตัวที่สองของลิสต์)
2. เก็บค่าปัจจุบันไว้ในตัวแปรชั่วคราว (key)
3. เปรียบเทียบ key กับค่าก่อนหน้า ถ้าค่าก่อนหน้ามากกว่า key → เลื่อนค่าไปขวา
4. ทำซ้ำจนกว่าจะหาตำแหน่งที่เหมาะสม → แทรก key เข้าไป
5. ทำซ้ำขั้นตอน 1–4 จนครบทุกสมาชิก

---

## 3. Pseudocode
```
procedure insertionSort(A)
    for i ← 1 to length(A)-1 do
        key ← A[i]
        j ← i - 1
        while j ≥ 0 and A[j] > key do
            A[j+1] ← A[j]
            j ← j - 1
        A[j+1] ← key
end procedure
```

---

## 4. Python Example
```python
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

# Example usage
data = [5, 3, 8, 4, 2]
sorted_data = insertion_sort(data)
print(sorted_data)  # Output: [2, 3, 4, 5, 8]
```

---

## 5. Complexity Analysis
| Case       | Time Complexity | Explanation                              |
|------------|----------------|------------------------------------------|
| Best       | O(n)           | ลิสต์เรียงอยู่แล้ว → ไม่มีการเลื่อนค่า |
| Average    | O(n²)          | ต้องเลื่อนค่าทุกตัวหลายรอบ              |
| Worst      | O(n²)          | ลิสต์เรียงแบบตรงข้ามทั้งหมด              |
| Space      | O(1)           | ใช้พื้นที่ในลิสต์เดิม (In-place)        |

---

## 6. Use Cases
- เหมาะกับ **ข้อมูลขนาดเล็ก** ที่ต้องการความเรียบง่าย
- ดีสำหรับข้อมูลที่เกือบเรียงอยู่แล้ว (Nearly Sorted)
- ใช้ใน Embedded Systems หรือระบบที่ไม่สามารถใช้หน่วยความจำมาก

---

## 7. Visualization (Shift Highlight)

### Initial
[5, 3, 8, 4, 2]

---

### Pass 1 (i=1, key=3)
- เปรียบเทียบ 5 กับ 3 → เลื่อน 5 ไปขวา → แทรก 3 → [3, 5, 8, 4, 2]

### Pass 2 (i=2, key=8)
- 8 > 5 → ไม่ต้องเลื่อน → [3, 5, 8, 4, 2]

### Pass 3 (i=3, key=4)
- เลื่อน 8 → 5 → แทรก 4 → [3, 4, 5, 8, 2]

### Pass 4 (i=4, key=2)
- เลื่อน 8 → 5 → 4 → 3 → แทรก 2 → [2, 3, 4, 5, 8]

---

✅ **Sorted Result:** [2, 3, 4, 5, 8]

---

## 🎥 ดูวิดีโอบน YouTube  
🔗 https://www.youtube.com/watch?v=Q1JdRUh1_98
