# Selection Sort

## 1. Concept
**Selection Sort** เป็นอัลกอริทึมการจัดเรียงที่ทำงานโดยการเลือกค่าที่น้อยที่สุดจากส่วนที่ยังไม่ได้เรียง แล้วนำไปไว้ตำแหน่งต้นของลิสต์ที่ยังไม่ได้จัดเรียง

- ลักษณะ: เลือกค่าต่ำสุด/สูงสุดแล้ววางไว้ข้างหน้า
- ประเภท: **Comparison-based Sorting**
- ความเสถียร: **Unstable** (แต่สามารถปรับให้ stable ได้)

---

## 2. Algorithm Steps
1. เริ่มจากตำแหน่งแรกของลิสต์ (index 0)
2. หาค่าที่น้อยที่สุดจากตำแหน่งปัจจุบันจนถึงตัวสุดท้าย
3. สลับค่าที่น้อยที่สุดกับตำแหน่งปัจจุบัน
4. ขยับตำแหน่งไปทางขวาทีละ 1 แล้วทำซ้ำจนสุดลิสต์

---

## 3. Pseudocode
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

---

## 4. Python Example
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

---

## 5. Complexity Analysis
| Case       | Time Complexity | Explanation                              |
|------------|----------------|------------------------------------------|
| Best       | O(n²)          | ต้องเปรียบเทียบทั้งหมดแม้เรียงแล้ว      |
| Average    | O(n²)          | ทำ n(n-1)/2 comparisons                   |
| Worst      | O(n²)          | ลิสต์เรียงแบบตรงข้ามทั้งหมด              |
| Space      | O(1)           | สลับในที่เดิม (In-place)                 |

---

## 6. Use Cases
- เหมาะกับ **ข้อมูลขนาดเล็ก** หรือข้อมูลที่ swap มีต้นทุนสูง
- เข้าใจง่าย ใช้สอนเบื้องต้นได้ดี
- มีจำนวนครั้งในการ swap ต่ำสุดในกลุ่ม comparison-based sorting

---

## 7. Visualization (Min Selection)

### Initial
[5, 3, 8, 4, 2]

---

### Pass 1 (i=0)
- หาค่าน้อยสุดใน [5, 3, 8, 4, 2] → 2 → สลับกับ 5 → [2, 3, 8, 4, 5]

### Pass 2 (i=1)
- หาค่าน้อยสุดใน [3, 8, 4, 5] → 3 → ไม่ต้องสลับ → [2, 3, 8, 4, 5]

### Pass 3 (i=2)
- หาค่าน้อยสุดใน [8, 4, 5] → 4 → สลับกับ 8 → [2, 3, 4, 8, 5]

### Pass 4 (i=3)
- หาค่าน้อยสุดใน [8, 5] → 5 → สลับกับ 8 → [2, 3, 4, 5, 8]

---

✅ **Sorted Result:** [2, 3, 4, 5, 8]

---

## 🎥 ดูวิดีโอบน YouTube  
🔗 https://www.youtube.com/watch?v=Iccmrk2ZWoc
