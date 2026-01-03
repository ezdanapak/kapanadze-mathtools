# Kapanadze MathTools

მარტივი მათემატიკური ხელსაწყოების ბიბლიოთეკა Python-ისთვის.

## დაყენება

```bash
pip install kapanadze-mathtools
```

## გამოყენება

```python
from kapanadze_mathtools import statistics, geometry, text_tools, converters

# სტატისტიკური გამოთვლები
numbers = [1, 2, 3, 4, 5]
print(statistics.mean(numbers))  # საშუალო
print(statistics.median(numbers))  # მედიანა

# გეომეტრიული გამოთვლები
print(geometry.circle_area(5))  # წრის ფართობი
print(geometry.rectangle_area(4, 6))  # მართკუთხედის ფართობი

# ტექსტის დამუშავება
print(text_tools.count_words("გამარჯობა მსოფლიო"))  # სიტყვების რაოდენობა
print(text_tools.is_palindrome("radar"))  # პალინდრომია?

# ერთეულების კონვერტაცია
print(converters.celsius_to_fahrenheit(25))  # ცელსიუსი → ფარენჰეიტი
print(converters.kilometers_to_miles(10))  # კილომეტრი → მილი
```

## მოდულები

- `statistics` - სტატისტიკური გამოთვლები
- `geometry` - გეომეტრიული გამოთვლები
- `text_tools` - ტექსტის დამუშავება
- `converters` - ერთეულების კონვერტაცია
