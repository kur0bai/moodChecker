FROM ubuntu:22.04

ENV DEBIAN_FRONTEND=noninteractive
ENV PYTHONUNBUFFERED=1

# Dependencies fixed
RUN apt-get update && apt-get install -y \
    build-essential curl git python3 python3-pip python3-dev \
    libgl1-mesa-glx libglib2.0-0 \
    libsm6 libxrender1 libxext6 \
    ffmpeg \
    libxcb1 libx11-xcb1 libxcomposite1 libxi6 libxtst6 \
    libxrandr2 libxfixes3 libxcb-shm0 libxcb-shape0 libxcb-xfixes0 \
    && rm -rf /var/lib/apt/lists/*


WORKDIR /app

COPY . /app

RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt

CMD ["python3", "main.py"]
