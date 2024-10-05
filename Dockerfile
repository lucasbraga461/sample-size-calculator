FROM python:3.9.12

WORKDIR /app

COPY . .

# Create a virtual environment, activate and install the requirements
RUN python -m venv venv
ENV PATH="/app/venv/bin:$PATH"
RUN pip install --upgrade pip && \
    pip install -r requirements.txt

EXPOSE 8080

CMD ["streamlit", "run", "--server.address", "0.0.0.0", "--server.port", "8080", "--server.enableCORS", "true", "--server.enableXsrfProtection", "true", "streamlit_sample_size_calculator.py"]
