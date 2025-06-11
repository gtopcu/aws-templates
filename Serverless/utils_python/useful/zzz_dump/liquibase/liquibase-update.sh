rpm --import https://repo.liquibase.com/liquibase.asc
yum-config-manager --add-repo https://repo.liquibase.com/repo-liquibase-com.repo
yum install liquibase

liquibase update \
          --driver=org.postgresql.Driver \
          --search-path=path/to/changelog/files \
          --changelog-file=com/example/db.changelog.xml \
          --url="jdbc:postgresql://$host:$port/$db" \
          --username=scott \
          --password=tiger
