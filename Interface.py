# Nome do grupo: Plane-It
#Nome do aluno: Gustavo Pereira Castro
#RA do aluno: 02231052

from tkinter import *
from tkinter.ttk import *
from tkinter.scrolledtext import ScrolledText
import time as t
import psutil as ps
import mysql.connector

tDados = mysql.connector.connect(
    host="localhost",
    user="acessoProducao",
    password="urubu100",
    database="monitorBilhete"
)
cursorBanco = tDados.cursor()

root = Tk()
root.title("Monitor de Máquinas Bilhete Único")
root.resizable(False,False)
root.iconbitmap("./assets/favicon.ico")

# Informações do usuário ===============================================
containerInfos = LabelFrame(root, text="Informações do sistema operacional")
containerInfos.grid(column=0,row=0,padx=20,pady=30)

# Informações da máquina (PRINCIPAL) ===============================================
containerDesemp = LabelFrame(containerInfos, text="Desempenho das máquinas")
containerDesemp.grid(column=0,row=1)
# Historico
containerHistorico = LabelFrame(containerInfos, text="Histórico")
containerHistorico.grid(column=0,row=2)
historico = ScrolledText(containerHistorico,height="10",width="70")
historico["state"] = "disabled"
historico.pack()

# Configurações ===============================================
containerOpt = LabelFrame(containerInfos,  text="Opções")
containerOpt.grid(column=0,row=3)

containerTempoAtualiz = LabelFrame(containerOpt, text="Tempo de atualização dos dados (em segundos)")
containerTempoAtualiz.pack()

tempoAtualizacao = StringVar()
cmbTempoAtualiz = Combobox(containerTempoAtualiz, textvariable=tempoAtualizacao)
cmbTempoAtualiz["values"] = ("1","3","5","10","15")
cmbTempoAtualiz["state"] = "readonly"
cmbTempoAtualiz.set(cmbTempoAtualiz["values"][0])
cmbTempoAtualiz.pack()

# Campos da estrutura do desempenho ===============================================
colunas = ("Recarga 1","Recarga 2","Recarga 3")

infos = ("Uso da CPU","Uso da memória","Uso de disco")

cpu1 = StringVar()
mem1 = StringVar()
disc1 = StringVar()

cpu2 = StringVar()
mem2 = StringVar()
disc2 = StringVar()

cpu3 = StringVar()
mem3 = StringVar()
disc3 = StringVar()

dados = ((cpu1,mem1,disc1),(cpu2,mem2,disc2),(cpu3,mem3,disc3))

indiceGrid = 0
for coluna in colunas:
    div = LabelFrame(containerDesemp,text=coluna)
    div.grid(column=indiceGrid,row=0,ipadx=0,ipady=0)

    i=0
    for info in infos:
        divInfo = LabelFrame(div,text=info)
        lbDado = Label(divInfo,textvariable=dados[indiceGrid][i])
        divInfo.pack()
        lbDado.pack()
        i += 1
    
    indiceGrid += 1

# Renderização da parte gráfica =================================================================
while(True):
    tcpu1 = round(100-ps.cpu_times_percent(interval=1)[2],1)
    tmem1 = ps.virtual_memory().percent
    tdisc1 = ps.disk_usage("/").percent

    tcpu2 = tcpu1*1.1
    tmem2 = tmem1*1.15
    tdisc2 = tdisc1*0.95

    tcpu3 = tcpu2*1.05
    tmem3 = tmem2*0.95
    tdisc3 = tdisc2*1.33

    temp = ((tcpu1,tmem1,tdisc1),(tcpu2,tmem2,tdisc2),(tcpu3,tmem3,tdisc3))
    
    historico["state"] = "normal"
    historico.insert("0.0","\n\n")
    c = 0
    for dadoColuna in dados:
        d = 0
        for dadoLinha in dados[c]:
            dadoLinha.set(str(round(temp[c][d],1))+" %")
            historico.insert("0.0"," | "+infos[d]+": "+dadoLinha.get())
            d+=1
        historico.insert("0.0","\nMáquina "+str(c+1)+"\n")
        c+=1
    historico.insert("0.0","["+t.strftime("%H:%M:%S",t.gmtime())+"]")
    historico["state"] = "disabled"

    root.update()
    t.sleep(int(tempoAtualizacao.get()))

    sql = "INSERT INTO dados VALUES (%s, %s, %s, %s, %s, now())"
    idMaquina = 1
    idDado = 0
    for dadoColuna in dados:
        valor = list()
        valor.append(idMaquina)
        cursorBanco.execute("select idDado from dados where idMaquina = %s order by idDado desc",valor)
        resultado = cursorBanco.fetchall()
        if(len(resultado) == 0):
            idDado = 1
        else:
            idDado = int(str(resultado[0][0]))+1

        valores = list()
        valores.append(idMaquina)
        valores.append(idDado)
        idComponente = 0
        for dadoLinha in dadoColuna:
            valores.append(temp[idMaquina-1][idComponente])
            idComponente+=1
        cursorBanco.execute(sql, valores)
        idMaquina+=1

        tDados.commit()
        print(cursorBanco.rowcount, "tupla inserida.")