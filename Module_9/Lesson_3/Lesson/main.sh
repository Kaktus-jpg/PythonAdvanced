sudo apt-get remove docker docker.engine docker.io containerd runc
# Add Docker's official GPG key:
sudo apt update
sudo apt install ca-certificates curl
sudo install -m 0755 -d /etc/apt/keyrings
sudo curl -fsSL https://download.docker.com/linux/ubuntu/gpg -o /etc/apt/keyrings/docker.asc
sudo chmod a+r /etc/apt/keyrings/docker.asc

# Add the repository to Apt sources:
sudo tee /etc/apt/sources.list.d/docker.sources <<EOF
Types: deb
URIs: https://download.docker.com/linux/ubuntu
Suites: $(. /etc/os-release && echo "${UBUNTU_CODENAME:-$VERSION_CODENAME}")
Components: stable
Architectures: $(dpkg --print-architecture)
Signed-By: /etc/apt/keyrings/docker.asc
EOF

sudo apt update
sudo apt upgrade

sudo apt install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
sudo docker run hello-world

sudo groupadd docker
sudo usermod -aG docker $USER

docker run hello-world
docker run debian echo "Hello world"
docker run debian echo "Hello world"

docker run -it debian bash
docker run -h HOST -it debian bash
rm -r /bin
ls
docker ps
docker diff <name>
docker logs <name>
exit
docker ps
docker ps -a
docker rm <name>
docker -it --rm 06kelly/nyancat