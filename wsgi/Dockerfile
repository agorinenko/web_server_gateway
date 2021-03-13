FROM python:3.8

EXPOSE 8000

WORKDIR /opt/app
COPY . .

RUN python -m pip install --upgrade pip
RUN pip install -r requirements.txt --default-timeout=100

RUN chgrp -R 0 /opt/app/ && chmod -R g=u /opt/app/
RUN ["chmod", "+x", "/opt/app/docker-entrypoint.sh"]

ENTRYPOINT ["/opt/app/docker-entrypoint.sh"]