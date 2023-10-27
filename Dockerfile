# Imagem base
FROM python:3.11-slim

# Define o diretório de trabalho
WORKDIR /root

COPY . .
# Copia os arquivos Pipfile e Pipfile.lock para o diretório de trabalho

# COPY Pipfile Pipfile.lock ./
# Instala o pipenv
RUN pip install pipenv

# Instala as dependências do projeto
RUN pipenv install --system --deploy


# Comando de execução do container
# CMD ["python", "app.py"]
