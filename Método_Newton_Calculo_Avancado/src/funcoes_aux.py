import sympy as sp 
from sympy.parsing.mathematica import parse_mathematica

def funcao_para_calcular():
    """
    Função para ser definida pelo usuário.
    Retorna uma expressão simbólica.
    """
    x = sp.symbols('x')
    while True : 
        try : 
            print("-=-" * 30 )
            func_str = input("\n Digite a função em termos de x, ex: f(x) = x**3 - 2*x - 5 : \n f(x) = ")
            #Mudança paro o formato matematico do sympy
            func_pronta = sp.sympify(func_str)
            if x not in func_pronta.free_symbols :
                print("\n A função deve depender da variável x.")      
                continue
            print ("-=-" * 30 )
            return func_pronta , x  
        except (sp.SympifyError, SyntaxError) :
            print("\n Função inválida. Tente novamente.")

def derivada_funcao(func_pronta , variavel):
    """ 
    Calcula a derivada simbólica de uma função.
    """
    deriva = sp.diff(func_pronta, variavel )
    return deriva
                
