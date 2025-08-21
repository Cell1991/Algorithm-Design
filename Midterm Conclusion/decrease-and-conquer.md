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

## 🔸 Johnson-Trotter Algorithm

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

### 5. Principle / How it works

* **หลักการคิด:**

  1. กำหนดทิศทางเริ่มต้นของแต่ละ element ให้ชี้ซ้าย
  2. หาตัวเลขที่ **mobile** (สามารถเลื่อนไปตามทิศทางโดยไม่ชนขอบหรือ element ที่ใหญ่กว่า) ที่มีค่ามากที่สุด
  3. สลับตำแหน่งตัวเลข mobile กับ neighbor ในทิศทางที่ชี้
  4. พลิกทิศทางของ element ที่มีค่ามากกว่าตัวเลข mobile ล่าสุด
  5. ทำซ้ำจนไม่มีตัวเลข mobile
* **Minimal-change:** permutation แต่ละตัวแตกต่างจากตัวก่อนหน้าด้วยการสลับเพียง 2 element เท่านั้น

### 6. Example

* **เริ่มต้น:** \[1, 2, 3] (ทิศทางทั้งหมดชี้ซ้าย)
* **Step 1:** largest mobile = 3 → swap 3 กับ 2 → \[1, 3, 2]
* **Step 2:** largest mobile = 3 → swap 3 กับ 1 → \[3, 1, 2]
* **Step 3:** largest mobile = 2 → swap 2 กับ 1 → \[3, 2, 1]
* **Step 4:** largest mobile = 3 → swap 3 กับ 2 → \[2, 3, 1]
* **Step 5:** largest mobile = 2 → swap 2 กับ 1 → \[2, 1, 3]
* **Step 6:** largest mobile = 3 → swap 3 กับ 1 → \[1, 2, 3] (กลับสู่ permutation เริ่มต้น)


* Generating permutations for testing all possibilities
* Simulations ที่ต้องลองทุก permutation
* Problems ที่ต้องการ minimal-change permutations

### 7. Pseudocode

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

### 8. Python Example

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
---

## 🔸 Lexicographic Order

### 1. Concept / Purpose

* Lexicographic order เป็น **วิธีการเรียงลำดับ sequence** (เช่น string, permutation, array) **เหมือนพจนานุกรม**
* หลักการ: เปรียบเทียบ element ตัวแรกของ sequence หากเท่ากัน ให้เปรียบเทียบตัวถัดไปจนกว่าจะเจอตัวที่ต่างกัน
* ใช้ในการ **generate permutations หรือ combinations ในลำดับที่ชัดเจน**

### 2. Motivation / Why use it

* ต้องการสร้าง sequence หรือ permutation ในลำดับที่ predictable และ deterministic
* ใช้งานได้ดีใน combinatorial problems, dictionary sorting, และ algorithms ที่ต้องการเรียงลำดับ
* ง่ายต่อการเชื่อมต่อกับ algorithms อื่น เช่น next\_permutation

### 3. Complexity Analysis

| Aspect | Complexity                            |
| ------ | ------------------------------------- |
| Time   | O(n!) for generating all permutations |
| Space  | O(n)                                  |

### 4. Use Cases

* Sorting strings ตาม dictionary order
* Generating all permutations in lexicographic order
* Next permutation problems in coding competitions
* Combinatorial enumeration problems

### 5. Principle / How it works

* **หลักการคิด:**

  1. เริ่มจาก permutation เริ่มต้นในลำดับน้อยสุด (เช่น 1,2,3,...,n)
  2. หาตัวเลขตัวขวาสุดที่ยังสามารถ swap กับตัวขวาของมันเพื่อสร้าง permutation ถัดไปในลำดับ
  3. Swap และ sort ตัวเลขที่เหลือทางด้านขวาเพื่อให้เรียงลำดับน้อยที่สุด
  4. ทำซ้ำจนได้ permutation มากที่สุด
* ทำให้ sequence ถูก generate **ตามลำดับ dictionary (lexicographically)**

### 6. Example

* **เริ่มต้น:** \[1, 2, 3]
* **Step 1:** swap 2 กับ 3 → \[1, 3, 2]
* **Step 2:** swap 1 กับ 2 → \[2, 1, 3]
* **Step 3:** swap 1 กับ 3 → \[2, 3, 1]
* **Step 4:** swap 3 กับ 1 → \[3, 1, 2]
* **Step 5:** swap 1 กับ 2 → \[3, 2, 1]
* Sequence ทั้งหมดเรียงตาม lexicographic order: \[1,2,3], \[1,3,2], \[2,1,3], \[2,3,1], \[3,1,2], \[3,2,1]

### 7. Pseudocode

```
procedure NextPermutation(array):
    i = length(array) - 2
    while i >= 0 and array[i] >= array[i+1]:
        i -= 1
    if i >= 0:
        j = length(array) - 1
        while array[j] <= array[i]:
            j -= 1
        swap(array[i], array[j])
    reverse(array[i+1:])
    return array
```

### 8. Python Example

```python
def next_permutation(arr):
    i = len(arr) - 2
    while i >= 0 and arr[i] >= arr[i+1]:
        i -= 1
    if i >= 0:
        j = len(arr) - 1
        while arr[j] <= arr[i]:
            j -= 1
        arr[i], arr[j] = arr[j], arr[i]
    arr[i+1:] = reversed(arr[i+1:])
    return arr

# Example usage
arr = [1,2,3]
for _ in range(5):
    print(arr)
    arr = next_permutation(arr)
# Output:
# [1, 2, 3]
# [1, 3, 2]
# [2, 1, 3]
# [2, 3, 1]
# [3, 1, 2]
# [3, 2, 1]
```


---

## 🔸 Binary Reflected Gray Code (BRGC)

### 1. Concept / Purpose

* Binary Reflected Gray Code เป็น **sequence ของ binary numbers** ที่มีความยาว n บิต
* จุดเด่น: **แต่ละตัวเลขต่างจากตัวก่อนหน้าด้วย 1 บิตเท่านั้น (single-bit change)**
* ใช้สำหรับการ **generate code หรือ state sequences ที่ minimal-change**
* เหมาะกับ hardware design, error correction, และ combinatorial generation

### 2. Motivation / Why use it

* ต้องการ sequence ที่ **เปลี่ยนค่าเพียงบิตเดียวต่อ step**
* ลดความผิดพลาดเมื่อเปลี่ยน state ใน digital circuits หรือ hardware
* ใช้ใน applications: Karnaugh maps, rotary encoders, analog to digital conversion

### 3. Complexity Analysis

| Aspect | Complexity |
| ------ | ---------- |
| Time   | O(2^n)     |
| Space  | O(2^n)     |

### 4. Use Cases

* Digital hardware sequencing
* Error correction codes
* Generating combinatorial objects with minimal-change
* Karnaugh maps optimization

### 5. Principle / How it works

* **หลักการคิด:**

  1. เริ่มต้นที่ 0 (all zeros)
  2. สร้าง Gray code ของ n-1 บิต
  3. เพิ่มบิตนำหน้า 0 ให้กับ sequence เดิม
  4. สะท้อน sequence เดิมแล้วเพิ่มบิตนำหน้า 1 สำหรับ reflected sequence
  5. ทำซ้ำจนได้ sequence ของ n บิต
* **Minimal-change:** แต่ละเลขใน sequence แตกต่างจากเลขก่อนหน้าด้วย **1 บิตเท่านั้น**

### 6. Example (3-bit Gray Code)

* **Step 0:** 0 → 000
* **Step 1:** 001
* **Step 2:** 011
* **Step 3:** 010
* **Step 4:** 110
* **Step 5:** 111
* **Step 6:** 101
* **Step 7:** 100
* Sequence ทั้งหมด: 000, 001, 011, 010, 110, 111, 101, 100

### 7. Pseudocode

```
procedure GrayCode(n):
    if n == 0:
        return [""]
    prev = GrayCode(n-1)
    result = []
    # Prefix 0
    for code in prev:
        result.append("0" + code)
    # Prefix 1 for reversed previous sequence
    for code in reversed(prev):
        result.append("1" + code)
    return result
```

### 8. Python Example

```python
def gray_code(n):
    if n == 0:
        return [""]
    prev = gray_code(n-1)
    result = []
    # Prefix 0
    result += ['0' + code for code in prev]
    # Prefix 1 for reversed previous sequence
    result += ['1' + code for code in reversed(prev)]
    return result

# Example usage
for code in gray_code(3):
    print(code)
# Output:
# 000
# 001
# 011
# 010
# 110
# 111
# 101
# 100
```

---

## 🔹 Binary Search

### 1. Concept / Purpose

* Binary Search เป็น **search algorithm** ที่ใช้สำหรับค้นหาค่าใน **sorted array**
* หลักการ: **แบ่งครึ่ง array** เพื่อลดพื้นที่ค้นหาอย่างรวดเร็ว
* ประหยัดเวลาในการค้นหาเมื่อเทียบกับ linear search

### 2. Motivation / Why use it

* ลดเวลาในการค้นหาในข้อมูลขนาดใหญ่
* ใช้งานได้ดีใน database, search engines, และ applications ที่ต้องค้นหาข้อมูลซ้ำๆ
* Efficiency สูงสำหรับ static datasets

### 3. Complexity Analysis

| Aspect | Complexity                          |
| ------ | ----------------------------------- |
| Time   | O(log n)                            |
| Space  | O(1) iterative / O(log n) recursive |

### 4. Use Cases

* ค้นหา element ใน sorted array
* Dictionary lookup
* Database index search
* Binary search in coding challenges, algorithmic problems

### 5. Principle / How it works

* **หลักการคิด:**

  1. กำหนด low = 0, high = n-1
  2. คำนวณ mid = (low + high) // 2
  3. เปรียบเทียบ target กับ array\[mid]

     * ถ้า target == array\[mid] → เจอแล้ว
     * ถ้า target < array\[mid] → search ในครึ่งซ้าย (high = mid - 1)
     * ถ้า target > array\[mid] → search ในครึ่งขวา (low = mid + 1)
  4. ทำซ้ำจน low > high หรือเจอ target
* ใช้ **divide and conquer** principle

### 6. Example

* Array = \[1, 3, 5, 7, 9, 11], target = 7
* Step 1: low=0, high=5, mid=2 → array\[2]=5 < 7 → search right half
* Step 2: low=3, high=5, mid=4 → array\[4]=9 > 7 → search left half
* Step 3: low=3, high=3, mid=3 → array\[3]=7 → เจอ target

### 7. Pseudocode

```
procedure BinarySearch(array, target):
    low = 0
    high = length(array) - 1
    while low <= high:
        mid = (low + high) // 2
        if array[mid] == target:
            return mid
        else if array[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1  # not found
```

### 8. Python Example

```python
def binary_search(array, target):
    low, high = 0, len(array) - 1
    while low <= high:
        mid = (low + high) // 2
        if array[mid] == target:
            return mid
        elif array[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1

# Example usage
arr = [1, 3, 5, 7, 9, 11]
target = 7
index = binary_search(arr, target)
print(index)  # Output: 3
```

---

## 🔹 Fake-Coin Problem

### 1. Concept / Purpose

* Fake-Coin Problem เป็น **classic combinatorial puzzle**
* ปัญหา: มีเหรียญ n เหรียญ หนึ่งเหรียญเป็น **fake coin** ที่น้ำหนักแตกต่างจากเหรียญจริง
* ต้องหาวิธี **หาตัวเหรียญปลอมด้วยจำนวนครั้งชั่งตาชั่งให้น้อยที่สุด**
* ใช้แนวคิด **logical deduction**

### 2. Motivation / Why use it

* ฝึกทักษะการวิเคราะห์และวางกลยุทธ์
* ใช้ในการเรียนรู้ **binary search แบบปรับปรุง** และ optimization problems
* พัฒนาความสามารถในการวางแผนและคิดแบบ combinatorial

### 3. Complexity Analysis

| Aspect | Complexity                             |
| ------ | -------------------------------------- |
| Time   | O(log\_3 n) (จำนวนครั้งชั่งน้อยที่สุด) |
| Space  | O(1) หรือ O(n) สำหรับเก็บเหรียญ        |

### 4. Use Cases

* Classic puzzle problems
* Training problem-solving and logical reasoning
* Optimization strategy for minimal tests

### 5. Principle / How it works

* **หลักการคิด:**

  1. แบ่งเหรียญทั้งหมดเป็น 3 กองเท่าๆ กัน
  2. ชั่ง 2 กองบนตาชั่ง

     * ถ้าสมดุล → เหรียญปลอมอยู่ในกองที่เหลือ
     * ถ้าเอียง → เหรียญปลอมอยู่ในกองที่เบาหรือหนักกว่า (ขึ้นอยู่กับเงื่อนไขของปัญหา)
  3. เลือกกองที่มีเหรียญปลอมและแบ่ง 3 กองใหม่
  4. ทำซ้ำจนเหลือ 1 เหรียญ → นั่นคือเหรียญปลอม
* ใช้ **divide and conquer 3-way** เพื่อลดจำนวนการชั่งให้น้อยที่สุด

### 6. Example

* มีเหรียญ 9 เหรียญ หนึ่งเหรียญปลอมที่เบากว่า
* **Step 1:** แบ่งเป็น 3 กอง กองละ 3 เหรียญ → ชั่งกอง A กับ B

  * สมดุล → เหรียญปลอมอยู่ในกอง C
  * เอียง → เหรียญปลอมอยู่กองที่เบากว่า
* **Step 2:** จากกองที่เลือก แบ่งเป็น 3 กอง กองละ 1 เหรียญ → ชั่ง 2 กอง
* **Step 3:** เหรียญที่เหลือไม่ต้องชั่ง คือเหรียญปลอม
* จำนวนชั่ง = 2 ครั้ง

### 7. Pseudocode

```
procedure FindFakeCoin(coins):
    while length(coins) > 1:
        Divide coins into 3 groups: G1, G2, G3
        result = weigh(G1, G2)
        if result == balanced:
            coins = G3
        else if G1 lighter or heavier depending on problem:
            coins = G1 or G2 accordingly
    return coins[0]  # fake coin
```

### 8. Python Example

```python
def find_fake_coin(coins, weigh):
    while len(coins) > 1:
        n = len(coins) // 3
        G1 = coins[:n]
        G2 = coins[n:2*n]
        G3 = coins[2*n:]
        result = weigh(G1, G2)  # function returns 'balanced', 'left', 'right'
        if result == 'balanced':
            coins = G3
        elif result == 'left':  # adjust according to problem (lighter/heavier)
            coins = G1
        else:
            coins = G2
    return coins[0]

# Example usage
coins = list(range(1,10))
# Define weigh function as needed, e.g., fake coin = 7, lighter
# find_fake_coin(coins, weigh)
```

---

## 🔹 Russian Peasant Multiplication

### 1. Concept / Purpose

* Russian Peasant Multiplication เป็น **algorithm สำหรับคูณตัวเลขสองจำนวน** โดยใช้การ **halve และ double**
* หลักการ: ลดการคูณใหญ่เป็นการบวกและการหารแบบง่าย ๆ
* ใช้แนวคิด **binary representation** ของตัวเลข

### 2. Motivation / Why use it

* ต้องการวิธีคูณแบบ efficient โดยไม่ใช้ multiplication operator
* ใช้งานได้ใน computing, embedded systems, หรือเมื่อคูณด้วยมือ
* เหมาะสำหรับการสอนวิธีคิดแบบ binary และ algorithmic thinking

### 3. Complexity Analysis

| Aspect | Complexity                        |
| ------ | --------------------------------- |
| Time   | O(log b) (b = ตัวเลขที่ถูก halve) |
| Space  | O(1) iterative                    |

### 4. Use Cases

* Multiplication without using \* operator
* Teaching binary representation and algorithmic thinking
* Embedded or low-level computing

### 5. Principle / How it works

* **หลักการคิด:**

  1. เขียนเลขสองจำนวน a และ b
  2. ทำการ halve ตัวเลขหนึ่ง (b) และ double อีกตัว (a)
  3. ถ้า b เป็นเลขคี่ ให้จด a ไว้
  4. ทำซ้ำจน b = 0
  5. บวกเลขทั้งหมดที่จดไว้ → ผลลัพธ์การคูณ
* ใช้ **bit manipulation** และการบวกแทนการคูณตรง ๆ

### 6. Example

* a = 18, b = 25
  \| a (double) | b (halve) | Record a if b odd |
  \|------------|------------|-----------------|
  \| 18         | 25         | 18              |
  \| 36         | 12         |                 |
  \| 72         | 6          |                 |
  \| 144        | 3          | 144             |
  \| 288        | 1          | 288             |
* Sum of recorded a: 18 + 144 + 288 = 450 → 18 \* 25 = 450

### 7. Pseudocode

```
procedure RussianPeasantMultiplication(a, b):
    result = 0
    while b > 0:
        if b is odd:
            result += a
        a = a * 2
        b = b // 2
    return result
```

### 8. Python Example

```python
def russian_peasant(a, b):
    result = 0
    while b > 0:
        if b % 2 == 1:
            result += a
        a *= 2
        b //= 2
    return result

# Example usage
a, b = 18, 25
print(russian_peasant(a, b))  # Output: 450
```

---

## 🔹 Josephus Problem

### 1. Concept / Purpose

* Josephus Problem เป็น **combinatorial problem** ที่เกี่ยวกับการลบคนในวงกลมตามกฎที่กำหนด
* ปัญหา: มี n คน ยืนเรียงเป็นวงกลม ลบทุก k-th คน จนเหลือคนสุดท้าย
* วัตถุประสงค์: หาตำแหน่งคนสุดท้ายที่รอดชีวิต
* ใช้แนวคิด **recursion / mathematical formula** ในการแก้ปัญหา

### 2. Motivation / Why use it

* ฝึกการคิดเชิง algorithmic และ mathematical reasoning
* ใช้ใน **simulation, circular linked list problems, recursion exercises**
* เป็นตัวอย่าง classic ของ **problem reduction** และ recursive formula

### 3. Complexity Analysis

| Aspect | Complexity                            |
| ------ | ------------------------------------- |
| Time   | O(n) iterative / O(n) recursive       |
| Space  | O(1) iterative / O(n) recursive stack |

### 4. Use Cases

* Classic algorithmic problem solving
* Circular data structures (linked list, queue) problems
* Recursive function practice
* Coding challenge and interview problems

### 5. Principle / How it works

* **หลักการคิด:**

  1. เริ่มจาก n คนในวงกลม
  2. นับทุก k-th คนแล้วลบออก
  3. ทำซ้ำจนเหลือคนสุดท้าย
  4. ใช้ **recursive relation:**

     * สำหรับ n คน และ step k, Josephus(n, k) = (Josephus(n-1, k) + k) % n
     * Base case: Josephus(1, k) = 0 (คนสุดท้ายคือ index 0)
* Concept: **problem reduction** → ลดขนาดวงกลมทีละ 1 จนเหลือ 1 คน

### 6. Example

* n = 7, k = 3
* People = \[1,2,3,4,5,6,7]
* Step by step elimination:

  1. นับ 3 → remove 3 → \[1,2,4,5,6,7]
  2. นับ 3 → remove 6 → \[1,2,4,5,7]
  3. นับ 3 → remove 2 → \[1,4,5,7]
  4. นับ 3 → remove 7 → \[1,4,5]
  5. นับ 3 → remove 5 → \[1,4]
  6. นับ 3 → remove 1 → \[4]
* คนสุดท้ายที่รอด = 4

### 7. Pseudocode

```
procedure Josephus(n, k):
    if n == 1:
        return 0
    else:
        return (Josephus(n-1, k) + k) % n
```

### 8. Python Example

```python
def josephus(n, k):
    if n == 1:
        return 0
    else:
        return (josephus(n-1, k) + k) % n

# Example usage
n, k = 7, 3
last_person_index = josephus(n, k)
print(last_person_index + 1)  # Output: 4 (index +1 for 1-based position)
```

---

## 🔹 Lomuto Partitioning

### 1. Concept / Purpose

* Lomuto Partitioning เป็น **partition scheme** ใช้ใน Quick Sort
* วัตถุประสงค์: แบ่ง array ออกเป็นสองส่วน

  * ส่วนที่มีค่า <= pivot
  * ส่วนที่มีค่า > pivot
* ช่วยให้ Quick Sort ทำงานแบบ **divide and conquer** ได้ง่ายขึ้น

### 2. Motivation / Why use it

* ต้องการ partition array ใน Quick Sort แบบเรียบง่ายและเข้าใจง่าย
* ใช้เพื่อศึกษาและฝึก algorithm design
* เหมาะสำหรับ educational purpose และ implementation ที่ไม่ซับซ้อน

### 3. Complexity Analysis

| Aspect | Complexity         |
| ------ | ------------------ |
| Time   | O(n) per partition |
| Space  | O(1) in-place      |

### 4. Use Cases

* Quick Sort implementation
* Partitioning problems
* Teaching basic algorithm and in-place sorting techniques

### 5. Principle / How it works

* **หลักการคิด:**

  1. เลือก pivot (มักใช้ element ตัวสุดท้ายของ array)
  2. ใช้ pointer i เพื่อ track ตำแหน่งสุดท้ายของ element <= pivot
  3. วนผ่าน array ด้วย pointer j:

     * ถ้า array\[j] <= pivot → swap array\[i] กับ array\[j], เพิ่ม i
  4. หลังจาก loop จบ → swap pivot กับ array\[i]
  5. pivot อยู่ในตำแหน่งสุดท้ายที่ถูกต้อง, array ถูก partition เรียบร้อย

### 6. Example

* Array = \[9, 3, 8, 5, 2], pivot = 2 (last element)
* i starts at 0
* Loop j:

  * j=0: 9 > 2 → do nothing
  * j=1: 3 > 2 → do nothing
  * j=2: 8 > 2 → do nothing
  * j=3: 5 > 2 → do nothing
* Swap pivot (2) with array\[i=0] → \[2,3,8,5,9]
* Partitioned array: left ≤ pivot (2), right > pivot

### 7. Pseudocode

```
procedure LomutoPartition(arr, low, high):
    pivot = arr[high]
    i = low
    for j = low to high - 1:
        if arr[j] <= pivot:
            swap arr[i], arr[j]
            i += 1
    swap arr[i], arr[high]
    return i  # pivot index
```

### 8. Python Example

```python
def lomuto_partition(arr, low, high):
    pivot = arr[high]
    i = low
    for j in range(low, high):
        if arr[j] <= pivot:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
    arr[i], arr[high] = arr[high], arr[i]
    return i

# Example usage
arr = [9, 3, 8, 5, 2]
pivot_index = lomuto_partition(arr, 0, len(arr)-1)
print(arr)        # Output: [2, 3, 8, 5, 9]
print(pivot_index) # Output: 0
```

---


