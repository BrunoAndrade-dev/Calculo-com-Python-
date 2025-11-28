import streamlit as st
from calcular_newton import calcular_newton
import sympy as sp
import numpy as np
import matplotlib.pyplot as plt
st.title(" 💻​➕​➖​ Cálculo Avançado: Método de Newton")
st.markdown(st.markdown("""

---

## 📖 Visão Geral do Projeto

Este projeto implementa o **Método de Newton-Raphson**, um dos algoritmos numéricos mais eficientes para encontrar as **raízes (zeros)** de uma função $f(x)$. A aplicação utiliza o poder das bibliotecas Python, como o **SymPy** (para cálculo simbólico da derivada) e o **Matplotlib** (para visualização gráfica).

O principal objetivo é permitir que o usuário insira uma função qualquer, o chute inicial ($x_0$), e observe o processo iterativo de convergência.

---

## 💡 O Método de Newton em Resumo

O método se baseia na ideia geométrica de usar a **reta tangente** à curva da função para encontrar uma aproximação cada vez melhor da raiz.



### A Fórmula Iterativa

O próximo valor de $x$ é calculado a partir do valor atual, subtraindo o quociente da função pelo valor da sua derivada:

$$x_{n+1} = x_n - \\frac{f(x_n)}{f'(x_n)}$$

### Convergência (Taxa de Erro)

O método é conhecido por sua **convergência quadrática** (ordem 2). Isso significa que, quando a aproximação está próxima da raiz, o número de dígitos corretos **dobra** a cada nova iteração, resultando em uma convergência extremamente rápida.

---

## 🚀 Funcionalidades da Aplicação

A interface construída no Streamlit oferece:

1.  **Entrada de Dados:** Widgets para digitar a função $f(x)$, o chute inicial ($x_0$) e a tolerância ($\epsilon$).
2.  **Cálculo Automático:** O **SymPy** calcula e exibe a derivada $f'(x)$ simbolicamente.
3.  **Tabela de Iterações:** Exibe a convergência passo a passo, mostrando $x_{n}$, $f(x_n)$ e o **Erro Absoluto** a cada etapa.
4.  **Gráfico de Erro:** Plota o **Erro Absoluto vs. Número de Iterações** em escala logarítmica, demonstrando visualmente a rapidez da convergência quadrática.
"""))

tab1, tab2 = st.tabs(['📥 Entrada de Dados', '📊 Resultados e Visualizações'])

with tab1 :
    st.header("📥 Entrada de Dados para o Método de Newton")
    st.markdown("""
    Insira a função \( f(x) \), o chute inicial \( x_0 \), a tolerância \( \epsilon \) e o número máximo de iterações.
    """)
    x = sp.symbols('x')
    func_input = st.text_input("Digite a função \( f(x) \):", "x**3 - 2*x - 5")
    x0_input = st.number_input("Chute inicial \( x_0 \):", value=2.0)
    tol_input = st.number_input("Tolerância \( \epsilon \):", value=1e-6, format="%.10f")
    max_iter_input = st.number_input("Número máximo de iterações:", min_value=1, value=50)
    
    try:
        func_pronta = sp.sympify(func_input)
        if x not in func_pronta.free_symbols:
            st.error("A função deve depender da variável x.")
            st.stop()
        deriva = sp.diff(func_pronta, x)
        st.success(f"Derivada calculada: \( f'(x) = {sp.latex(deriva)} \)")
    except (sp.SympifyError, SyntaxError):
        st.error("Função inválida. Tente novamente.")
        st.stop()
    
    if st.button("Calcular Raiz usando o Método de Newton"):
        tabela_dados, erros, raiz, status_msg = calcular_newton(
            sp.lambdify(x, func_pronta, "numpy"),
            sp.lambdify(x, deriva, "numpy"),
            x0_input,
            tol_input,
            max_iter_input
        )
        
        with tab2:
            st.header("📊 Resultados e Visualizações do Método de Newton")
            st.subheader("Status da Execução")
            st.write(status_msg)
            
            if tabela_dados:
                st.subheader("Tabela de Iterações")
                st.table(tabela_dados)
                
                st.subheader("Gráfico de Erro Absoluto")
                iteracoes = np.arange(1, len(erros) + 1)
                plt.figure(figsize=(10,6))
                plt.semilogy(iteracoes, erros, marker='o', linestyle='--', color='b')
                plt.title("Convergência do Método de Newton")
                plt.xlabel("Número de Iterações")
                plt.ylabel("Erro Absoluto")
                plt.grid(True, which='both', linestyle='--', linewidth=0.5)
                st.pyplot(plt)
