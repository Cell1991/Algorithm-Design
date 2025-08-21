## **3️⃣ Divide and Conquer**

แบ่งปัญหาเป็นหลายส่วน แก้แต่ละส่วน แล้วรวมผลลัพธ์

### สารบัญ

🔥 [Merge Sort](#-merge-sort)  
⚡ [Quick Sort](#-quick-sort)  
🌳 [Binary Tree Traversals and Related Properties](#-binary-tree-traversals-and-related-properties)  
🌀 [Closest-pair Problem](#-closest-pair-problem)  
💎 [Convex-hull Problem](#-convex-hull-problem)

## Merge Sort

### 1. Concept
**Merge Sort** เป็นอัลกอริทึมแบบ Divide & Conquer
ที่แบ่งลิสต์ออกเป็นสองส่วนซ้ำ ๆ จนแต่ละส่วนมีแค่ 1 ตัว แล้วรวมกลับอย่างมีลำดับ (Merge)

- ลักษณะ: แบ่งแล้วรวม
- ประเภท: **Comparison-based Sorting**
- ความเสถียร: **Stable** (ลำดับค่าที่เท่ากันไม่เปลี่ยน)
- ลักษณะพิเศษ: ใช้ Recursion และต้องใช้หน่วยความจำเพิ่มเติม

### 2. Algorithm Steps
1. ถ้าลิสต์มีความยาว ≤ 1 → ถือว่าเรียงแล้ว
2. แบ่งลิสต์ครึ่งหนึ่งเป็นซ้ายและขวา
3. ใช้ Merge Sort กับซ้ายและขวา (เรียกตัวเอง - recursive)
4. รวมลิสต์ซ้ายและขวาที่เรียงแล้วให้เป็นลิสต์เดียว (merge แบบเรียง)
5. ส่งลิสต์ที่รวมเสร็จกลับขึ้นไป

### 3. Pseudocode
```
procedure mergeSort(A)
    if length(A) ≤ 1 then return A
    mid ← length(A) / 2
    left ← mergeSort(A[0..mid-1])
    right ← mergeSort(A[mid..end])
    return merge(left, right)

procedure merge(left, right)
    result ← empty list
    while left and right not empty do
        if left[0] ≤ right[0] then
            append left[0] to result; remove left[0]
        else
            append right[0] to result; remove right[0]
    append remaining elements of left and right to result
    return result
```

### 4. Python Example
```python
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result

# Example usage
data = [5, 3, 8, 4, 2]
sorted_data = merge_sort(data)
print(sorted_data)  # Output: [2, 3, 4, 5, 8]
```

---

### 5. Complexity Analysis
| Case       | Time Complexity | Explanation                                |
|------------|----------------|--------------------------------------------|
| Best       | O(n log n)     | แบ่งครึ่งทุกครั้ง และรวมทุกระดับ          |
| Average    | O(n log n)     | เสถียรไม่ว่าลิสต์จะเป็นแบบไหน             |
| Worst      | O(n log n)     | กรณีแย่ที่สุดก็ยังคง log-linear            |
| Space      | O(n)           | ต้องใช้ลิสต์ใหม่ตอน merge (ไม่ in-place)  |

### 6. Use Cases
- เหมาะกับข้อมูลขนาดใหญ่ที่ต้องการประสิทธิภาพสูง
- ใช้ได้ดีแม้ลิสต์จะไม่เรียงมาก่อน
- ใช้ในระบบที่ต้องการความเสถียรของการจัดเรียง

### 7. Visualization (Divide & Merge)

#### Initial
[5, 3, 8, 4, 2]

→ แบ่ง: [5, 3] | [8, 4, 2]  
→ แบ่ง: [5] [3] | [8] [4, 2]  
→ แบ่ง: [4] [2] → รวม: [2, 4]  
→ รวม: [3, 5] | [2, 4, 8] → รวมสุดท้าย: [2, 3, 4, 5, 8]

✅ **Sorted Result:** [2, 3, 4, 5, 8]

### 🎥 ดูวิดีโอบน YouTube  
🔗 https://www.youtube.com/watch?v=5Z9dn2WTg9o

---

## Quick Sort (ฉบับเต็ม: Pivot Strategies + i/j Explanation)

### 1. Concept
**Quick Sort** เป็นอัลกอริทึมแบบ Divide & Conquer ที่แบ่งลิสต์โดยการเลือก "Pivot" แล้วจัดเรียงค่ารอบ ๆ Pivot  
เพื่อให้ค่าที่น้อยกว่ามาอยู่ทางซ้าย และค่าที่มากกว่ามาอยู่ทางขวา แล้วใช้ Quick Sort ซ้ำกับทั้งสองฝั่ง

- ประเภท: Comparison-based, Recursive
- ความซับซ้อนเฉลี่ย: O(n log n)
- ความเสถียร: ❌ Unstable
- ใช้หน่วยความจำต่ำ: ✅ In-place (ถ้าใช้ Lomuto/Hoare)

### 2. วิธีเลือก Pivot

| วิธี | อธิบาย | จุดเด่น |
|------|--------|---------|
| First Element | ใช้ค่าตัวแรก | ง่าย แต่เสี่ยงถ้าข้อมูลเรียงแล้ว |
| Last Element | ใช้ค่าตัวสุดท้าย | ใช้คู่กับ **Lomuto Partition** |
| Middle Element | ค่ากลาง `arr[(low+high)//2]` | ดีกว่าการเลือกขอบ |
| Random | สุ่ม index | ปลอดภัยจาก worst-case |
| Median-of-Three | หาค่ากลางจาก `[low, mid, high]` | ลดความลำเอียงของข้อมูลเรียงแล้ว |

### 3. หลักการ i/j ใน Lomuto Partition (Pivot = arr[high])

```text
- i: ตำแหน่ง "ล่าสุด" ที่พบค่าที่ <= pivot
- j: วนตรวจสอบทุกตำแหน่งจาก low → high-1
- ถ้า arr[j] <= pivot → เพิ่ม i แล้วสลับ i กับ j
- สุดท้ายสลับ i+1 กับ pivot เพื่อให้ pivot ไปอยู่ตรงกลาง
```

#### ตัวอย่าง: Lomuto Partition
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

### 4. โค๊ด Quick Sort – Pivot Strategies (แยกแต่ละแบบ)

#### Pivot แบบที่ 1: First Element
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

#### Pivot แบบที่ 2: Last Element (Lomuto)
```python
def quick_sort_last(arr, low=0, high=None):
    if high is None:
        high = len(arr) - 1
    if low < high:
        p = partition(arr, low, high)  # ใช้ตัวท้ายเป็น pivot โดยตรง
        quick_sort_last(arr, low, p - 1)
        quick_sort_last(arr, p + 1, high)
```

#### Pivot แบบที่ 3: Middle Element
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

#### Pivot แบบที่ 4: Random Element
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

#### Pivot แบบที่ 5: Median-of-Three
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

#### ฟังก์ชัน Partition (ใช้ร่วมกัน)
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

#### ตัวอย่างการใช้งาน
```python
data = [5, 3, 8, 4, 2]
quick_sort_median3(data)
print(data)  # Output: [2, 3, 4, 5, 8]
```

### 5. เปรียบเทียบ Pivot Strategies

| Pivot | Stable | ปลอดภัยกับข้อมูลเรียงแล้ว | เหมาะกับกรณี |
|-------|--------|-----------------------------|---------------|
| First | ❌ | ❌ | ง่าย, ใช้เรียนรู้ |
| Last  | ❌ | ❌ | ใช้กับ Lomuto |
| Middle| ❌ | ✅ | ปานกลาง |
| Random| ✅ | ✅ | ทั่วไป |
| Median3| ✅ | ✅ | ป้องกัน worst-case |

### 6. Complexity Analysis

| Case | Time | Space |
|------|------|--------|
| Best | O(n log n) | O(log n) |
| Avg  | O(n log n) | O(log n) |
| Worst| O(n²)      | O(log n) |

- Worst-case = ข้อมูลเรียงอยู่แล้ว + pivot แย่ (แก้ได้ด้วย Random / Median-3)

### 7. Visualization (Pivot แบ่งกลุ่ม)

```
Original Array: [5, 3, 8, 4, 2]
เลือก Pivot = 2 (ตัวสุดท้าย)

1. เริ่ม Partition:  
   เปรียบเทียบจากซ้ายไปขวาจนถึงก่อน Pivot  
   ไม่มีตัวไหน ≤ 2 → ไม่มีการ swap

2. สลับ Pivot ไปอยู่ตำแหน่งแรก:  
   [2, 3, 8, 4, 5] ← pivot (2) อยู่ตำแหน่งที่ถูกต้องแล้ว

→ left = []  
→ right = [3, 8, 4, 5]

3. เรียก QuickSort ทางขวา:  
   - pivot = 5  
   - แบ่งได้เป็น left = [3, 4], right = [8]  
   - เรียก QuickSort ซ้ำไป

4. เมื่อเรียงครบทุกฝั่ง → รวมผลลัพธ์:

→ QuickSort(left) = []  
→ Pivot = 2  
→ QuickSort(right) = [3, 4, 5, 8]

✅ Result = [] + [2] + [3, 4, 5, 8] = [2, 3, 4, 5, 8]
```

✅ **ผลลัพธ์ที่ได้:** [2, 3, 4, 5, 8]

### 🎥 วิดีโอแนะนำ (Pivot Strategies & Partitioning)

🔗 https://www.youtube.com/watch?v=WprjBK0p6rw



