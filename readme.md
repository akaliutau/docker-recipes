
About 
=======

This is a collection of recipes demonstrating different use-cases involving docker.
  


Overview
==========

/basics - contains absolute basics to build of and work with docker images

The following commands demonstrate basic operations which can be performed with a standard linux image.
The first two commands use Dockerfile (container description) file. Note, that one can include any local files into image.

1) Builds image with tag linux-java:1.0. Note the dot at the end of the command.
```
docker build -t linux-java:1.0 .
```

2) Instantiates container and executes commands specified in ENTRYPOINT section of dockerfile 
```
docker run linux-java:1.0
```

Next two commands are related to Dockerfile1 (container description) file

3) Builds image with tag linux-java:1.0. Note the dot at the end of the command.
```
docker -d Dockerfile1 build -t linux-java:2.0 .
```

4) Instantiates container and connects it to standard console.
```
docker run -it linux-java:2.0 /bin/bash
```

/multistage - contains multi step process pipelines with data transfer between steps

/server - an example of dockerized server
