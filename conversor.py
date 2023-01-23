from playsound import playsound
import gtts
import os


# cores
class colors:
    cyan = '\033[1;36m'
    yellow = '\033[1;33m'
    green = '\033[92m'
    red = '\033[91m'
    end = '\033[0m'


# função para converter o texto em áudio
def converter_txt_em_audio(texto, nome_arquivo='audio',):
    print(f'{colors.yellow}Convertendo arquivo....{colors.end}')
    arquivo = gtts.gTTS(texto, lang='pt')
    arquivo.save(f'{nome_arquivo}.mp3')
    return nome_arquivo


os.system('cls')
print('-' * 30)
print('Conversor de texto pra áudio')
print('-' * 30)
print('[1] - Escolha um arquivo existente\n[2] - Digite o texto a ser convertido')
opcao = input('Escolha uma opção: ')

os.system('cls')
if opcao == '1':
    try:
        nome_arquivo = input('Digite o nome do aquivo a ser lido: ')
        texto = ''
        with open(f'{nome_arquivo}.txt', 'r', encoding='utf-8') as arquivo:
            for linha in arquivo:
                texto += linha
        print(colors.cyan, texto, colors.end)
        converter_txt_em_audio(texto, nome_arquivo)
    except:
        print(f'{colors.yellow}Arquivo não encontrado!{colors.end}')
        print(f'{colors.red}Programa Encerrado...{colors.end}')
        exit()
elif opcao == '2':
    texto = input('Digite o texto a ser lido: ')
    nome_arquivo = converter_txt_em_audio(texto)
else:
    print(f'{colors.yellow}Opção invalida!{colors.end}')
    print(f'{colors.red}Programa Encerrado...{colors.end}')
    exit()

print(f'{colors.green}Tocando...{colors.end}')
playsound(f'{nome_arquivo}.mp3')
os.remove(f'{nome_arquivo}.mp3')
print(f'{colors.red}Finalizado!{colors.end}')
