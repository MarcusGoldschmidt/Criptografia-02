# Cripto

Neste trabalho o aluno deverá desenvolver um programa de criptografia e decriptografia
para arquivos texto em codificação ASCII, a linguagem de programação será C ou Python
(escolher) e seu funcionamento será da seguinte forma:
Entradas

⦁ Chave alfanumérica de 64 bits ou 128 bits (permitir escolha do usuário) (8 ou 16
caracteres)

⦁ Path para um arquivo texto
⦁ Modo:

    ⦁ C para criptografar o arquivo; e
    ⦁ D para decriptografar o arquivo.
    
## Processamento

⦁ Separar o arquivo em blocos do tamanho da chave (64 ou 128 bits), caso necessário,
preencha o último bloco com o valor 0.

    ⦁ Ex: Imagine que o arquivo tenha 136 bits (17 caracteres ASCII) e que a chave
    escolhida tenha 64 bits, neste caso o arquivo deverá ser dividido em 3
    blocos (64+64+8 = 136), sendo que o último bloco deverá ser
    complementado com 0 até completar 64 bits.

⦁ Para cada bloco, realize uma operação XOR com a chave.

## Saída

Arquivo texto criptografado quando o modo escolhido foi o “C” ou
Arquivo texto decriptografado quando o modo escolhido foi o “D”.

Exemplo de funcionamento para um arquivo de 24 bits e uma chave de 16 bits

Chave: IC (ASCII) 01001001 01000011 (Binário)

Texto: ADA (ASCII) 01000001 01000100 01000001 (Binário)

Modo: C

Blocos: [01000001 01000100] e [01000001 00000000]

Saída: 1000000001110000100001000011