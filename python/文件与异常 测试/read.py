from pathlib import Path

path=Path('test_work/pi_digits.txt')
contents=path.read_text()
print(contents)

lines=contents.split()
print(lines)
add=''
for line in lines:
    add+=line
print(add)
print(list(range(10)))