from tkinter import *
from tkinter.ttk import *
from time import sleep as s
import psutil as ps

root = Tk()
root.title("Monitor de Performance")
root.resizable(False,False)
root.iconbitmap("./assets/favicon.ico")

# Informações do usuário ===============================================
containerInfos = LabelFrame(root, text="Informações do sistema operacional")
containerInfos.grid(column=0,row=0,padx=20,pady=30)

containerUser = LabelFrame(containerInfos, text="Informações de usuário")
containerUser.grid(column=0,row=0)
lbUsuario = Label(containerUser, text=("Usuário atual: "+ps.users()[0].name))
lbUsuario.pack()

# Informações da máquina (PRINCIPAL) ===============================================
containerDesemp = LabelFrame(containerInfos, text="Informações de desempenho")
containerDesemp.grid(column=0,row=1)

# Configurações ===============================================
containerOpt = LabelFrame(containerInfos,  text="Opções")
containerOpt.grid(column=0,row=2)

containerTempoAtualiz = LabelFrame(containerOpt, text="Tempo de atualização dos dados (em segundos)")
containerTempoAtualiz.pack()

tempoAtualizacao = StringVar()
cmbTempoAtualiz = Combobox(containerTempoAtualiz, textvariable=tempoAtualizacao)
cmbTempoAtualiz["values"] = ("1","3","5","10","15")
cmbTempoAtualiz["state"] = "readonly"
cmbTempoAtualiz.set(cmbTempoAtualiz["values"][1])
cmbTempoAtualiz.pack()

# Campos da estrutura do desempenho ===============================================
colunas = ("CPU","Disco","Memória RAM")

infos = (
("Processadores físicos","Processadores lógicos","Frequência","Percentual de uso"),
("Número de partições","Total","Uso atual","Percentual de uso"),
("Total","Uso atual","Percentual de uso"))

CPUFisc = StringVar()
CPULogc = StringVar()
CPUFreq = StringVar()
CPUPercent = StringVar()

HDNumParcs = StringVar()
HDTotal = StringVar()
HDAtual = StringVar()
HDPercent = StringVar()

RAMTot = StringVar()
RAMAtual = StringVar()
RAMPercent = StringVar()

dados = ((CPUFisc,CPULogc,CPUFreq,CPUPercent),(HDNumParcs,HDTotal,HDAtual,HDPercent),(RAMTot,RAMAtual,RAMPercent))

indiceGrid = 0
for coluna in colunas:
    div = LabelFrame(containerDesemp,text=coluna)
    div.grid(column=indiceGrid,row=0,ipadx=0,ipady=0)

    i=0
    for info in infos[indiceGrid]:
        divInfo = LabelFrame(div,text=info)
        lbDado = Label(divInfo,textvariable=dados[indiceGrid][i])
        divInfo.pack()
        lbDado.pack()
        i += 1
    
    indiceGrid += 1

while(True):
    dados[0][0].set(str(ps.cpu_count(False)))
    dados[0][1].set(str(ps.cpu_count(True)))
    dados[0][2].set(str(ps.cpu_freq(False).current)+"MHz")
    dados[0][3].set(str(round(100-ps.cpu_times_percent(interval=1)[2],1))+"%")

    dados[1][0].set(str(len(ps.disk_partitions(True))))
    dados[1][1].set(str(round((ps.disk_usage("/").used)*10**-9,2))+"GB")
    dados[1][2].set(str(round((ps.disk_usage("/").total)*10**-9,2))+"GB")
    dados[1][3].set(str(ps.disk_usage("/").percent)+"%")

    dados[2][0].set(str(round((ps.virtual_memory().total)*10**-9,2))+"GB")
    dados[2][1].set(str(round((ps.virtual_memory().used)*10**-9,2))+"GB")
    dados[2][2].set(str(ps.virtual_memory().percent)+"%")
    root.update()
    s(int(tempoAtualizacao.get()))