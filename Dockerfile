# Base image
FROM python:3.11-slim

# Define o diretório de trabalho
WORKDIR /app

# Copia os arquivos de dependências
COPY requirements.txt .

# Instala as dependências
RUN pip install --no-cache-dir -r requirements.txt

# Copia o código do projeto para o container
COPY . .

# Expõe a porta 8000 para o Django
EXPOSE 8000

# Comando de entrada
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
