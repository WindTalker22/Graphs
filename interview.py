pairs = {
    "cat": "bob",
    "dog": 23,
    19: 18,
    90: "fish"
}
sum = 0

for value in pairs.values():
    if isinstance(value, int):
        sum += value
        print(sum)
