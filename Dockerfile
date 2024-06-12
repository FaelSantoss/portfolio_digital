FROM python:latest

WORKDIR /home

COPY . .

RUN pip install -r requirements.txt

EXPOSE 5000

CMD npm run dev