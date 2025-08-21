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

---

## 🔹 Generating Permutations  

### 1. Concept / Purpose  
**Permutation** คือ **การจัดเรียงลำดับ** ของสมาชิกในเซตหนึ่ง ๆ โดยไม่ซ้ำกัน  
การสร้าง permutation เป็นพื้นฐานใน **Combinatorics**, **Backtracking Algorithms**, และการแก้ปัญหา optimization  

- **ลักษณะ**: สร้างทุกการจัดเรียงที่เป็นไปได้  
- **ประเภท**: Recursive / Backtracking  
- **ข้อดี**: ครอบคลุมทุกความเป็นไปได้ ใช้เป็น baseline หรือ brute-force solution ได้  
- **ข้อเสีย**: **ไม่ efficient** เมื่อ n มีค่ามาก เพราะจำนวน permutation คือ $n!$  

### 2. Mathematical Formulation  
สำหรับเซต $S = \{1,2,\dots,n\}$  

จำนวนการจัดเรียง (Permutation) ของ $n$ องค์ประกอบ:  

$$
P(n) = n!
$$

เช่น สำหรับ $n = 3$:  
$\{1,2,3\} \rightarrow \{123,132,213,231,312,321\}$  

### 3. Motivation / Why use it  
- ใช้ใน **Combinatorial Problems** เช่น Traveling Salesman Problem (TSP)  
- ใช้ใน **Cryptography และ Security**  
- ใช้ใน **Testing / Simulation** (เช่น exhaustive input ordering)  
- พื้นฐานของ **Backtracking Algorithm**  

### 4. Algorithm Steps (Backtracking)  
1. เริ่มจากลิสต์ที่ยังว่างเปล่า  
2. เลือกสมาชิกที่ยังไม่ได้ใช้ ใส่ลงไปในลิสต์  
3. ทำซ้ำโดยการเรียก recursive function  
4. เมื่อได้ลิสต์ยาว $n$ → บันทึกเป็นหนึ่ง permutation  
5. Backtrack กลับเพื่อลองทางเลือกอื่น  

### 5. Pseudocode  
```
procedure generatePermutation(A, chosen, used)
    if length(chosen) = length(A) then
        output chosen
    else
        for each element x in A do
            if not used[x] then
                mark used[x] = true
                append x to chosen
                generatePermutation(A, chosen, used)
                remove last element from chosen
                mark used[x] = false
end procedure
```  

### 6. Python Example  
```python
def generate_permutations(arr, path=None, used=None):
    if path is None:
        path = []
    if used is None:
        used = [False] * len(arr)

    if len(path) == len(arr):
        print(path)
        return

    for i in range(len(arr)):
        if not used[i]:
            used[i] = True
            generate_permutations(arr, path + [arr[i]], used)
            used[i] = False

# Example usage
generate_permutations([1, 2, 3])
# Output:
# [1, 2, 3]
# [1, 3, 2]
# [2, 1, 3]
# [2, 3, 1]
# [3, 1, 2]
# [3, 2, 1]
```

### 7. Complexity Analysis  
| Case  | Time Complexity | Explanation                                   |
| ----- | --------------- | --------------------------------------------- |
| All   | O(n · n!)       | มีทั้งหมด $n!$ permutations และแต่ละ permutation ใช้เวลา O(n) |
| Space | O(n)            | recursion stack + used array                  |

### 8. Use Cases  
- แก้ปัญหา **TSP ขนาดเล็ก**  
- สร้าง **test cases** ครอบคลุมทุกการเรียงลำดับ  
- ปัญหา **puzzle / game state** เช่น 8-puzzle  
- ใช้ใน **brute-force search** หรือ algorithm design  

---

# 🔸 Minimal-change Requirement

### 1. Concept / Purpose

**Minimal-change Requirement** คือแนวคิดในการ **สร้าง permutation ต่อเนื่องกันโดยเปลี่ยน element น้อยที่สุด**
เปรียบเทียบกับการสร้าง permutation แบบธรรมดาที่อาจสลับหลายตำแหน่งระหว่าง permutation

- **ลักษณะ**: Combinatorial / Algorithmic Problem
- **ประเภท**: Problem-solving / Permutation Generation
- **ข้อดี**: ลดจำนวนการเปลี่ยนแปลงระหว่าง permutation → ดีสำหรับ hardware, animation, Gray code
- **ข้อเสีย**: อัลกอริทึมซับซ้อนกว่าการสร้าง permutation แบบ brute-force

### 2. Motivation / Why use it

- ใช้ในการ **hardware testing** เพื่อเปลี่ยน state ทีละน้อย
- ใช้ใน **Gray code generation**
- ลด **computational cost** ของการสลับหลายตำแหน่งพร้อมกัน
- เหมาะสำหรับ **animation / visual simulation** ที่ต้องการ transition ละเอียด

### 3. Complexity Analysis

| Case       | Time Complexity | Explanation                              |
|------------|----------------|------------------------------------------|
| Generation | O(n!)          | ต้องสร้างทุก permutation ของ n elements |
| Space      | O(n)           | ใช้ recursion stack หรือ temporary array |

### 4. Use Cases

- Gray code generation
- Hardware / circuit testing
- Stepwise animation / simulation
- Minimizing changes in combinatorial enumeration

### 5. Pseudocode (Johnson-Trotter Algorithm Concept)

```
procedure minimalChangePermutation(arr)
    initialize direction of each element to LEFT
    repeat
        output current permutation
        find largest mobile element k
        if no mobile element exists then exit
        swap k with adjacent element in its direction
        reverse direction of all elements larger than k
end procedure
```

### 6. Python Example (Simplified Johnson-Trotter)

```python
def minimal_change_permutation(arr):
    n = len(arr)
    dir = [-1] * n  # -1 = LEFT, 1 = RIGHT
    def largest_mobile():
        mobile = -1
        idx = -1
        for i in range(n):
            if dir[i] == -1 and i != 0 and arr[i] > arr[i-1]:
                if arr[i] > mobile:
                    mobile = arr[i]
                    idx = i
            elif dir[i] == 1 and i != n-1 and arr[i] > arr[i+1]:
                if arr[i] > mobile:
                    mobile = arr[i]
                    idx = i
        return idx
    while True:
        print(arr)
        i = largest_mobile()
        if i == -1:
            break
        swap_with = i + dir[i]
        arr[i], arr[swap_with] = arr[swap_with], arr[i]
        dir[i], dir[swap_with] = dir[swap_with], dir[i]
        k = arr[swap_with]
        for j in range(n):
            if arr[j] > k:
                dir[j] *= -1

# Example usage
minimal_change_permutation([1,2,3])
```

---

## 🧩 Johnson-Trotter Algorithm

### 1. Concept / Purpose

* Johnson-Trotter เป็น **algorithm สำหรับ generating all permutations ของ n element**
* จุดเด่น: **minimal-change requirement** → แต่ละ permutation ต่างจากตัวก่อนหน้าด้วยการสลับ element แค่ 2 ตัว
* ใช้แนวคิดของ **mobile integers** (ตัวเลขที่ยังสามารถสลับได้ไปทางที่ชี้) เพื่อสร้าง permutation ต่อไป

### 2. Motivation / Why use it

* ต้องการ generate permutation โดย **เปลี่ยนให้น้อยที่สุดในแต่ละ step**
* เหมาะกับการสร้าง permutation สำหรับ **backtracking, simulation, หรือ testing**
* มีประสิทธิภาพสำหรับ n เล็กถึงกลาง

### 3. Complexity Analysis

| Aspect | Complexity |
| ------ | ---------- |
| Time   | O(n!)      |
| Space  | O(n)       |

### 4. Use Cases

* Generating permutations for testing all possibilities
* Simulations ที่ต้องลองทุก permutation
* Problems ที่ต้องการ minimal-change permutations

### 5. Pseudocode

```
procedure JohnsonTrotter(n):
    Initialize permutation P = [1, 2, ..., n]
    Set all directions to LEFT
    while there is a mobile integer:
        Find the largest mobile integer k
        Swap k with the adjacent element in its direction
        Reverse direction of all integers larger than k
        Output current permutation
```

### 6. Python Example

```python
# Johnson-Trotter Algorithm implementation
def johnson_trotter(n):
    perm = list(range(1, n+1))
    # Initialize directions (-1 means LEFT, 1 means RIGHT)
    dir = [-1] * n

    def mobile():
        m = -1
        idx = -1
        for i in range(n):
            neighbor = i + dir[i]
            if 0 <= neighbor < n and perm[i] > perm[neighbor]:
                if perm[i] > m:
                    m = perm[i]
                    idx = i
        return idx

    while True:
        print(perm)
        idx = mobile()
        if idx == -1:
            break
        # Swap with neighbor in direction
        neighbor = idx + dir[idx]
        perm[idx], perm[neighbor] = perm[neighbor], perm[idx]
        dir[idx], dir[neighbor] = dir[neighbor], dir[idx]
        idx = neighbor
        # Reverse direction of all elements greater than perm[idx]
        for i in range(n):
            if perm[i] > perm[idx]:
                dir[i] *= -1

# Example usage
johnson_trotter(3)
# Output:
# [1, 2, 3]
# [1, 3, 2]
# [3, 1, 2]
# [3, 2, 1]
# [2, 3, 1]
# [2, 1, 3]
```

