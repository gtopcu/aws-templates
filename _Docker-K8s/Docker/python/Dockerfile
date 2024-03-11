# https://hub.docker.com/_/python
FROM python:3.12.2

COPY requirements.txt ./
RUN pip install -r requirements.txt
COPY . ./

CMD [ "python3", "process.py" ]

# -----------------------------------------------------------------

FROM python:3

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD [ "python", "./your-daemon-or-script.py" ]

# docker build -t my-python-app .
# docker run -it --rm --name python-app python-app

# Run script in Docker directly without dockerfile:
# docker run -it --rm --name running-script -v "$PWD":/usr/src/myapp -w /usr/src/myapp python:3 python script.py