FROM debian:bullseye-slim

WORKDIR /app/

RUN apt-get update && apt-get install -y --no-install-recommends \
    python3 \
    python3-pip \
    python3-venv \
    && apt-get clean && rm -rf /var/lib/apt/lists/*


COPY requirements.txt .

RUN pip3 install --no-cache-dir -r requirements.txt

RUN echo "requirements are installed"

COPY . . 


RUN python3 manage.py makemigrations

EXPOSE 8000

CMD ["python3","manage.py","runserver","0.0.0.0:8000"]
