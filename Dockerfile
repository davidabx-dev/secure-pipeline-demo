# Usa uma imagem base leve do Python (Linux Alpine ou Slim)
FROM python:3.9-slim

# Define a pasta de trabalho dentro do container (como se fosse um 'cd /app')
WORKDIR /app

# Copia os arquivos da sua pasta atual (Windows) para dentro do container (Linux)
COPY . .

# Instala as dependências dentro do container
RUN pip install --no-cache-dir -r requirements.txt

# Expõe a porta 5000 (a mesma que o Flask usa)
EXPOSE 5000

# Comando para iniciar a aplicação quando o container rodar
CMD ["python", "app.py"]