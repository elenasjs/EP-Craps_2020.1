# -*- coding: utf-8 -*-
"""
Created on Fri Apr  3 22:52:45 2020

@author: Bruno
"""

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