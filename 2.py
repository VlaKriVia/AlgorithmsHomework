from collections import deque

def hex_add(x, y, z):
    transform_dict = {"0" : 0, "1" : 1, "2" : 2, "3" : 3, "4" : 4,
                "5" : 5, "6" : 6, "7" : 7, "8" : 8, "9" : 9,
                "A" : 10, "B" : 11, "C" : 12, "D" : 13, "E" : 14, "F" : 15}
    retransform_dict = {0 : "0", 1 : "1", 2 : "2", 3 : "3", 4 : "4",
                5 : "5", 6 : "6", 7 : "7", 8 : "8", 9 : "9",
                10 : "A", 11 : "B", 12 : "C", 13 : "D", 14 : "E", 15 : "F",}
    hex_sum = transform_dict.get(x) + transform_dict.get(y) + transform_dict.get(z)
    return retransform_dict.get(hex_sum % 16), retransform_dict.get(hex_sum // 16)

a = deque(input())
b = deque(input())
res = deque()

max_len = len(a) if len(b) < len(a) else len(b)
a.extendleft(["0"] * (max_len - len(a) + 1))
b.extendleft(["0"] * (max_len - len(b) + 1))

remainder = "0"
for i in range(max_len):
    sub_res, remainder = hex_add(a.pop(), b.pop(), remainder)
    res.extendleft(sub_res)

if res[0] == "0":
    res.popleft()
print(res)
