class BubbleSortTracer:
    def __init__(self, arr, hide_self_swaps=True):
        self.original = list(arr)
        self.arr = list(arr)
        self.rounds = []
        self.hide_self_swaps = hide_self_swaps
        self.round_no = 0

    def sort(self):
        n = len(self.arr)
        for i in range(n):
            swaps = []
            sub_before = list(self.arr)
            for j in range(0, n - i - 1):
                if self.arr[j] > self.arr[j + 1]:
                    a, b = self.arr[j], self.arr[j+1]
                    self.arr[j], self.arr[j+1] = self.arr[j+1], self.arr[j]
                    swaps.append({
                        "type": "swap",
                        "i": j,
                        "j": j+1,
                        "a": a,
                        "b": b,
                        "array_after": list(self.arr)
                    })
                else:
                    if not self.hide_self_swaps:
                        swaps.append({
                            "type": "no_swap",
                            "i": j,
                            "j": j+1,
                            "a": self.arr[j],
                            "b": self.arr[j+1],
                            "array_after": list(self.arr)
                        })
            self.round_no += 1
            round_record = {
                "round": self.round_no,
                "subarray_before": sub_before,
                "swaps": swaps,
                "array_after_round": list(self.arr)
            }
            self.rounds.append(round_record)
        return self.arr, self.rounds

    def print_trace(self):
        for r in self.rounds:
            print(f"รอบที่ {r['round']}")
            print(f"  ก่อนรอบ: {r['subarray_before']}")
            if r["swaps"]:
                print(f"  มีการสลับ {len(r['swaps'])} ครั้ง:")
                for k, s in enumerate(r["swaps"], 1):
                    if s["type"] == "swap":
                        print(f"    {k}) swap({s['i']},{s['j']}) ค่า {s['a']} ↔ {s['b']} → {s['array_after']}")
                    elif s["type"] == "no_swap":
                        print(f"    {k}) ไม่สลับ({s['i']},{s['j']}) ค่า {s['a']} , {s['b']} → {s['array_after']}")
            else:
                print("  ไม่มีการสลับในรอบนี้")
            print(f"  หลังรอบ: {r['array_after_round']}")
            print("-" * 80)


if __name__ == "__main__":
    data = [3, 2, 5, 0, 1, 8, 7, 6, 9, 4]
    tracer = BubbleSortTracer(data, hide_self_swaps=True)
    sorted_arr, trace = tracer.sort()
    tracer.print_trace()
    print("ผลลัพธ์สุดท้าย:", sorted_arr)
