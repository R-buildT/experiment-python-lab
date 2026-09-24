import re

a='h3e4l5l6o bro 1h2o3w3 a5r6e7 8y9o4u2 doing i want7e5d 6t3o6 3s3ay7 3t2ha5t68 y3o4u6 8f3o5r35g6o3t5 2t6h5e 5l2u5n25c6h 42b6o3x5 2t5h6at3 5y4ou2 4we63re2 5m42ea35n5t2 2t4o 3eat'
b=r''

for i in re.finditer(b,a):
    print(i.group(),i.span())