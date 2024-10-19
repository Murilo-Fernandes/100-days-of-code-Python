n = 100
soma = (n * (n + 1)) // 2  # Use // para divisão inteira
print(f"A soma dos primeiros {n} números é: {soma}")

total_sum = 0 

for number in range(1,101):
    total_sum += number

print(total_sum)