Best practice
==============

# Always Set a USER

It's important to set the USER statement in all your Dockerfiles (or change the user within an ENTRYPOINT or CMD script). 
If you don't do this, your processes will be running as root within the container.
As UIDs are the same within a container and on the host, should an attacker manage to break the container, he will have root access to the host machine.

```
RUN groupadd -r uwsgi && useradd -r -g uwsgi uwsgi
USER uwsgi
```

# Organizing metadata with labels
Docker Inc. recommends recording metadata with labels to help organize images, networks, containers, and other objects. 
Each label key should be prefixed with the reverse DNS notation of a domain that is controlled or collaborating with the author,
such as `com.<your company>.some-label.` 
Labels are flexible, extensible, and lightweight, but the lack of structure makes leveraging the information difficult.

Example:

```shell
version=0.6
docker image build -t mailer:${version} \
  -f Dockerfile.mailer.df \
  --build-arg VERSION=${version} .
  
docker image inspect --format '{{ json .Config.Labels }}' mailer:0.6
```

