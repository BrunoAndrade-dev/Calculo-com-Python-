import scipy.io.wavfile as wav 
import numpy as np 
import os 
import matplotlib.pyplot as plt

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
        
        return fs , audio_data 
    
    except FileExistsError as e :
        print ('Erro ao ler o arquivo .wav : ', e)
        return None , None
    except Exception as e :
        print ('Erro inesperado ao ler o arquivo .wav : ', e)
        return None , None
    
def vizualizar (fs , audio_data , magnitude=False):  
    """
    Função para visualizar o sinal de áudio e sua magnitude por meior de gráfico 

    """
    N = len(audio_data)
    time = np.arange(0 , N) / fs
    freq_axis = np.arange(0, N )* fs / N 
    metade_N = N// 2 
    freq_axis = freq_axis[:metade_N]
    spectrum_plot = magnitude[:metade_N]
    plt.figure(figsize =(14,6))

    #Primeiro subplot 
    plt.subplot(2,2,1)
    plt.plot(time, audio_data)
    plt.title('Sinal de Áudio no Domínio do Tempo')
    plt.xlabel('Tempo (s)')
    plt.ylabel('Amplitude')
    plt.grid(True)

    #Segundo subplot
    plt.subplot(2,2,2)
    plt.plot(freq_axis, spectrum_plot)
    plt.title('Espectro de Frequência')
    plt.xlabel('Frequência (Hz)')
    plt.ylabel('Magnitude')
    plt.grid(True)
    plt.tight_layout()
    try :
        plt.savefig('data/saida/visualizacao_audio.png')
        print ('Gráfico salvo em data/saida/visualizacao_audio.png')
    except Exception as e :
        print ('Erro ao salvar o gráfico : ', e)    
    plt.show()
    