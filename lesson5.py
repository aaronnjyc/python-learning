def calculate_average(numbers):
    return sum(numbers) / len(numbers)

def find_maximum(numbers):
    return max(numbers)

def count_high_expression(numbers):
    count = 0

    for values in numbers:
        if values > 20:
            count += 1

    return count

gene_expression = [12.5, 18.0, 22.5, 15.0, 32.0, 8.5, 40.0]

print("Average:", calculate_average(gene_expression))
print("Maximum:", find_maximum(gene_expression))
print("High Expression Count:", count_high_expression(gene_expression))