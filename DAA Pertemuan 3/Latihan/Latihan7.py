nested_tuple = ((100), (200, 400, 600), (300), (400,800))

print(f"pertama     :{nested_tuple[0]}")
print(f"Kedua       :{nested_tuple[1][0]}, {nested_tuple[1][1]}, {nested_tuple[1][2]}")
print(f"Ketiga      :{nested_tuple[2]}")
print(f"Keempat     :{nested_tuple[3][0]}, {nested_tuple[3][1]}")