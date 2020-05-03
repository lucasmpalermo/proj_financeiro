# -*- coding: utf-8 -*-
"""
Created on Mon Apr 20 01:11:23 2020

@author: lucas
"""

#importando as bibliotecas necessárias
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import pandas_datareader.data as web
import yfinance as yf
import seaborn as sns

#sobrescreve as buscas de cotacoes do yahoo finance pelo pandasdatareader por essa nova
yf.pdr_override() 


#Obter os dados do ibovespa
ticker = input("Qual ativo gostaria de ver o gráfico?")
sns.set()   
ativo = web.get_data_yahoo(ticker)
ativo["Close"].plot(figsize=(22,8))

plt.xlabel("Ano")
plt.ylabel("Valor")
plt.title("Variação de Preço")
plt.plot()


# Calculo para definir o valor máximo de rolagem em uma THL
vol = float(input("Qual a volatilidade? "))
strike = float(input("Qual o Strike da Opção? "))
val_rol = (strike * (0.32 + ((0.114) * vol))) / 100
print("O valor de rolagem máximo da opção (CALL) deve ser R$ %.2f" % val_rol)

# Calculo para saber o montante final de um investimento
v_inic = float(input("Qual o valor inicial do investimento? "))
duracao = float(input("Daqui a quantos anos vence o seu investimento? "))
taxa_per = float(input("Taxa de retorno anual do investimento (%a.a)? "))
v_final = float(v_inic * (1 + (taxa_per / 100)) ** duracao)
print("Ao final de %d" % duracao + " anos você terá um total de R$ %.2f" % v_final)

