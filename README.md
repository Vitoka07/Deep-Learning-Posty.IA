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
![Foto 1](https://github.com/user-attachments/assets/dc98f374-8961-48d4-84a6-69dfc3f96a11)
(Utilizando Texto para gerar o anúncio com a imagem ✏️)
![Foto](https://github.com/user-attachments/assets/7949c6ce-dfd3-4fbc-b309-210e85e71380)

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
## Executando o projeto

$ streamlit run app.py

Lembre-se de adicionar sua chave da Hugging Face no campo "HUGGINGFACE_API_KEY".

## License

[MIT licensed](LICENSE).
