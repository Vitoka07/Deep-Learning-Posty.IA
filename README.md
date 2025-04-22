# Postly.IA

![capa-dl](https://github.com/user-attachments/assets/4ac2d3b0-b344-4e57-89a2-7e1a81472437)

# Sobre o projeto

Postly.IA é uma aplicação que utiliza modelos de Deep Learning para gerar automaticamente postagens publicitárias voltadas para redes sociais, a partir de imagens ou textos fornecidos pelo usuário. O objetivo é auxiliar pequenas e médias empresas a criarem conteúdos de qualidade com agilidade, criatividade e foco no público-alvo.

O nome do projeto surgiu da junção entre "Post" (publicações para redes sociais) e "IA" (Inteligência Artificial), reforçando a proposta de automação criativa através da tecnologia. O sufixo “.IA” remete tanto à Inteligência Artificial quanto à identidade digital da ferramenta, tornando o nome moderno, direto e autoexplicativo.

## Descrição
Front End feito em Python utilizando Streamlit como interface interativa para o projeto da Faculdade Senac PE.
A aplicação integra modelos da Hugging Face para geração de imagens, descrição automática de conteúdo visual e criação de textos publicitários, todos conectados a partir de APIs.

O usuário pode selecionar uma área temática (como Comida, Esporte, Viagem ou Vestuário), escolher entre fornecer uma imagem ou texto, e receberá como retorno uma sugestão de anúncio pronto para redes sociais, com imagem e frase gerada automaticamente.

(Utilizando Imagem para gerar o anúncio 📢)
![WhatsApp Image 2025-01-31 at 21 07 33](https://github.com/user-attachments/assets/2aaa77c5-cad3-4e79-959b-898267c43d03)

(Utilizando Texto para gerar o anúncio ✏️)
![Foto](https://github.com/user-attachments/assets/f8b3f0d4-fb8f-4b04-ab40-2929dfc75e4e)


## Tecnologias Utilizadas 👨‍💻:
 - Python
 - Streamlit
 - Hugging Face Hub
 - LangChain
 - Requests
 - OpenAI API

## Instalação apos Download do projeto
No terminal (recomenda-se o uso do VSCode), execute:

```bash
# development
$ pip install -r requirements.txt

## Executando o projeto

$ streamlit run app.py

Lembre-se de adicionar sua chave da Hugging Face no campo "HUGGINGFACE_API_KEY".

## License

[MIT licensed](LICENSE).
