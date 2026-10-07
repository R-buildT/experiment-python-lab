from pathlib import Path

path = Path('/home/rt-builds/Desktop/git/experiment-python-lab/week9/nuclearfusion.txt')
path.write_text('hi bro2')
a =path.read_text()
print(a)