FROM python:3

WORKDIR /sprint4

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD [ "python", "carguru.py" ]