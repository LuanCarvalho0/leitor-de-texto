from playsound import playsound
import gtts
import os


# função para converter o texto em áudio
def converter_txt_em_audio(nome_arquivo, texto):
    print('Convertendo arquivo....')
    arquivo = gtts.gTTS(texto, lang='pt')
    arquivo.save(f'{nome_arquivo}.mp3')


print('-' * 30)
print('Conversor de texto pra áudio')
print('-' * 30)
print('[1] - Escolha um arquivo existente\n[2] - Digite o texto a ser convertido')
opcao = input('Escolha uma opção: ')


if opcao == '1':
    nome_arquivo = input('Digite o nome do aquivo: ')
    texto = ''
    with open(f'{nome_arquivo}.txt', 'r', encoding='utf-8') as arquivo:
        for linha in arquivo:
            texto += linha
    print(texto)
    converter_txt_em_audio(nome_arquivo, texto)
elif opcao == '2':
    nome_arquivo = input('Digite o nome do aquivo: ')
    texto = input('Digite o texto: ')
    converter_txt_em_audio(nome_arquivo, texto)
else:
    print('Opção invalida!')
    print('Programa Encerrado...')
    exit()

print('Tocando...')
playsound(f'{nome_arquivo}.mp3')
os.remove(f'{nome_arquivo}.mp3')
print('Finalizado!')
