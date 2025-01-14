import pyautogui
import time

pyautogui.PAUSE = 0.5 #esperar 0.5 segundos entre os comandos

# pyautogui.press -> pressionar uma tecla
# pyautogui.write -> escrever
# pyautogui.click -> clicar
# pyauotgui.hotkey -> atalho ("ctrl", "c")

pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")

pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")

# esperar alguns segundos para realizar outro comando
time.sleep(0.5)

# fazer login
pyautogui.click(x=372, y=357)
pyautogui.write("gab7@gmail.com")
pyautogui.press("tab") #passa para o campo senha
pyautogui.write("gab777")
pyautogui.press("tab") #passa para o botão "logar"
pyautogui.press("enter")

# importar a base de dados dos produtos
import pandas
tabela = pandas.read_csv("produtos.csv")

# cadastrar os produtos

for linha in tabela.index:
    pyautogui.click(x=312, y=253) #clicar no 1º campo

    #código
    codigo = tabela.loc[linha, "codigo"]
    pyautogui.write(str(codigo)) 
    pyautogui.press("tab")

    #marca
    marca = tabela.loc[linha, "marca"]
    pyautogui.write(str(marca)) 
    pyautogui.press("tab")

    #tipo
    tipo = tabela.loc[linha, "tipo"]
    pyautogui.write(str(tipo))
    pyautogui.press("tab")

    #categoria
    categoria = tabela.loc[linha, "categoria"]
    pyautogui.write(str(categoria)) 
    pyautogui.press("tab")

    #preço
    preco_unitario = tabela.loc[linha, "preco_unitario"]
    pyautogui.write(str(preco_unitario)) 
    pyautogui.press("tab")

    #custo
    custo = tabela.loc[linha, "custo"]
    pyautogui.write(str(custo)) 
    pyautogui.press("tab")

    #obs
    obs = str(tabela.loc[linha, "obs"])
    if obs != "nan":
        pyautogui.write(obs)
    pyautogui.press("tab")
    # nan = valor vazio em uma base de dados (not a number)

    pyautogui.press("enter") #apertar o botão de enviar

# numero positivo = scroll para cima
# numero negativo = scroll para baixo
# pyautogui.scroll(500)
