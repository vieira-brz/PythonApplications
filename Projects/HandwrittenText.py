# pip install pywhatkit==4.5
import pywhatkit as pw
import os

# Texto que será convertido para escrita à mão
txt = """On a quiet Sunday afternoon, the wind gently rustled the leaves as the sun dipped below the horizon, painting the sky in hues of orange and pink. Birds chirped softly, and the world felt at peace."""

# Diretório onde a imagem será salva, na mesma pasta do script
current_dir = os.path.dirname(os.path.abspath(__file__))
save_dir = os.path.join(current_dir, 'HandwrittenTexts')
save_path = os.path.join(save_dir, 'imagem.png')

# Verifica se o diretório existe, se não existir, cria
if not os.path.exists(save_dir):
    os.makedirs(save_dir)

# Converte o texto para "escrita à mão" e salva a imagem
pw.text_to_handwriting(txt, save_path)

print(f"Imagem salva em: {save_path}")