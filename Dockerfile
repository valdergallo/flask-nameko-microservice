FROM python:3.6.6-alpine

LABEL maintainer="valdergallo@gmail.com"
LABEL description="Create the Flask/Nameko micro-service image"


# expose port 5000
EXPOSE 5001

RUN apk update && \
    apk add python3-dev build-base linux-headers pcre-dev postgresql-dev && \
    rm -rf \
    /usr/src/postgresql \
    /usr/local/share/doc \
    /usr/local/share/man && \
    find /usr/local -name '*.a' -delete

ADD . /code
WORKDIR /code

RUN pip install --upgrade pip

RUN pip install -r requirements/prod.txt

CMD ["flask", "db", "upgrade"]

RUN chmod +x entrypoint.sh

CMD ["/bin/sh", "/code/entrypoint.sh"]

