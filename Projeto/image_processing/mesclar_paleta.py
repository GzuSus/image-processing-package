from PIL import Image

def aplicar_paleta_customizada(img_base, img_paleta, num_cores=8):
    """
    Converte a imagem base para tons de cinza e aplica uma paleta baseada na imagem de referência.
    """
    img_base = img_base.convert("RGB")
    img_paleta = img_paleta.convert("RGB")

    # Reduz a paleta da imagem de referência
    paleta_reduzida = img_paleta.quantize(colors=num_cores).convert("RGB")
    cores = paleta_reduzida.getcolors(1000000)  # Lista de (contagem, cor)

    if not cores:
        raise ValueError("Não foi possível extrair a paleta da imagem de referência.")

    # Ordena por frequência
    cores.sort(reverse=True, key=lambda x: x[0])
    paleta = [cor for _, cor in cores[:num_cores]]

    # Converte a imagem base em tons de cinza
    img_cinza = img_base.convert("L")

    largura, altura = img_base.size
    nova_img = Image.new("RGB", (largura, altura))

    pixels_cinza = img_cinza.load()
    pixels_nova = nova_img.load()

    for x in range(largura):
        for y in range(altura):
            intensidade = pixels_cinza[x, y]  # 0-255
            indice_cor = int(intensidade * (len(paleta) - 1) / 255)
            pixels_nova[x, y] = paleta[indice_cor]

    return nova_img
