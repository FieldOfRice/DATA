#!/bin/bash

# Exit immediately if a command exits with a non-zero status
set -e

echo "### system update..."
apt update && apt upgrade -y

echo "### install required packages..."
apt install ca-certificates curl -y 

echo "### create GPG key folder..."
install -m 0755 -d /etc/apt/keyrings

echo "### downlaod docker GPG-key..."
curl -fsSL https://download.docker.com/linux/ubuntu/gpg -o /etc/apt/keyrings/docker.asc

echo "### change access rights of GPG key..."
chmod a+r /etc/apt/keyrings/docker.asc

echo "### add docker repository..."
echo \
  "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.asc] https://download.docker.com/linux/ubuntu \
  $(. /etc/os-release && echo "$VERSION_CODENAME") stable" | \
  tee /etc/apt/sources.list.d/docker.list > /dev/null

echo "### update package lists..."
apt update

echo "### install docker related packages..."
apt install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin -y

echo "### install docker compose..."
curl -L https://github.com/docker/compose/releases/download/v$(curl -Ls https://www.servercow.de/docker-compose/latest.php)/docker-compose-$(uname -s)-$(uname -m) -o /usr/local/bin/docker-compose
chmod +x /usr/local/bin/docker-compose

echo "### start portainer container..."
docker run -d -p 9443:9443 --name portainer --restart=always \
  -v /var/run/docker.sock:/var/run/docker.sock \
  -v portainer_data:/data \
  portainer/portainer-ce:latest

echo "### install complete."
