# Use Astronomer's standard Airflow runtime
FROM quay.io/astronomer/astro-runtime:10.0.0

# Copy requirements.txt and install packages
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt
