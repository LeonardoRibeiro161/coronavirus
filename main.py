import requests
import json
import matplotlib as plt
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
#api = "https://covid19-brazil-api.now.sh/api/report/v1"
api = "https://covid19-brazil-api.now.sh/api/report/v1/brazil/uf/"

uf = input("Informe o UF do estado:")
resposta = requests.get(api+uf)
#resposta = json.loads(resposta.text)

resposta = resposta.json()

print("Estado:"+str(resposta['state']))
print("Casos Confirmados:"+str(resposta['cases']))
print("Mortos:"+str(resposta['deaths']))
print("Suspeitos:"+str(resposta['suspects']))

estados = ('Confirmados', 'Mortos','Suspeitos')
y_posicao = np.arange(len(estados))
dados = [int(resposta['cases']), int(resposta['deaths']), int(resposta['suspects'])]

#Configuracao do grafigo

plt.bar(y_posicao,dados,align='center',width=0.5)
plt.xticks(y_posicao,estados)
plt.ylabel('Casos')
plt.title('Casos de Corona Virus em '+resposta['state'])
#plt.savefig("test.png")
plt.show()