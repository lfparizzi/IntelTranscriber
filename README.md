# IntelTranscriber
Transcrição de áudio e integração com IA.

## Objetivo:
Transcrever todos os arquivos de áudio proveniente de reuniões e ligações telefônicas e realizar uma integração com IA para sumarizar reuniões, apontar informações sensíveis vazadas, identificar pendências e urgências, reportar problemas e sugerir soluções.

## Como funciona?
Um arquivo de áudio contendo toda a conversação é inserido em uma pasta sincronizada entre o computador e o google drive. O programa automaticamente fará a transcrição do arquivo alterando seu nome para "Transcrito_arquivo.mp3" e irá gerar um output em .txt em um local seguro no computador. O arquivo de texto contém toda a conversa e contexto, será enviado junto com um Prompt para uma IA local como o Ollama, que avaliará toda a transcrição dando insights poderosos, a depender do prompt.

