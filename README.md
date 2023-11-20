# Project Overview:
https://github.com/mubeena12/final-project-assignment-YoctoNanoWebContainer/wiki/AESD-Project-Overview

# Project Schedule
https://github.com/users/mubeena12/projects/1/views/1

# Docker Scaffolding

## To test the sample postgres and webapp stack

```bash
cd docker
./test-webapp.sh
```

## To start/stop the sample postgres and webapp stack

### To start

```bash
cd docker
./start-stop-webapp.sh start
```

### To stop

```bash
cd docker
./start-stop-webapp.sh stop
```

NOTE: Running `test-webapp.sh` will delete the existing postgres and webapp containers, leading to data loss.
