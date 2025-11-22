from src.func_auxiliar import read_wav_file , vizualizar
from src.dft_processador import transformada_Fourier , magnitude
import numpy as np
import os 
audio_name = 'file_example_WAV_5MG.wav'
base_dir = os.path.dirname(os.path.abspath(__file__))
audio_path = os.path.join(base_dir , "data" , "entrada" , audio_name)

def main():
    fs , audio_data = read_wav_file(audio_path)
    if fs is not None and audio_data is not None :
        print ('-=' *30)
        print ('Processamento do áudio pode continuar aqui...')
        print(f'tipo de dados do array de áudio : {audio_data.dtype}')
        print (f'Primeiras 5 amostras do áudio : {audio_data[:5]}')
        N = 1024 
        signal_block = audio_data[:N]
        # Calculo da dft :
        print (f'Iniciando o processamento DFT para os primeiros {N} samples do áudio...')
        X_complexo = transformada_Fourier(signal_block)
        print (f'Resultado da DFT (valores complexos) para os primeiros {N} samples :')
        print (X_complexo)
        # Cálculo da magnitude
        print ('\n Magnitude dos valroes da DFT :')
        result_magnitude = magnitude(X_complexo)
        print ('Resultados da magnitude :')
        print (result_magnitude)
        print ("-=" *30)
        #Plotagem dos resultados
        print ("\n Visualizando os resultados...")
        vizualizar (fs , signal_block, result_magnitude)
        #Iniciando validação dos resultados com numpy.ftt (Prova Cientifica)
        print ("\n ==== Iniciando validação dos resultados com numpy.fft...====")
        X_complexo_np = np.fft.fft(signal_block)
        magnitude_np = np.abs(X_complexo_np)
        #Calculo do erro absoluto :
        erro_absoluto = np.sum(np.abs(result_magnitude - magnitude_np))
        erro_escalar = erro_absoluto.item()
        print (f'A soma total do erro absoluto entre os dois métodos é : {np.sum(erro_absoluto)}')
        if erro_absoluto.item() < 1e-9: 
            print ("Validação bem sucedida! Os resultados estão de acordo com numpy.fft.")
        else :
            print ("\n Houve erro na validação dos resultados com numpy.ftt")
        print ("\n======Processamento concluído.======")
        print ("-=" *30)    
    else :
        print ("Erro na leitura do arquivo de áudio. Verifique o caminho e o formato do arquivo.")
    #Definindo blocos de código para execução direta
if __name__ == '__main__' :
    main()
