# Docker
1. **更新软件包列表：**
   ```bash
   sudo apt update
   ```
2. **安装依赖包：**
   ```bash
   sudo apt install -y apt-transport-https ca-certificates curl software-properties-common
   ```
3. **添加Docker GPG密钥：**
   ```bash
   curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg
   ```
4. **设置稳定版本的Docker存储库：**
   ```bash
   echo "deb [signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
   ```

   如果你想安装Docker的测试版，可以使用以下命令：
   ```bash
   echo "deb [signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/ubuntu $(lsb_release -cs) test" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
   ```
5. **安装Docker Engine：**
   ```bash
   sudo apt update
   sudo apt install -y docker-ce docker-ce-cli containerd.io
   ```
6. **启动Docker服务：**
   ```bash
   sudo systemctl start docker
   ```
7. **将当前用户添加到`docker`组（可选，以便无需使用`sudo`运行Docker命令）：**
   ```bash
   sudo usermod -aG docker $USER
   ```

   请记得注销并重新登录，以使组成员身份更改生效。
8. **验证Docker安装是否成功：**
   ```bash
   docker --version
   docker run hello-world
   ```