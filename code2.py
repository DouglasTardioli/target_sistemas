def fibonacci(n):
    sequencia = [0, 1]
    while sequencia[-1] < n:
        sequencia.append(sequencia[-1] + sequencia[-2])
    return sequencia

def pertence_fibonacci(num):
    sequencia = fibonacci(num)
    if num in sequencia:
        return f"O número {num} pertence à sequência de Fibonacci."
    else:
        return f"O número {num} não pertence à sequência de Fibonacci."


numero = int(input("Informe um número: "))
print(pertence_fibonacci(numero))