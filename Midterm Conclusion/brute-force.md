 # 1️⃣ Brute Force

วิธีแก้ปัญหาแบบตรงไปตรงมา ลองทุกความเป็นไปได้ 

### สารบัญ
[⚡ Exhaustive Search](#-exhaustive-search)  
[🔹 Bubble Sort](#-bubble-sort)  
[🔹 Selection Sort](#-selection-sort)  
[🔹 Sequential Search](#-sequential-search)  
[🔹 Brute-force String Matching](#-brute-force-string-matching)  
[🔹 Closest-Pair Problem](#-closest-pair-problem)  
[🔹 Convex-Hull Problem](#-convex-hull-problem)  
[🗺️ Traveling Salesman Problem](#-traveling-salesman-problem)  
[🎒 Knapsack Problem](#-knapsack-problem)  
[📝 Assignment Problem](#-assignment-problem)  
[🌲 Depth-First Search DFS](#-depth-first-search-dfs)
[🌳 Breadth-First Search BFS](#-breadth-first-search-bfs)


---

## ⚡ Exhaustive Search

### 1. Concept / Purpose  
Exhaustive Search (หรือ Brute-force Search) เป็น **แนวคิดการแก้ปัญหาแบบตรงไปตรงมา**  
โดยการ **ตรวจสอบทุกความเป็นไปได้** เพื่อหา solution ที่ถูกต้อง  

- ** ลักษณะ** ตรวจทุก candidate solution โดยไม่มีการคาดเดาหรือ optimization  
- ** ประเภท** Problem-solving strategy  
- ** ข้อดี** เข้าใจง่าย, implementation ไม่ซับซ้อน  
- ** ข้อเสีย** **ไม่ efficient** สำหรับปัญหาขนาดใหญ่  

### 2. Motivation / Why use it
- เหมาะสำหรับปัญหาที่ **ขนาดเล็ก** หรือจำนวนความเป็นไปได้จำกัด  
- เป็นวิธี **baseline** เพื่อเปรียบเทียบ algorithm ที่ซับซ้อนกว่า  
- ใช้ตรวจสอบ **correctness ของ solution**  

### 3. Complexity Analysis
| Case       | Time Complexity | Explanation                                        |
|------------|----------------|---------------------------------------------------|
| All cases  | O(n^k)         | ต้องตรวจทุก combination ของ candidate solutions |
| Space      | O(1) หรือ O(n) | ขึ้นกับการเก็บ candidate หรือ recursion stack   |

> **💡 หมายเหตุ** n = จำนวน element, k = จำนวนที่เลือกต่อครั้ง (เช่นคู่, triple)  

### 4. Use Cases
- ปัญหา **TSP ขนาดเล็ก** (Traveling Salesman Problem)  
- **Knapsack Problem** ขนาดเล็ก  
- การค้นหา **string matching** แบบ brute-force  
- ตรวจสอบ **graph paths** หรือ **combinatorial problems**  

### 5. General Pseudocode
```text
procedure exhaustiveSearch(problem)
    best_solution ← null
    best_value ← -∞
    
    for each candidate in all_possible_solutions(problem) do
        if is_valid(candidate) then
            value ← evaluate(candidate)
            if value > best_value then
                best_value ← value
                best_solution ← candidate
    return best_solution
end procedure
```
---

## 🔹 Bubble Sort
### 1. Concept
**Bubble Sort** เป็นอัลกอริทึมการจัดเรียงแบบง่าย (Simple Sorting Algorithm)  
ทำงานโดยการ **เปรียบเทียบ** องค์ประกอบที่อยู่ติดกัน (Adjacent Elements) และ **สลับตำแหน่ง** ถ้าลำดับไม่ถูกต้อง  
ทำซ้ำหลายรอบจนกว่าลิสต์จะเรียงสมบูรณ์

- ลักษณะ: เปรียบเทียบทีละคู่เหมือนฟองอากาศลอยขึ้นไปด้านบน
- ประเภท: **Comparison-based Sorting**
- ความเสถียร: **Stable** (ค่าที่เท่ากันจะไม่สลับลำดับเดิม)

### 2. Algorithm Steps
1. เริ่มจากตำแหน่งแรกของลิสต์
2. เปรียบเทียบคู่ของค่าที่อยู่ติดกัน
3. ถ้าค่าด้านซ้าย > ค่าด้านขวา → สลับตำแหน่ง
4. เลื่อนไปยังคู่ถัดไป
5. หลังจากรอบแรก ค่ามากที่สุดจะอยู่ท้ายสุด
6. ทำซ้ำขั้นตอน 1–5 โดย **ลดจำนวนการเปรียบเทียบลงทีละ 1** ในแต่ละรอบ
7. หยุดเมื่อไม่มีการสลับตำแหน่งเกิดขึ้นในรอบหนึ่ง

### 3. Pseudocode
```
procedure bubbleSort(A)
    n ← length(A)
    repeat
        swapped ← false
        for i ← 0 to n-2 do
            if A[i] > A[i+1] then
                swap A[i], A[i+1]
                swapped ← true
        n ← n - 1
    until swapped = false
end procedure
```

### 4. Python Example
```python
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr

# Example usage
data = [5, 3, 8, 4, 2]
sorted_data = bubble_sort(data)
print(sorted_data)  # Output: [2, 3, 4, 5, 8]
```

### 5. Complexity Analysis
| Case       | Time Complexity | Explanation                              |
|------------|----------------|------------------------------------------|
| Best       | O(n)           | ลิสต์เรียงอยู่แล้ว → หยุดทันที          |
| Average    | O(n²)          | ต้องเปรียบเทียบและสลับหลายรอบ           |
| Worst      | O(n²)          | ลิสต์เรียงแบบตรงข้ามทั้งหมด              |
| Space      | O(1)           | ใช้การสลับตำแหน่งในที่เดิม (In-place)   |

### 6. Use Cases
- เหมาะกับ **ข้อมูลขนาดเล็ก** ที่ไม่ต้องการประสิทธิภาพสูง
- ใช้สอนพื้นฐานการคิดเชิงอัลกอริทึม
- ใช้ในระบบที่ความง่ายสำคัญกว่าความเร็ว

### 7. Visualization (Swap Highlight)

#### Initial
[5, 3, 8, 4, 2]

### Pass 1
- 🟢 Step 1: Compare 5 & 3 → swap → [3, 5, 8, 4, 2]  
- 🔴 Step 2: Compare 5 & 8 → no swap → [3, 5, 8, 4, 2]  
- 🟢 Step 3: Compare 8 & 4 → swap → [3, 5, 4, 8, 2]  
- 🟢 Step 4: Compare 8 & 2 → swap → [3, 5, 4, 2, 8]

### Pass 2
- 🔴 Step 1: Compare 3 & 5 → no swap → [3, 5, 4, 2, 8]  
- 🟢 Step 2: Compare 5 & 4 → swap → [3, 4, 5, 2, 8]  
- 🟢 Step 3: Compare 5 & 2 → swap → [3, 4, 2, 5, 8]

### Pass 3
- 🔴 Step 1: Compare 3 & 4 → no swap → [3, 4, 2, 5, 8]  
- 🟢 Step 2: Compare 4 & 2 → swap → [3, 2, 4, 5, 8]

### Pass 4
- 🟢 Step 1: Compare 3 & 2 → swap → [2, 3, 4, 5, 8]

✅ **Sorted Result:** [2, 3, 4, 5, 8]

### 🎥 ดูวิดีโอบน YouTube  
🔗 https://www.youtube.com/watch?v=hahrx5WUeNI

---


## 🔹 Selection Sort

### 1. Concept
**Selection Sort** เป็นอัลกอริทึมการจัดเรียงที่ทำงานโดยการเลือกค่าที่น้อยที่สุดจากส่วนที่ยังไม่ได้เรียง แล้วนำไปไว้ตำแหน่งต้นของลิสต์ที่ยังไม่ได้จัดเรียง

- ลักษณะ: เลือกค่าต่ำสุด/สูงสุดแล้ววางไว้ข้างหน้า
- ประเภท: **Comparison-based Sorting**
- ความเสถียร: **Unstable** (แต่สามารถปรับให้ stable ได้)

### 2. Algorithm Steps
1. เริ่มจากตำแหน่งแรกของลิสต์ (index 0)
2. หาค่าที่น้อยที่สุดจากตำแหน่งปัจจุบันจนถึงตัวสุดท้าย
3. สลับค่าที่น้อยที่สุดกับตำแหน่งปัจจุบัน
4. ขยับตำแหน่งไปทางขวาทีละ 1 แล้วทำซ้ำจนสุดลิสต์

### 3. Pseudocode
```
procedure selectionSort(A)
    for i ← 0 to length(A)-2 do
        minIndex ← i
        for j ← i+1 to length(A)-1 do
            if A[j] < A[minIndex] then
                minIndex ← j
        swap A[i], A[minIndex]
end procedure
```

### 4. Python Example
```python
def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

# Example usage
data = [5, 3, 8, 4, 2]
sorted_data = selection_sort(data)
print(sorted_data)  # Output: [2, 3, 4, 5, 8]
```

### 5. Complexity Analysis
| Case       | Time Complexity | Explanation                              |
|------------|----------------|------------------------------------------|
| Best       | O(n²)          | ต้องเปรียบเทียบทั้งหมดแม้เรียงแล้ว      |
| Average    | O(n²)          | ทำ n(n-1)/2 comparisons                   |
| Worst      | O(n²)          | ลิสต์เรียงแบบตรงข้ามทั้งหมด              |
| Space      | O(1)           | สลับในที่เดิม (In-place)                 |

### 6. Use Cases
- เหมาะกับ **ข้อมูลขนาดเล็ก** หรือข้อมูลที่ swap มีต้นทุนสูง
- เข้าใจง่าย ใช้สอนเบื้องต้นได้ดี
- มีจำนวนครั้งในการ swap ต่ำสุดในกลุ่ม comparison-based sorting

### 7. Visualization (Min Selection)

### Initial
[5, 3, 8, 4, 2]

#### Pass 1 (i=0)
- หาค่าน้อยสุดใน [5, 3, 8, 4, 2] → 2 → สลับกับ 5 → [2, 3, 8, 4, 5]

#### Pass 2 (i=1)
- หาค่าน้อยสุดใน [3, 8, 4, 5] → 3 → ไม่ต้องสลับ → [2, 3, 8, 4, 5]

#### Pass 3 (i=2)
- หาค่าน้อยสุดใน [8, 4, 5] → 4 → สลับกับ 8 → [2, 3, 4, 8, 5]

#### Pass 4 (i=3)
- หาค่าน้อยสุดใน [8, 5] → 5 → สลับกับ 8 → [2, 3, 4, 5, 8]

✅ **Sorted Result:** [2, 3, 4, 5, 8]

### 🎥 ดูวิดีโอบน YouTube  
🔗 https://www.youtube.com/watch?v=Iccmrk2ZWoc

---

## 🔹 Sequential Search

### 1. Concept
**Sequential Search** (หรือ Linear Search) เป็น **อัลกอริทึมการค้นหาข้อมูลแบบง่าย**
โดยทำการตรวจสอบแต่ละ element ในลิสต์ **เรียงลำดับทีละตัว** จนกว่าจะเจอ target หรือสิ้นสุดลิสต์

- ลักษณะ: ตรวจสอบทีละ element ตามลำดับ
- ประเภท: **Search Algorithm**
- ความเสถียร: N/A (ผลลัพธ์ไม่เปลี่ยนลำดับของลิสต์)

### 2. Algorithm Steps
1. เริ่มจากตำแหน่งแรกของลิสต์
2. เปรียบเทียบค่าปัจจุบันกับ target
3. ถ้าเจอ target → return ตำแหน่ง
4. ถ้าไม่เจอ → เลื่อนไปยัง element ถัดไป
5. ทำซ้ำจนถึงตัวสุดท้ายของลิสต์
6. ถ้าไม่เจอ target → return Not Found

### 3. Pseudocode
```
procedure sequentialSearch(A, target)
    for i ← 0 to length(A)-1 do
        if A[i] = target then
            return i
    return -1  // Not found
end procedure
```

### 4. Python Example
```python
def sequential_search(arr, target):
    for i, value in enumerate(arr):
        if value == target:
            return i
    return -1

# Example usage
data = [5, 3, 8, 4, 2]
index = sequential_search(data, 4)
print(index)  # Output: 3
```

### 5. Complexity Analysis
| Case       | Time Complexity | Explanation                      |
|------------|----------------|----------------------------------|
| Best       | O(1)           | Target อยู่ตำแหน่งแรก           |
| Average    | O(n)           | ต้องตรวจสอบประมาณครึ่งลิสต์   |
| Worst      | O(n)           | Target อยู่ท้ายสุดหรือไม่มีในลิสต์ |
| Space      | O(1)           | ใช้พื้นที่คงที่                  |

### 6. Use Cases
- ลิสต์ **ขนาดเล็ก** หรือไม่เรียงลำดับ  
- ใช้เป็น **baseline** เปรียบเทียบกับ search algorithm ที่ซับซ้อนกว่า  
- ตรวจสอบค่าที่ **จำนวนไม่มาก** และ **ไม่จำเป็นต้องเร็วมาก**

### 7. Visualization (Search Step)
#### Initial
[5, 3, 8, 4, 2], target = 4

#### Step 1
Compare 5 → not target

#### Step 2
Compare 3 → not target

#### Step 3
Compare 8 → not target

#### Step 4
Compare 4 → found! ✅

---

## 🔹 Brute-force String Matching

### 1. Concept
**Brute-force String Matching** เป็นวิธีการค้นหา **pattern** ภายใน **text** แบบตรงไปตรงมา  
โดยตรวจสอบทุกตำแหน่งที่เป็นไปได้ของ text ว่าตรงกับ pattern หรือไม่  

- ลักษณะ: ตรวจสอบทุกตำแหน่งทีละตัวจนกว่าจะเจอ match  
- ประเภท: **String Search Algorithm**  
- ความเสถียร: N/A  

### 2. Algorithm Steps
1. เริ่มจากตำแหน่งแรกของ text  
2. เปรียบเทียบ pattern กับ substring ของ text ขนาดเท่ากัน  
3. ถ้า match → return ตำแหน่ง  
4. ถ้าไม่ match → เลื่อนตำแหน่งใน text ไปทีละ 1  
5. ทำซ้ำจนถึงตัวสุดท้ายของ text หรือเจอ match  

### 3. Pseudocode
```
procedure bruteForceStringMatch(text, pattern)
    n ← length(text)
    m ← length(pattern)
    
    for i ← 0 to n - m do
        match ← true
        for j ← 0 to m - 1 do
            if text[i+j] != pattern[j] then
                match ← false
                break
        if match = true then
            return i  // Match found
    return -1  // Not found
end procedure
```

### 4. Python Example
```python
def brute_force_string_match(text, pattern):
    n = len(text)
    m = len(pattern)
    
    for i in range(n - m + 1):
        match = True
        for j in range(m):
            if text[i + j] != pattern[j]:
                match = False
                break
        if match:
            return i
    return -1

# Example usage
text = "hello world"
pattern = "world"
index = brute_force_string_match(text, pattern)
print(index)  # Output: 6
```

### 5. Complexity Analysis
| Case       | Time Complexity | Explanation                         |
|------------|----------------|-------------------------------------|
| Best       | O(n)           | Pattern เจอตำแหน่งแรกทันที         |
| Average    | O((n-m+1)*m)   | ตรวจสอบหลายตำแหน่งและหลายตัว      |
| Worst      | O(nm)   | Pattern ไม่พบ ต้องตรวจทุกตำแหน่ง   |
| Space      | O(1)           | ใช้พื้นที่คงที่                     |

### 6. Use Cases
- **Pattern ขนาดเล็ก** ใน text ขนาดเล็กถึงกลาง  
- ใช้ **baseline** เปรียบเทียบกับ string matching algorithm ที่ซับซ้อนกว่า เช่น KMP หรือ Boyer-Moore  
- ตรวจสอบ **correctness** ของ pattern matching  


### 7. Visualization (Matching Step)
#### Text
"hello world"
#### Pattern
"world"

- Step 1: Compare text[0:5] "hello" → not match
- Step 2: Compare text[1:6] "ello " → not match
- Step 3: Compare text[2:7] "llo w" → not match
- Step 4: Compare text[3:8] "lo wo" → not match
- Step 5: Compare text[4:9] "o wor" → not match
- Step 6: Compare text[5:10] " worl" → not match
- Step 7: Compare text[6:11] "world" → found! ✅

---

## 🔹 Closest-Pair Problem

### 1. Concept

* หา **คู่จุดที่ใกล้ที่สุด** ในชุดของจุด 2D
* ลักษณะ: **Combinatorial / Geometric Problem**
* ประเภท: **Computational Geometry**
* Brute-force ได้ แต่ถ้าจำนวนจุดเยอะจะไม่ efficient

### 2. Mathematical Formulation

* ให้ชุดของจุด \$P = {p\_1, p\_2, ..., p\_n}\$
* ระยะระหว่างจุด \$p\_i = (x\_i, y\_i)\$ และ \$p\_j = (x\_j, y\_j)\$ คือ **Euclidean distance**:

$$
d(p_i, p_j) = \sqrt{(x_i - x_j)^2 + (y_i - y_j)^2}
$$

* Closest-Pair:

$$
(p^*, q^*) = \arg\min_{\substack{p_i, p_j \in P \\ i \neq j}} d(p_i, p_j)
$$

### 3. Brute-force Approach

1. ตรวจสอบ **ทุกคู่จุด**
2. คำนวณระยะระหว่างจุดแต่ละคู่
3. เก็บค่าที่เล็กที่สุด

### 4. Pseudocode

```
procedure closestPair(points)
    min_distance ← ∞
    n ← length(points)
    for i ← 0 to n-2 do
        for j ← i+1 to n-1 do
            d ← distance(points[i], points[j])
            if d < min_distance then
                min_distance ← d
                pair ← (points[i], points[j])
    return pair, min_distance
end procedure
```

### 5. Python Example

```python
import math

def distance(p1, p2):
    return math.sqrt((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2)

def closest_pair(points):
    min_dist = float('inf')
    pair = None
    n = len(points)
    for i in range(n-1):
        for j in range(i+1, n):
            d = distance(points[i], points[j])
            if d < min_dist:
                min_dist = d
                pair = (points[i], points[j])
    return pair, min_dist

points = [(2,3),(12,30),(40,50),(5,1),(12,10),(3,4)]
pair, dist = closest_pair(points)
print(pair, dist)
```

### 6. Complexity Analysis

| Problem      | Approach    | Time Complexity | Space Complexity |
| ------------ | ----------- | --------------- | ---------------- |
| Closest-Pair | Brute-force | \$O(n^2)\$      | \$O(1)\$         |

### 7. Use Cases

* Computational geometry ขนาด **เล็กถึงกลาง**
* เป็น **baseline** สำหรับ algorithm ที่ซับซ้อนกว่า
* ตรวจสอบ **correctness** สำหรับจำนวนจุดไม่มาก

---

## 🔹 Convex-Hull Problem

### 1. Concept

* หา **polygon convex** ที่ครอบจุดทั้งหมด โดยมีพื้นที่หรือ perimeter น้อยที่สุด
* ลักษณะ: **Combinatorial / Geometric Problem**
* ประเภท: **Computational Geometry**
* Brute-force ทำได้ แต่ไม่ efficient สำหรับจำนวนจุดเยอะ

### 2. Mathematical Formulation

* ให้ชุดของจุด \$P = {p\_1, p\_2, ..., p\_n}\$
* Convex Hull คือ **subset ของจุด** \$H \subseteq P\$ ที่:

$$
\text{ConvexHull}(P) = \text{smallest convex polygon containing all points in } P
$$

* การตรวจสอบ convexity ใช้ **cross product**:

$$
\text{cross}(a, b, c) = (b_x - a_x)(c_y - a_y) - (b_y - a_y)(c_x - a_x)
$$

* สำหรับทุกสามจุด consecutive \$(a,b,c)\$ ใน polygon:

$$
\text{cross}(a,b,c) > 0 \implies \text{left turn (convex)}
$$

* Perimeter ของ polygon convex:

$$
P = \sum_{i=1}^{m} \sqrt{(x_{i+1}-x_i)^2 + (y_{i+1}-y_i)^2}
$$

* Area ของ polygon convex (Shoelace formula):

$$
A = \frac{1}{2} \left| \sum_{i=1}^{m} (x_i y_{i+1} - x_{i+1} y_i) \right|
$$

### 3. Brute-force Approach

1. ตรวจสอบ **ทุก subset ของจุด**
2. สร้าง polygon convex ครอบทุก subset
3. เลือก polygon ที่ **area** หรือ **perimeter** น้อยที่สุด

### 4. Complexity Analysis

| Problem     | Approach    | Time Complexity    | Space Complexity |
| ----------- | ----------- | ------------------ | ---------------- |
| Convex-Hull | Brute-force | \$O(n \cdot 2^n)\$ | \$O(n)\$         |

### 5. Use Cases

* Computational geometry **ขนาดเล็กมาก**
* เป็น **baseline** สำหรับ algorithm ที่เร็วกว่า เช่น Graham Scan, Jarvis March

---
## 🗺️ Traveling Salesman Problem

### 1. Concept

**Traveling Salesman Problem (TSP)** คือปัญหาในการหา **เส้นทางสั้นที่สุด** ที่ผู้ขายสินค้าจะต้องเยี่ยมชมทุกเมือง **ครั้งเดียว** และกลับมาที่เมืองเริ่มต้น

* ลักษณะ: **Combinatorial Optimization Problem**
* ประเภท: **NP-Hard Problem**
* ใช้ Brute-force ได้ แต่สำหรับเมืองจำนวนมากไม่ practical

### 2. Brute-force Approach

1. สร้าง **ทุก permutation ของเมือง**
2. คำนวณระยะทางรวมของแต่ละ permutation
3. เลือก permutation ที่มีระยะทางรวมสั้นที่สุด

### 3. Pseudocode

```
procedure TSP_BruteForce(cities, distanceMatrix)
    best_distance ← ∞
    best_route ← null
    for each permutation p of cities do
        d ← totalDistance(p, distanceMatrix)
        if d < best_distance then
            best_distance ← d
            best_route ← p
    return best_route, best_distance
end procedure
```

### 4. Python Example

```python
import itertools

def total_distance(route, distance_matrix):
    dist = 0
    n = len(route)
    for i in range(n-1):
        dist += distance_matrix[route[i]][route[i+1]]
    dist += distance_matrix[route[-1]][route[0]]  # return to start
    return dist

def tsp_bruteforce(distance_matrix):
    n = len(distance_matrix)
    cities = list(range(n))
    min_dist = float('inf')
    best_route = None
    for perm in itertools.permutations(cities):
        d = total_distance(perm, distance_matrix)
        if d < min_dist:
            min_dist = d
            best_route = perm
    return best_route, min_dist

# Example usage
distance_matrix = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]
route, dist = tsp_bruteforce(distance_matrix)
print(route, dist)
```

### 5. Complexity Analysis

| Case        | Time Complexity | Explanation                     |
| ----------- | --------------- | ------------------------------- |
| Brute-force | O(n!)           | ตรวจทุก permutation ของ n เมือง |
| Space       | O(n)            | เก็บ route ปัจจุบันและดีที่สุด  |

### 6. Use Cases

* เหมาะสำหรับ **จำนวนเมืองน้อย** (n ≤ 10)
* ใช้เป็น **baseline** สำหรับเปรียบเทียบ heuristic/approximation methods เช่น **Nearest Neighbor**, **Genetic Algorithm**, **Dynamic Programming**
* ใช้ใน **Logistics, Route Planning** และ **Optimization Research**

### 7. Visualization (Example)

#### Cities

0, 1, 2, 3

#### Distance Matrix

```
0 10 15 20
10 0 35 25
15 35 0 30
20 25 30 0
```

* Step 1: Consider route (0,1,2,3,0) → distance 10+35+30+20=95
* Step 2: Consider route (0,1,3,2,0) → distance 10+25+30+15=80 ✅
* Continue forทุก permutation → Best route = (0,1,3,2,0)

---

## 🎒 Knapsack Problem

### 1. Concept
**Knapsack Problem** เป็นปัญหาในการเลือกชุดของ items ที่มีน้ำหนักและมูลค่า เพื่อให้ใส่ใน **กระเป๋าที่มีน้ำหนักจำกัด** แล้วได้ **มูลค่าสูงสุด**  

- ลักษณะ: **Combinatorial Optimization Problem**  
- ประเภท: **NP-Hard Problem** (สำหรับ 0/1 Knapsack)  
- สามารถแก้แบบ Brute-force ได้ แต่ไม่ practical สำหรับจำนวน items มาก  

### 2. Brute-force Approach
1. สร้าง **ทุก subset ของ items**  
2. ตรวจสอบว่า subset นั้น **ไม่เกินน้ำหนักสูงสุด**  
3. คำนวณมูลค่ารวมของ subset  
4. เลือก subset ที่ให้มูลค่าสูงสุด  

### 3. Pseudocode
```
procedure Knapsack_BruteForce(items, maxWeight)
    best_value ← 0
    best_subset ← null
    for each subset S of items do
        totalWeight ← sum(weights in S)
        totalValue ← sum(values in S)
        if totalWeight ≤ maxWeight and totalValue > best_value then
            best_value ← totalValue
            best_subset ← S
    return best_subset, best_value
end procedure
```

### 4. Python Example
```python
import itertools

def knapsack_bruteforce(weights, values, max_weight):
    n = len(weights)
    best_value = 0
    best_subset = None
    for r in range(n+1):
        for subset in itertools.combinations(range(n), r):
            total_weight = sum(weights[i] for i in subset)
            total_value = sum(values[i] for i in subset)
            if total_weight <= max_weight and total_value > best_value:
                best_value = total_value
                best_subset = subset
    return best_subset, best_value

# Example usage
weights = [2, 3, 4, 5]
values = [3, 4, 5, 6]
max_weight = 5
subset, value = knapsack_bruteforce(weights, values, max_weight)
print(subset, value)  # Output: (1, 0) 7
```

### 5. Complexity Analysis
| Case       | Time Complexity | Explanation                                      |
|------------|----------------|-------------------------------------------------|
| Brute-force| O(2^n)         | ตรวจทุก subset ของ n items                     |
| Space      | O(n)           | เก็บ subset ปัจจุบันและดีที่สุด               |

### 6. Use Cases
- เหมาะสำหรับ **จำนวน items น้อย**  
- ใช้เป็น **baseline** สำหรับเปรียบเทียบ dynamic programming หรือ heuristic methods  
- ใช้ใน **Resource Allocation, Budgeting, Logistics Optimization**  

### 7. Notes
- สำหรับ **Fractional Knapsack** สามารถใช้ **Greedy approach** แทน Brute-force ได้

---

## 📝 Assignment Problem

### 1. Concept
**Assignment Problem** เป็นปัญหาในการมอบหมายงาน (tasks) ให้กับผู้ทำงาน (agents) โดยให้ได้ **ค่าใช้จ่ายรวมต่ำสุด** หรือ **ผลประโยชน์รวมสูงสุด**  

- ลักษณะ: **Combinatorial Optimization Problem**  
- ประเภท: **Linear Assignment Problem / Matching Problem**  
- สำหรับจำนวนงานเล็ก ๆ สามารถแก้แบบ brute-force แต่จำนวนมากควรใช้ **Hungarian Algorithm** หรือ **Linear Programming**  

### 2. Brute-force Approach
1. สร้าง **ทุก permutation ของ assignment**  
2. คำนวณค่าใช้จ่ายรวมสำหรับแต่ละ permutation  
3. เลือก assignment ที่ได้ **ค่าใช้จ่ายต่ำสุด**  

### 3. Pseudocode
```
procedure Assignment_BruteForce(costMatrix)
    n ← number of tasks
    best_cost ← ∞
    best_assignment ← null
    for each permutation p of tasks do
        cost ← sum(costMatrix[i][p[i]] for i=1 to n)
        if cost < best_cost then
            best_cost ← cost
            best_assignment ← p
    return best_assignment, best_cost
end procedure
```

### 4. Python Example
```python
import itertools

def assignment_bruteforce(cost_matrix):
    n = len(cost_matrix)
    min_cost = float('inf')
    best_assignment = None
    for perm in itertools.permutations(range(n)):
        cost = sum(cost_matrix[i][perm[i]] for i in range(n))
        if cost < min_cost:
            min_cost = cost
            best_assignment = perm
    return best_assignment, min_cost

# Example usage
cost_matrix = [
    [9, 2, 7],
    [6, 4, 3],
    [5, 8, 1]
]
assignment, cost = assignment_bruteforce(cost_matrix)
print(assignment, cost)  # Output: (1, 2, 0) 9
```

### 5. Complexity Analysis
| Case       | Time Complexity | Explanation                              |
|------------|----------------|------------------------------------------|
| Brute-force| O(n!)          | ตรวจทุก permutation ของ n งาน           |
| Space      | O(n)           | เก็บ assignment ปัจจุบันและดีที่สุด     |

### 6. Use Cases
- เหมาะสำหรับ **จำนวนงานและผู้ทำงานน้อย**  
- ใช้เป็น **baseline** สำหรับเปรียบเทียบ **Hungarian Algorithm**  
- ใช้ใน **งาน Scheduling, Resource Allocation, Task Assignment**

---

## 🌲 Depth-First Search (DFS)

### 1. Concept
- DFS เป็น **การสำรวจ graph/tree แบบลึกสุดก่อนกลับ**
- เริ่มจาก node หนึ่ง → เดินไปยัง neighbor ที่ยังไม่ถูกเยี่ยมชม → ทำซ้ำจนไปถึง node สุดท้าย → ค่อย backtrack
- ใช้ **stack** หรือ recursion

### 2. Algorithm Steps
1. เริ่มจาก node เริ่มต้น
2. ทำเครื่องหมาย node ว่า visited
3. สำหรับ neighbor ทุกตัวที่ยังไม่ visited → เรียก DFS recursively

### 3. Pseudocode
```
procedure DFS(node):
    mark node as visited
    for each neighbor of node do
        if neighbor not visited then
            DFS(neighbor)
```

### 4. Python Example
```python
def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)
    print(start, end=' ')
    for neighbor in graph[start]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)
    return visited

graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

print("DFS:")
dfs(graph, 'A')  # Output: A B D E F C
```

### 5. Characteristics
- **Traversal style:** ลึกสุดก่อนค่อยกลับ
- **Data structure:** Stack (หรือ recursion)
- **Use cases:** Maze solving, Topological sort, Cycle detection, Path finding

---

## 🌳 Breadth-First Search (BFS)

### 1. Concept
- BFS เป็น **การสำรวจ graph/tree แบบระดับต่อระดับ (level-order)**
- เริ่มจาก node หนึ่ง → สำรวจ neighbor ทั้งหมดของ node นั้นก่อน → ขยับไป neighbor ของ neighbor
- ใช้ **queue**

### 2. Algorithm Steps
1. เริ่มจาก node เริ่มต้น
2. ทำเครื่องหมาย node ว่า visited
3. ใส่ node ลง queue
4. Dequeue node → ตรวจ neighbor ที่ยังไม่ visited → ทำเครื่องหมาย visited → enqueue neighbor
5. ทำซ้ำจน queue ว่าง

### 3. Pseudocode
```
procedure BFS(startNode):
    create empty queue Q
    enqueue startNode to Q
    mark startNode as visited
    while Q not empty do
        node ← dequeue Q
        for each neighbor of node do
            if neighbor not visited then
                enqueue neighbor
                mark neighbor as visited
```

### 4. Python Example
```python
from collections import deque

def bfs(graph, start):
    visited = set()
    queue = deque([start])
    visited.add(start)
    while queue:
        node = queue.popleft()
        print(node, end=' ')
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

print("\nBFS:")
bfs(graph, 'A')  # Output: A B C D E F
```

### 5. Characteristics
- **Traversal style:** สำรวจระดับต่อระดับ
- **Data structure:** Queue
- **Use cases:** Shortest path (unweighted), Level-order traversal, Social network search

---

### 🔹 สรุปความต่าง DFS vs BFS

| Feature          | DFS                           | BFS                           |
|-----------------|-------------------------------|-------------------------------|
| Traversal style | ลึกสุดก่อนกลับ               | ระดับต่อระดับ               |
| Data structure  | Stack / Recursion             | Queue                        |
| Use case        | Maze solving, Topological sort | Shortest path (unweighted), Level-order traversal |
| Memory          | O(V) (recursion stack)        | O(V) (queue)                 |


