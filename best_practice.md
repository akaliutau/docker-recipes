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


