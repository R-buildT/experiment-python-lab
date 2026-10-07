from pathlib import Path

content = Path("grocery.txt").read_text(encoding="utf-8")
print('\n')
print('\n',content)
