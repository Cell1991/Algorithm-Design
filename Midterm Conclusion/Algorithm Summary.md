# **📚 Algorithm Summary**

สรุปเนื้อหาการออกแบบอัลกอริทึม (Algorithm Design Techniques)  
จัดเรียงตามแนวคิดหลัก: **Brute Force → Decrease and Conquer → Divide and Conquer**

---

## **1️⃣ [Brute Force](brute-force.md)**
วิธีแก้ปัญหาแบบตรงไปตรงมา ลองทุกความเป็นไปได้ (`Exhaustive Search`)  

⚡ `Exhaustive Search`  
🔹 `Bubble Sort`  
🔹 `Selection Sort`  
🔹 `Sequential Search`  
🔹 `Brute-force String Matching`  
🔹 `Closest-pair and Convex-hull Problems`  
🗺️ `Traveling Salesman Problem (TSP)`  
🎒 `Knapsack Problem`  
📝 `Assignment Problem`  
🌳 `Depth-First Search (DFS)` and `Breadth-First Search (BFS)`

---

## **2️⃣ Decrease and Conquer**
ลดขนาดของปัญหาแล้วแก้ทีละขั้น โดยแบ่งตามวิธีลดขนาด

### **2.1 ⬇️ Decrease by a Constant**
ลดปัญหาแบบคงที่ทีละขั้น  

🔹 `Greatest Common Divisor (GCD)`  
🔹 `Insertion Sort`  
🔹 `Topological Sorting (DFS)`  
🔹 `Generating Permutations`  
  🔸 Minimal-change requirement  
  🔸 Johnson-Trotter algorithm  
  🔸 Lexicographic order  
  🔸 Binary Reflected Gray Code *(แนวคิด Minimal Change)*

### **2.2 🔽 Decrease by a Constant Factor**
ลดปัญหาลงทีละสัดส่วน เช่น ครึ่งหนึ่งของขนาดเดิม  

🔹 `Binary Search`  
🔹 `Fake-Coin Problem`  
🔹 `Russian Peasant Multiplication`  
🔹 `Josephus Problem`

### **2.3 🔄 Variable Size Decrease**
ลดปัญหาแบบไม่คงที่ ขึ้นกับเงื่อนไขหรือสถานการณ์  

🔹 `Lomuto Partitioning`  
🔹 `Quick Select`  
🔹 `Interpolation Search`  
🌳 `Binary Search Tree`

---

## **3️⃣ Divide and Conquer**
แบ่งปัญหาเป็นหลายส่วน แก้แต่ละส่วน แล้วรวมผลลัพธ์  

🔹 `Merge Sort`  
🔹 `Quick Sort`  
🌳 `Binary Tree Traversals and Related Properties`  
🔹 `Closest-pair and Convex-hull Problems` *(ประสิทธิภาพดีกว่า Brute Force)*

---

# 🔹 Closest-Pair Problem

## 1. Concept

* หา **คู่จุดที่ใกล้ที่สุด** ในชุดของจุด 2D
* ลักษณะ: **Combinatorial / Geometric Problem**
* ประเภท: **Computational Geometry**
* Brute-force ได้ แต่ถ้าจำนวนจุดเยอะจะไม่ efficient

## 2. Mathematical Formulation

* ให้ชุดของจุด \$P = {p\_1, p\_2, ..., p\_n}\$
* ระยะระหว่างจุด \$p\_i = (x\_i, y\_i)\$ และ \$p\_j = (x\_j, y\_j)\$ คือ **Euclidean distance**:

$$
d(p_i, p_j) = \sqrt{(x_i - x_j)^2 + (y_i - y_j)^2}
$$

* Closest-Pair:

$$
(p^*, q^*) = \arg\min_{\substack{p_i, p_j \in P \\ i \neq j}} d(p_i, p_j)
$$

## 3. Brute-force Approach

1. ตรวจสอบ **ทุกคู่จุด**
2. คำนวณระยะระหว่างจุดแต่ละคู่
3. เก็บค่าที่เล็กที่สุด

## 4. Pseudocode

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

## 5. Python Example

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

## 6. Complexity Analysis

| Problem      | Approach    | Time Complexity | Space Complexity |
| ------------ | ----------- | --------------- | ---------------- |
| Closest-Pair | Brute-force | \$O(n^2)\$      | \$O(1)\$         |

## 7. Use Cases

* Computational geometry ขนาด **เล็กถึงกลาง**
* เป็น **baseline** สำหรับ algorithm ที่ซับซ้อนกว่า
* ตรวจสอบ **correctness** สำหรับจำนวนจุดไม่มาก

---

# 🔹 Convex-Hull Problem

## 1. Concept

* หา **polygon convex** ที่ครอบจุดทั้งหมด โดยมีพื้นที่หรือ perimeter น้อยที่สุด
* ลักษณะ: **Combinatorial / Geometric Problem**
* ประเภท: **Computational Geometry**
* Brute-force ทำได้ แต่ไม่ efficient สำหรับจำนวนจุดเยอะ

## 2. Mathematical Formulation

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

## 3. Brute-force Approach

1. ตรวจสอบ **ทุก subset ของจุด**
2. สร้าง polygon convex ครอบทุก subset
3. เลือก polygon ที่ **area** หรือ **perimeter** น้อยที่สุด

## 4. Complexity Analysis

| Problem     | Approach    | Time Complexity    | Space Complexity |
| ----------- | ----------- | ------------------ | ---------------- |
| Convex-Hull | Brute-force | \$O(n \cdot 2^n)\$ | \$O(n)\$         |

## 5. Use Cases

* Computational geometry **ขนาดเล็กมาก**
* เป็น **baseline** สำหรับ algorithm ที่เร็วกว่า เช่น Graham Scan, Jarvis March




