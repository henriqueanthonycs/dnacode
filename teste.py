with open("Bits2DNA.txt", "r") as f:
    linhas = f.readlines()

oligo = linhas[0].strip()

dados_dna = oligo[41:137]


bits = ""
for base in dados_dna:
    if base in "ac":
        bits += "0"
    else:
        bits += "1"

texto_decodificado = ""
for i in range(0, 96, 8):
    byte_bits = bits[i:i+8]
    numero_ascii = int(byte_bits, 2)
    texto_decodificado += chr(numero_ascii)

print("Inicio: ")
print(texto_decodificado)