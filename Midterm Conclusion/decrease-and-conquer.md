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

Topological Sorting คือการ **เรียงลำดับจุดยอด (vertices)** ของ
**Directed Acyclic Graph (DAG)**\
โดยต้องเรียงให้ **ทุกเส้นทาง (u → v)** มี `u` อยู่ก่อน `v` ในลำดับ

-   **ลักษณะ** ใช้ได้เฉพาะ DAG เท่านั้น\
-   **ประเภท** Graph algorithm\
-   **ข้อดี** ใช้เป็นพื้นฐานในหลายปัญหา เช่น scheduling, dependency
    resolution\
-   **ข้อเสีย** ใช้ไม่ได้ถ้าเป็นกราฟที่มี cycle

------------------------------------------------------------------------

### 2. Motivation / Why use it

-   ใช้ในการ **จัดลำดับงานที่มี dependency** (เช่น
    งานที่ต้องทำก่อนหลัง)\
-   ใช้เป็นพื้นฐานในอัลกอริทึมอื่น เช่น **Critical Path Method**,
    **Course Scheduling**\
-   ใช้ช่วยแก้ปัญหาที่เกี่ยวกับ **การจัดลำดับ dependency**

------------------------------------------------------------------------

### 3. Algorithm Idea (DFS Approach)

1.  ใช้ DFS เดินทางในกราฟ\
2.  เมื่อเยี่ยมครบทุกเพื่อนบ้านของ vertex แล้ว ให้ **push vertex เข้าสู่
    stack**\
3.  หลัง DFS ครบทุก node → pop stack ออกมาจะได้ topological order

------------------------------------------------------------------------

### 4. Pseudocode

    procedure topologicalSortDFS(G):
        visited ← set()
        stack ← empty
        
        for each vertex v in G:
            if v not in visited:
                DFS(v, visited, stack)
        
        return reverse(stack)

    procedure DFS(v, visited, stack):
        mark v as visited
        for each neighbor u of v:
            if u not in visited:
                DFS(u, visited, stack)
        push v into stack

------------------------------------------------------------------------

### 5. Python Example

``` python
from collections import defaultdict

class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        self.graph[u].append(v)

    def topological_sort_util(self, v, visited, stack):
        visited[v] = True
        for neighbor in self.graph[v]:
            if not visited[neighbor]:
                self.topological_sort_util(neighbor, visited, stack)
        stack.append(v)

    def topological_sort(self):
        visited = [False] * self.V
        stack = []
        for i in range(self.V):
            if not visited[i]:
                self.topological_sort_util(i, visited, stack)
        return stack[::-1]

# Example
g = Graph(6)
g.add_edge(5, 2)
g.add_edge(5, 0)
g.add_edge(4, 0)
g.add_edge(4, 1)
g.add_edge(2, 3)
g.add_edge(3, 1)

print("Topological Sort:", g.topological_sort())
```

------------------------------------------------------------------------

### 6. Complexity Analysis

  Case        Time Complexity   Explanation
  ----------- ----------------- ---------------------------------
  All cases   O(V + E)          DFS ต้องเยี่ยมทุก vertex + edge
  Space       O(V)              เก็บ visited + recursion stack

------------------------------------------------------------------------

### 7. Use Cases

-   **Scheduling งาน** ที่มี dependency (เช่น วิชาที่ต้องเรียนตามลำดับ)\
-   **Task dependency resolution** ในระบบ build tools (เช่น Makefile,
    Gradle)\
-   **การจัดการลำดับงาน** ใน compiler หรือ job scheduler

------------------------------------------------------------------------


