FROM mysql:latest
ENV MYSQL_DATABASE=contacts_db
ENV MYSQL_USER=contacts_user
ENV MYSQL_PASSWORD=contacts_pass
ENV MYSQL_ROOT_PASSWORD=contacts_pass
EXPOSE 3306
ADD init.sql /docker-entrypoint-initdb.d/

