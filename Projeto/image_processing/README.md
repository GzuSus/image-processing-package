# Projeto de Processamento de Imagens - Versão Inicial

Este projeto oferece funcionalidades básicas para processamento de imagens usando Python e PIL (Pillow), incluindo:

- Abrir imagens locais ou via URL
- Aplicar filtros simples (tons de cinza, redimensionamento, filtro de contorno)
- Mesclar paleta de cores de uma imagem de referência em outra imagem
- Salvar imagens processadas com nomes sequenciais
- Visualizar imagens após processamento

---

## Como usar

1. Certifique-se de ter as dependências instaladas:
```bash
pip install pillow requests numpy
Coloque uma imagem chamada exemplo.jpg na pasta do projeto para usar como imagem de exemplo.

Execute o script principal:

python exemplo.py
Siga as instruções no terminal:

Escolha usar imagem de exemplo ou inserir URL de imagem.

Escolha aplicar filtros normais ou mesclar com paleta de cores de outra imagem (arquivo local ou URL).

As imagens processadas serão salvas na pasta atual com nomes como produto_1.jpg, produto_2.jpg etc.

As imagens serão exibidas automaticamente após o processamento.

Observações
Esta é uma versão bem inicial do projeto, focada em demonstrar funcionalidades básicas e a estrutura do código.

Ainda não há interface gráfica nem tratamento avançado de erros.

A função de mesclagem de paletas usa uma simplificação para mapear tons de cinza para cores da paleta de referência.

Sinta-se à vontade para contribuir, melhorar e expandir!

Estrutura do projeto
exemplo.py — script principal para interagir e testar o processamento

image_processing/ — módulo com funções para abrir, salvar e manipular imagens

mesclar_paleta.py — função para mesclar paleta de cores entre imagens