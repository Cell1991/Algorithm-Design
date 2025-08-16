# Quick Sort (ฉบับเต็ม: Pivot Strategies)

## 1. Concept
**Quick Sort** เป็นอัลกอริทึมแบบ Divide & Conquer ที่เลือกค่า `pivot` แล้วแบ่งลิสต์เป็นสองกลุ่ม:
- ด้านซ้ายของ pivot: ค่าน้อยกว่าหรือเท่ากับ
- ด้านขวาของ pivot: ค่ามากกว่า
จากนั้นใช้ Quick Sort ซ้ำกับกลุ่มซ้ายและขวา แล้วรวมผลแบบ In-place หรือแบบ functional ก็ได้

---

## 2. วิธีเลือก Pivot ที่นิยม
1. **First Element** → ใช้ค่าตัวแรกของช่วงที่กำลังเรียง
2. **Last Element** → ใช้ค่าตัวสุดท้ายของช่วง (ใช้บ่อยกับ Lomuto Partition)
3. **Middle Element** → ค่ากลาง (index = (low+high)//2)
4. **Random Element** → สุ่มค่าจากในช่วง
5. **Median-of-Three** → หาค่ากลางจาก 3 ค่าคือ [ซ้าย, กลาง, ขวา] แล้วใช้ค่านั้นเป็น pivot

---

## 3. หลักการทำงานของ i, j (Lomuto Partition)
- `pivot = arr[high]` (ตัวท้าย)
- `i` = ตำแหน่งล่าสุดที่พบค่าที่ ≤ pivot
- `j` = วิ่งจาก `low` ถึง `high-1`
- ถ้า `arr[j] ≤ pivot` → เพิ่ม i แล้วสลับ `arr[i] ↔ arr[j]`
- หลังจบ loop → สลับ `arr[i+1]` กับ `pivot` เพื่อให้อยู่ตำแหน่งที่ถูกต้อง

### ตัวอย่าง
```python
arr = [5, 3, 8, 4, 2]
pivot = 2 (arr[high])
เริ่ม i = -1, j ไล่ตั้งแต่ 0 → 3
j=0: arr[0]=5 > 2 → ข้าม
j=1: arr[1]=3 > 2 → ข้าม
...
จบ loop → i = -1 → สลับ arr[0] กับ pivot → [2, 3, 8, 4, 5]
pivot = index 0
แบ่งกลุ่มได้: [] + [2] + [3, 8, 4, 5]
```

---

## 4. Python Code (Lomuto + เลือก Pivot หลายแบบ)
```python
import random

def quick_sort(arr, low=0, high=None, pivot_method='last'):
    if high is None:
        high = len(arr) - 1
    if low < high:
        p = partition(arr, low, high, pivot_method)
        quick_sort(arr, low, p - 1, pivot_method)
        quick_sort(arr, p + 1, high, pivot_method)

def partition(arr, low, high, pivot_method):
    if pivot_method == 'first':
        arr[low], arr[high] = arr[high], arr[low]
    elif pivot_method == 'middle':
        mid = (low + high) // 2
        arr[mid], arr[high] = arr[high], arr[mid]
    elif pivot_method == 'random':
        rand_idx = random.randint(low, high)
        arr[rand_idx], arr[high] = arr[high], arr[rand_idx]
    elif pivot_method == 'median3':
        mid = (low + high) // 2
        triple = [(arr[low], low), (arr[mid], mid), (arr[high], high)]
        triple.sort(key=lambda x: x[0])
        median_index = triple[1][1]
        arr[median_index], arr[high] = arr[high], arr[median_index]
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
quick_sort(data, pivot_method='median3')
print(data)  # Output: [2, 3, 4, 5, 8]
```

---

## 5. Summary
| Pivot Strategy | เสถียรภาพ | ปลอดภัยกับข้อมูลเรียงแล้ว? | เหมาะกับกรณี             |
|----------------|------------|-----------------------------|----------------------------|
| First Element  | ❌         | ไม่ปลอดภัย                  | ข้อมูลสุ่ม                 |
| Last Element   | ❌         | ไม่ปลอดภัย                  | ใช้บ่อยกับ Lomuto         |
| Middle Element | ❌         | ดีกว่าบางกรณี               | ข้อมูลค่อนข้างเรียงแล้ว   |
| Random Element | ✅         | ปลอดภัยดีมาก                | ข้อมูลสุ่มหรือไม่แน่นอน  |
| Median-of-3    | ✅         | ปลอดภัยดีมาก                | ข้อมูลเรียง/เกือบเรียง    |

---

✅ **Sorted Result (ทุกแบบ):** [2, 3, 4, 5, 8]

---

## 🎥 ดูวิดีโอบน YouTube  
🔗 https://www.youtube.com/watch?v=Q1JdRUh1_98
