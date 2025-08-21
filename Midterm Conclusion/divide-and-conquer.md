## **3️⃣ Divide and Conquer**

แบ่งปัญหาเป็นหลายส่วน แก้แต่ละส่วน แล้วรวมผลลัพธ์

### สารบัญ

🔥 [Merge Sort](#-merge-sort)  
⚡ [Quick Sort](#-quick-sort)  
🌳 [Binary Tree Traversals and Related Properties](#-binary-tree-traversals-and-related-properties)  
🌀 [Closest-pair Problem](#-closest-pair-problem)  
💎 [Convex-hull Problem](#-convex-hull-problem)

## 🔥 Merge Sort

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

## ⚡ Quick Sort

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

---

## 🔸 Minimal-change Requirement

### 1. Concept / Purpose

* Minimal-change Requirement เป็น **แนวคิดในการสร้าง sequence ของ permutations**
* วัตถุประสงค์: แต่ละ permutation **แตกต่างจากตัวก่อนหน้าเพียงการสลับ 2 elements เท่านั้น**
* ใช้ใน **generating permutations efficiently** โดยลดความซับซ้อนของการเปลี่ยนแปลง

### 2. Motivation / Why use it

* ลดความซับซ้อนของการเปลี่ยนแปลงระหว่าง permutations
* ใช้ใน **backtracking, simulation, combinatorial testing**
* ทำให้ sequence ของ permutations สามารถ **trace หรือ reproduce** ได้ง่าย

### 3. Complexity Analysis

| Aspect | Complexity |
| ------ | ---------- |
| Time   | O(n!)      |
| Space  | O(n)       |

### 4. Use Cases

* Generating permutations for testing all possibilities
* Simulations ที่ต้องลอง permutation หลายแบบ
* Problems ที่ต้องการ minimal-change sequences

### 5. Principle / How it works

* **หลักการคิด:**

  1. เริ่มจาก permutation แรก (เช่น \[1,2,3,...,n])
  2. สร้าง permutation ถัดไปโดย **สลับเพียง 2 elements**
  3. ทำซ้ำจนได้ทุก permutation
* ตัวอย่าง algorithms ที่ใช้: **Johnson-Trotter, Gray code based permutations**

### 6. Example

* n = 3, permutations sequence แบบ minimal-change:

```
[1, 2, 3]
[1, 3, 2]  # swap 2 and 3
[3, 1, 2]  # swap 1 and 3
[3, 2, 1]  # swap 1 and 2
[2, 3, 1]  # swap 2 and 3
[2, 1, 3]  # swap 1 and 2
```

* สังเกตว่าแต่ละ step **เปลี่ยนแค่ 2 elements**

### 7. Pseudocode

```
procedure MinimalChangePermutation(n):
    Initialize first permutation P = [1, 2, ..., n]
    while not all permutations generated:
        Find next permutation by swapping 2 elements according to algorithm
        Output current permutation
```

### 8. Python Example

```python
def minimal_change_permutation(n):
    # Example using Johnson-Trotter idea
    perm = list(range(1, n+1))
    dir = [-1] * n  # -1 means LEFT, 1 means RIGHT

    def mobile():
        m, idx = -1, -1
        for i in range(n):
            neighbor = i + dir[i]
            if 0 <= neighbor < n and perm[i] > perm[neighbor]:
                if perm[i] > m:
                    m, idx = perm[i], i
        return idx

    while True:
        print(perm)
        idx = mobile()
        if idx == -1:
            break
        neighbor = idx + dir[idx]
        perm[idx], perm[neighbor] = perm[neighbor], perm[idx]
        dir[idx], dir[neighbor] = dir[neighbor], dir[idx]
        idx = neighbor
        for i in range(n):
            if perm[i] > perm[idx]:
                dir[i] *= -1

# Example usage
minimal_change_permutation(3)
# Output:
# [1, 2, 3]
# [1, 3, 2]
# [3, 1, 2]
# [3, 2, 1]
# [2, 3, 1]
# [2, 1, 3]
```

## 🔹 Binary Tree Traversals and Related Properties

### 1. Concept / Purpose

* อธิบายวิธีเดิน (traverse) โครงสร้างข้อมูลแบบ Binary Tree เพื่อเข้าถึงทุก node อย่างเป็นระบบ
* Traversals หลัก ๆ: Preorder, Inorder, Postorder (DFS-family) และ Level-order (BFS)
* เชื่อมโยงคุณสมบัติเชิงทฤษฎีของ Binary Tree (เช่น ความสูง จำนวนโหนด ความสัมพันธ์ใบ/โหนดภายใน ฯลฯ)

### 2. Motivation / Why use it

* จำเป็นต่อการประมวลผล/แปลงต้นไม้ เช่น สร้าง expression, ประเมินค่า, serialization/deserialization
* ใช้ใน BST (Inorder ให้ผลลัพธ์เรียงลำดับ), Heaps, Parsing, Compilers
* พื้นฐานของการสร้างต้นไม้กลับ (tree reconstruction) จากชุด traversal บางคู่

### 3. Complexity Analysis

| Operation                                        | Time | Extra Space                  |
| ------------------------------------------------ | ---- | ---------------------------- |
| Preorder / Inorder / Postorder (recursive)       | O(n) | O(h) recursion stack         |
| Preorder / Inorder / Postorder (iterative stack) | O(n) | O(h)                         |
| Level-order (BFS queue)                          | O(n) | O(w) (w = ความกว้างสูงสุด)   |
| Morris Traversal (Inorder/Preorder)              | O(n) | O(1) (ปรับ pointer ชั่วคราว) |

> n = จำนวน node, h = ความสูงของต้นไม้ (สูงสุด n-1 ถ้า skewed), w = maximum width

### 4. Traversal Types (Principle / How it works)

**4.1 DFS Family (Depth-First Traversals)**

* Preorder (Root, Left, Right): เยี่ยม root ก่อน → ใช้สำหรับ copy tree / prefix notation
* Inorder (Left, Root, Right): สำหรับ BST จะได้ลำดับเรียงจากน้อยไปมาก
* Postorder (Left, Right, Root): ใช้ลบต้นไม้/คำนวณค่านิพจน์ (ต้องทราบค่าลูกก่อน)

**4.2 BFS (Level-order)**

* เยี่ยม node ทีละระดับ (level) จากซ้ายไปขวา ด้วย queue

**4.3 Euler Tour View (มุมมองเดียวครอบคลุม)**

* คิดว่าเราเดิน “รอบ” ต้นไม้: ก่อนเข้าซ้าย (pre), กลับจากซ้าย (in), กลับจากขวา (post)

**4.4 Morris Traversal (Inorder/Preorder แบบ O(1) space)**

* สร้าง/คืนค่า thread ชั่วคราวจาก predecessor → ไม่ใช้ stack/recursion

### 5. Worked Example (Step by Step)

พิจารณาต้นไม้ตัวอย่าง (ค่าภายในเป็นตัวอักษร):

```
        A
       / \
      B   C
     / \   \
    D   E   F
```

* Preorder: A, B, D, E, C, F
* Inorder: D, B, E, A, C, F
* Postorder: D, E, B, F, C, A
* Level-order: A, B, C, D, E, F

### 6. Traversal → Reconstruction (คุณสมบัติสำคัญ)

* Inorder + Preorder → สร้างต้นไม้ได้หนึ่งเดียว (keys ไม่ซ้ำ)
* Inorder + Postorder → สร้างต้นไม้ได้หนึ่งเดียว (keys ไม่ซ้ำ)
* Preorder + Postorder → โดยทั่วไปไม่พอ (ไม่ unique) ยกเว้น full/proper binary tree (ทุกโหนดภายในมีลูก 2 คน)
* สำหรับ BST: มีเพียง Preorder หรือ Postorder อย่างเดียว (ไม่มี inorder) ก็ reconstruct ได้ (เพราะ invariant ของ BST)

### 7. Related Properties of Binary Trees

**นิยาม**

* Height (h): จำนวน edge จากรากถึงใบลึกสุด (กำหนด root สูง 0)
* Depth ของ node: จำนวน edge จากรากถึง node นั้น
* Level i: กลุ่ม node ที่มี depth = i (root อยู่ level 0)

**ขอบเขตเชิงปริมาณ**

* จำนวน node สูงสุดที่ level i = 2^i
* จำนวน node สูงสุดของต้นไม้สูง h (perfect) = 2^(h+1) - 1
* ความสูงต่ำสุดของต้นไม้ที่มี n node = ceil(log2(n+1)) - 1
* ต้นไม้ perfect: ทุก level เติมเต็ม → n = 2^(h+1) - 1
* ต้นไม้ complete: ทุก level ยกเว้นอาจ level สุดท้ายเติมเต็ม และ level สุดท้ายเรียงซ้ายสุด
* ต้นไม้ full/proper: ทุกโหนดภายในมีลูก 2 คน → ความสัมพันธ์สำคัญ: ใบ (L) = โหนดภายใน (I) + 1 และ n = 2L - 1
* จำนวน null pointers (link ว่าง) ใน binary tree แบบ linked มีค่า n + 1

**ผลลัพธ์พิเศษบน BST**

* Inorder traversal ของ BST จะให้ลำดับ sorted non-decreasing
* การแทรก/ลบที่ไม่ balance อาจทำให้ h → O(n) (skewed) → traversal/ค้นหาแย่ลง

### 8. Pseudocode

**8.1 Recursive**

```
procedure Preorder(node):
    if node == null: return
    visit(node)
    Preorder(node.left)
    Preorder(node.right)

procedure Inorder(node):
    if node == null: return
    Inorder(node.left)
    visit(node)
    Inorder(node.right)

procedure Postorder(node):
    if node == null: return
    Postorder(node.left)
    Postorder(node.right)
    visit(node)

procedure LevelOrder(root):
    if root == null: return
    Q ← empty queue
    enqueue(Q, root)
    while Q not empty:
        u ← dequeue(Q)
        visit(u)
        if u.left  != null: enqueue(Q, u.left)
        if u.right != null: enqueue(Q, u.right)
```

**8.2 Iterative (ตัวอย่าง Inorder ด้วย stack)**

```
procedure InorderIterative(root):
    S ← empty stack
    curr ← root
    while curr != null or S not empty:
        while curr != null:
            push(S, curr)
            curr ← curr.left
        curr ← pop(S)
        visit(curr)
        curr ← curr.right
```

**8.3 Morris Inorder (O(1) extra space)**

```
procedure MorrisInorder(root):
    curr ← root
    while curr != null:
        if curr.left == null:
            visit(curr)
            curr ← curr.right
        else:
            pre ← curr.left
            while pre.right != null and pre.right != curr:
                pre ← pre.right
            if pre.right == null:        # สร้าง thread
                pre.right ← curr
                curr ← curr.left
            else:                         # ลบ thread และ visit
                pre.right ← null
                visit(curr)
                curr ← curr.right
```

### 9. Python Example

```python
from collections import deque

class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

# Recursive traversals

def preorder(node, out):
    if not node: return
    out.append(node.key)
    preorder(node.left, out)
    preorder(node.right, out)

def inorder(node, out):
    if not node: return
    inorder(node.left, out)
    out.append(node.key)
    inorder(node.right, out)

def postorder(node, out):
    if not node: return
    postorder(node.left, out)
    postorder(node.right, out)
    out.append(node.key)

# Iterative inorder (stack)

def inorder_iterative(root):
    res, stack = [], []
    curr = root
    while curr or stack:
        while curr:
            stack.append(curr)
            curr = curr.left
        curr = stack.pop()
        res.append(curr.key)
        curr = curr.right
    return res

# Level-order (BFS)

def level_order(root):
    if not root: return []
    res, q = [], deque([root])
    while q:
        u = q.popleft()
        res.append(u.key)
        if u.left: q.append(u.left)
        if u.right: q.append(u.right)
    return res

# Build example tree
#         'A'
#        /    \
#      'B'    'C'
#      /  \      \
#    'D'  'E'    'F'
A = Node('A'); B = Node('B'); C = Node('C')
D = Node('D'); E = Node('E'); F = Node('F')
A.left, A.right = B, C
B.left, B.right = D, E
C.right = F

po, io, pto = [], [], []
preorder(A, po); inorder(A, io); postorder(A, pto)
print('Preorder   :', po)   # ['A','B','D','E','C','F']
print('Inorder    :', io)   # ['D','B','E','A','C','F']
print('Postorder  :', pto)  # ['D','E','B','F','C','A']
print('Level-order:', level_order(A))  # ['A','B','C','D','E','F']
```

### 10. Edge Cases & Tips

* Empty tree / single node: โค้ดควรรองรับได้
* Skewed tree (เหมือนลิงก์ลิสต์): h ≈ n-1 → ระวัง recursion stack ลึก
* Duplicates: นิยาม BST ต้องชัด (เช่น ซ้ำไปทางซ้ายเสมอ หรืออนุญาตเท่ากันอยู่ขวา)
* Stability ของ traversal: Inorder ของ BST ให้ลำดับเรียงเสมอ แต่ถ้ามี duplicate ต้องกำหนดข้อตกลง
* Morris: เร็วและใช้ O(1) space แต่แก้ pointer ชั่วคราว ควรระวังถ้าต้นไม้แชร์/อ้างอิงที่อื่น

### เพิ่มเติม — ขยายความเชิงลึก (Detailed Additions)

#### A. Iterative Traversals (more variants)

* **Iterative Preorder (stack, efficient):**

  1. push root
  2. while stack not empty: node = pop; visit(node); if node.right push; if node.left push
  3. ผลได้เป็น Root, Left, Right

```
def preorder_iterative(root):
    if not root: return []
    res, stack = [], [root]
    while stack:
        node = stack.pop()
        res.append(node.key)
        if node.right: stack.append(node.right)
        if node.left:  stack.append(node.left)
    return res
```

* **Postorder — two stacks (ง่ายเข้าใจ):**

  1. s1.push(root)
  2. while s1: u = s1.pop(); s2.push(u); if u.left s1.push(u.left); if u.right s1.push(u.right)
  3. pop s2 จะได้ postorder

```
def postorder_two_stacks(root):
    if not root: return []
    s1, s2, res = [root], [], []
    while s1:
        node = s1.pop()
        s2.append(node)
        if node.left: s1.append(node.left)
        if node.right: s1.append(node.right)
    while s2:
        res.append(s2.pop().key)
    return res
```

* **Postorder — one stack (lastVisited trick):**

  * เก็บ pointer lastVisited เพื่อรู้ว่าเพิ่งกลับมาจากลูกขวาหรือยัง

```
def postorder_one_stack(root):
    res, stack = [], []
    curr, lastVisited = root, None
    while curr or stack:
        while curr:
            stack.append(curr)
            curr = curr.left
        peek = stack[-1]
        if not peek.right or peek.right == lastVisited:
            res.append(peek.key)
            lastVisited = stack.pop()
        else:
            curr = peek.right
    return res
```

#### B. Morris Traversal (เพิ่มเติม)

* **Morris Inorder**: ใช้ predecessor ของ node ใน left subtree เพื่อสร้าง temporary thread → O(1) extra space. (พอมีในเอกสารแล้ว)
* **Morris Preorder**: คล้าย Inorder แต่ visit ก่อนสร้าง thread

```
def morris_preorder(root):
    res = []
    curr = root
    while curr:
        if not curr.left:
            res.append(curr.key)
            curr = curr.right
        else:
            pre = curr.left
            while pre.right and pre.right != curr:
                pre = pre.right
            if not pre.right:
                res.append(curr.key)  # visit before threading
                pre.right = curr
                curr = curr.left
            else:
                pre.right = None
                curr = curr.right
    return res
```

* **Morris Postorder (concept):** ทำโดยการสร้าง dummy root, thread ไปยัง predecessor แล้วเมื่อลบ thread ให้ reverse path ระหว่างสอง node เพื่อ collect nodes ใน order ที่ต้องการ → ซับซ้อนขึ้นแต่ยัง O(1) space

#### C. Reconstruction Algorithms (โค้ดตัวอย่าง)

* **Reconstruct from Inorder + Preorder** (unique if keys distinct)

```
def build_tree_pre_in(preorder, inorder):
    if not preorder or not inorder: return None
    root_val = preorder[0]
    root = Node(root_val)
    i = inorder.index(root_val)
    root.left = build_tree_pre_in(preorder[1:1+i], inorder[:i])
    root.right = build_tree_pre_in(preorder[1+i:], inorder[i+1:])
    return root
```

* **Reconstruct from Inorder + Postorder**

```
def build_tree_post_in(postorder, inorder):
    if not postorder or not inorder: return None
    root_val = postorder[-1]
    root = Node(root_val)
    i = inorder.index(root_val)
    root.left = build_tree_post_in(postorder[:i], inorder[:i])
    root.right = build_tree_post_in(postorder[i:-1], inorder[i+1:])
    return root
```

#### D. Expression Trees & Evaluation (application)

* สร้าง expression tree จาก postfix (หรือ inorder+postfix) แล้ว **evaluate** โดย postorder traversal

```
def evaluate_postfix(tokens):
    stack = []
    for t in tokens:
        if t.isdigit(): stack.append(int(t))
        else:
            b = stack.pop(); a = stack.pop()
            if t == '+': stack.append(a+b)
            elif t == '-': stack.append(a-b)
            elif t == '*': stack.append(a*b)
            elif t == '/': stack.append(a//b)
    return stack[-1]
```

#### E. Serialization / Deserialization

* **Preorder with null markers** (เช่น '#' หรือ None) ใช้ serialize tree เป็น stream แล้ว deserialize ได้โดยการอ่าน stream ตาม preorder

```
def serialize(root):
    res = []
    def dfs(u):
        if not u:
            res.append('#'); return
        res.append(str(u.key))
        dfs(u.left); dfs(u.right)
    dfs(root)
    return ' '.join(res)

def deserialize(tokens):
    it = iter(tokens.split())
    def dfs():
        val = next(it)
        if val == '#': return None
        node = Node(val)
        node.left = dfs(); node.right = dfs()
        return node
    return dfs()
```

#### F. Tree Metrics computable by traversal

* **Count nodes**: single traversal, O(n)
* **Count leaves**: check node.left == node.right == None
* **Height**: recursive depth
* **Diameter** (longest path):

  * naive O(n^2): for every node compute height left+right
  * optimal O(n): single postorder that returns (height, diameter)

```
def diameter(root):
    ans = 0
    def dfs(u):
        nonlocal ans
        if not u: return 0
        L = dfs(u.left); R = dfs(u.right)
        ans = max(ans, L + R)
        return 1 + max(L, R)
    dfs(root)
    return ans
```

#### G. Threaded Binary Trees (idea)

* แทนที่จะมี null pointers ไว้ เชื่อม pointer ของ node ที่ไม่มี child ไปยัง successor/predecessor (inorder) → ทำให้ traversal ง่ายขึ้นและบางครั้งไม่ต้องใช้ stack/recursion

#### H. Practical Tips / Pitfalls

* ระวัง recursion depth ถ้าต้นไม้ skewed → ใช้ iterative หรือ increase recursion limit
* เลือกวิธี traversal ตาม constraint: หากต้องการ O(1) extra space → Morris (แต่มี side-effect กับ pointer)
* ในการ reconstruct, ถ้ามี duplicate keys ต้องใช้ extra information (เช่น unique id)
* สำหรับ parallel processing ของต้นไม้: level-order ช่วยแบ่งงานเป็นระดับ ๆ

---

