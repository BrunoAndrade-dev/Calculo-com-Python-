
import sys
import os
sys.path.append( os.path.abspath( os.path.join( os.path.dirname(__file__) , '..' , 'src' ) ) )
from funcoes_aux import *
import numpy as np 
import matplotlib.pyplot as plt
import sympy as sp

def metodo_newton(func_pronta , deriva ,x_simbolo ,  x0, tol = 1e-6 , max_iter = 50 ):
    """
    Implementa o Método de Newton para encontrar raízes de uma função.
    """
    print ("-=-" *30)
    print ("\n Entrada dos dados para o Método de Newton: " )
    print ("-=-" *30)
    X_n = x0
    erros = []
    print ("\n Iniciando o Método com x0 = {:.6f}, tol = {}, max_iter = {}".format(x0, tol, max_iter) )
    # Criamos "funções lambdas" (funções anônimas) para avaliar rapidamente.
    # O SymPy converte a expressão simbólica para uma função que o Python pode calcular.
    f_num = sp.lambdify(x_simbolo, func_pronta, "numpy")
    f_derivada_num = sp.lambdify(x_simbolo, deriva, "numpy")
    for n in range (1, max_iter + 1 ) :
        f_val = f_num(X_n)
        f_derivada_val = f_derivada_num(X_n)
        erro = abs(f_val)
        erros.append(erro)
        if abs(f_derivada_val) < 1e-10:
            print ("\n Derivada muito próxima de zero. O método falhou.")
            return None
        X_n1 = X_n - f_val / f_derivada_val #Formula do metodo de newton 
        erro = abs(X_n1 - X_n)
        print (" Iteração {}: x = {:.6f}, f(x) = {:.6f}".format(n, X_n1, f_num(X_n1)) )
        if erro < tol : 
           
                print ("\n Raiz encontrada: x = {:.6f}, f(x) = {:.6f}, após {} iterações.".format(X_n1, f_num(X_n1), n) )
                
        X_n = X_n1
    if erro <tol :
        try:
            iteracoes = np.arange(1, n+1)
            plt.figure(figsize=(10,6))
            plt.semilogy(iteracoes , erros , marker = 'o' , linestyle = '--' , color = 'b' )
            plt.title("Convergência do Método de Newton")
            plt.xlabel("Número de Iterações")
            plt.ylabel("Erro absoluto")
            plt.grid(True , which = 'both' , linestyle = '--' , linewidth = 0.5)
            plt.show()
            print ("-=-" *30)
            print ("\n Plotagem feita com sucesso. ")
        except TypeError as e  :
            print ("\n Falha ao plotar o gráfico de convergência: {}".format(e) )
            return X_n1
            
                  
    print ("-=-" *30)
    print ("\n O Metodo de Newton não convergiu após {} iterações.".format(max_iter) )
    print ("-=-" *30)
    return None 

if __name__ == "__main__" :
   func_pronta , x_simbolo = funcao_para_calcular()
   calc_derivada = derivada_funcao(func_pronta , x_simbolo := sp.symbols('x') )
   print ("-=-" *30)
   print (f"\n  A função definida pelo usuário é :f(x)= {func_pronta} " )
   print (f"\n  A derivada da função é : f'(x) = {calc_derivada} " )
   print ("-=-" *30)
   while True :
       try:
            x0_input = input("\n Digite o valor inicial x0 para o Método de Newton (ex: 1.0) : \n x0 = ")
            x0 = float(x0_input)
            break
       except ValueError :
            print ("\n Valor inválido para x0. Tente novamente.")
   metodo_newton(func_pronta , calc_derivada , x_simbolo , x0)
