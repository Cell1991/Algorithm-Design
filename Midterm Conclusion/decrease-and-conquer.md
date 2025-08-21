## **2️⃣ [Decrease and Conquer](decrease-and-conquer.md)**
ลดขนาดของปัญหาแล้วแก้ทีละขั้น โดยแบ่งตามวิธีลดขนาด

### สารบัญ 

**2.1 ⬇️ Decrease by a Constant**  
ลดปัญหาแบบคงที่ทีละขั้น  

🔹 [Greatest Common Divisor (GCD)](#-greatest-common-divisor-gcd)  
🔹 [Insertion Sort](#-insertion-sort)  
🔹 [Topological Sorting (DFS)](#-topological-sorting-dfs)  
🔹 [Generating Permutations](#-generating-permutations)  

  🔸 [Minimal-change requirement](#-minimal-change-requirement)  
  🔸 [Johnson-Trotter algorithm](#-johnson-trotter-algorithm)  
  🔸 [Lexicographic order](#-lexicographic-order)  
  🔸 [Binary Reflected Gray Code *(แนวคิด Minimal Change)*](#-binary-reflected-gray-code-แนวคิด-minimal-change)

**2.2 🔽 Decrease by a Constant Factor**  
ลดปัญหาลงทีละสัดส่วน เช่น ครึ่งหนึ่งของขนาดเดิม  

🔹 [Binary Search](#-binary-search)  
🔹 [Fake-Coin Problem](#-fake-coin-problem)  
🔹 [Russian Peasant Multiplication](#-russian-peasant-multiplication)  
🔹 [Josephus Problem](#-josephus-problem)

**2.3 🔄 Variable Size Decrease**  
ลดปัญหาแบบไม่คงที่ ขึ้นกับเงื่อนไขหรือสถานการณ์  

🔹 [Lomuto Partitioning](#-lomuto-partitioning)  
🔹 [Quick Select](#-quick-select)  
🔹 [Interpolation Search](#-interpolation-search)  
🌳 [Binary Search Tree](#-binary-search-tree)

---
## 🔹 Greatest Common Divisor (GCD)

### 1. Concept / Purpose

**GCD (Greatest Common Divisor)** คือ **ตัวเลขจำนวนเต็มที่มากที่สุด** ที่สามารถหารจำนวนเต็มสองตัวหรือมากกว่านั้นลงตัว

* **ลักษณะ**: ปัญหาเชิงคณิตศาสตร์ / Number Theory
* **ประเภท**: Problem-solving / Decrease-and-Conquer
* **ข้อดี**: ช่วยในการลดเศษส่วน, คำนวณ LCM, แก้สมการ Diophantine
* **ข้อเสีย**: สำหรับวิธี brute-force จะ **ไม่ efficient** เมื่อจำนวนใหญ่

### 2. Mathematical Formulation

สำหรับจำนวนเต็ม $a$ และ $b$ (ไม่เป็นศูนย์ทั้งคู่):

$$
\text{GCD}(a, b) = \max \{ d \in \mathbb{Z}^+ \mid d \mid a \text{ and } d \mid b \}
$$

#### Euclidean Algorithm

ถ้า $a > b$:

$$
\text{GCD}(a, b) = \text{GCD}(b, a \bmod b)
$$

และ

$$
\text{GCD}(a, 0) = a
$$

### 3. Motivation / Why use it

* ใช้ในการ **ลดเศษส่วน** ให้เหลือน้อยที่สุด
* ใช้ในการคำนวณ **Least Common Multiple (LCM)**:

$$
\text{LCM}(a,b) = \frac{a \cdot b}{\text{GCD}(a,b)}
$$

* ใช้ในปัญหา **Number Theory**, **Cryptography**, และ **algorithm optimization**

### 4. Algorithm Steps (Euclidean)

1. รับจำนวนเต็ม $a$ และ $b$
2. ถ้า $b = 0$ → return $a$
3. คำนวณ $a \bmod b$
4. กำหนดค่าใหม่: $a \leftarrow b, b \leftarrow a \bmod b$
5. ทำซ้ำขั้นตอน 2–4 จนกว่า $b = 0$

### 5. Pseudocode

```
procedure GCD(a, b)
    while b ≠ 0 do
        temp ← b
        b ← a mod b
        a ← temp
    return a
end procedure
```

### 6. Python Example

```python
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

# Example usage
print(gcd(48, 18))  # Output: 6
```

### 7. Complexity Analysis

| Case  | Time Complexity | Explanation                                          |
| ----- | --------------- | ---------------------------------------------------- |
| Worst | O(log min(a,b)) | Euclidean algorithm จะลดค่าตัวเลขทุกขั้นอย่างรวดเร็ว |
| Space | O(1)            | ใช้ตัวแปรชั่วคราวในที่เดียว                          |

### 8. Use Cases

* ลด **fraction** ให้เหลือน้อยที่สุด: $\frac{48}{18} \rightarrow \frac{8}{3}$
* คำนวณ **LCM** ของจำนวนเต็มหลายตัว
* ปัญหา **Diophantine Equations**
* **Cryptography**, เช่น RSA Algorithm

---

## 🔹 Insertion Sort

### 1. Concept
**Insertion Sort** เป็นอัลกอริทึมการจัดเรียงที่ทำงานโดยการแทรกค่าทีละตัวเข้าไปในตำแหน่งที่เหมาะสมในลิสต์ที่เรียงแล้ว
เริ่มจากสมาชิกที่สอง และขยับค่าทางซ้ายไปเรื่อย ๆ เพื่อหาตำแหน่งที่ควรแทรก

- ลักษณะ: คล้ายการเรียงไพ่ในมือ
- ประเภท: **Comparison-based Sorting**
- ความเสถียร: **Stable** (ค่าที่เท่ากันจะไม่สลับลำดับเดิม)

### 2. Algorithm Steps
1. เริ่มจากตำแหน่งที่ 1 (ตัวที่สองของลิสต์)
2. เก็บค่าปัจจุบันไว้ในตัวแปรชั่วคราว (key)
3. เปรียบเทียบ key กับค่าก่อนหน้า ถ้าค่าก่อนหน้ามากกว่า key → เลื่อนค่าไปขวา
4. ทำซ้ำจนกว่าจะหาตำแหน่งที่เหมาะสม → แทรก key เข้าไป
5. ทำซ้ำขั้นตอน 1–4 จนครบทุกสมาชิก

### 3. Pseudocode
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

### 4. Python Example
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

### 5. Complexity Analysis
| Case       | Time Complexity | Explanation                              |
|------------|----------------|------------------------------------------|
| Best       | O(n)           | ลิสต์เรียงอยู่แล้ว → ไม่มีการเลื่อนค่า |
| Average    | O(n²)          | ต้องเลื่อนค่าทุกตัวหลายรอบ              |
| Worst      | O(n²)          | ลิสต์เรียงแบบตรงข้ามทั้งหมด              |
| Space      | O(1)           | ใช้พื้นที่ในลิสต์เดิม (In-place)        |

### 6. Use Cases
- เหมาะกับ **ข้อมูลขนาดเล็ก** ที่ต้องการความเรียบง่าย
- ดีสำหรับข้อมูลที่เกือบเรียงอยู่แล้ว (Nearly Sorted)
- ใช้ใน Embedded Systems หรือระบบที่ไม่สามารถใช้หน่วยความจำมาก

### 7. Visualization (Shift Highlight)

### Initial
[5, 3, 8, 4, 2]


#### Pass 1 (i=1, key=3)
- เปรียบเทียบ 5 กับ 3 → เลื่อน 5 ไปขวา → แทรก 3 → [3, 5, 8, 4, 2]

#### Pass 2 (i=2, key=8)
- 8 > 5 → ไม่ต้องเลื่อน → [3, 5, 8, 4, 2]

#### Pass 3 (i=3, key=4)
- เลื่อน 8 → 5 → แทรก 4 → [3, 4, 5, 8, 2]

#### Pass 4 (i=4, key=2)
- เลื่อน 8 → 5 → 4 → 3 → แทรก 2 → [2, 3, 4, 5, 8]

✅ **Sorted Result:** [2, 3, 4, 5, 8]


### 🎥 ดูวิดีโอบน YouTube  
🔗 https://www.youtube.com/watch?v=Q1JdRUh1_98

---

## 🔹 Topological Sorting (DFS)

### 1. Concept / Purpose
**Topological Sorting** คือการจัดเรียงลำดับของ **Directed Acyclic Graph (DAG)**  
โดยที่ถ้ามีเส้นเชื่อม $u \to v$ จะต้องให้ $u$ อยู่ก่อน $v$ เสมอ  

- **ลักษณะ**: ใช้กับ DAG เท่านั้น  
- **ประเภท**: Graph Algorithm / Decrease-and-Conquer  
- **ข้อดี**: ใช้เป็นพื้นฐานในการจัดการ dependency เช่น scheduling, compilation  
- **ข้อเสีย**: ใช้ไม่ได้ถ้า graph มี cycle  

### 2. Mathematical Formulation
สำหรับ Directed Acyclic Graph $G = (V, E)$  
Topological order คือ ลำดับ $v_1, v_2, \dots, v_n$ ที่ทำให้  

$$
\forall (u,v) \in E \quad \Rightarrow \quad \text{pos}(u) < \text{pos}(v)
$$

โดยที่ $\text{pos}(x)$ = ตำแหน่งของ $x$ ในลำดับ

### 3. Motivation / Why use it
- **Scheduling**: เช่น งานที่ต้องทำงานก่อนหลังกัน  
- **Compilation order**: โปรแกรมที่มี dependency ระหว่าง module  
- **Course prerequisite**: ลำดับการลงทะเบียนเรียน  
- **Build systems**: เช่น `make`, `npm`, `maven`  

### 4. Algorithm Steps (DFS-based)
1. เริ่มจาก node ที่ยังไม่ได้เยี่ยมชม  
2. ทำ DFS ไปยังทุก neighbor  
3. เมื่อเยี่ยมชม node เสร็จ → push node เข้า stack (หรือ append ที่ต้นลิสต์)  
4. ทำซ้ำจนกว่าจะครบทุก node  
5. ลำดับใน stack ที่ได้คือ **Topological Order**

### 5. Pseudocode
```
procedure TopologicalSortDFS(G):
    mark all vertices as unvisited
    stack ← empty
    
    for each vertex v in G do
        if v is unvisited then
            DFS(v, stack)

    return reverse(stack)

procedure DFS(v, stack):
    mark v as visited
    for each neighbor u of v do
        if u is unvisited then
            DFS(u, stack)
    push v onto stack
```

### 6. Python Example
```python
from collections import defaultdict

def topological_sort_dfs(graph):
    visited = set()
    stack = []

    def dfs(v):
        visited.add(v)
        for neighbor in graph[v]:
            if neighbor not in visited:
                dfs(neighbor)
        stack.append(v)

    for node in graph:
        if node not in visited:
            dfs(node)

    return stack[::-1]  # reverse for correct order

# Example usage
graph = {
    "A": ["C"],
    "B": ["C", "D"],
    "C": ["E"],
    "D": ["F"],
    "E": ["H", "F"],
    "F": ["G"],
    "G": [],
    "H": []
}

print(topological_sort_dfs(graph))
# Possible Output: ['B', 'D', 'A', 'C', 'E', 'H', 'F', 'G']
```

### 7. Complexity Analysis
| Case       | Time Complexity | Explanation                      |
|------------|----------------|----------------------------------|
| All cases  | O(V + E)       | DFS ต้องเยี่ยมทุก node และ edge  |
| Space      | O(V)           | recursion stack + visited + output |

### 8. Use Cases
- การจัดลำดับงานที่มี **dependency**  
- การคำนวณ **compilation order** ของไฟล์ source code  
- การแก้ปัญหา **course prerequisite**  
- การวิเคราะห์ **dependency resolution** ในระบบ build  

### 9. Visualization (Example Graph)
```
B → C → E → F → G
A ─┘     ↓
        H
D ──────┘
```

✅ Topological Order (หนึ่งในคำตอบ):  
`[B, D, A, C, E, H, F, G]`


