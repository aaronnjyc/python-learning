gene_expression = [12.5, 18.0, 22.5, 15.0, 32.0, 8.5, 40.0]

for value in gene_expression:
        print(value)

print("---------------------")

for value in gene_expression:
    if value > 20:
        print(value)

print("---------------------")

for value in gene_expression:
    if value > 30:
        print("Very High")
    elif value > 20:
         print("High")
    else:
         print("Low")

print("---------------------")

count = 0
for value in gene_expression:
    if value > 20:
        count += 1

print(count)
