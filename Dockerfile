FROM python:3.8
ENV PYTHONUNBUFFERED=1
RUN apt update 
WORKDIR /usr/scr/app
COPY req.txt ./
RUN pip install -r req.txt
COPY . .
EXPOSE 8000
#CMD ["python","manage.py","runserver","0.0.0.0:8000"]

