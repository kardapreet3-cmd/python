for i in range(1,100):
    if i==0:
        print(i)
        break
count = 0
for i in range(1, 100):
    if i % 7 == 0:
        count += 1
        if count == 3:
            print(i)
            break