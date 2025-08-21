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

## 🌳 Binary Tree Traversals and Related Properties

### 1. Concept / Purpose
การ Traversal หมายถึงการเดินไปตาม node ของต้นไม้ (Binary Tree) เพื่อเข้าถึงทุก node อย่างเป็นระบบและมีลำดับที่แน่นอน  
เป็นพื้นฐานสำหรับงานต่าง ๆ เช่น:
- การประเมินค่า expression (Expression Tree)
- การ serialize/deserialize tree
- การค้นหา / เรียงลำดับใน BST

### 2. Traversal Types & Visual Explanation

เราจะใช้ต้นไม้ตัวอย่างนี้ในการอธิบาย (Root = A):

```
        A
       / \
      B   C
     / \   \
    D   E   F
```

### 🔸 Preorder Traversal (Root → Left → Right)

1. เยี่ยม Root ก่อน (A)
2. เดินซ้าย (B → D → E)
3. เดินขวา (C → F)

**ลำดับที่ได้:** A → B → D → E → C → F

**ภาพ Step-by-step:**

- Visit A → **[A]**
- ไปซ้าย: Visit B → **[A, B]**
- ไปซ้ายสุด: Visit D → **[A, B, D]**
- กลับมาที่ B ไปขวา: Visit E → **[A, B, D, E]**
- กลับไป Root ไปขวา: Visit C → **[A, B, D, E, C]**
- ไปขวาของ C: Visit F → **[A, B, D, E, C, F]**

### 🔸 Inorder Traversal (Left → Root → Right)

1. ไปซ้ายสุด (D)
2. กลับขึ้นมา visit Root ของ subtree (B)
3. ไปขวา (E)
4. กลับ root A
5. ไปขวา (C → F)

**ลำดับที่ได้:** D → B → E → A → C → F

**ภาพ Step-by-step:**

- ไปซ้ายสุด: D → **[D]**
- กลับมาที่ B → **[D, B]**
- ไปขวา B: E → **[D, B, E]**
- กลับ Root A → **[D, B, E, A]**
- ไปขวา A: C → **[D, B, E, A, C]**
- ไปขวา C: F → **[D, B, E, A, C, F]**

### 🔸 Postorder Traversal (Left → Right → Root)

1. ไปซ้ายสุด (D → E)
2. กลับมาที่ B
3. ไปขวา (C → F)
4. สุดท้าย Root A

**ลำดับที่ได้:** D → E → B → F → C → A

**ภาพ Step-by-step:**

- ไปซ้ายสุด D → **[D]**
- กลับมาที่ B → ไปขวา: E → **[D, E]**
- กลับมาที่ B → **[D, E, B]**
- ไปขวาของ Root: C → ไปขวา F → **[D, E, B, F]**
- กลับ C → **[D, E, B, F, C]**
- สุดท้าย Root A → **[D, E, B, F, C, A]**

### 🔸 Level-order Traversal (Breadth-First, ใช้ Queue)

1. เริ่มจาก Root (A)
2. ไปซ้าย → ขวาของแต่ละระดับ

**ลำดับที่ได้:** A → B → C → D → E → F

**Step:**

- Level 0: A → **[A]**
- Level 1: B, C → **[A, B, C]**
- Level 2: D, E, F → **[A, B, C, D, E, F]**

### 3. สรุปเปรียบเทียบการเดิน

| Traversal  | ลำดับเยี่ยม |
|------------|-------------|
| Preorder   | Root → Left → Right |
| Inorder    | Left → Root → Right |
| Postorder  | Left → Right → Root |
| Levelorder | ทีละระดับ (ซ้าย → ขวา) |

### 4. ความซับซ้อน (Complexity)

- ทุก traversal ใช้เวลา **O(n)** (ต้อง visit ทุก node)
- Recursive → ใช้ stack ลึกสุด **O(h)** (h = ความสูงของ tree)
- Iterative → ใช้ stack/queue **O(h) หรือ O(w)** (w = ความกว้างสูงสุด)
- Morris Traversal → เวลา O(n), space O(1)

### 5. Python ตัวอย่างโค้ด

```python
from collections import deque

class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

# Traversals
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

def level_order(root):
    if not root: return []
    res, q = [], deque([root])
    while q:
        u = q.popleft()
        res.append(u.key)
        if u.left: q.append(u.left)
        if u.right: q.append(u.right)
    return res

# ตัวอย่าง
A = Node('A'); B = Node('B'); C = Node('C')
D = Node('D'); E = Node('E'); F = Node('F')
A.left, A.right = B, C
B.left, B.right = D, E
C.right = F

out = []
preorder(A, out); print("Preorder  :", out)
out = []
inorder(A, out); print("Inorder   :", out)
out = []
postorder(A, out); print("Postorder :", out)
print("Levelorder:", level_order(A))
```

### 6. Properties ที่เกี่ยวข้อง

- **Height (h):** ระยะทาง edge ยาวสุดจาก root ถึง leaf
- **Depth:** ระยะทางจาก root ถึง node
- **Level i:** กลุ่ม node ที่ depth = i
- **สูตรพื้นฐาน:**
  - จำนวน node สูงสุดที่ level i = 2^i
  - จำนวน node ของ perfect tree = 2^{h+1} - 1
  - สำหรับ full/proper tree: L (leaf) = I (internal) + 1
- **Diameter:** ค่าที่ยาวที่สุดของ path ระหว่างสอง node ใด ๆ (คำนวณ O(n) ด้วย postorder)

### 7. Traversal → Reconstruction (uniqueness)

* Inorder + Preorder → **unique** binary tree (เมื่อ keys distinct)  
* Inorder + Postorder → **unique** binary tree (เมื่อ keys distinct)  
* Preorder + Postorder → โดยทั่วไป **ไม่ unique** (แต่จะ unique ถ้า tree เป็น full/proper)  
* สำหรับ BST: Preorder (หรือ Postorder) เดียวก็ reconstruct ได้โดยใช้ invariant ของ BST  

**ตัวอย่าง reconstruct (แนวคิด)**  
* Preorder ให้ root เป็นตัวแรก → หา index ใน inorder แบ่ง left/right subtrees → ทำซ้ำแบบ recursive  

### 8. Related Properties ของ Binary Trees (สำคัญ)

**นิยามพื้นฐาน**  
* Height (h): จำนวน edges จาก root ถึง leaf ที่ลึกที่สุด  
* Depth ของ node: จำนวน edges จาก root ถึง node นั้น  
* Level i: กลุ่ม node ที่ depth = i (root ที่ level 0)  

**สูตร/ความสัมพันธ์สำคัญ**  
* จำนวน node สูงสุดที่ level i = 2^i  
* จำนวน node ของ perfect tree สูงสุดเมื่อ height = h: n = 2^{h+1} - 1  
* สำหรับ tree ที่มี n node: minimum possible height ≈ ⌈log2(n+1)⌉ - 1  
* full/proper tree (ทุก internal node มี 2 ลูก): L (จำนวนใบ) = I (จำนวน internal) + 1; n = 2L - 1  
* complete tree: เติมจากซ้าย → ใช้ array index mapping (parent i ⇒ children 2i+1, 2i+2)  

**Diameter (เส้นทางยาวสุด)**  
* Diameter = max over nodes (height(left) + height(right))  
* คำนวณแบบ O(n) โดยใช้ postorder (คืน height และปรับค่า diameter ระหว่าง traversal)  

### 9. Implementations — Python Examples

* recursive, iterative, Morris สำหรับ inorder *

```python
from collections import deque

class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

# --- Recursive traversals ---
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

# --- Iterative variants ---
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

def preorder_iterative(root):
    if not root: return []
    res, stack = [], [root]
    while stack:
        node = stack.pop()
        res.append(node.key)
        if node.right: stack.append(node.right)
        if node.left:  stack.append(node.left)
    return res

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

def level_order(root):
    if not root: return []
    res, q = [], deque([root])
    while q:
        u = q.popleft()
        res.append(u.key)
        if u.left: q.append(u.left)
        if u.right: q.append(u.right)
    return res

# --- Morris Inorder (O(1) space) ---
def morris_inorder(root):
    res = []
    curr = root
    while curr:
        if not curr.left:
            res.append(curr.key)
            curr = curr.right
        else:
            pre = curr.left
            while pre.right and pre.right is not curr:
                pre = pre.right
            if not pre.right:
                pre.right = curr
                curr = curr.left
            else:
                pre.right = None
                res.append(curr.key)
                curr = curr.right
    return res

# --- Example tree ---
A = Node('A'); B = Node('B'); C = Node('C')
D = Node('D'); E = Node('E'); F = Node('F')
A.left, A.right = B, C
B.left, B.right = D, E
C.right = F

# Test
print('Preorder   :', (lambda: (lambda out: (preorder(A,out), out)[1])([]))())
print('Inorder    :', (lambda: (lambda out: (inorder(A,out), out)[1])([]))())
print('Postorder  :', (lambda: (lambda out: (postorder(A,out), out)[1])([]))())
print('Inorder itr:', inorder_iterative(A))
print('Preorder itr:', preorder_iterative(A))
print('Postorder 1stk:', postorder_one_stack(A))
print('Level-order:', level_order(A))
print('Morris Inorder:', morris_inorder(A))

```

---

## 🌀 Closest-Pair Problem

### 1. Concept / Purpose

Closest-Pair Problem คือการหาคู่จุด $(p_i, p_j)$ ที่ **ระยะห่างระหว่างกันน้อยที่สุด** ในชุดจุด 2D หรือ nD

เป็นพื้นฐานของงานด้าน **computational geometry**, เช่น:

* Clustering / finding nearest neighbors
* Collision detection ใน computer graphics
* Spatial analysis และ mapping

---

### 2. Problem Definition

* **Input:** ชุดของ n จุด $P = \{p_1, p_2, ..., p_n\}$ ใน 2D
* **Output:** คู่จุด $(p_i, p_j)$ ที่มีระยะ Euclidean สั้นที่สุด

**Distance Formula (2D):**

$$
d(p_i, p_j) = \sqrt{(x_i - x_j)^2 + (y_i - y_j)^2}
$$

**Brute-force Approach:**
ตรวจทุกคู่จุด → **O(n²)**

---

### 3. Divide & Conquer Approach

**Step-by-step:**

1. **Sort points by x-coordinate**
2. **Divide:** แบ่งจุดออกเป็นสองครึ่ง (Left, Right) ตาม median x
3. **Conquer:** หาคู่ใกล้สุดในแต่ละครึ่ง (recursively) → $d_L$, $d_R$
4. **Combine:**

   * ตรวจจุดที่อยู่ใกล้เส้นแบ่งในช่วง $\pm \delta$ (strip)
   * เฉพาะจุดใน strip ต้อง check ระยะใกล้สุด → O(n)
   * $\delta = \min(d_L, d_R)$

**Key Insight:**

* จุดใน strip แค่ check กับจุดใน strip ที่อยู่ไม่เกิน 7 จุดด้านบน/ล่าง (2D)
* ทำให้เวลา Combine เป็น O(n)

---

### 4. Visual Example (Step-by-step)

สมมติชุดจุดเล็ก ๆ:

```
Points: P = [(2,3), (12,30), (40,50), (5,1), (12,10), (3,4)]
```

**Step 1: Sort by x-coordinate**

```
Sorted by x: [(2,3), (3,4), (5,1), (12,10), (12,30), (40,50)]
```

**Step 2: Divide**

* Left half: \[(2,3), (3,4), (5,1)]
* Right half: \[(12,10), (12,30), (40,50)]

**Step 3: Conquer**

* Find closest in Left: (2,3) & (3,4) → distance = $\sqrt{2}$
* Find closest in Right: (12,10) & (12,30) → distance = 20

**Step 4: Combine**

* Minimum distance overall: $\delta = \min(d_L, d_R) = \min(\sqrt{2}, 20) = \sqrt{2}$
* Points in strip around median (x≈5\~12) → check pairs
* Closest pair in strip? (5,1) & (12,10) → distance > δ
* Result: closest pair = (2,3) & (3,4)

**ASCII Illustration:**

```
Y
50 |                             F(40,50)
30 |                     E(12,30)
20 |
10 |             D(12,10)
5  |
4  |     B(3,4)
3  | A(2,3)
1  |     C(5,1)
0  +--------------------------- X
   0   5   10  15  20  ...  40
```

---

### 5. Complexity

| Approach         | Time Complexity | Space Complexity                     |
| ---------------- | --------------- | ------------------------------------ |
| Brute-force      | O(n²)           | O(1)                                 |
| Divide & Conquer | O(n log n)      | O(n) (for sorted arrays / recursion) |

**Remarks:**

* Sorting points initially: O(n log n)
* Recursive divide & combine: O(n log n)
* Only check limited points in strip → constant factor

---

### 6. Python Implementation

```python
import math

def distance(p1, p2):
    return math.sqrt((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2)

# Brute-force
def closest_pair_brute(points):
    min_d = float('inf')
    pair = None
    n = len(points)
    for i in range(n):
        for j in range(i+1, n):
            d = distance(points[i], points[j])
            if d < min_d:
                min_d = d
                pair = (points[i], points[j])
    return pair, min_d

# Divide & Conquer
def closest_pair_dc(points):
    def _closest(Px, Py):
        n = len(Px)
        if n <= 3:
            return closest_pair_brute(Px)
        
        mid = n // 2
        Qx, Rx = Px[:mid], Px[mid:]
        midpoint = Px[mid][0]
        Qy = list(filter(lambda p: p[0] <= midpoint, Py))
        Ry = list(filter(lambda p: p[0] > midpoint, Py))
        
        (p1, q1), d1 = _closest(Qx, Qy)
        (p2, q2), d2 = _closest(Rx, Ry)
        delta = min(d1, d2)
        best_pair = (p1,q1) if d1 <= d2 else (p2,q2)
        
        # Build strip
        strip = [p for p in Py if abs(p[0]-midpoint) < delta]
        for i in range(len(strip)):
            for j in range(i+1, min(i+7, len(strip))):
                d = distance(strip[i], strip[j])
                if d < delta:
                    delta = d
                    best_pair = (strip[i], strip[j])
        return best_pair, delta
    
    Px = sorted(points, key=lambda x: x[0])
    Py = sorted(points, key=lambda x: x[1])
    return _closest(Px, Py)

# Example
points = [(2,3), (12,30), (40,50), (5,1), (12,10), (3,4)]
print("Brute-force:", closest_pair_brute(points))
print("Divide & Conquer:", closest_pair_dc(points))
```

---

## 💎 Convex-Hull Problem 

### 1. Concept / Purpose

Convex-Hull คือ **รูปหลายเหลี่ยม convex เล็กที่สุด** ที่ครอบจุดทั้งหมดในชุด P

เป็นพื้นฐานของงานด้าน computational geometry เช่น:

* การตรวจจับการชน (Collision detection)
* การวิเคราะห์รูปทรง / การรู้จำรูปแบบ (Pattern recognition)
* การวางแผนเส้นทางและ GIS

---

### 2. Problem Definition

* **Input:** ชุดของ n จุด $P = \{p_1, p_2, ..., p_n\}$ ใน 2D
* **Output:** ชุดจุดที่สร้าง **Convex Hull** ล้อมรอบทุกจุดใน P

**ตัวอย่างแนวคิดภาพรวม:**

```
Y
|
|       *E
|   *B       *D
|       *C
|*A
+---------------- X
```

* Convex hull จะเป็นรูปหลายเหลี่ยม A-B-D-E-A (เรียงตามลำดับ)
* จุด C อยู่ภายใน, ไม่อยู่บน hull

---

### 3. Properties of Convex Hull

* **Convex Polygon:** เส้นตรงระหว่างจุดสองจุดใด ๆ อยู่ภายใน polygon
* **Number of vertices:** ≤ n
* **Boundary:** จุดบน hull เป็น subset ของ P

---

### 4. Algorithms

**Common 2D Algorithms (O(n log n))**

1. **Graham’s Scan:**

   * จัดเรียงจุดตามมุมโพลาร์จาก pivot (จุด y ต่ำสุด)
   * เพิ่มจุดลง stack ตรวจสอบทิศทางการหมุน (cross product)
2. **Jarvis March (Gift Wrapping):**

   * เริ่มจากจุดซ้ายสุด
   * เลือกจุดต่อไปที่มุมโพลาร์น้อยที่สุด ทำซ้ำจนวนรอบ
   * ความซับซ้อน O(nh) (h = จำนวนจุดบน hull)
3. **Divide & Conquer:**

   * แบ่งจุด → คำนวณ hull ซ้าย/ขวา → รวมกัน
   * ความซับซ้อน O(n log n)

**Key Operations:**

* ใช้ cross product เพื่อตรวจสอบทิศทาง (เลี้ยวซ้าย, เลี้ยวขวา)

---

### 5. Orientation & Cross Product

สำหรับจุดสามจุด $p, q, r$:

$$
\text{orientation} = (q_x - p_x)(r_y - p_y) - (q_y - p_y)(r_x - p_x)
$$

* > 0 → เลี้ยวซ้าย
* \=0 → อยู่บนเส้นตรงเดียวกัน
* <0 → เลี้ยวขวา

---

### 6. Python Example (Graham’s Scan)

```python
def cross(o, a, b):
    return (a[0]-o[0])*(b[1]-o[1]) - (a[1]-o[1])*(b[0]-o[0])

def graham_scan(points):
    points = sorted(set(points))  # ลบจุดซ้ำ
    if len(points) <= 1:
        return points
    
    # สร้าง lower hull
    lower = []
    for p in points:
        while len(lower) >= 2 and cross(lower[-2], lower[-1], p) <= 0:
            lower.pop()
        lower.append(p)
    
    # สร้าง upper hull
    upper = []
    for p in reversed(points):
        while len(upper) >= 2 and cross(upper[-2], upper[-1], p) <= 0:
            upper.pop()
        upper.append(p)
    
    # รวม lower และ upper hull (ไม่รวมจุดซ้ำ)
    return lower[:-1] + upper[:-1]

# ตัวอย่าง
points = [(0,0), (1,1), (2,2), (2,0), (1,-1), (0,2)]
hull = graham_scan(points)
print("Convex Hull:", hull)
```

---

### 7. Complexity

| Algorithm        | Time Complexity |
| ---------------- | --------------- |
| Graham’s Scan    | O(n log n)      |
| Jarvis March     | O(nh)           |
| Divide & Conquer | O(n log n)      |

---

### 8. Notes / Insights

* จุดบน Convex Hull คือ **จุดขอบสุด (Extreme points)**
* ใช้ใน computational geometry สำหรับ **ตรวจจับการชน, การรู้จำรูปแบบ**
* Convex hull 3D: ซับซ้อนกว่า ใช้ QuickHull หรือ divide & conquer 3D

---

### 9. References / Related Concepts

* Computational Geometry: บท Convex-Hull
* Plane Sweep Algorithm
* k-d tree สำหรับ nearest neighbor
* CLRS, Section on Divide & Conquer Geometry







