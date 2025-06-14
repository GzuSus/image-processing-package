from image_processing import (
    abrir_imagem,
    salvar_imagem,
    converter_para_cinza,
    redimensionar,
    aplicar_filtro,
    aplicar_paleta_customizada
)
import os

def obter_novo_nome(prefixo="produto"):
    i = 1
    while True:
        nome = f"{prefixo}_{i}.jpg"
        if not os.path.exists(nome):
            return nome
        i += 1

def main():
    try:
        escolha_origem = input("Deseja usar a imagem de exemplo ou fornecer uma URL? (exemplo/url): ").strip().lower()
        if escolha_origem == "exemplo":
            caminho_img = "exemplo.jpg"
        elif escolha_origem == "url":
            url = input("Insira a URL da imagem: ").strip()
            caminho_img = abrir_imagem(url, salvar_local="downloaded_exemplo.jpg")
            if caminho_img is None:
                print("Erro ao baixar a imagem da URL.")
                return
            # abrir_imagem aqui já retorna um objeto Image, então precisamos salvar ele para abrir de novo
            caminho_img = "downloaded_exemplo.jpg"
        else:
            print("Opção inválida. Encerrando.")
            return

        img = abrir_imagem(caminho_img)
        if img is None:
            print("Erro: imagem não encontrada ou inválida.")
            return

        print("Imagem original carregada.")
        img.show()

        modo = input("Deseja aplicar filtros normais ou mesclar com outra imagem-paleta? (normal/mesclar): ").strip().lower()

        if modo == "normal":
            # Cinza
            img_cinza = converter_para_cinza(img)
            nome_cinza = obter_novo_nome()
            salvar_imagem(img_cinza, nome_cinza)
            print(f"Imagem em tons de cinza salva como {nome_cinza}")
            img_cinza.show()

            # Redimensionar
            img_redimensionada = redimensionar(img, 200, 200)
            nome_red = obter_novo_nome()
            salvar_imagem(img_redimensionada, nome_red)
            print(f"Imagem redimensionada salva como {nome_red}")
            img_redimensionada.show()

            # Filtro
            img_filtrada = aplicar_filtro(img)
            nome_filtro = obter_novo_nome()
            salvar_imagem(img_filtrada, nome_filtro)
            print(f"Imagem com filtro salva como {nome_filtro}")
            img_filtrada.show()

        elif modo == "mesclar":
            caminho_paleta = input("Digite o caminho ou URL da imagem-paleta de cores: ").strip()
            if caminho_paleta.startswith("http"):
                paleta_img = abrir_imagem(caminho_paleta, salvar_local="downloaded_paleta.jpg")
                if paleta_img is None:
                    print("Erro ao baixar a imagem-paleta.")
                    return
                caminho_paleta = "downloaded_paleta.jpg"
            else:
                paleta_img = abrir_imagem(caminho_paleta)
                if paleta_img is None:
                    print("Erro ao abrir a imagem-paleta.")
                    return

            img_mesclada = aplicar_paleta_customizada(img, paleta_img)
            nome_mescla = obter_novo_nome()
            salvar_imagem(img_mesclada, nome_mescla)
            print(f"Imagem mesclada com paleta salva como {nome_mescla}")
            img_mesclada.show()

        else:
            print("Modo inválido. Encerrando.")

    except Exception as e:
        print(f"Erro durante a execução: {e}")

if __name__ == "__main__":
    main()
