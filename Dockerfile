FROM python:3.11.1

WORKDIR /code

# Copia los archivos necesarios
COPY ./ /code/

# Instala el controlador ODBC para SQL Server
RUN curl https://packages.microsoft.com/keys/microsoft.asc | apt-key add - \
    && curl https://packages.microsoft.com/config/debian/11/prod.list > /etc/apt/sources.list.d/mssql-release.list \
    && apt-get update \
    && ACCEPT_EULA=Y apt-get install -y msodbcsql17

# Instala wkhtmltopdf desde los repositorios oficiales de Ubuntu
#RUN apt-get update && apt-get install -y wkhtmltopdf

# Instala las dependencias de Python
RUN pip install --no-cache-dir --upgrade -r requirements.txt

# CMD para ejecutar tu aplicación
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "5080"]
