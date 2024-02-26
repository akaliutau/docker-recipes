Fundamentals 
=============

# Layers

Each instruction in a Dockerfile results in a new image layer, which can also be used to start a container. 
The new layer is created by starting a container using the image of the previous layer, executing the Dockerfile instruction and saving a new image. 
When a Dockerfile instruction successfully completes, the intermediate container will be deleted, unless the `--rm=false` argument was given.

One can see the full set of layers that make up an image:

```shell
docker history mongo:latest
```

# Building the image

```shell
docker build -t flask-app -f ./Dockerfile.flask_app.df .
docker run -d -p 5000:5000 flask-app
```

# Running a command inside

Runing a command inside a container can be used to perform maintenance tasks or as a replacement for ssh to log in to a container

```shell
ID=$(docker run -d debian sh -c "while true; do sleep 1; done;")
docker exec $ID echo "Hello"
Hello
docker exec -it $ID /bin/bash
```

# Killing container

Sends a signal to the main process (PID 1) in a container (default: SIGKILL), which will cause the container to exit immediately. 
Alternatively, the signal can be specified with the -s argument. The container ID is returned.

```shell
ID=$(docker run -d debian bash -c "trap 'echo caught' SIGTRAP; while true; do sleep 1; done;")
docker kill -s SIGTRAP $ID
e33da73c275b56e734a4bbbefc0b41f6ba84967d09ba08314edd860ebd2da86c

docker logs $ID
caught

docker kill $ID
```

# Get the detailed information on given containers or images

The information includes most configuration information and covers network settings and volume mappings.

```shell
docker inspect
```

# List the exposed port mappings for the given container

Can optionally be given the internal container port and protocol to look up. 
Often used after `docker run -P <image>` to discover the assigned ports.

```shell
ID=$(docker run -P -d redis)
docker port $ID
6379/tcp -> 0.0.0.0:32768

docker port $ID 6379
0.0.0.0:32768

docker port $ID 6379/tcp
0.0.0.0:32768
```

# Connecting Containers to the external world

Publish ports with the -p or -P commands

```shell
docker run -d -p 8000:80 nginx
```

# Linking Containers
Docker links are the simplest way to allow containers on the same host to talk to each other. 
With default Docker networking model, communication between containers will be over an internal Docker network
(ie. communications are not exposed to the host network)

```shell
docker run -d --name myredis redis
docker run --link myredis:redis debian env
```

# Setting Volume Permissions in Dockerfiles

Note: the VOLUME command should be set _last_ (otherwise the perms will not be set)

```
FROM debian:wheezy
RUN useradd foo
RUN mkdir /data && touch /data/x
RUN chown -R foo:foo /data
VOLUME /data
```







