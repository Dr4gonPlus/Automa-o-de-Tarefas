# Algoritmo para automação de tarefas

import pyautogui
import time 
import pandas 

# Passo 1: abrir o navegador  

pyautogui.PAUSE = 0.5

pyautogui.press("win")

pyautogui.write("Microsoft Edge")

pyautogui.press("enter")

# Passo 2: Entrar no sistema da empresa - https://dlp.hashtagtreinamentos.com/python/intensivao/login

link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"

pyautogui.write(link)

pyautogui.press("enter")

time.sleep(2)

# Passo 3: Fazer login

pyautogui.click(x=1163, y=447)
pyautogui.write("dr4gonplusfyre@gmail.com")

#3.1: passar para o próximo campo sem a necessidade de usar o pyauto.click com a tecla tab

pyautogui.press("tab")
pyautogui.write("minha senha aqui")

pyautogui.click(x=977, y=645, clicks=2)

time.sleep(2)

# Passo 4: Importar a base de dados 

tabela = pandas.read_csv("produtos.csv")
print(tabela)


# Passo 5: Cadastrar 1 produto

# 5.1 prenchimento dos campos:

# para cada linha da minha tabela

for linha in tabela.index:
    
    pyautogui.click(x=1061, y=315)

    # codigo
    codigo = tabela.loc[linha, "codigo"]
    pyautogui.write(str(codigo))
    pyautogui.press("tab")

    # marca
    marca = tabela.loc[linha, "marca"]
    pyautogui.write(str(marca))
    pyautogui.press("tab")

    # tipo
    tipo = tabela.loc[linha, "tipo"]
    pyautogui.write(str(tipo))
    pyautogui.press("tab")

    # categoria
    categoria = tabela.loc[linha, "categoria"]
    pyautogui.write(str(categoria))
    pyautogui.press("tab")

    # preço unitario
    preco = tabela.loc[linha, "preco_unitario"]
    pyautogui.write(str(preco))
    pyautogui.press("tab")

    # custo
    custo = tabela.loc[linha, "custo"]
    pyautogui.write(str(custo))
    pyautogui.press("tab")

    # obs
    obs = tabela.loc[linha, "obs"]
    if not pandas.isna(obs):
        pyautogui.write(str(obs))
    pyautogui.press("tab")

    # clicar no botão enviar 

    pyautogui.press("enter")
    pyautogui.scroll(5000)

    # Passo 6: Repetir o processo de cadastro até acabar os produtos

