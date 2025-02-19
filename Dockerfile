# Usa una imagen base de Python
FROM python:3.11-slim

# Establece el directorio de trabajo
WORKDIR /app

# Instala dependencias del sistema necesarias (libpq-dev y build-essential)
RUN apt-get update && apt-get install -y libpq-dev build-essential

# Copia los archivos de requisitos e instala las dependencias
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copia el resto del código
COPY . .

# Expone el puerto 8000
EXPOSE 8000

# Comando para ejecutar el servidor de Django con Daphne
CMD ["daphne", "-b", "0.0.0.0", "-p", "8000", "main.asgi:application"]
