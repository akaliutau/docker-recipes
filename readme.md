
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

/build - contains recipe to compose already existing image with the new one (to be build from Dockerfile)

This example shows how to build two containers from Redis image and RubbitMQ image with runtime customization.


/multistage - contains multi step process pipelines with data transfer between steps

/pyserver - contains simple socket server written in Python 3.x

```
docker build -t pyserver:1.0 .
```

run server:

```
docker run pyserver:1.0
```

/server - an example of dockerized server

Index
======

* [Best practice in writing a Dockerfile](https://docs.docker.com/articles/dockerfile_best-practices/)

* [Fundamentals](./fundamentals.md)

* [Common Commands](./commands.md)

* [Best practice](./best_practice.md)


