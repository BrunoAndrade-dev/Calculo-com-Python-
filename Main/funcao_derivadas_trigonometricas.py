import sympy as sp

z = sp.symbols('z')
i = sp.I  # Unidade imaginária
def calculo_derivada_(expressao , variavel):
    """
    Calcula a derivada de uma expressão em relação a uma variável complexa.
    """
    try:
        derivada = sp.diff(expressao,variavel)
        derivada_simplificada = sp.simplify(derivada)
        print ("-=" * 30)
        print ("Função original : ")
        print ("\n", expressao)
        print ("\n Derivada em relação a uma variável complexa :")
        print ("\n", derivada_simplificada)
        print ("-=" * 30)
    except Exception as e:
        print("Erro ao calcular a derivada:", e)

# Seu arquivo: funcao_derivadas_trigonometricas.py

# Seu arquivo: funcao_derivadas_trigonometricas.py

def grafico_derivada_trigonometrica(expressao, variavel, intervalo):
    
    import matplotlib.pyplot as plt
    derivada = sp.diff(expressao, variavel)
    
    
    p = sp.plot(expressao, derivada, (variavel, intervalo[0], intervalo[1]), 
                show=False, adaptive=False, title='Funções e sua Derivada Trigonométrica')
    p[0].line_color = 'blue'
    p[0].label = 'Função Original'
    p[1].line_color = 'red'
    p[1].label = 'Derivada'
    p.legend = True
    p.show()
    
    
   
    
    
   