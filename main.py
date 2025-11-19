from func_auxiliar import read_wav_file
from dft_processador import transformada_Fourier , magnitude
import os 
audio_name = 'meu_audio.wav'
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
        print (f'Iniciando o processamento DFT para os primeiros {N} samples do áudio...')
        X_complexo = transformada_Fourier(signal_block)
        print (f'Resultado da DFT (valores complexos) para os primeiros {N} samples :')
        print (X_complexo)
        print ('\n Magnitude dos valroes da DFT :')
        result_magnitude = magnitude(X_complexo)
        print ('Resultados da magnitude :')
        print (result_magnitude)
    print ('\nFim do processamento ')

    #Definindo blocos de código para execução direta
    if __name__ == '__main__' :
        main()
