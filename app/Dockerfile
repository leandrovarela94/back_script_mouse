# Imagem base
FROM python:3.11-slim

# Define o diretório de trabalho
WORKDIR /app

EXPOSE 8000

COPY . /app
# Copia os arquivos Pipfile e Pipfile.lock para o diretório de trabalho

# Instala o pipenv
RUN pip install pip --upgrade
RUN pip install pipenv
RUN pip install pyautogui
RUN pipenv clean
# Instala as dependências do projeto
RUN pipenv install --deploy

CMD ["uvicorn", "app:app", "--host", "0.0.0.0"]