"""
kapanadze-mathtools ბიბლიოთეკის გამოყენების მაგალითები
"""

from kapanadze_mathtools import statistics, geometry

print("=" * 50)
print("სტატისტიკური გამოთვლები")
print("=" * 50)

# რიცხვების სია
numbers = [85, 90, 78, 92, 88, 76, 95, 89]

print(f"რიცხვები: {numbers}")
print(f"საშუალო: {statistics.mean(numbers):.2f}")
print(f"მედიანა: {statistics.median(numbers)}")
print(f"დისპერსია: {statistics.variance(numbers):.2f}")
print(f"სტანდარტული გადახრა: {statistics.std_dev(numbers):.2f}")

print("\n" + "=" * 50)
print("გეომეტრიული გამოთვლები")
print("=" * 50)

# წრის გამოთვლები
radius = 5
print(f"\nწრე რადიუსით {radius}:")
print(f"  ფართობი: {geometry.circle_area(radius):.2f}")
print(f"  გარშემოწერილობა: {geometry.circle_circumference(radius):.2f}")

# მართკუთხედის გამოთვლები
length, width = 10, 6
print(f"\nმართკუთხედი {length}x{width}:")
print(f"  ფართობი: {geometry.rectangle_area(length, width)}")
print(f"  პერიმეტრი: {geometry.rectangle_perimeter(length, width)}")

# სამკუთხედის გამოთვლები
base, height = 8, 5
print(f"\nსამკუთხედი (ფუძე={base}, სიმაღლე={height}):")
print(f"  ფართობი: {geometry.triangle_area(base, height)}")
