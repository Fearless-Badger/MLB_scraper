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

# to BUILD
#   docker build -t mlb_app .
# where "." is the path to the dockerfile

# to RUN
#   docker run -d -p 5000:5000 mlb_app


# to LIST containers
#   docker ps

# to QUIT 
#   docker container stop <CONTAINER NAME>
# where CONTAINER NAME is the name associtaed with the container.
