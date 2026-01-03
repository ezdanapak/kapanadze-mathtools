# Kapanadze MathTools

მარტივი მათემატიკური ხელსაწყოების ბიბლიოთეკა Python-ისთვის.

## დაყენება

```bash
pip install kapanadze-mathtools
```

## გამოყენება

```python
from kapanadze_mathtools import statistics, geometry

# სტატისტიკური გამოთვლები
numbers = [1, 2, 3, 4, 5]
print(statistics.mean(numbers))  # საშუალო
print(statistics.median(numbers))  # მედიანა

# გეომეტრიული გამოთვლები
print(geometry.circle_area(5))  # წრის ფართობი
print(geometry.rectangle_area(4, 6))  # მართკუთხედის ფართობი
```

## მოდულები

- `statistics` - სტატისტიკური გამოთვლები
- `geometry` - გეომეტრიული გამოთვლები
