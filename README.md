# UI Card Post IG App

![App Screenshot](src/card.png)

Esta é uma UI de um post real do Instagram, desenvolvido apenas para fins de estudo, usei como exemplo o time que eu torço e uma postagem que curti. O card exibe informações básicas do post, como nome de quem postou, foto do perfil, foto postada, curtidas, legenda, número de comentários e a quanto tempo essa foto foi postada.

## Estrutura do Projeto

- `main.py`: Arquivo único e principal do card.
- `src/card.png`: Print de como o card ficou.
- `src/real_post.png`: Print da postagem real.

## Como Rodar o Projeto

Para executar o projeto, siga as etapas abaixo:

1. Certifique-se de ter o Python instalado. Caso contrário, baixe e instale a partir do [site oficial do Python](https://www.python.org/downloads/).
2. Clone o repositório em seu ambiente de desenvolvimento.
3. Crie um ambiente virtual (opcional, mas recomendado):
- python -m venv venv
4. Ative o ambiente virtual:
- No Windows:
  ```
  venv\Scripts\activate
  ```
- No MacOS/Linux:
  ```
  source venv/bin/activate
  ```
5. Instale as dependências do projeto:
    ```
    pip install -r requirements.txt
    ```
6. Execute o aplicativo:
    ```
    flet -r main.py
    ```
