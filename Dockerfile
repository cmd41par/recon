# For more information, please refer to https://aka.ms/vscode-docker-python
FROM python:3.13-bookworm as builder

# Keeps Python from generating .pyc files in the container
ENV PYTHONDONTWRITEBYTECODE=1

# Turns off buffering for easier container logging
ENV PYTHONUNBUFFERED=1

# Create a virtual environment
RUN python -m venv /opt/venv

# Ensure the virtual environment is used:
ENV PATH="/opt/venv/bin:$PATH"

# Install Python dependencies
RUN pip install pandas pytest openpyxl pydantic ipykernel matplotlib ruff ipywidgets jinja2

# Set the PYTHONPATH environment variable
ENV PYTHONPATH=/app/src

# Set the working directory
WORKDIR /app
COPY . /app

FROM python:3.13-slim-bookworm as prod
RUN apt-get update && apt-get install -y git make && apt-get clean && rm -rf /var/lib/apt/lists/*

# Copy the Python dependencies from the builder stage
COPY --from=builder /opt/venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"
#COPY --from=builder /usr/local/bin /usr/local/bin
WORKDIR /app
COPY . /app

# Creates a non-root user with an explicit UID and adds permission to access the /app folder
RUN adduser -u 5678 --disabled-password --gecos "" appuser && chown -R appuser /app

# Switch to the non-root user
USER appuser

# Start SSH service and the application
# CMD ["/bin/bash"]