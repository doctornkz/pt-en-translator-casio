with open('tradutor.py','r') as f:
    content = f.read()
    f.close

for char in content:
    if char not in 'abcdefghijklmnopqrstuvwxyz":, .':
        print(char)