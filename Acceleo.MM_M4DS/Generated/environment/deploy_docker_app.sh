#!/bin/bash
set -e

sudo apt-get update --yes
sudo apt-get install ca-certificates curl
sudo install -m 0755 -d /etc/apt/keyrings
sudo curl -fsSL https://download.docker.com/linux/ubuntu/gpg -o /etc/apt/keyrings/docker.asc
sudo chmod a+r /etc/apt/keyrings/docker.asc

echo \
  "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.asc] https://download.docker.com/linux/ubuntu \
  $(. /etc/os-release && echo "$VERSION_CODENAME") stable" | \
  sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
sudo apt-get update --yes

sudo apt-get install docker-ce docker-ce-cli containerd.io docker-buildx-plugin --yes

docker build -t ubuntu-base:dist-amd64 -f Dockerfile .

clear

docker run -it --rm --name wf_model_dataset_python_dockerContainer --mount type=bind,source=/home/carlos/Escritorio/datasets,target=/wf_model_dataset_python/data ubuntu-base:dist-amd64

docker rmi ubuntu-base:dist-amd64

clear

echo -e "Exiting the application...\n"
