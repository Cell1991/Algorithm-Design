# Quick Sort (ฉบับเต็ม: Pivot Strategies + i/j Explanation)

## 1. Concept
**Quick Sort** เป็นอัลกอริทึมแบบ Divide & Conquer ที่แบ่งลิสต์โดยการเลือก "Pivot" แล้วจัดเรียงค่ารอบ ๆ Pivot  
เพื่อให้ค่าที่น้อยกว่ามาอยู่ทางซ้าย และค่าที่มากกว่ามาอยู่ทางขวา แล้วใช้ Quick Sort ซ้ำกับทั้งสองฝั่ง

- ประเภท: Comparison-based, Recursive
- ความซับซ้อนเฉลี่ย: O(n log n)
- ความเสถียร: ❌ Unstable
- ใช้หน่วยความจำต่ำ: ✅ In-place (ถ้าใช้ Lomuto/Hoare)

---

## 2. วิธีเลือก Pivot

| วิธี | อธิบาย | จุดเด่น |
|------|--------|---------|
| First Element | ใช้ค่าตัวแรก | ง่าย แต่เสี่ยงถ้าข้อมูลเรียงแล้ว |
| Last Element | ใช้ค่าตัวสุดท้าย | ใช้คู่กับ **Lomuto Partition** |
| Middle Element | ค่ากลาง `arr[(low+high)//2]` | ดีกว่าการเลือกขอบ |
| Random | สุ่ม index | ปลอดภัยจาก worst-case |
| Median-of-Three | หาค่ากลางจาก `[low, mid, high]` | ลดความลำเอียงของข้อมูลเรียงแล้ว |

---

## 3. หลักการ i/j ใน Lomuto Partition (Pivot = arr[high])

```text
- i: ตำแหน่ง "ล่าสุด" ที่พบค่าที่ <= pivot
- j: วนตรวจสอบทุกตำแหน่งจาก low → high-1
- ถ้า arr[j] <= pivot → เพิ่ม i แล้วสลับ i กับ j
- สุดท้ายสลับ i+1 กับ pivot เพื่อให้ pivot ไปอยู่ตรงกลาง
```

### ตัวอย่าง: Lomuto Partition
```python
arr = [5, 3, 8, 4, 2]
pivot = 2 (arr[high])
i = -1

j = 0 → 5 > 2 → ไม่ขยับ  
j = 1 → 3 > 2 → ไม่ขยับ  
j = 2 → 8 > 2 → ไม่ขยับ  
j = 3 → 4 > 2 → ไม่ขยับ  

จบ loop → สลับ arr[i+1]=arr[0] กับ pivot → [2, 3, 8, 4, 5]
```

---

## 4. โค๊ด Quick Sort – Pivot Strategies (แยกแต่ละแบบ)

## Pivot แบบที่ 1: First Element
```python
def quick_sort_first(arr, low=0, high=None):
    if high is None:
        high = len(arr) - 1
    if low < high:
        arr[low], arr[high] = arr[high], arr[low]  # สลับมาไว้ท้าย
        p = partition(arr, low, high)
        quick_sort_first(arr, low, p - 1)
        quick_sort_first(arr, p + 1, high)
```

## Pivot แบบที่ 2: Last Element (Lomuto)
```python
def quick_sort_last(arr, low=0, high=None):
    if high is None:
        high = len(arr) - 1
    if low < high:
        p = partition(arr, low, high)  # ใช้ตัวท้ายเป็น pivot โดยตรง
        quick_sort_last(arr, low, p - 1)
        quick_sort_last(arr, p + 1, high)
```

## Pivot แบบที่ 3: Middle Element
```python
def quick_sort_middle(arr, low=0, high=None):
    if high is None:
        high = len(arr) - 1
    if low < high:
        mid = (low + high) // 2
        arr[mid], arr[high] = arr[high], arr[mid]  # นำค่ากลางมาไว้ท้าย
        p = partition(arr, low, high)
        quick_sort_middle(arr, low, p - 1)
        quick_sort_middle(arr, p + 1, high)
```

## Pivot แบบที่ 4: Random Element
```python
import random

def quick_sort_random(arr, low=0, high=None):
    if high is None:
        high = len(arr) - 1
    if low < high:
        rand = random.randint(low, high)
        arr[rand], arr[high] = arr[high], arr[rand]  # สลับ random มาไว้ท้าย
        p = partition(arr, low, high)
        quick_sort_random(arr, low, p - 1)
        quick_sort_random(arr, p + 1, high)
```

## Pivot แบบที่ 5: Median-of-Three
```python
def quick_sort_median3(arr, low=0, high=None):
    if high is None:
        high = len(arr) - 1
    if low < high:
        mid = (low + high) // 2
        triple = [(arr[low], low), (arr[mid], mid), (arr[high], high)]
        triple.sort()
        median_idx = triple[1][1]
        arr[median_idx], arr[high] = arr[high], arr[median_idx]  # median ไว้ท้าย
        p = partition(arr, low, high)
        quick_sort_median3(arr, low, p - 1)
        quick_sort_median3(arr, p + 1, high)
```

## ฟังก์ชัน Partition (ใช้ร่วมกัน)
```python
def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i+1], arr[high] = arr[high], arr[i+1]
    return i + 1
```

## ตัวอย่างการใช้งาน
```python
data = [5, 3, 8, 4, 2]
quick_sort_median3(data)
print(data)  # Output: [2, 3, 4, 5, 8]
```

---

## 5. เปรียบเทียบ Pivot Strategies

| Pivot | Stable | ปลอดภัยกับข้อมูลเรียงแล้ว | เหมาะกับกรณี |
|-------|--------|-----------------------------|---------------|
| First | ❌ | ❌ | ง่าย, ใช้เรียนรู้ |
| Last  | ❌ | ❌ | ใช้กับ Lomuto |
| Middle| ❌ | ✅ | ปานกลาง |
| Random| ✅ | ✅ | ทั่วไป |
| Median3| ✅ | ✅ | ป้องกัน worst-case |

---

## 6. Complexity Analysis

| Case | Time | Space |
|------|------|--------|
| Best | O(n log n) | O(log n) |
| Avg  | O(n log n) | O(log n) |
| Worst| O(n²)      | O(log n) |

- Worst-case = ข้อมูลเรียงอยู่แล้ว + pivot แย่ (แก้ได้ด้วย Random / Median-3)

---

## 7. Visualization (Pivot แบ่งกลุ่ม)

```
[5, 3, 8, 4, 2]
Pivot = 5

→ left = [3, 4, 2]  
→ right = [8]

→ QuickSort(left) = [2, 3, 4]  
→ QuickSort(right) = [8]

→ Result = [2, 3, 4] + [5] + [8] = ✅ [2, 3, 4, 5, 8]
```

---

✅ **ผลลัพธ์ที่ได้:** [2, 3, 4, 5, 8]

---

## 🎥 วิดีโอแนะนำ (Pivot Strategies & Partitioning)

🔗 https://www.youtube.com/watch?v=WprjBK0p6rw
