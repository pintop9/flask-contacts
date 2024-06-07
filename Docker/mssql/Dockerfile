FROM mcr.microsoft.com/mssql/server:latest
ENV ACCEPT_EULA=Y
ENV MSSQL_DATABASE=contacts_db
ENV MSSQL_PID=Developer
ENV MSSQL_SA_PASSWORD=Y9&ZvR4*2?BdNp
ENV MSSQL_TCP_PORT=1433
ARG SA_PASSWORD

EXPOSE 1433
COPY init.sql /var/opt/mssql/scripts/init.sql


RUN /opt/mssql/bin/sqlservr & sleep 30 && \
    /opt/mssql-tools/bin/sqlcmd -S localhost -U sa -P "${MSSQL_SA_PASSWORD}" -i /var/opt/mssql/scripts/init.sql

CMD /opt/mssql/bin/sqlservr
