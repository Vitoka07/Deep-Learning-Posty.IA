
#####################################################

import streamlit as st
import requests
import json
from PIL import Image
from io import BytesIO
import IPython.display as display
import numpy as np
from langchain.llms import HuggingFaceHub
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from huggingface_hub import InferenceClient
import time
from openai import OpenAI

#####################################################

# Exibição do titulo simulador HTML om CSS
image_url = "https://i.postimg.cc/tgxs8F79/capa-dl.png"

# Define a largura desejada (em pixels)
st.image(image_url, width=710)

st.write("<h3 style='color: #4F5161; font-size:20px;'> Faculdade SENAC/ PE - MBA Ciência de Dados e Inteligência Artificial </h3>", unsafe_allow_html=True)
st.write("<h5 style='color: #4F5161; font-size:15px;'> Projeto: Deep Learning (Prof. Geraldo Gomes) * Janeiro 2025 </h5>", unsafe_allow_html=True)
st.write("<h5 style='color: #4F5161; font-size:15px;'> Case: 6 - Geração de Postagens Publicitárias para Redes Sociais </h5>", unsafe_allow_html=True)
st.write("<h5 style='color: #4F5161; font-size:15px;'> Equipe: Anízio Neto | Mario Souza | Ivan Filho | Gentil Ribeiro | Vinicius Gomes </h5>", unsafe_allow_html=True)

st.write("---")

#####################################################

HUGGINGFACE_API_KEY = ""  # Seu token da Huggingface API


#####################################################

API_URL_DESCRICAO_IMG = "https://api-inference.huggingface.co/models/Salesforce/blip-image-captioning-base"

API_URL_GENERATE_IMG = "https://api-inference.huggingface.co/models/black-forest-labs/FLUX.1-dev"


#####################################################

def describe_image(image_file):

    # Função para descrever uma imagem enviada pelo usuário.
    # Utiliza a API HuggingFace para geração de texto a partir de imagens.

    headers = {
        # Autenticação da API
        "Authorization": f"Bearer {HUGGINGFACE_API_KEY}",
        # Tipo de conteúdo enviado (arquivo em bytes)
        "Content-Type": "application/octet-stream"
    }
    image_bytes = image_file.read()  # Lê o conteúdo do arquivo de imagem
    # Faz a requisição para a API
    response = requests.post(API_URL_DESCRICAO_IMG,
                             headers=headers, data=image_bytes)

    if response.status_code == 200:  # Verifica se a requisição foi bem-sucedida
        try:
            result = response.json()  # Converte a resposta JSON da API
            if isinstance(result, list) and 'generated_text' in result[0]:
                # Extrai a descrição gerada
                description = result[0]['generated_text']
                return description
            else:
                st.error("Resposta inesperada da API de descrição de imagem.")
                return None
        except KeyError:
            # Erro caso o JSON esteja mal formatado
            st.error("Erro ao processar a resposta da API")
            return None
    else:
        # Exibe erro caso a requisição falhe
        st.error(f"Erro na API: {response.text}")
        return None

#####################################################


def generate_image(prompt):

    # Função para gerar uma imagem baseada no texto do prompt.
    # Utiliza a API HuggingFace para geração de imagens.

    headers = {"Authorization": f"Bearer {
        HUGGINGFACE_API_KEY}"}  # Autenticação da API
    payload = {"inputs": prompt}  # Define o texto de entrada (prompt)
    # Faz a requisição para a API
    response = requests.post(API_URL_GENERATE_IMG,
                             headers=headers, json=payload)

    if response.status_code == 200:  # Verifica sucesso da requisição
        try:
            # Converte a resposta para imagem
            image = Image.open(BytesIO(response.content))
            return image
        except Exception as e:
            st.error(f"Erro ao processar a imagem: {str(e)}")
            return None
    else:
        # Exibe erro em caso de falha
        st.error(f"Erro ao gerar imagem: {response.text}")
        return None

#####################################################


def generate_postly(area, descricao):
    retry_attempts = 3  # Número de tentativas
    for attempt in range(retry_attempts):
        try:
            content = (
                f"Criar um texto para um anúncio na área '{area}' e baseado na descrição da imagem '{
                    descricao}', para publicação em rede social, que deve ser curto para postagem, retorne apenas uma sugestão de anuncio com o texto já em portgues brasileiro."
            )
            client = OpenAI(
                base_url="https://huggingface.co/api/inference-proxy/together",
                api_key=HUGGINGFACE_API_KEY
            )
            messages = [
                {
                    "role": "user",
                    "content": content
                }
            ]
            completion = client.chat.completions.create(
                model="deepseek-ai/DeepSeek-V3",
                messages=messages,
                max_tokens=500
            )

            return completion.choices[0].message.content
        except Exception as e:
            st.warning(f"Tentativa {attempt + 1} falhou: {str(e)}")
            time.sleep(5)
    st.error(f"Erro ao gerar anúncio: {str(e)}")
    return None

#####################################################


def en_to_pt(txt_en):
    retry_attempts = 3  # Número de tentativas
    for attempt in range(retry_attempts):
        try:
            content = (
                f"Retorne apenas p texto '{
                    txt_en}' traduzido para o português brasileiro."
            )
            client = OpenAI(
                base_url="https://huggingface.co/api/inference-proxy/together",
                api_key=HUGGINGFACE_API_KEY
            )
            messages = [
                {
                    "role": "user",
                    "content": content
                }
            ]
            completion = client.chat.completions.create(
                model="deepseek-ai/DeepSeek-V3",
                messages=messages,
                max_tokens=500
            )

            return completion.choices[0].message.content
        except Exception as e:
            st.warning(f"Tentativa {attempt + 1} falhou: {str(e)}")
            time.sleep(5)
    st.error(f"Erro ao gerar anúncio: {str(e)}")
    return None

#####################################################


def main():

    # Passo 1: Tipo de input
    tipo_input = st.radio("Selecione o tipo de input:", ("Imagem", "Texto"))

    if tipo_input:
        # Passo 2: Seleção de área
        area = st.selectbox("Defina uma área:", [
                            "Comida", "Esporte", "Viagem", "Vestuário"])

        if area:
            # Passo 3: Inputs dinâmicos baseados na seleção
            if tipo_input == "Imagem":
                imagem = st.file_uploader(
                    "Faça o upload de uma imagem da área selecionada", type=["jpg", "jpeg", "png"])
            elif tipo_input == "Texto":
                texto = st.text_area(
                    "Insira aqui um texto relacionado a área selecionada")
            if st.button("Iniciar"):
                if tipo_input == "Imagem":
                    descricao = describe_image(imagem)
                    texto = en_to_pt(descricao)
                if tipo_input == "Texto":
                    imagem = generate_image(texto)

                anuncio = generate_postly(area, texto)
                # anuncio_pt = en_to_pt(anuncio)
                if imagem:
                    st.image(imagem, use_column_width=True)
                st.markdown(f"""<meta charset="UTF-8">
                    <div style="background-color: #262730;
                                border-radius: 5px;
                                padding: 20px;
                                text-align: center;
                                border: 2px solid #E91313;">
                        <h3 style="color: #ffffff;">Sugestão para postagem:</h3>
                        <h2 style="color: #E91313;">{anuncio}</h2>
                    </div>
                    """, unsafe_allow_html=True)
                st.success("Anúncio gerado com sucesso!")


if __name__ == "__main__":
    main()
