## Corpo principal do códgigo
from funcao_derivadas_trigonometricas import *
import sympy as sp

# Definindo exemplos para cálculo de derivadas e gráficos
z = sp.symbols('z')
# Exemplo 1: Derivada de uma função trigonométrica
expressao1 = sp.sin(z) + sp.cos(z)
calculo_derivada_(expressao1 , z)
grafico_derivada_trigonometrica(expressao1, z, (-2 *sp.pi, 2 * sp.pi))
expressao2 = sp.cos(z)* 3 - sp.sin(z)*3
calculo_derivada_(expressao2 , z)
grafico_derivada_trigonometrica(expressao2, z, (-2 *sp.pi, 2 * sp.pi))
# Exemplo 2: Derivada de outra função trigonométrica (Secante , cossecante)
expressao3 = sp.sec(z) + sp.csc(z)
calculo_derivada_(expressao3 , z)
grafico_derivada_trigonometrica(expressao3, z, (-2 *sp.pi, 2 * sp.pi))
expressao4 = sp.sec(z)* 3 - sp.csc(z)* 3 
calculo_derivada_(expressao4 , z)
grafico_derivada_trigonometrica(expressao4, z, (-2 *sp.pi, 2 * sp.pi))