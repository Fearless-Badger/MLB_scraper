FROM python:3.9-slim
RUN python -m venv /venv
ENV PATH = "/venv/bin:$PATH"
RUN pip install --upgrade pip setuptools
WORKDIR /mlb_scraper

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
EXPOSE 5000

CMD ["gunicorn", "-w", "2", "-b", "0.0.0.0:5000", "app:app"]
