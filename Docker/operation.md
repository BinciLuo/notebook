## Build
`docker build -t ${IMAGE_NAME:TAG} -f ${DOCKERFILE} (--no-cache) .`
## Run
`docker run (--name ${CONTAINER_NAME}) (-p ${HOST_PORT}:{CONTAINER_PORT}) ${IMAGE_NAME:TAG} (/bin/bash -c "${YOUR ENTRY_POINT}")`