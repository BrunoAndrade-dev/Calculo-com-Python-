# 🎓 Projeto: Análise Espectral de Áudio (DFT Manual)

## ✨ Introdução

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

---

## ⚙️ Estrutura do Repositório

analise_audio/ ├── src/ │ ├── dft_processador.py # Implementação da DFT manual e cálculo da magnitude. │ └── func_auxiliar.py # Funções de I/O (leitura WAV) e vizualizar (Matplotlib). │ ├── data/ │ └── entrada/ # Diretório para colocar o arquivo .wav de entrada. │ ├── main.py # Script principal que coordena a execução e a validação. └── requirements.txt # Lista de dependências Python.



## 🛠️ Instalação e Requisitos

Este projeto requer as seguintes bibliotecas para manipulação numérica e plotagem.

## 1. Instalar as Dependências

Na pasta raiz do projeto, utilize o `pip` para instalar todas as dependências listadas no `requirements.txt`

#```bash
#pip install -r requirements.txt 

## 🧬​ Clonando o Repositório do Git Hub 

. No terminal : 
    - git clone [URL]
    - cd diretorio

##  ​🏃🏻‍♂️​ Run do programa  
    - Dentro do arquivo 'Main.py'
    - Coloque seu arquivo de áudio no diretório /data/entrada
    - Abra o terminal 
    - Navegue para o src ->  cd src
    - python main.py 
    - Ou indo nos comandos de run e debug do próprio Visual Studio Code 

