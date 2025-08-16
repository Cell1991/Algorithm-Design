class QuickSortTracer:
    def __init__(self, arr, hide_self_swaps=True):
        self.original = list(arr)
        self.arr = list(arr)
        self.rounds = []
        self.hide_self_swaps = hide_self_swaps
        self.round_no = 0

    def sort(self):
        if len(self.arr) <= 1:
            return self.arr, []
        self._quicksort(0, len(self.arr) - 1, 0)
        return self.arr, self.rounds

    def _quicksort(self, low, high, depth):
        if low < high:
            p = self._partition(low, high, depth)
            self._quicksort(low, p - 1, depth + 1)
            self._quicksort(p + 1, high, depth + 1)

    def _partition(self, low, high, depth):
        pivot = self.arr[high]
        i = low - 1
        sub_before = self.arr[low:high+1]
        swaps = []
        for j in range(low, high):
            if self.arr[j] <= pivot:
                i += 1
                if i != j:
                    a, b = self.arr[i], self.arr[j]
                    self.arr[i], self.arr[j] = self.arr[j], self.arr[i]
                    swaps.append({
                        "type": "swap",
                        "i": i,
                        "j": j,
                        "a": a,
                        "b": b,
                        "array_after": list(self.arr)
                    })
                else:
                    if not self.hide_self_swaps:
                        swaps.append({
                            "type": "swap_noop",
                            "i": i,
                            "j": j,
                            "a": self.arr[i],
                            "b": self.arr[j],
                            "array_after": list(self.arr)
                        })
        pi = i + 1
        if pi != high:
            a, b = self.arr[pi], self.arr[high]
            self.arr[pi], self.arr[high] = self.arr[high], self.arr[pi]
            swaps.append({
                "type": "pivot_swap",
                "i": pi,
                "j": high,
                "a": a,
                "b": b,
                "array_after": list(self.arr)
            })
        else:
            if not self.hide_self_swaps:
                swaps.append({
                    "type": "pivot_swap_noop",
                    "i": pi,
                    "j": high,
                    "a": self.arr[pi],
                    "b": self.arr[high],
                    "array_after": list(self.arr)
                })
        self.round_no += 1
        round_record = {
            "round": self.round_no,
            "depth": depth,
            "low": low,
            "high": high,
            "pivot": pivot,
            "pivot_final_index": pi,
            "subarray_before": sub_before,
            "swaps": swaps,
            "left_after": self.arr[low:pi],
            "pivot_after": self.arr[pi],
            "right_after": self.arr[pi+1:high+1],
            "array_after_partition": list(self.arr)
        }
        self.rounds.append(round_record)
        return pi

    def print_trace(self):
        for r in self.rounds:
            print(f"รอบที่ {r['round']} (depth={r['depth']}) ช่วงดัชนี [{r['low']}..{r['high']}]")
            print(f"  ก่อนแบ่ง: {r['subarray_before']}")
            print(f"  pivot = {r['pivot']} (เลือกตัวสุดท้าย)")
            if r['swaps']:
                print(f"  รายการสลับทั้งหมด {len(r['swaps'])} ครั้ง:")
                for k, s in enumerate(r['swaps'], 1):
                    if s['type'] == 'swap':
                        print(f"    {k}) swap({s['i']},{s['j']}) ค่า {s['a']} ↔ {s['b']} → {s['array_after']}")
                    elif s['type'] == 'pivot_swap':
                        print(f"    {k}) swap_pivot({s['i']},{s['j']}) ค่า {s['a']} ↔ {s['b']} → {s['array_after']}")
                    elif s['type'] == 'swap_noop':
                        print(f"    {k}) swap({s['i']},{s['j']}) ข้าม (ตำแหน่งเดียวกัน) → {s['array_after']}")
                    elif s['type'] == 'pivot_swap_noop':
                        print(f"    {k}) swap_pivot({s['i']},{s['j']}) ข้าม (pivot อยู่ถูกที่แล้ว) → {s['array_after']}")
            else:
                print("  ไม่มีการสลับในรอบนี้")
            print(f"  หลังแบ่ง: left={r['left_after']} | pivot=[{r['pivot_after']}] | right={r['right_after']}")
            print(f"  อาร์เรย์หลังจบรอบ: {r['array_after_partition']}")
            print("-" * 80)


if __name__ == "__main__":
    data = [3, 2, 5, 0, 1, 8, 7, 6, 9, 4]
    tracer = QuickSortTracer(data, hide_self_swaps=True)
    sorted_arr, trace = tracer.sort()
    tracer.print_trace()
    print("ผลลัพธ์สุดท้าย:", sorted_arr)
