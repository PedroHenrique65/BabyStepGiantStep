import math

# Dados fornecidos
p = 12517003747
g = 6866887293
h = 3795858184
r = 178020863
c = 805670146399042780
senha = "HELLO"  # A senha convertida para números: "0805121215"

# Função para calcular o inverso modular de 'a' mod 'm'
def mod_inverse(a, m):
    m0, x0, x1 = m, 0, 1
    while a > 1:
        q = a // m
        m, a = a % m, m
        x0, x1 = x1 - q * x0, x0
    return x1 + m0 if x1 < 0 else x1

# Converta a senha para um número inteiro
m = int("".join(["{:02d}".format(ord(char) - ord('A') + 1) for char in senha]))

# Calcule N (raiz quadrada de p)
N = math.ceil(math.sqrt(p))

# Baby Steps - Precompute g^i mod p para i em [0, N]
baby_steps = {}
for i in range(N):
    baby_steps[pow(g, i, p)] = i

# Encontre z
z = (h * pow(g, -N * m, p)) % p

# Giant Steps
for j in range(N):
    # Calcule g^(j*N) mod p
    giant_step = pow(g, j * N, p)

    # Verifique se corresponde a um valor em baby_steps
    if giant_step in baby_steps:
        i = baby_steps[giant_step]
        kA = (N * i + j) % p

        # Verifique se encontramos kA
        if kA == m:
            print("Chave Privada de Alice (kA):", kA)
            break

# Decifre a mensagem
plaintext = c * mod_inverse(pow(r, kA, p), p) % p
print("Texto em claro:", plaintext)
