
# docker run -it ubuntu bash

# docker build -t ubuntu-python .
# docker tag ubuntu-python gtopcu/ubuntu-python
# docker run -it ubuntu-python bash | -dp 8080:8080

# docker run ubuntu-python
# docker run ubuntu-python -dp 8080:8080
# docker run -it ubuntu-python bash

# runs as root - no need for sudo!
# apt list search show install reinstall remove autoremove update upgrade full-upgrade edit-sources satisfy
# 140MB

FROM ubuntu:latest
RUN apt update -y && \
    apt install python3 python3-pip -y python3-venv -y
# RUN apt remove python3 python3-pip python3-venv -y
WORKDIR /app
COPY . /app
RUN python3 -m venv /app/venv
ENV PATH="/app/venv/bin:$PATH"
RUN pip3 install --no-cache-dir -r requirements.txt
CMD ["/app/venv/bin/python3", "app.py"] 

# CMD ["python3", "app.py"]
# EXPOSE 8080
# ENTRYPOINT ["executable"]
# Either create a virtual env, or install libs system-wide: apt install python3-requests
# RUN python3 -m venv .venv 
# RUN . .venv/bin/activate
# RUN chown -R root .venv
# RUN chmod u+rwx .venv
# RUN pip install requests
# RUN pip install --no-cache-dir -r requirements.txt