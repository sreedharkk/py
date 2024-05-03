FROM python:3.9
WORKDIR /app 

 
COPY ./app /app
COPY ./requirements.txt  /app 
# here Set the working directory inside the container
 

ENV PIP_NO_CERTIFICATE 1
RUN pip3 install --upgrade pip  
 
RUN pip3 install --no-cache-dir --upgrade -r requirements.txt
 
 
RUN apt-get update
 
 
EXPOSE 8080

#CMD ["python", "main.py"]
 
#CMD ["uvicorn", "main:app", "--proxy-headers", "--host", "0.0.0.0", "--port", "80"]
 
CMD ["uvicorn", "app.main:app", "--workers","2","--worker-class", "uvicorn.workers.UvicornWorker" ,"-b", "127.0.0.1:8080"]
 
 
#CMD ["sh", "-c", "uvicorn src.main:app --host 0.0.0.0 --port ${PORT:-${WEBSITES_PORT:-8080}}"]
