FROM ubuntu:20.04

ARG JAR_FILE=flow-0.2-SNAPSHOT.jar
ARG JAR_CONFIG=config

# cd /usr/local/runme
WORKDIR /usr/local/runme

# copy to /usr/local/runme/app.jar
COPY ${JAR_FILE} app.jar

# copy project dependencies
# cp folders to  /usr/local/runme/lib, etc
ADD ${JAR_CONFIG} config/

ENTRYPOINT ["java","-jar","flow-0.2-SNAPSHOT.jar"]

RUN apt-get update && \
	apt-get install -y openjdk-11-jdk && \
	apt-get install -y ant && \
	apt-get clean && \
	rm -rf /var/lib/apt/lists/* && \
	rm -rf /var/cache/oracle-jdk8-installer;
	
# Fix certificate issues, found as of 
# https://bugs.launchpad.net/ubuntu/+source/ca-certificates-java/+bug/983302
RUN apt-get update && \
	apt-get install -y ca-certificates-java && \
	apt-get clean && \
	update-ca-certificates -f && \
	rm -rf /var/lib/apt/lists/* && \
	rm -rf /var/cache/oracle-jdk8-installer;

# Setup JAVA_HOME, this is useful for docker commandline
ENV JAVA_HOME /usr/lib/jvm/java-11-openjdk-amd64/

RUN export JAVA_HOME

