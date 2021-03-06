FROM python:latest

COPY . /usr/src/app

EXPOSE 8000

WORKDIR /usr/src/app

#ENV GOOGLE_APPLICATION_CREDENTIALS=/usr/src/app/key/fmpchat-udbn-6fb390582ddb.json
ENV GOOGLE_APPLICATION_CREDENTIALS=/usr/src/app/key/chatbot-proj-1eb411a5599f.json

RUN pip install -r requirements.txt

CMD ["python", "main.py"]
