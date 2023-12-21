# I. Init

- [I. Init](#i-init)
  - [1. Installation de Docker](#1-installation-de-docker)
  - [2. Vérifier que Docker est bien là](#2-vérifier-que-docker-est-bien-là)
  - [3. sudo c pa bo](#3-sudo-c-pa-bo)
  - [4. Un premier conteneur en vif](#4-un-premier-conteneur-en-vif)
  - [5. Un deuxième conteneur en vif](#5-un-deuxième-conteneur-en-vif)

## 1. Installation de Docker

Pour installer Docker, il faut **toujours** (comme d'hab en fait) se référer à la doc officielle.

**Je vous laisse donc suivre les instructions de la doc officielle pour installer Docker dans la VM.**

> ***Il n'y a pas d'instructions spécifiques pour Rocky dans la doc officielle**, mais rocky est très proche de CentOS. Vous pouvez donc suivre les instructions pour CentOS 9.*

## 2. Vérifier que Docker est bien là

```bash
# est-ce que le service Docker existe ?
systemctl status docker

# si oui, on le démarre alors
sudo systemctl start docker

# voyons si on peut taper une commande docker
sudo docker info
sudo docker ps
```

## 3. sudo c pa bo
🌞 **Ajouter votre utilisateur au groupe `docker`**

```bash
[lytzeer@tp1 ~]$ sudo usermod -aG docker lytzeer
```

## 4. Un premier conteneur en vif

🌞 **Lancer un conteneur NGINX**

- avec la commande suivante :

```bash
[lytzeer@tp1 ~]$ docker run -d -p 9999:80 nginx
```

> Si tu mets pas le `-d` tu vas perdre la main dans ton terminal, et tu auras les logs du conteneur directement dans le terminal. `-d` comme *daemon* : pour lancer en tâche de fond. Essaie pour voir !

🌞 **Visitons**

```bash
[lytzeer@tp1 ~]$ docker ps
CONTAINER ID   IMAGE     COMMAND                  CREATED          STATUS          PORTS
   NAMES
0b6c4d68aba3   nginx     "/docker-entrypoint.…"   22 minutes ago   Up 21 minutes   0.0.0.0:9999->80/tcp, :::9999->80/tcp   objective_wiles

[lytzeer@tp1 ~]$ docker logs 0b
/docker-entrypoint.sh: /docker-entrypoint.d/ is not empty, will attempt to perform configuration
/docker-entrypoint.sh: Looking for shell scripts in /docker-entrypoint.d/
/docker-entrypoint.sh: Launching /docker-entrypoint.d/10-listen-on-ipv6-by-default.sh
10-listen-on-ipv6-by-default.sh: info: Getting the checksum of /etc/nginx/conf.d/default.conf
10-listen-on-ipv6-by-default.sh: info: Enabled listen on IPv6 in /etc/nginx/conf.d/default.conf
/docker-entrypoint.sh: Sourcing /docker-entrypoint.d/15-local-resolvers.envsh
/docker-entrypoint.sh: Launching /docker-entrypoint.d/20-envsubst-on-templates.sh
/docker-entrypoint.sh: Launching /docker-entrypoint.d/30-tune-worker-processes.sh
/docker-entrypoint.sh: Configuration complete; ready for start up
2023/12/21 09:49:14 [notice] 1#1: using the "epoll" event method
2023/12/21 09:49:14 [notice] 1#1: nginx/1.25.3
2023/12/21 09:49:14 [notice] 1#1: built by gcc 12.2.0 (Debian 12.2.0-14)
2023/12/21 09:49:14 [notice] 1#1: OS: Linux 5.14.0-284.30.1.el9_2.x86_64
2023/12/21 09:49:14 [notice] 1#1: getrlimit(RLIMIT_NOFILE): 1073741816:1073741816
2023/12/21 09:49:14 [notice] 1#1: start worker processes
2023/12/21 09:49:14 [notice] 1#1: start worker process 30
2023/12/21 09:49:14 [notice] 1#1: start worker process 31
```
- Docker inspect
    <details>

```
[lytzeer@tp1 ~]$ docker inspect 0b
[
    {
        "Id": "0b6c4d68aba36617dc75264623b1fbe63548e3defa237de115e73114dbbc802f",
        "Created": "2023-12-21T09:49:13.552766878Z",
        "Path": "/docker-entrypoint.sh",
        "Args": [
            "nginx",
            "-g",
            "daemon off;"
        ],
        "State": {
            "Status": "running",
            "Running": true,
            "Paused": false,
            "Restarting": false,
            "OOMKilled": false,
            "Dead": false,
            "Pid": 1696,
            "ExitCode": 0,
            "Error": "",
            "StartedAt": "2023-12-21T09:49:14.473726858Z",
            "FinishedAt": "0001-01-01T00:00:00Z"
        },
        "Image": "sha256:d453dd892d9357f3559b967478ae9cbc417b52de66b53142f6c16c8a275486b9",
        "ResolvConfPath": "/var/lib/docker/containers/0b6c4d68aba36617dc75264623b1fbe63548e3defa237de115e73114dbbc802f/resolv.conf",
        "HostnamePath": "/var/lib/docker/containers/0b6c4d68aba36617dc75264623b1fbe63548e3defa237de115e73114dbbc802f/hostname",
        "HostsPath": "/var/lib/docker/containers/0b6c4d68aba36617dc75264623b1fbe63548e3defa237de115e73114dbbc802f/hosts",
        "LogPath": "/var/lib/docker/containers/0b6c4d68aba36617dc75264623b1fbe63548e3defa237de115e73114dbbc802f/0b6c4d68aba36617dc75264623b1fbe63548e3defa237de115e73114dbbc802f-json.log",
        "Name": "/objective_wiles",
        "RestartCount": 0,
        "Driver": "overlay2",
        "Platform": "linux",
        "MountLabel": "",
        "ProcessLabel": "",
        "AppArmorProfile": "",
        "ExecIDs": null,
        "HostConfig": {
            "Binds": null,
            "ContainerIDFile": "",
            "LogConfig": {
                "Type": "json-file",
                "Config": {}
            },
            "NetworkMode": "default",
            "PortBindings": {
                "80/tcp": [
                    {
                        "HostIp": "",
                        "HostPort": "9999"
                    }
                ]
            },
            "RestartPolicy": {
                "Name": "no",
                "MaximumRetryCount": 0
            },
            "AutoRemove": false,
            "VolumeDriver": "",
            "VolumesFrom": null,
            "ConsoleSize": [
                30,
                120
            ],
            "CapAdd": null,
            "CapDrop": null,
            "CgroupnsMode": "private",
            "Dns": [],
            "DnsOptions": [],
            "DnsSearch": [],
            "ExtraHosts": null,
            "GroupAdd": null,
            "IpcMode": "private",
            "Cgroup": "",
            "Links": null,
            "OomScoreAdj": 0,
            "PidMode": "",
            "Privileged": false,
            "PublishAllPorts": false,
            "ReadonlyRootfs": false,
            "SecurityOpt": null,
            "UTSMode": "",
            "UsernsMode": "",
            "ShmSize": 67108864,
            "Runtime": "runc",
            "Isolation": "",
            "CpuShares": 0,
            "Memory": 0,
            "NanoCpus": 0,
            "CgroupParent": "",
            "BlkioWeight": 0,
            "BlkioWeightDevice": [],
            "BlkioDeviceReadBps": [],
            "BlkioDeviceWriteBps": [],
            "BlkioDeviceReadIOps": [],
            "BlkioDeviceWriteIOps": [],
            "CpuPeriod": 0,
            "CpuQuota": 0,
            "CpuRealtimePeriod": 0,
            "CpuRealtimeRuntime": 0,
            "CpusetCpus": "",
            "CpusetMems": "",
            "Devices": [],
            "DeviceCgroupRules": null,
            "DeviceRequests": null,
            "MemoryReservation": 0,
            "MemorySwap": 0,
            "MemorySwappiness": null,
            "OomKillDisable": null,
            "PidsLimit": null,
            "Ulimits": null,
            "CpuCount": 0,
            "CpuPercent": 0,
            "IOMaximumIOps": 0,
            "IOMaximumBandwidth": 0,
            "MaskedPaths": [
                "/proc/asound",
                "/proc/acpi",
                "/proc/kcore",
                "/proc/keys",
                "/proc/latency_stats",
                "/proc/timer_list",
                "/proc/timer_stats",
                "/proc/sched_debug",
                "/proc/scsi",
                "/sys/firmware",
                "/sys/devices/virtual/powercap"
            ],
            "ReadonlyPaths": [
                "/proc/bus",
                "/proc/fs",
                "/proc/irq",
                "/proc/sys",
                "/proc/sysrq-trigger"
            ]
        },
        "GraphDriver": {
            "Data": {
                "LowerDir": "/var/lib/docker/overlay2/373db2783f911a19f82ec40cff49c8881cfa47bceeda2b87505703f9a8833e16-init/diff:/var/lib/docker/overlay2/95f81120cc028b539ec78a711ff096649570e9c884e894087a6d0a4482f0a880/diff:/var/lib/docker/overlay2/66b293e3189248ff13170db07a37189c7e917c60f8840bd5a4e72010eac33ead/diff:/var/lib/docker/overlay2/bafac2c9476c4c6e8f3c37f7df06dff455fcc3045c3a0c3b08e1eec6a49ee7ec/diff:/var/lib/docker/overlay2/a3e91fba52901d43bb0f050374f0b6c88778910e96093bc12a39a20463a9b896/diff:/var/lib/docker/overlay2/af6cde245b9c58f142097e4a122e1d3bfe14a86fd473d2890cf0a24a3974d960/diff:/var/lib/docker/overlay2/9f23eb4a34543c59b0a8eb57797ffebbb7b1b36d11f83f8dfdf18a579e42c01a/diff:/var/lib/docker/overlay2/270d1f9775a54ea19f69f8772a36805c0d7c719ab34c6a82da1cbd876f0b2195/diff",
                "MergedDir": "/var/lib/docker/overlay2/373db2783f911a19f82ec40cff49c8881cfa47bceeda2b87505703f9a8833e16/merged",
                "UpperDir": "/var/lib/docker/overlay2/373db2783f911a19f82ec40cff49c8881cfa47bceeda2b87505703f9a8833e16/diff",
                "WorkDir": "/var/lib/docker/overlay2/373db2783f911a19f82ec40cff49c8881cfa47bceeda2b87505703f9a8833e16/work"
            },
            "Name": "overlay2"
        },
        "Mounts": [],
        "Config": {
            "Hostname": "0b6c4d68aba3",
            "Domainname": "",
            "User": "",
            "AttachStdin": false,
            "AttachStdout": false,
            "AttachStderr": false,
            "ExposedPorts": {
                "80/tcp": {}
            },
            "Tty": false,
            "OpenStdin": false,
            "StdinOnce": false,
            "Env": [
                "PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin",
                "NGINX_VERSION=1.25.3",
                "NJS_VERSION=0.8.2",
                "PKG_RELEASE=1~bookworm"
            ],
            "Cmd": [
                "nginx",
                "-g",
                "daemon off;"
            ],
            "Image": "nginx",
            "Volumes": null,
            "WorkingDir": "",
            "Entrypoint": [
                "/docker-entrypoint.sh"
            ],
            "OnBuild": null,
            "Labels": {
                "maintainer": "NGINX Docker Maintainers <docker-maint@nginx.com>"
            },
            "StopSignal": "SIGQUIT"
        },
        "NetworkSettings": {
            "Bridge": "",
            "SandboxID": "b5939c972c28b9857552579a03e9e070a87bd2b40e133ecc9d67417ba0f0b87a",
            "HairpinMode": false,
            "LinkLocalIPv6Address": "",
            "LinkLocalIPv6PrefixLen": 0,
            "Ports": {
                "80/tcp": [
                    {
                        "HostIp": "0.0.0.0",
                        "HostPort": "9999"
                    },
                    {
                        "HostIp": "::",
                        "HostPort": "9999"
                    }
                ]
            },
            "SandboxKey": "/var/run/docker/netns/b5939c972c28",
            "SecondaryIPAddresses": null,
            "SecondaryIPv6Addresses": null,
            "EndpointID": "9cae6ba4ac06f4551f5fedf4f91a9aba5ca1e4ea77a5a7bf71a917239a65a68b",
            "Gateway": "172.17.0.1",
            "GlobalIPv6Address": "",
            "GlobalIPv6PrefixLen": 0,
            "IPAddress": "172.17.0.2",
            "IPPrefixLen": 16,
            "IPv6Gateway": "",
            "MacAddress": "02:42:ac:11:00:02",
            "Networks": {
                "bridge": {
                    "IPAMConfig": null,
                    "Links": null,
                    "Aliases": null,
                    "NetworkID": "07ca6d5b08236e3875bf08f1af5a7b92159e139b64c4493a1988e30d71aa9801",
                    "EndpointID": "9cae6ba4ac06f4551f5fedf4f91a9aba5ca1e4ea77a5a7bf71a917239a65a68b",
                    "Gateway": "172.17.0.1",
                    "IPAddress": "172.17.0.2",
                    "IPPrefixLen": 16,
                    "IPv6Gateway": "",
                    "GlobalIPv6Address": "",
                    "GlobalIPv6PrefixLen": 0,
                    "MacAddress": "02:42:ac:11:00:02",
                    "DriverOpts": null
                }
            }
        }
    }
]
```

</details>

```
[lytzeer@tp1 ~]$ sudo ss -lnpt | grep docker
LISTEN 0      4096         0.0.0.0:9999      0.0.0.0:*    users:(("docker-proxy",pid=1652,fd=4))

[lytzeer@tp1 ~]$ sudo firewall-cmd --add-port=9999/tcp --permanent
success
[lytzeer@tp1 ~]$ sudo firewall-cmd --reload
success
[lytzeer@tp1 ~]$ sudo firewall-cmd --list-all | grep ports
  ports: 9999/tcp
```

🌞 **On va ajouter un site Web au conteneur NGINX**

- exemple de `index.html` :

```html
<h1>MEOOOW</h1>
```

- config NGINX minimale pour servir un nouveau site web dans `site_nul.conf` :

```nginx
server {
    listen        8080;

    location / {
        root /var/www/html/;
    }
}
```

```bash
docker run -d -p 9999:8080 -v /home/lytzeer/nginx/index.html:/var/www/html/index.html -v /home/lytzeer/nginx/site_nul.conf:/etc/nginx/conf.d/site_nul.conf nginx
```

🌞 **Visitons**

```bash
[lytzeer@tp1 nginx]$ docker ps
CONTAINER ID   IMAGE     COMMAND                  CREATED          STATUS          PORTS                                               NAMES
63517fff1747   nginx     "/docker-entrypoint.…"   43 seconds ago   Up 41 seconds   80/tcp, 0.0.0.0:9999->8080/tcp, :::9999->8080/tcp   sad_cray
```

## 5. Un deuxième conteneur en vif

🌞 **Lance un conteneur Python, avec un shell**

```bash
[lytzeer@tp1 ~]$ docker run -it python bash
```

🌞 **Installe des libs Python**

```bash
root@2852f21c459d:/# pip install aiohttp
root@2852f21c459d:/# pip install aioconsole
root@2852f21c459d:/# python
Python 3.12.1 (main, Dec 19 2023, 20:14:15) [GCC 12.2.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> import aiohttp
>>>
```

```bash
root@2852f21c459d:/# ls
bin   dev  home  lib32  libx32  mnt  proc  run   srv  tmp  var
boot  etc  lib   lib64  media   opt  root  sbin  sys  usr

root@2852f21c459d:/# ip a
bash: ip: command not found
```

# II. Images

- [II. Images](#ii-images)
  - [1. Images publiques](#1-images-publiques)
  - [2. Construire une image](#2-construire-une-image)

## 1. Images publiques

🌞 **Récupérez des images**

```
[lytzeer@tp1 ~]$ docker pull python:3.11
3.11: Pulling from library/python
bc0734b949dc: Already exists
b5de22c0f5cd: Already exists
917ee5330e73: Already exists
b43bd898d5fb: Already exists
7fad4bffde24: Already exists
1f68ce6a3e62: Pull complete
e27d998f416b: Pull complete
fefdcd9854bf: Pull complete
Digest: sha256:4e5e9b05dda9cf699084f20bb1d3463234446387fa0f7a45d90689c48e204c83
Status: Downloaded newer image for python:3.11
docker.io/library/python:3.11

[lytzeer@tp1 ~]$ docker pull mysql:5.7
5.7: Pulling from library/mysql
20e4dcae4c69: Pull complete
1c56c3d4ce74: Pull complete
e9f03a1c24ce: Pull complete
68c3898c2015: Pull complete
6b95a940e7b6: Pull complete
90986bb8de6e: Pull complete
ae71319cb779: Pull complete
ffc89e9dfd88: Pull complete
43d05e938198: Pull complete
064b2d298fba: Pull complete
df9a4d85569b: Pull complete
Digest: sha256:4bc6bc963e6d8443453676cae56536f4b8156d78bae03c0145cbe47c2aad73bb
Status: Downloaded newer image for mysql:5.7
docker.io/library/mysql:5.7

[lytzeer@tp1 ~]$ docker pull wordpress:latest
latest: Pulling from library/wordpress
af107e978371: Already exists
6480d4ad61d2: Pull complete
95f5176ece8b: Pull complete
0ebe7ec824ca: Pull complete
673e01769ec9: Pull complete
74f0c50b3097: Pull complete
1a19a72eb529: Pull complete
50436df89cfb: Pull complete
8b616b90f7e6: Pull complete
df9d2e4043f8: Pull complete
d6236f3e94a1: Pull complete
59fa8b76a6b3: Pull complete
99eb3419cf60: Pull complete
22f5c20b545d: Pull complete
1f0d2c1603d0: Pull complete
4624824acfea: Pull complete
79c3af11cab5: Pull complete
e8d8239610fb: Pull complete
a1ff013e1d94: Pull complete
31076364071c: Pull complete
87728bbad961: Pull complete
Digest: sha256:be7173998a8fa131b132cbf69d3ea0239ff62be006f1ec11895758cf7b1acd9e
Status: Downloaded newer image for wordpress:latest
docker.io/library/wordpress:latest

[lytzeer@tp1 ~]$ docker pull linuxserver/wikijs
Using default tag: latest
latest: Pulling from linuxserver/wikijs
8b16ab80b9bd: Pull complete
07a0e16f7be1: Pull complete
145cda5894de: Pull complete
1a16fa4f6192: Pull complete
84d558be1106: Pull complete
4573be43bb06: Pull complete
20b23561c7ea: Pull complete
Digest: sha256:131d247ab257cc3de56232b75917d6f4e24e07c461c9481b0e7072ae8eba3071
Status: Downloaded newer image for linuxserver/wikijs:latest
docker.io/linuxserver/wikijs:latest
```

```bash
[lytzeer@tp1 ~]$ docker images
REPOSITORY           TAG       IMAGE ID       CREATED        SIZE
linuxserver/wikijs   latest    869729f6d3c5   5 days ago     441MB
mysql                5.7       5107333e08a8   8 days ago     501MB
python               latest    fc7a60e86bae   13 days ago    1.02GB
wordpress            latest    fd2f5a0c6fba   2 weeks ago    739MB
python               3.11      22140cbb3b0c   2 weeks ago    1.01GB
nginx                latest    d453dd892d93   8 weeks ago    187MB
```

🌞 **Lancez un conteneur à partir de l'image Python**

```bash
[lytzeer@tp1 ~]$ docker run -it python:3.11 bash
root@6e66e46a6fa6:/# python
Python 3.11.7 (main, Dec 19 2023, 20:33:49) [GCC 12.2.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>>
```

## 2. Construire une image

Pour construire une image il faut :

- créer un fichier `Dockerfile`
- exécuter une commande `docker build` pour produire une image à partir du `Dockerfile`

🌞 **Ecrire un Dockerfile pour une image qui héberge une application Python**

- l'image doit contenir
  - une base debian (un `FROM`)
  - l'installation de Python (un `RUN` qui lance un `apt install`)
    - il faudra forcément `apt update` avant
    - en effet, le conteneur a été allégé au point d'enlever la liste locale des paquets dispos
    - donc nécessaire d'update avant de install quoique ce soit
  - l'installation de la librairie Python `emoji` (un `RUN` qui lance un `pip install`)
  - ajout de l'application (un `COPY`)
  - le lancement de l'application (un `ENTRYPOINT`)
- le code de l'application :

```bash
[lytzeer@tp1 ~]$ mkdir build_nul
[lytzeer@tp1 ~]$ cd build_nul
[lytzeer@tp1 build_nul]$ nano Dockerfile
FROM debian
RUN apt update -y && apt install -y python3 && apt install -y python3-emoji && mkdir app
COPY app.py /app/app.py
ENTRYPOINT ["python3","/app/app.py"]
[lytzeer@tp1 build_nul]$ nano app.py
import emoji

print(emoji.emojize("Cet exemple d'application est vraiment naze :thumbs_down:"))
```

🌞 **Build l'image**

```bash
[lytzeer@tp1 build_nul]$ docker build . -t python_app:version_de_ouf
[+] Building 40.1s (8/8) FINISHED                            docker:default
 => [internal] load build definition from Dockerfile                   0.0s
 => => transferring dockerfile: 260B                                   0.0s
 => [internal] load .dockerignore                                      0.0s
 => => transferring context: 2B                                        0.0s
 => [internal] load metadata for docker.io/library/debian:latest       3.1s
 => [1/3] FROM docker.io/library/debian@sha256:bac353db4cc04bc672b140  0.2s
 => => resolve docker.io/library/debian@sha256:bac353db4cc04bc672b140  0.1s
 => => sha256:2a033a8c63712da54b5a516f5d69d41606cfb5c 1.46kB / 1.46kB  0.0s
 => => sha256:bac353db4cc04bc672b14029964e686cd7bad56 1.85kB / 1.85kB  0.0s
 => => sha256:0dc902c61cb495db4630a6dc2fa14cd45bd9f8515f2 529B / 529B  0.0s
 => [internal] load build context                                      0.1s
 => => transferring context: 188B                                      0.0s
 => [2/3] RUN apt update -y && apt install -y python3 && apt install  35.7s
 => [3/3] COPY app.py /app/app.py                                      0.1s
 => exporting to image                                                 0.7s
 => => exporting layers                                                0.6s
 => => writing image sha256:0711e82082255d1cf5c43081cbab65c5e50826da4  0.0s
 => => naming to docker.io/library/python_app:version_de_ouf           0.0s
```

```bash
[lytzeer@tp1 build_nul]$ docker images | grep python_app
python_app           version_de_ouf   0711e8208225   52 seconds ago   189MB
```

🌞 **Lancer l'image**

```bash
[lytzeer@tp1 build_nul]$ docker run python_app:version_de_ouf
Cet exemple d'application est vraiment naze 👎
```

# III. Docker compose

Pour la fin de ce TP on va manipuler un peu `docker compose`.

🌞 **Créez un fichier `docker-compose.yml`**

```bash
[lytzeer@tp1 ~]$ mkdir compose_test
[lytzeer@tp1 ~]$ nano compose_test/docker-compose.yml
version: "3"

services:
  conteneur_nul:
    image: debian
    entrypoint: sleep 9999
  conteneur_flopesque:
    image: debian
    entrypoint: sleep 9999
```

🌞 **Lancez les deux conteneurs** avec `docker compose`

```bash
[lytzeer@tp1 ~]$ cd compose_test

[lytzeer@tp1 compose_test]$ docker compose up -d
[+] Running 3/3
 ✔ conteneur_nul 1 layers [⣿]      0B/0B      Pulled                   2.9s
   ✔ bc0734b949dc Already exists                                       0.0s
 ✔ conteneur_flopesque Pulled                                          3.2s
[+] Running 3/3
 ✔ Network compose_test_default                  Created               0.3s
 ✔ Container compose_test-conteneur_nul-1        Started               0.1s
 ✔ Container compose_test-conteneur_flopesque-1  Started               0.1s
```

🌞 **Vérifier que les deux conteneurs tournent**

- toujours avec une commande `docker`
- tu peux aussi use des trucs comme `docker compose ps` ou `docker compose top` qui sont cools dukoo
  - `docker compose --help` pour voir les bails

```bash
[lytzeer@tp1 compose_test]$ docker compose ps
NAME                                 IMAGE     COMMAND        SERVICE               CREATED         STATUS         PORTS
compose_test-conteneur_flopesque-1   debian    "sleep 9999"   conteneur_flopesque   3 minutes ago   Up 3 minutes
compose_test-conteneur_nul-1         debian    "sleep 9999"   conteneur_nul         3 minutes ago   Up 3 minutes
```

🌞 **Pop un shell dans le conteneur `conteneur_nul`**

```bash
[lytzeer@tp1 compose_test]$ docker exec -it compose_test-conteneur_nul-1 bash
root@87b8801476f5:/#

root@87b8801476f5:/# apt update

root@87b8801476f5:/# apt install ping

root@87b8801476f5:/# ping conteneur_flopesque
PING conteneur_flopesque (172.18.0.2) 56(84) bytes of data.
64 bytes from compose_test-conteneur_flopesque-1.compose_test_default (172.18.0.2): icmp_seq=1 ttl=64 time=0.423 ms
64 bytes from compose_test-conteneur_flopesque-1.compose_test_default (172.18.0.2): icmp_seq=2 ttl=64 time=0.188 ms
64 bytes from compose_test-conteneur_flopesque-1.compose_test_default (172.18.0.2): icmp_seq=3 ttl=64 time=0.081 ms
64 bytes from compose_test-conteneur_flopesque-1.compose_test_default (172.18.0.2): icmp_seq=4 ttl=64 time=0.088 ms
64 bytes from compose_test-conteneur_flopesque-1.compose_test_default (172.18.0.2): icmp_seq=5 ttl=64 time=0.278 ms

--- conteneur_flopesque ping statistics ---
5 packets transmitted, 5 received, 0% packet loss, time 4042ms
rtt min/avg/max/mdev = 0.081/0.211/0.423/0.128 ms
```

![In the future](./img/in_the_future.jpg)