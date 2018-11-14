'''
docker build -t <your username>/media .
docker images
docker run -p 5000:5000 -d <your username>/media
docker ps
docker logs <container id>
docker exec -it <container id> /bin/bash
'''