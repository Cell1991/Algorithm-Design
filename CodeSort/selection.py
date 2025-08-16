class SelectionSortTracer:
    def __init__(self, arr):
        self.original = list(arr)
        self.arr = list(arr)
        self.rounds = []
        self.round_no = 0

    def sort(self):
        n = len(self.arr)
        for i in range(n-1):
            min_index = i
            sub_before = list(self.arr)

            # หา index ของค่าที่เล็กที่สุดในช่วง [i..n-1]
            for j in range(i+1, n):
                if self.arr[j] < self.arr[min_index]:
                    min_index = j

            swaps = []
            if min_index != i:
                a, b = self.arr[i], self.arr[min_index]
                self.arr[i], self.arr[min_index] = self.arr[min_index], self.arr[i]
                swaps.append({
                    "type": "swap",
                    "i": i,
                    "j": min_index,
                    "a": a,
                    "b": b,
                    "array_after": list(self.arr)
                })

            self.round_no += 1
            self.rounds.append({
                "round": self.round_no,
                "i": i,
                "min_index": min_index,
                "subarray_before": sub_before,
                "swaps": swaps,
                "array_after_round": list(self.arr)
            })

        return self.arr, self.rounds

    def print_trace(self):
        for r in self.rounds:
            print(f"รอบที่ {r['round']} (i={r['i']}, min_index={r['min_index']})")
            print(f"  ก่อนรอบ: {r['subarray_before']}")
            if r["swaps"]:
                for k, s in enumerate(r["swaps"], 1):
                    print(f"    {k}) swap({s['i']},{s['j']}) ค่า {s['a']} ↔ {s['b']} → {s['array_after']}")
            else:
                print("  ไม่มีการสลับ (ตัวที่เล็กสุดอยู่แล้ว)")
            print(f"  หลังรอบ: {r['array_after_round']}")
            print("-" * 80)


if __name__ == "__main__":
    data = [3, 2, 5, 0, 1, 8, 7, 6, 9, 4]
    tracer = SelectionSortTracer(data)
    sorted_arr, trace = tracer.sort()
    tracer.print_trace()
    print("ผลลัพธ์สุดท้าย:", sorted_arr)
