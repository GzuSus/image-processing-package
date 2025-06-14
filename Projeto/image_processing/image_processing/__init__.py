from PIL import Image, ImageFilter
import math
from mesclar_paleta import aplicar_paleta_customizada
import os
import requests
from PIL import Image
from io import BytesIO

def abrir_imagem(caminho, salvar_local=None):
    try:
        if caminho.startswith("http"):
            response = requests.get(caminho)
            response.raise_for_status()
            img = Image.open(BytesIO(response.content)).convert("RGB")

            if salvar_local:
                if isinstance(salvar_local, str):
                    caminho_salvar = salvar_local
                    if not os.path.splitext(caminho_salvar)[1]:
                        caminho_salvar += ".jpg"
                else:  # salvar_local == True (bool)
                    caminho_salvar = "imagem_baixada.jpg"

                img.save(caminho_salvar)
                print(f"Imagem da URL salva como: {caminho_salvar}")

            return img
        else:
            img = Image.open(caminho).convert("RGB")
            return img
    except Exception as e:
        print(f"Erro ao abrir imagem: {e}")
        return None

def salvar_imagem(imagem, caminho):
    """Salva a imagem modificada no caminho especificado."""
    imagem.save(caminho)

def converter_para_cinza(imagem):
    """Converte a imagem para tons de cinza."""
    return imagem.convert("L")

def redimensionar(imagem, largura, altura):
    """Redimensiona a imagem para a largura e altura especificadas."""
    return imagem.resize((largura, altura))

def aplicar_filtro(imagem):
    """Aplica um filtro de contorno à imagem."""
    return imagem.filter(ImageFilter.CONTOUR)

def distancia_cor(c1, c2):
    return math.sqrt(sum((a-b)**2 for a, b in zip(c1, c2)))

def extrair_cores_paleta(img_paleta):
    img_paleta = img_paleta.convert("RGB")
    cores = img_paleta.getcolors(maxcolors=256*256)
    return [cor[1] for cor in cores]

def aplicar_paleta(imagem, img_paleta):
    cores_paleta = extrair_cores_paleta(img_paleta)
    largura, altura = imagem.size
    imagem = imagem.convert("RGB")
    pixels = imagem.load()

    for x in range(largura):
        for y in range(altura):
            cor_original = pixels[x,y]
            cor_mais_proxima = min(cores_paleta, key=lambda c: distancia_cor(cor_original, c))
            pixels[x,y] = cor_mais_proxima
    
    return imagem