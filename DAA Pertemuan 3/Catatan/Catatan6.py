bin_colors= {
    "manual_color" : "Yellow",
    "approved _color" : "Green",
    "Refused_color": "red"
}
print(bin_colors)

print(bin_colors.get("Refused_color"))

print(bin_colors["approved _color"])

del bin_colors["approved _color"]
print(bin_colors)