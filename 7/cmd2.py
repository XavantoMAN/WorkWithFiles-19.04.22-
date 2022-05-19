s = ''
while True:
    try:
        line = input()
    except EOFError:
        break
    s += line + '\n'
print('V7----------------V7')
print(s)
print('V7----------------V7')
