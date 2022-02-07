FROM nginx/unit:1.22.0-python3.9
COPY requirements.txt /app/
RUN apt-get update && apt-get install -y python3-pip
RUN pip3 install -r /app/requirements.txt

COPY config/unit.json /docker-entrypoint.d/

COPY Data/user.json  /app/Data/
WORKDIR /app
COPY user_service.py /app/
COPY index.html /app/
COPY img1.jpg /app/ 