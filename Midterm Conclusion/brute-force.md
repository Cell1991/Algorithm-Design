# 1️⃣ Brute Force

วิธีแก้ปัญหาแบบตรงไปตรงมา ลองทุกความเป็นไปได้ 

### **สารบัญ (Table of Contents)**
- [⚡ Exhaustive Search](#exhaustive-search)
- [🔹 Bubble Sort](#bubble-sort)
- [🔹 Selection Sort](#selection-sort)
- [🔹 Sequential Search](#sequential-search)
- [🔹 Brute-force String Matching](#brute-force-string-matching)
- [🔹 Closest-pair and Convex-hull Problems](#closest-pair-and-convex-hull-problems)
- [🗺️ Traveling Salesman Problem (TSP)](#traveling-salesman-problem-tsp)
- [🎒 Knapsack Problem](#knapsack-problem)
- [📝 Assignment Problem](#assignment-problem)
- [🌳 Depth-First Search (DFS) and Breadth-First Search (BFS)](#depth-first-search-dfs-and-breadth-first-search-bfs)

---

## ⚡ Exhaustive Search
**Concept / Purpose:**  
Exhaustive Search (หรือ Brute-force Search) เป็นวิธีแก้ปัญหาแบบตรงไปตรงมา  
โดยการ **ตรวจสอบทุกความเป็นไปได้** เพื่อหา solution ที่ถูกต้อง  

- **ลักษณะ:** ตรวจทุก candidate solution โดยไม่มีการคาดเดาหรือ optimization  
- **ประเภท:** Problem-solving strategy  
- **ข้อดี:** เข้าใจง่าย, implementation ไม่ซับซ้อน  
- **ข้อเสีย:** **ไม่ efficient** สำหรับปัญหาขนาดใหญ่  

**Motivation / Why use it:**  
- เหมาะสำหรับปัญหาที่ขนาดเล็กหรือจำนวนความเป็นไปได้จำกัด  
- เป็นวิธี baseline เพื่อเปรียบเทียบ algorithm ที่ซับซ้อนกว่า  
- ใช้ตรวจสอบ correctness ของ solution  

---

## Algorithm Steps (General)
1. กำหนด **set ของทุก candidate solution**  
2. ตรวจสอบแต่ละ candidate ว่าตรงตาม **เงื่อนไขของปัญหา** หรือไม่  
3. ถ้าพบ candidate ที่ถูกต้อง → เก็บหรือ return  
4. ทำซ้ำจนตรวจสอบครบทุก candidate  
5. เลือก solution ที่ **ดีที่สุด** ตาม criteria (เช่น min, max, shortest path)  

---

## Pseudocode
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

---

## 🔹 Bubble Sort
*(รายละเอียดเต็มแบบตัวอย่างที่คุณให้ไว้)*

---

## 🔹 Selection Sort
*(สามารถใส่รายละเอียดแบบเดียวกับ Bubble Sort)*

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
