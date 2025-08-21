# Merge Sort

## 1. Concept
**Merge Sort** เป็นอัลกอริทึมแบบ Divide & Conquer
ที่แบ่งลิสต์ออกเป็นสองส่วนซ้ำ ๆ จนแต่ละส่วนมีแค่ 1 ตัว แล้วรวมกลับอย่างมีลำดับ (Merge)

- ลักษณะ: แบ่งแล้วรวม
- ประเภท: **Comparison-based Sorting**
- ความเสถียร: **Stable** (ลำดับค่าที่เท่ากันไม่เปลี่ยน)
- ลักษณะพิเศษ: ใช้ Recursion และต้องใช้หน่วยความจำเพิ่มเติม

---

## 2. Algorithm Steps
1. ถ้าลิสต์มีความยาว ≤ 1 → ถือว่าเรียงแล้ว
2. แบ่งลิสต์ครึ่งหนึ่งเป็นซ้ายและขวา
3. ใช้ Merge Sort กับซ้ายและขวา (เรียกตัวเอง - recursive)
4. รวมลิสต์ซ้ายและขวาที่เรียงแล้วให้เป็นลิสต์เดียว (merge แบบเรียง)
5. ส่งลิสต์ที่รวมเสร็จกลับขึ้นไป

---

## 3. Pseudocode
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

---

## 4. Python Example
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

---

## 5. Complexity Analysis
| Case       | Time Complexity | Explanation                                |
|------------|----------------|--------------------------------------------|
| Best       | O(n log n)     | แบ่งครึ่งทุกครั้ง และรวมทุกระดับ          |
| Average    | O(n log n)     | เสถียรไม่ว่าลิสต์จะเป็นแบบไหน             |
| Worst      | O(n log n)     | กรณีแย่ที่สุดก็ยังคง log-linear            |
| Space      | O(n)           | ต้องใช้ลิสต์ใหม่ตอน merge (ไม่ in-place)  |

---

## 6. Use Cases
- เหมาะกับข้อมูลขนาดใหญ่ที่ต้องการประสิทธิภาพสูง
- ใช้ได้ดีแม้ลิสต์จะไม่เรียงมาก่อน
- ใช้ในระบบที่ต้องการความเสถียรของการจัดเรียง

---

## 7. Visualization (Divide & Merge)

### Initial
[5, 3, 8, 4, 2]

→ แบ่ง: [5, 3] | [8, 4, 2]  
→ แบ่ง: [5] [3] | [8] [4, 2]  
→ แบ่ง: [4] [2] → รวม: [2, 4]  
→ รวม: [3, 5] | [2, 4, 8] → รวมสุดท้าย: [2, 3, 4, 5, 8]

---

✅ **Sorted Result:** [2, 3, 4, 5, 8]

---

## 🎥 ดูวิดีโอบน YouTube  
🔗 https://www.youtube.com/watch?v=5Z9dn2WTg9o
