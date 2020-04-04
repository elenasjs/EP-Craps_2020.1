# -*- coding: utf-8 -*-
"""
Created on Fri Apr  3 22:22:16 2020

@author: elena
"""

import random
D=150
while D>0:
    print("Voce tem {} fichas".format(D))
    p1= str(input("Voce quer apostar? Sim/Não:"))
    if p1== "Não":
        print("Você saiu do jogo!")
        break
    if p1== "Sim":
        print("Voce esta na fase Come Out")
        aposta= int(input("Quanto voce quer apostar?"))
        tipo_aposta= str(input("Qual aposta voce quer fazer: Pass Line Bet; Field; Any Craps; Twelve?"))
        n= random.randint(2,12)
        if tipo_aposta== "Pass Line Bet":
            print("Soma dos dados é {}".format(n))
            if n==7 or n==11:
                D= D+ aposta
            elif n==2 or n==3 or n==12:
                D= D-aposta
            else:
                print("Voce agora está na fase Point")
                tipo_aposta2=str(input('Voce gostaria de fazer outro tipo de aposta? (Não; Field; Any Craps; Twelve)'))
                if tipo_aposta2== 'Não':
                    x=str(input('Digite j para jogar os dados:'))
                    if x== 'j':
                        n2=random.randint(2,12)
                        print('O novo lançamento dos dados é {}'.format(n2))
                        if n2==n:
                            D=D+aposta
                        if n2==7:
                            D=0
                        else:
                            while n2!=n and n2!=7:
                                x=str(input('Digite j para jogar os dados'))
                                if x=='j':
                                    n2=random.randint(2,12)
                                    print('O novo lancamento dos dados é {}'.format(n2))
                                if n2==7:
                                    D=0
                                if n2==n:
                                    D=D+aposta
                if tipo_aposta2== 'Field': 
                    D=D-aposta
                    aposta2=int(input('Quanto voce quer apostar?'))
                    n2=random.randint(2,12)
                    print('O novo lançamento dos dados é {}'.format(n2)) 
                    if n2== 5 or n2==6 or n2==7 or n2==8:
                        D=0
                    elif n2== 3 or n2==4 or n2==9 or n2==10 or n2==11:
                        D= D+aposta2
                    elif n== 2:
                        D= D + 2*aposta2
                    else:
                        D= D+ 3*aposta2
                if tipo_aposta2== 'Any Craps':
                    D=D-aposta
                    aposta2=int(input('Quanto voce quer apostar?'))
                    n2=random.randint(2,12)
                    print('O novo lançamento dos dados é {}'.format(n2))
                    if n2==2 or n2==3 or n2==12:
                        D= D + 7*aposta2
                    else:
                        D= D- aposta2
                if tipo_aposta2== 'Twelve':
                    D=D-aposta
                    aposta2=int(input('Quanto voce quer apostar?'))
                    n2=random.randint(2,12)
                    print('O novo lançamento dos dados é {}'.format(n2))
                    if n2==12:
                        D=D + 30*aposta2
                    else:
                        D= D-aposta2
        if tipo_aposta== "Field":
            print("Soma dos dados tirada é {}".format(n))
            if n== 5 or n==6 or n==7 or n==8:
                D=0
            elif n== 3 or n==4 or n==9 or n==10 or n==11:
                D= D+aposta
            elif n== 2:
                D= D + 2*aposta
            else:
                D= D+ 3*aposta
            
        if tipo_aposta== "Any Craps":
            print("Soma dos dados tirada é {}".format(n))
            if n==2 or n==3 or n==12:
                D= D + 7*aposta
            else:
                D= D- aposta
        if tipo_aposta== "Twelve":
            print("Soma dos dados tirada é {}".format(n))
            if n==12:
                D=D + 30*aposta
            else:
                D= D-aposta
        if D==0:
            print("Voce não tem mais dinheiro")
            print("Fim de Jogo!")
            break