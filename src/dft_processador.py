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
    X = np.zeros(N, dtype=np.complex128)      
    for k in range (N):
        soma_complexo = complex(0.0 , 0.0)  
        for n in range (N) :
            exponecial = np.exp(-1j *2* np.pi *  k * n / N) 
            soma_complexo += np.float64(sinal[n]) * exponecial  
        X[k] = soma_complexo  
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

