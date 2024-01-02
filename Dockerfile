FROM python:3.11.7
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY ./html .
EXPOSE 5000
ENV FLASK_APP=Controller.py
ENV FLASK_RUN_HOST=0.0.0.0
CMD ["python", "Controller.py"]