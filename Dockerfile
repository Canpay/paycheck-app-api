# Utilizamos la imagen oficial de Python 3.9
FROM python:3.9

# Definimos el directorio de trabajo dentro de la imagen
WORKDIR /app

# Copiamos los archivos de requerimientos a la imagen y los instalamos
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

# Copiamos el código de la aplicación a la imagen
COPY . .

# Exponemos el puerto 80 de la imagen
EXPOSE 80

# Iniciamos la aplicación utilizando Uvicorn
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]
