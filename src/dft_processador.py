import numpy as np 
def transformada_Fourier(sinal) :
    """
    Calcula a Transformada Discreta de Fourier (DFT) de um sinal de entrada.
    
    Args:
        signal (np.ndarray): O array de amostras do sinal no domínio do tempo (x[n]).

    Returns:
        np.ndarray: O array de resultados complexos no domínio da frequência (X[k]).
    """
    N = len(sinal) # Recebe o tamanho do sinal de entrada
    X = np.zeros(N, dtype=complex)  # Inicializa o array de saída com zeros (tipo complexo)     
    for x in range (N):
        sum_complexo = 0.0 + 0.0j  # Inicializa a soma complexa para cada k
        for n in range (N) :
            exponecial = np.exp(-2j *np * x * n / N) # Calcula o termo exponencial da DFT
            sum_complexo += sinal[n] * exponecial  # Acumula a soma complexa
        X[x] = sum_complexo  # Armazena o resultado da soma no array de saída     
    return X 

def magnitude(x) :
    """
    Calcula a magnitude de um array de números complexos.

    Args:
        x (np.ndarray): O array de números complexos.

    Returns:
        np.ndarray: O array contendo as magnitudes correspondentes.
    """
    mag = np.abs(x)  # Calcula a magnitude , ou seja , o módulo dos números complexos 
    return mag

