import scipy.io.wavfile as wav 
import numpy as np 
import os 

def read_wav_file(file_path):
    """
    Lê um arquivo WAV e retorna a taxa de amostragem (Fs) e os dados de áudio.

    Args:
        filepath (str): O caminho completo para o arquivo .wav.

    Returns:
        tuple: (fs, audio_data)
               fs (int): Taxa de amostragem (em Hertz).
               audio_data (np.ndarray): O sinal de áudio como um array NumPy.
    """
    try : 
        fs , data = wav.read(file_path)
        #Mostrando que o arquivo foi lido com sucesso 
        print ('Arquivo lido com sucesso')
        print (f'Taxa de amostragem : {fs} Hz')
        print (f'Duração do áudio : {len(data)/fs:.2f} segundos. ')

        if data.ndim > 1 : #Verificando se o áudio é estéreo, pois, não é possível processar áudio que tenha mais de um canal
            print ('Audio estereofônico detectado. Convertendo para mono...')
            audio_data = data[: , 0]#Pegando apenas o canal esquerdo
        audio_data = audio_data.astype(np.float64) #Normalizando audio para nao ter conflito de tipos
        
        return fs , data 
    
    except FileExistsError as e :
        print ('Erro ao ler o arquivo .wav : ', e)
        return None , None
    except Exception as e :
        print ('Erro inesperado ao ler o arquivo .wav : ', e)
        return None , None
    