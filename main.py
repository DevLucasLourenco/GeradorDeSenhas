import random
import time as t
from tkinter import *
from tkinter import messagebox



data_atual = t.localtime()
ano, mes, dia, hora, minuto, seg, dia_semana, dia_ano, isdst = data_atual



def adaptar_item(item):
    if item < 10:
        
        return '0' + str(item)
    else:
        return item  


def hora_setup():
    return f'{adaptar_item(dia)}/{adaptar_item(mes)}/{ano} - {adaptar_item(hora)}:{adaptar_item(minuto)}'


def main():
    
    senha = ''.join(random.sample(senha_complementos, tamanho))
    texto  = f'{senha} - {hora_setup()}\n'
    
    try:            
        ########### with read
        with open(f'SenhasGeradas{adaptar_item(dia)}.{adaptar_item(mes)}{ano}.txt', 'r') as arquivo:
            texto_arquivo = arquivo.read()
        

        ############ with write
        
        with open(f'SenhasGeradas{adaptar_item(dia)}.{adaptar_item(mes)}{ano}.txt','w') as arquivo:
            arquivo.write(texto_arquivo)
            arquivo.write(texto)
            

        print('\n'.join([f'Sua senha criada é: {senha}','Programa Encerrado',hora_setup()]))
        


    except:     
        
        with open(f'SenhasGeradas{adaptar_item(dia)}.{adaptar_item(mes)}{ano}.txt','w') as arquivo:
            arquivo.write(texto)
            

        print('\n'.join([f'Sua senha criada é: {senha}','Programa Encerrado',hora_setup()]))
   

def last():
    with open(f'SenhasGeradas{adaptar_item(dia)}.{adaptar_item(mes)}{ano}.txt','r') as file:
        texto_file = file.read()        
        last_password = texto_file.split('\n')
        last_password = last_password[-2]
        messagebox.showinfo('Ultima Senha',last_password)


def inf():
    help = '''
    Made by Lucas Lourenço
    '''
    messagebox.showinfo('Atenção',help)



########## Dados
l_mi = 'abcdefghijklmnopqrstuvwxyz'
l_ma = l_mi.upper()
numeros = '0123456789'
simb = '!@#$&'
tamanho = 12
senha_complementos = l_mi + l_ma + numeros + simb




######## TKinter
master = Tk()
master.geometry('360x260')
master.title('Gerador de Senhas')

master.configure(bg='light grey')


Button(master, 
       text='Start', 
       command=main).place(x=165,y=90)

Button(master, 
       text='Info', 
       command=inf).place(x=165,y=120)

Button(master, 
       text='Última senha', 
       command=last).place(x=140,y=150)


mainloop()