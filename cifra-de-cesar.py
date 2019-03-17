# Autor: Gabriel Fiorese Zancanela
# Professor: Ausberto S. Castro Vera
# Código auxiliar: https://github.com/python-cafe/exemplos/tree/master/criptografia

from tkinter import filedialog
from tkinter import *
from pathlib import Path
from tkinter import messagebox

# Início da janela gráfica
janela = Tk()
# Título da janela gráfica
janela.title("Criptografia de arquivos com Cifra de César by Gabriel Fiorese")
janela.iconbitmap("cripto_icon.ico")

# Chave de criptografia
chave = 7


# Função que altera o conteúdo do arquivo
def substituir(ind, chave, inicio, fim):
    n = fim - inicio + 1
    k = (ind + chave)%(fim+1) + ((ind + chave)//(fim+1))*inicio
    if ind + chave < inicio:
        k = k + n
    return chr(k)

# Função que criptografa/descriptografa o conteúdo do arquivo
def criptografar(mensagem, chave):
    nA, nZ, na, nz = ord('A'), ord('Z'), ord('a'), ord('z')
    cifrada = ""
    for caracter in mensagem:

        ind = ord(caracter)
        nova_letra = caracter

        if nA <= ind <= nZ:
            nova_letra = substituir(ind, chave, nA, nZ)

        elif ind in range(na, nz + 1):
            nova_letra = substituir(ind, chave, na, nz)

        cifrada = cifrada + nova_letra

    return cifrada

# ----------------- fim criptografia ---------------


# Função acionada pelo botão de procurar arquivo, que localiza o diretório e o arquivo txt para ser criptografado/descriptografado
def browse_button():
    janela.filename =  filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("text files","*.txt"),("all files","*.*")))
    link.configure(text=janela.filename)

    global conteudo
    global link_arquivo2

    link_arquivo = Path((janela.filename))
    link_arquivo2 = janela.filename[:-4]

    print (link_arquivo2)

    arquivo = open(link_arquivo, "r")
    conteudo = arquivo.read()
    arquivo.close()
    
    Texto1.delete(1.0,END)
    Texto1.insert(1.0,conteudo)



# Função acionada pelo botão de salvar, que salva o novo arquivo criptografado/descriptografado na mesma página que o arquivo original
def salvar():
    salvando = link_arquivo2+"_"+acao+".txt"
    arquivo = open(salvando, "w")
    arquivo.write(conteudo_mudado)
    arquivo.close()
    print ('feito!')
    messagebox.showinfo("Mensagem", "Arquivo salvo com sucesso!")


# Função acionada pelo botão de criptografia
def crip():
    global conteudo_mudado
    global acao
    acao = 'criptografado'
    conteudo_mudado = criptografar(conteudo, chave)
    titulo3.configure(text="Conteúdo criptografado com Cifra de César:", font=("Helvetica", 10, "bold"))
    Texto2.delete(1.0,END)
    Texto2.insert(1.0,conteudo_mudado)

# Função acionada pelo botão de descriptografia
def descrip():
    global conteudo_mudado
    global acao
    acao = 'descriptografado'
    conteudo_mudado = criptografar(conteudo, -chave)
    titulo3.configure(text="Conteúdo descriptografado com Cifra de César:", font=("Helvetica", 10, "bold"))
    Texto2.delete(1.0,END)
    Texto2.insert(1.0,conteudo_mudado)

# Componentes da janela gráfica
titulo = Label(text="Selecione uma arquivo do computador e uma opção desejada", font=("Helvetica", 13, "bold"), width=55, height=2)
button2 = Button(text="Procurar", command=browse_button, width=10, height=2)
bt1 = Button(janela, width=25, height=2, text="Criptografar", font="bold", command=crip)
bt2 = Button(janela, width=25, height=2, text="Descriptografar", font="bold", command=descrip)
link = Label(text="", height=3, font=("Helvetica", 10))
titulo2 = Label(text="Conteúdo do arquivo", font=("Helvetica", 10, "bold"))
Texto1 = Text(janela, height=6, width=50)
titulo3 = Label(text="", font=("Helvetica", 10, "bold"))
Texto2 = Text(janela, height=6, width=50)
bt3 = Button(janela, width=10, height=2, text="Salvar", font="bold", command=salvar)

# Posição dos componentes na janela gráfica
titulo.grid(row=1, column=0, columnspan=6, sticky=W+E)
button2.grid(row=2, column=0, padx=20)
link.grid(row=2, column=1, columnspan=4, sticky=W)
titulo2.grid(row=3, column=0, columnspan=6, sticky=W, padx=20)
Texto1.grid(row=4, column=0, columnspan=6, sticky=W+E, padx=20)
bt1.grid(row=5, column=2, pady=20, padx=10)
bt2.grid(row=5, column=3)
titulo3.grid(row=6, column=0, columnspan=6, sticky=W, padx=20)
Texto2.grid(row=7, column=0, columnspan=6, sticky=W+E, padx=20)
bt3.grid(row=8, column=5, pady=20, padx=20)

# Dimensões da janela gráfica (LarguraXAltura + DistanciaEsquerda + DistanciaDireita)
janela.geometry("750x525+300+100")

janela.mainloop()