### STANDALONE
```
conda create -n media-service python=3.6
source activate media-service
pip install -r requirements.txt
python serve.py	 
```




### DOCKER

```
docker build -t <your username>/media .
docker images
docker run -p 5000:5000 -d <your username>/media
docker ps
docker logs <container id>
docker exec -it <container id> /bin/bash
```
