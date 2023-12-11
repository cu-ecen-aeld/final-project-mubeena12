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

### Steps to add submodules SensorMonitoringWebApp and SensorMonitoringDriver
```bash
git submodule add git@github.com:Silex93/SensorMonitoringWebApp.git
git submodule add git@github.com:cu-ecen-aeld/final-project-Silex93.git SensorMonitoringDriver
git submodule update --init --recursive
cd SensorMonitoringDriver
git pull origin main
cd ../SensorMonitoringWebApp
git pull origin master
cd ..
docker build --platform linux/arm64 . -t ghcr.io/mubeena12/docker-webapp:latest
docker push ghcr.io/mubeena12/docker-webapp:latest
```

## Yocto Build

### Steps to build jetson-nano-2gb-devkit image using Yocto Project

```bash
git clone https://github.com/OE4T/tegra-demo-distro.git 
git checkout --track origin/kirkstone-l4t-r32.7.x
git submodule update --init
. ./setup-env --machine jetson-nano-2gb-devkit

# Copy the local.conf from this repo
cp <this-repo-clone-path>/jetson-nano-2gb-devkit/local.conf conf/local.conf 

# Alternatively, edit conf/local.conf and make the following changes.
# vi conf/local.conf 
# Uncomment: DL_DIR ?= "${TOPDIR}/downloads"
# Uncomment: SSTATE_DIR ?= "${TOPDIR}/sstate-cache"
# Uncomment: DL_DIR ?= TMPDIR = "${TOPDIR}/tmp"
# Add: IMAGE_INSTALL:append = " python3-docker-compose"
# Add: IMAGE_INSTALL:append = " python3-distutils"

bitbake demo-image-full
```
### Steps to create a custom docker-app layer
```bash
cd tegra-demo-distro
source ./setup-env
bitbake-layers create-layer ../layers/meta-docker-app
bitbake-layers add-layer ../layers/meta-docker-app # Add the layer
bitbake-layers show-layers  # Verify if the new layer is created
# Change the recipes-example and example directory name to recipes-containers and example respectively
cd ../layers/meta-docker-app/
mv recipes-example recipes-containers
cd recipes-containers
mv example docker-app
cd docker-app
# Change example_0.1.bb file name to docker-app_0.1.bb 
mv example_0.1.bb docker-app_0.1.bb
# Add the necessary docker files into a directory
mkdir files
cd files
cp <this-repo-clone-path>/jetson-nano-2gb-devkit/meta-docker-app/recipes-containers/docker-app/files/* .
# Copy the content of the docker-app_0.1.bb 
cp <this-repo-clone-path>/jetson-nano-2gb-devkit/meta-docker-app/recipes-containers/docker-app/docker-app_0.1.bb ../
# Verify the conf/bblayer.conf has the new custom layer
#".../tegra-demo-distro/layers/meta-docker-app/"

# Update the conf/local.conf with below line:
# Add: IMAGE_INSTALL:append = " docker-app"
# If docker is using specific port to forward like below,
# docker-compose.yml
#    ports:
#      - "5500:5500"
# Then include kernel-modules as well in conf/local.conf
# Add: IMAGE_INSTALL:append = " kernel-modules" 
# Or If docker is using "network_mode = host" in the docker-compose.yml file to forward the port then you can skip adding kernel-modules to conf/local.conf 

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
