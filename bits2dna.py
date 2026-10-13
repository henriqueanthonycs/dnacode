import random

entrada = open("in.html", "rb")
saida = open("Bits2DNA.txt", "w")

dados = entrada.read()


tabela = {
    "0": "a",
    "1": "G",
    "a": "c",
    "G": "T",
    "c": "a",
    "T": "G",
}

ultimas = ["", "", ""]

N = 12
L = 19

random.seed(2)

PRIMER_F = "CTACACGACGCTCTTCCGATCT"
PRIMER_R = "AGATCGGAAGAGCGGTTCAGCA"

n = 0

###########################################################

def bits_para_bases(bits):
    global ultimas
    resultado=""

    for bit in bits:
        base = tabela[bit]

        if random.random() < 0.5:
            base = tabela[base]

        if base == ultimas[0] == ultimas[1] == ultimas[2]:
            base = tabela[base]

        ultimas = [ultimas[1], ultimas[2], base]

        resultado += base

    return resultado

def byte_para_bases(byte):
    bits = format(byte, "08b")
    return bits_para_bases(bits)

def inteiro_para_bases(numero):
    bits = format(numero, "019b")
    bits = bits[::-1]
    return bits_para_bases(bits)

saida.write(PRIMER_F + inteiro_para_bases(0))

for byte in dados:
    saida.write(byte_para_bases(byte))
    n += 1

    if n % N == 0:
        saida.write(PRIMER_R + "\n")
        saida.write(PRIMER_F + inteiro_para_bases(n // N))


for k in range(n % N, N):
    saida.write(byte_para_bases(random.randint(0,255)))
saida.write(PRIMER_R + "\n")
saida.close()