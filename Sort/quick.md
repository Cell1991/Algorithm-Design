# Quick Sort

## 1. Concept
**Quick Sort** เป็นอัลกอริทึมแบบ Divide & Conquer ที่เลือกค่าหนึ่งเป็น `pivot` แล้วแบ่งลิสต์เป็นสองส่วน:
- ด้านซ้ายของ pivot จะมีแต่ค่าที่น้อยกว่า
- ด้านขวาของ pivot จะมีแต่ค่าที่มากกว่า
จากนั้นเรียกใช้ Quick Sort ซ้ำกับทั้งสองด้าน

- ลักษณะ: แบ่งแล้ว conquer เหมือน Merge Sort แต่ **ไม่รวม (merge)** ใช้สลับตำแหน่งแทน
- ประเภท: **Comparison-based Sorting**
- ความเสถียร: ❌ **Unstable** (ค่าที่เท่ากันอาจสลับตำแหน่ง)
- ใช้ได้แบบ In-place ไม่ต้องใช้หน่วยความจำเพิ่มเติมเท่ากับ Merge Sort

---

## 2. Algorithm Steps
1. ถ้าลิสต์มีขนาด ≤ 1 → ถือว่าเรียงแล้ว
2. เลือกค่าใดค่าหนึ่งเป็น `pivot` (เช่น ตัวแรก ตัวสุดท้าย หรือตัวกลาง)
3. แบ่งลิสต์ที่เหลือเป็น 2 กลุ่ม:
   - ค่าที่ ≤ pivot → กลุ่มซ้าย
   - ค่าที่ > pivot → กลุ่มขวา
4. เรียก Quick Sort กับกลุ่มซ้ายและขวา
5. รวมผลลัพธ์: `QuickSort(left) + [pivot] + QuickSort(right)`

---

## 3. Pseudocode (แบบ functional)
```
procedure quickSort(A)
    if length(A) ≤ 1 then return A
    pivot ← A[0]
    left ← [x in A[1..] where x ≤ pivot]
    right ← [x in A[1..] where x > pivot]
    return quickSort(left) + [pivot] + quickSort(right)
```

---

## 4. Python Example (แบบ functional)
```python
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[0]
    left = [x for x in arr[1:] if x <= pivot]
    right = [x for x in arr[1:] if x > pivot]
    return quick_sort(left) + [pivot] + quick_sort(right)

# Example usage
data = [5, 3, 8, 4, 2]
sorted_data = quick_sort(data)
print(sorted_data)  # Output: [2, 3, 4, 5, 8]
```

---

## 5. Python Example (แบบ in-place ด้วย Lomuto partition)
```python
def quick_sort_inplace(arr, low=0, high=None):
    if high is None:
        high = len(arr) - 1
    if low < high:
        p = partition(arr, low, high)
        quick_sort_inplace(arr, low, p - 1)
        quick_sort_inplace(arr, p + 1, high)

def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

# Example usage
data = [5, 3, 8, 4, 2]
quick_sort_inplace(data)
print(data)  # Output: [2, 3, 4, 5, 8]
```

---

## 6. Complexity Analysis
| Case       | Time Complexity | Explanation                                      |
|------------|----------------|--------------------------------------------------|
| Best       | O(n log n)     | แบ่งครึ่งสมดุลดี และเรียงได้เร็ว               |
| Average    | O(n log n)     | โดยเฉลี่ยทำงานเร็วมากในการใช้งานทั่วไป         |
| Worst      | O(n²)          | ถ้า pivot แย่ เช่น เลือกค่ามากหรือน้อยสุดเสมอ  |
| Space      | O(log n)       | ใช้ Stack ของ Recursion (in-place ไม่สร้างลิสต์ใหม่) |

---

## 7. Use Cases
- เหมาะกับข้อมูลขนาดใหญ่ที่ต้องการความเร็ว (เร็วกว่า Merge Sort โดยเฉลี่ย)
- ใช้ในระบบที่หน่วยความจำจำกัด เพราะไม่ต้องใช้ลิสต์เพิ่ม (in-place)
- ไม่เหมาะถ้าข้อมูลเรียงอยู่แล้ว และ pivot เลือกไม่ดี

---

## 8. Visualization (Pivot-Based Divide)
ตัวอย่าง: `[5, 3, 8, 4, 2]` → เลือก pivot = 5

→ left = [3, 4, 2], right = [8]  
→ QuickSort(left) = [2, 3, 4]  
→ รวม: [2, 3, 4] + [5] + [8] → ✅ `[2, 3, 4, 5, 8]`

---

✅ **Sorted Result:** [2, 3, 4, 5, 8]

---

## 🎥 ดูวิดีโอบน YouTube  
🔗 https://www.youtube.com/watch?v=Q1JdRUh1_98
