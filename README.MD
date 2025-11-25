# 🎓 Projeto Variáveis Complexas : 

## ✨ Seção 1  Análise Espectral de Áudio (DFT Manual) -->

Este projeto foi desenvolvido como um requisito prático para a disciplina de **Variáveis Complexas**. Ele demonstra a aplicação fundamental dos **números complexos** no campo do Processamento Digital de Sinais, especificamente através da implementação da **Transformada Discreta de Fourier (DFT)**.

O objetivo principal é decompor um sinal de áudio do domínio do tempo para o domínio da frequência, e provar que a implementação manual da DFT é matematicamente precisa.

---

## 🎯 Objetivos do Projeto

### 1. Aplicação de Conceitos Complexos

* **Implementação da DFT:** Codificar manualmente a fórmula da DFT, utilizando a **aritmética de números complexos** de Python, onde a parte real e a parte imaginária são essenciais para determinar a amplitude e a fase de cada frequência.
* **Validação Científica:** Comparar os resultados da DFT manual com a função otimizada de alto desempenho do NumPy (`np.fft.fft`), obtendo um **Erro Absoluto** residual mínimo.

### 2. Funcionalidade e Análise

* **Processamento de Sinais:** Utilizar a biblioteca SciPy para ler, pré-processar (conversão para mono e `float64`) e manipular as amostras de áudio.
* **Visualização:** Gerar gráficos que mostram o sinal no **Domínio do Tempo** e o **Espectro de Frequência** (Magnitude), permitindo a interpretação dos dados. [Image of the Fourier Transform showing a time-domain signal and its frequency-domain spectrum]

## 📐 Seção 2: Derivadas Trigonométricas com Variáveis Complexas

### ⚛️ Objetivos do Projeto de Derivadas

Este módulo anterior foca na aplicação de conceitos complexos para simplificar ou resolver operações de cálculo diferencial.

* **Derivação Simbólica/Numérica:** Implementar a lógica para calcular as derivadas de funções trigonométricas (como seno e cosseno) dentro do contexto da aritmética complexa.
* **Conexão com a Fórmula de Euler:** O projeto aproveita o fato de que as funções trigonométricas podem ser expressas usando a **Fórmula de Euler** ($e^{i\theta} = \cos(\theta) + i \sin(\theta)$), que é fundamental para a análise complexa e simplifica muitas operações de cálculo.
* **Demonstração da Propriedade:** Mostrar como as propriedades das exponenciais complexas são aplicadas à diferenciação, ilustrando que a derivada de $e^{ax}$ é $a e^{ax}$, o que é transferível para as funções seno e cosseno.

O projeto executa os seguintes passos para cada expressão:

1.  **Definição da Expressão:** Define uma função simbólica em 'z' (ex: sin(z) + cos(z)).
2.  **Cálculo Simbólico:** A função `calculo_derivada_` usa `SymPy` para encontrar a derivada da expressão em relação à variável 'z'.
3.  **Visualização:** A função `grafico_derivada_trigonometrica` usa `Matplotlib` para plotar a função original e sua respectiva derivada no mesmo gráfico, permitindo a **comparação visual** dos resultados.

### 📁 Módulos Relacionados às Derivadas

* `Main/funcao_derivadas_trigonometricas.py`
* `Main/Code.py`
---

## ⚙️ Estrutura do Repositório

Calculo-com-Python-/ ├── src/ │ ├── dft_processador.py # Implementação da DFT manual e cálculo da magnitude. │ └── func_auxiliar.py # Funções de I/O (leitura WAV) e vizualizar (plotagem). │ ├── Main/ │ ├── Code.py │ └── funcao_derivadas_trigonometricas.py # Código do projeto de Derivadas. │ ├── data/ │ └── entrada/ # Diretório para colocar o arquivo .wav de entrada. │ ├── main.py # Script principal para execução e validação do DFT. └── requirements.txt # Lista de dependências Python.

## 🛠️ Instalação e Requisitos

### 1. Início Rápido (Clonar Repositório)

Para começar a trabalhar no projeto, clone o repositório para sua máquina local :

### ```bash
git clone [URL]
#cd Calculo-com-Python-

## 1. Instalar as Dependências

Na pasta raiz do projeto, utilize o `pip` para instalar todas as dependências listadas no `requirements.txt`

#```bash
#pip install -r requirements.txt 

###  ​🏃🏻‍♂️​ Run do Projeto 
##      Transformada de Fourier 
        - Dentro do arquivo 'Main.py'
        - Coloque seu arquivo de áudio no diretório /data/entrada
        - Abra o terminal 
        - Navegue para o src ->  cd src
        - python main.py 
        - Ou indo nos comandos de run e debug do próprio Visual Studio Code 

##      Derivadas Trigonométricas 
        - Dentro do arquivo Main navegue até Code.py
        - Abra o terminal 
        - digite : python code.py
        - Ou pelos comandos do VScode 

