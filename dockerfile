FROM python:3.13

WORKDIR /app

COPY . .

RUN pip install pandas streamlit

ENTRYPOINT ["streamlit", "run", "main.py"]

CMD ["main.py"]

