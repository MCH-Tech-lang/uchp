
pattern=1
max_pattern=pattern
list_size=int(input("введите размер лист:"))
while True:
    # Пользователь вводит: 150 200 200 2000
    
    pvo_pattern = list(map(int, input("Введите все высоты через пробел: ").split()))

    if len(pvo_pattern)==list_size:
        break
for i in range(len(pvo_pattern)-1):
    if pvo_pattern[i]==pvo_pattern[i+1]:
        pattern+=1
        if pattern>max_pattern:
            max_pattern=pattern
    else:
        pattern=1
print(max_pattern)
