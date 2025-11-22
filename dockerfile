FROM python:3.13

WORKDIR /app

# Copy the current directory contents into the container
COPY . .

# Install dependencies using pip
RUN pip install pandas streamlit

# Set the entry point to run the app
ENTRYPOINT ["streamlit", "run", "main.py"]

# Optionally, you can specify a default command if needed
CMD ["main.py"]

