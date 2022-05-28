#Works only with Python 2
FROM python:2.7

# Add sample application
ADD application.py /tmp/application.py

EXPOSE 80

# Run it
ENTRYPOINT ["python", "/tmp/application.py"]