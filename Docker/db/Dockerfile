FROM postgres:latest

ENV POSTGRES_DB=contacts_db
ENV POSTGRES_USER=contacts_user
ENV POSTGRES_PASSWORD=contacts_pass

COPY init.sql /docker-entrypoint-initdb.d/