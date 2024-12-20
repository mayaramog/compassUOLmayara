FROM python:3

WORKDIR /Etapa3

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD [ "python", "etapa3.py" ]
