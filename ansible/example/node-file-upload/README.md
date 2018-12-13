# Example code how to handle large file upload in Node

Aka how to stream the data directly to disk while they are beeing uploaded.

**You can read more info https://pagep.net/2018/03/31/how-to-handle-large-file-upload-with-nodejs-express-server/**

But the code should be pretty self-explanatory...

**All the magic happens in the [main.js](https://github.com/petrvecera/node-file-upload/blob/master/main.js)**

## Run the code

1. `git clone https://github.com/petrvecera/node-file-upload.git`
2. `cd node-file-upload`
3. `npm install`
4. `node main.js`


## Run as docker

```
docker build -t node-file-upload .
docker run -p 3200:3200 -v /tmp/upload:/usr/src/app/fu node-file-upload:ex1
```

check on the running process ```docker ps```

check the logs ```docker logs <container id>```

login to the running container ```docker exec -it <container id> /bin/bash```

kill the container ```docker kill $(docker ps -q)```


