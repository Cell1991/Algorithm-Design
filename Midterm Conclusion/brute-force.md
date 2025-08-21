# 1️⃣ Brute Force

วิธีแก้ปัญหาแบบตรงไปตรงมา ลองทุกความเป็นไปได้ 

### สารบัญ
[⚡ Exhaustive Search](#-exhaustive-search)  
[🔹 Bubble Sort](#-bubble-sort)  
[🔹 Selection Sort](#-selection-sort)  
[🔹 Sequential Search](#-sequential-search)  
[🔹 Brute-force String Matching](#-brute-force-string-matching)  
[🔹 Closest-pair and Convex-hull Problems](#-closest-pair-and-convex-hull-problems)  
[🗺️ Traveling Salesman Problem TSP](#-traveling-salesman-problem-tsp)  
[🎒 Knapsack Problem](#-knapsack-problem)  
[📝 Assignment Problem](#-assignment-problem)  
[🌳 Depth-First Search DFS and Breadth-First Search BFS](#-depth-first-search-dfs-and-breadth-first-search-bfs)


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
*(รายละเอียด Concept, Pseudocode, Python Example, Complexity, Use Case)*

---

## 🔹 Brute-force String Matching
*(รายละเอียด Concept, Steps, Example, Complexity)*

---

## 🔹 Closest-pair and Convex-hull Problems
*(รายละเอียด Concept, Steps, Example, Complexity)*

---

## 🗺️ Traveling Salesman Problem (TSP)
*(รายละเอียด Concept, Steps, Example, Complexity)*

---

## 🎒 Knapsack Problem
*(รายละเอียด Concept, Steps, Example, Complexity)*

---

## 📝 Assignment Problem
*(รายละเอียด Concept, Steps, Example, Complexity)*

---

## 🌳 Depth-First Search (DFS) and Breadth-First Search (BFS)
*(รายละเอียด Concept, Steps, Example, Complexity)*
