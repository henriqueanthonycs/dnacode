import base64 #Importando a biblioteca que ajuda a converter a sequencia d ebytes em texto

with open("foto.jpg", "rb") as arquivo: #abre a foto em modo binario e chama o arquivo aberto de "arquivo".
    dados = arquivo.read() #Lê todos os bytes da foto e guarda na variavel "dados".

print(len(dados)) #Mostra quantos Bytes a foto tem. "len" significa "comprimento"


texto_b64 = base64.b64encode(dados).decode("ascii")
print(len(texto_b64))
print(texto_b64[:60])

html = "<html>\n"
html += "<head>\n"
html += '<meta charset="utf-8">\n'
html += "</head>\n"
html += "<body>\n"
html += '<img src="data:image/jpeg;base64,' + texto_b64 + '">\n'
html += "</body>\n"
html += "</html>\n"

with open("in.html", "w", encoding="utf-8") as saida:
    saida.write(html)

print("in.html criado")