# Ubuntu
https://docs.docker.com/engine/install/ubuntu/#install-from-a-package

1、sudo apt-get remove docker docker-engine docker.io containerd runc

2、sudo apt-get update

3、sudo apt-get install ca-certificates curl gnupg lsb-release

4、sudo mkdir -p /etc/apt/keyrings

5、curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /etc/apt/keyrings/docker.gpg

6、echo "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null

7、sudo apt-get update

8、sudo apt-get install docker-ce docker-ce-cli containerd.io docker-compose-plugin

9、sudo docker run hello-world