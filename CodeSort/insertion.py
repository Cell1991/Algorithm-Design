class InsertionSortTracer:
    def __init__(self, arr):
        self.original = list(arr)
        self.arr = list(arr)
        self.rounds = []
        self.round_no = 0

    def sort(self):
        for i in range(1, len(self.arr)):
            key = self.arr[i]
            j = i - 1
            sub_before = list(self.arr)
            moves = []

            # เลื่อนค่าไปทางขวาจนกว่าจะหาตำแหน่งของ key ได้
            while j >= 0 and self.arr[j] > key:
                moves.append({
                    "type": "shift",
                    "from": j,
                    "to": j+1,
                    "value": self.arr[j],
                    "array_before": list(self.arr)
                })
                self.arr[j+1] = self.arr[j]
                moves[-1]["array_after"] = list(self.arr)
                j -= 1

            # แทรก key ที่ตำแหน่งที่ถูกต้อง
            self.arr[j+1] = key
            moves.append({
                "type": "insert",
                "index": j+1,
                "value": key,
                "array_after": list(self.arr)
            })

            self.round_no += 1
            self.rounds.append({
                "round": self.round_no,
                "i": i,
                "key": key,
                "subarray_before": sub_before,
                "moves": moves,
                "array_after_round": list(self.arr)
            })

        return self.arr, self.rounds

    def print_trace(self):
        for r in self.rounds:
            print(f"รอบที่ {r['round']} (i={r['i']}, key={r['key']})")
            print(f"  ก่อนรอบ: {r['subarray_before']}")
            if r["moves"]:
                for k, m in enumerate(r["moves"], 1):
                    if m["type"] == "shift":
                        print(f"    {k}) shift ค่า {m['value']} จาก {m['from']} → {m['to']} → {m['array_after']}")
                    elif m["type"] == "insert":
                        print(f"    {k}) insert key={m['value']} ที่ index {m['index']} → {m['array_after']}")
            print(f"  หลังรอบ: {r['array_after_round']}")
            print("-" * 80)


if __name__ == "__main__":
    data = [3, 2, 5, 0, 1, 8, 7, 6, 9, 4]
    tracer = InsertionSortTracer(data)
    sorted_arr, trace = tracer.sort()
    tracer.print_trace()
    print("ผลลัพธ์สุดท้าย:", sorted_arr)
