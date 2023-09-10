# Monitor de Performance
Adaptação do Monitor de perfomance do sistema operacional em Python

## Exercício proposto:
Observe a figura a seguir. 
![](https://www.bahiajornal.com.br/images/noticias/21520/09f9af0dac6899a6052dd3f9b80d9a29.jpeg)
Dado o cenário, faça um script em python que lê o percentual de uso da CPU, percentual de uso de disco e percentual de uso da memória. 

São 3 máquinas laranjas de recarga de bilhete único, que contém um sistema computacional, com cpu, memória e disco em cada uma delas.

A máquina azul ao lado das 3 laranjas é a máquina servidora, e seu processador (CPU), disco e memória estão na Cloud da AWS.
Esta máquina azul tem apenas um monitor e sua conexão com a internet para enviar todos os dados ao servidor da nuvem. 

O seu script em Python deve coletar dados de CPU1, MEMO1 e DISCO 1 (simulado pelos valores do seu computador em sala de aula).
No Script em python vc vai capturar essa leitura várias vezes, automatizando a captura. Além disso, você precisa capturar os dados das demais máquinas.

Faça no mesmo script uma simulação, com os seguintes requisitos: 

- CPU2 tem mais 10% da CPU1 e menos 5% da CPU3
- MEMO2 tem mais 15% da MEMO1 e mais 5 % da MEMO3
- DISCO2 tem menos 5% do DISCO1 e é 1/3 do DISCO3
