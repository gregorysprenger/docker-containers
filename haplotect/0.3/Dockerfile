FROM abelhj/haplotect:0.3 AS haplotect

FROM ubuntu:jammy

RUN apt-get update

WORKDIR /data

COPY --from=haplotect /usr/local/openjdk-8 /usr/local/openjdk-8
COPY --from=haplotect /opt/hall-lab/gatk-package-4.1.8.1-18-ge2f02f1-SNAPSHOT-local.jar /opt

RUN echo '#!/bin/bash' > /usr/local/bin/Haplotect \
    && echo '/usr/local/openjdk-8/bin/java -Xmx6g -jar /opt/gatk-package-4.1.8.1-18-ge2f02f1-SNAPSHOT-local.jar Haplotect "$@"' >> /usr/local/bin/Haplotect \
    && chmod +x /usr/local/bin/Haplotect
