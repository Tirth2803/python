# loops example

# FOR LOOP

for i in range(1, 6):
    print("Number:", i)

# WHILE LOOP

count = 1
while count <= 5:
    print("Count:", count)
    count += 1

# break and continue

for i in range(1, 10):
    if i == 5:
        break
    if i == 2:
        continue
    print(i)