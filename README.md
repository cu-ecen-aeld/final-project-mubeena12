# AESD Final Project

## Project Overview:
https://github.com/mubeena12/final-project-assignment-YoctoNanoWebContainer/wiki/AESD-Project-Overview

## Project Schedule
https://github.com/users/mubeena12/projects/1/views/1

## Docker Scaffolding

### To build the docker webapp image

```bash
docker build --platform linux/arm64 . -t ghcr.io/mubeena12/docker-webapp:latest
```

### To push the docker webapp image

```bash
docker login ghcr.io
docker push ghcr.io/mubeena12/docker-webapp:latest
```

### To test the sample postgres and webapp stack

```bash
cd docker
./test-webapp.sh
```

### To start/stop the sample postgres and webapp stack

#### To start

```bash
cd docker
./start-stop-webapp.sh start
```

#### To stop

```bash
cd docker
./start-stop-webapp.sh stop
```

NOTE: Running `test-webapp.sh` will delete the existing postgres and webapp containers, leading to data loss.

## Yocto Build

### Steps to build jetson-nano-2gb-devkit image using Yocto Project

```bash
git clone https://github.com/OE4T/tegra-demo-distro.git 
git checkout --track origin/kirkstone-l4t-r32.7.x
git submodule update --init
. ./setup-env --machine jetson-nano-2gb-devkit
vi conf/local.conf 
# Uncomment: DL_DIR ?= "${TOPDIR}/downloads"
# Uncomment: SSTATE_DIR ?= "${TOPDIR}/sstate-cache"
# Uncomment: DL_DIR ?= TMPDIR = "${TOPDIR}/tmp"
# Add: IMAGE_INSTALL:append = " python3-docker-compose"
# Add: IMAGE_INSTALL:append = " python3-distutils"
bitbake demo-image-full
```

### Steps to deploy image on jetson-nano-2gb-devkit

```bash
mkdir deploy
cd deploy
ln -s ../tmp/deploy/images/jetson-nano-2gb-devkit/demo-image-full-jetson-nano-2gb-devkit.tegraflash.tar.gz
tar -xvf demo-image-full-jetson-nano-2gb-devkit.tegraflash.tar.gz
sudo ./doflash.sh
```

## Steps to verify image on jetson-nano-2gb-devkit

```bash
ssh root@jetson-nano-2gb-devkit
docker version
docker-compose version
```
