docker pull ubuntu
docker run -it ubuntu bash
uname -a
uname -a > version.txt
docker ps
docker diff <container>
rm --no-preserve-root -r /
docker run -d ubuntu sleep 600
docker ps
docker stop <container>
docker rm <container>