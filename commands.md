Common docker commands
=======================

# Viewing logs

```shell
docker logs --follow
```

# Get info about the Docker environment

```shell
docker -D info
```

# Running image:

```shell
docker run
```

## Common flags:

-i, --interactive
Keeps stdin open (even when it’s not attached). Generally used with -t to start an interactive container session.

```shell
docker run -it debian /bin/bash
```

-e, --env
Sets environment variables inside the container.

```shell
docker run -e var1=value -e var2="val 2" debian env
PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin
HOSTNAME=b15f833d65d8
var1=value
var2=val 2
HOME=/root
```

# Get a list of local images

Includs information such as repository name, tag name, and size. By default, intermediate images (used in the creation of top-level images) are not shown.

```shell
docker images | head -4
```

# Deleting images

```shell
docker rmi
```

To remove all dangling (intermediate) images

```shell
docker rmi $(docker images -q -f dangling=true)
```

# Using the Registry

All creds are stored in `$HOME/.docker/config.json`, new entries are added on `docker login`

```shell
{
	"auths": {
		"https://index.docker.io/v1/": {
			"auth": "<base64 of string user:password to connect to registry>"
		}
	},
	"credHelpers": {
		"asia.gcr.io": "gcloud",
		"eu.gcr.io": "gcloud",
		"gcr.io": "gcloud",
		"marketplace.gcr.io": "gcloud",
		"staging-k8s.gcr.io": "gcloud",
		"us.gcr.io": "gcloud"
	}
}
```

Other commands:

```shell
docker login
docker pull
docker push
```


