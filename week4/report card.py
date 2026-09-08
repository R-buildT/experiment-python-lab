dic = {
    'ranveer': {'english': 36, 'hindi': 30, 'science': 45, 'maths': 41},
    'aisha': {'english': 42, 'hindi': 38, 'science': 47, 'maths': 44},
    'vikram': {'english': 39, 'hindi': 35, 'science': 43, 'maths': 40},
    'meera': {'english': 45, 'hindi': 41, 'science': 48, 'maths': 46}
}

print('enter your student name')
a =input('>>> ')

if a.isalpha():
  print('SCORES ARE >> ')
  for b in (dic[a]):
    print((b),dic[a][b])


