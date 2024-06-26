FROM nikolaik/python-nodejs:latest

WORKDIR /home

COPY . .

RUN pip install -r requirements.txt && npm install

EXPOSE 5000

CMD npm run dev