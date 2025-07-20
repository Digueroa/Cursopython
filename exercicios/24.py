"""Exercício Python 24: Crie um programa que leia o nome de uma cidade diga se ela começa ou não com o nome “SANTO”.´
"""
n1=input("Digite o nome de uma Cidade?\n").strip()
print(n1[:5].upper()=="SANTO")
print(n1[-5:].upper()=="SANTO")