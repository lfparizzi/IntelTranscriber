import os
import time
import subprocess

# Configurações
folder_to_watch = r"E:\Google Drive\Meu Drive\Automação"  # Substitua pelo caminho da sua pasta
processed_files = set()  # Para rastrear arquivos já processados
audio_extensions = ('.mp3', '.MP3', '.wav', '.m4a', '.flac', '.aac', '.ogg', '.wma')

def process_new_files():
    global processed_files
    
    # Listar todos os arquivos na pasta
    current_files = set(os.listdir(folder_to_watch))
    
    # Identificar novos arquivos
    new_files = current_files - processed_files
    
    for file in new_files:
        # Ignorar arquivos que já começam com "Transcrito_"
        if file.startswith("Transcrito_") or not file.endswith(audio_extensions):
            continue
        
        file_path = os.path.join(folder_to_watch, file)
        
        # Montar o comando PowerShell
        command = f'python -m whisper "{file_path}" --language pt --model medium --device cuda --output_format txt --output_dir "E:\Textos Transcritos"'
        
        try:
            # Executar o comando no PowerShell
            subprocess.run(["powershell", "-Command", command], check=True)
            print(f"Arquivo processado: {file}")
            
            # Renomear o arquivo após processamento
            new_name = f"Transcrito_{file}"
            new_path = os.path.join(folder_to_watch, new_name)
            os.rename(file_path, new_path)
            print(f"Arquivo renomeado para: {new_name}")
        
        except subprocess.CalledProcessError as e:
            print(f"Erro ao processar o arquivo {file}: {e}")
    
    # Atualizar arquivos processados
    processed_files.update(current_files)

def main():
    print(f"Monitorando a pasta: {folder_to_watch}")
    while True:
        process_new_files()
        time.sleep(5)  # Aguarda 5 segundos antes de verificar novamente

if __name__ == "__main__":
    main()
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
#   for file in new_files:
#        if file.endswith('.mp3'):
#           file_path = os.path.join(folder_to_watch, file)
#          
#            # Montar o comando PowerShell
#            command = f'python -m whisper "{file_path}" --language pt --model medium --device cuda --output_format txt --output_dir "E:\Textos Transcritos"'
#            
#            try:
#                # Executar o comando no PowerShell
#                subprocess.run(["powershell", "-Command", command], check=True)
#                print(f"Arquivo processado: {file}")
#            except subprocess.CalledProcessError as e:
#                print(f"Erro ao processar o arquivo {file}: {e}")
#    
#    # Atualizar arquivos processados
#    processed_files.update(new_files)
#
#def main():
#    print(f"Monitorando a pasta: {folder_to_watch}")
#    while True:
#        process_new_files()
#        time.sleep(5)  # Aguarda 5 segundos antes de verificar novamente
#
#if __name__ == "__main__":
#    main()
#