# 参考
- https://segmentfault.com/a/1190000042002239
- https://stackoverflow.com/questions/32163955/how-to-run-shell-script-on-host-from-docker-container

# docker-compose.yml
```yaml
# MySQL
version: '3'
services:
  dahua-mysql:
    user: root
    pid: host # 开启容器执行宿主机shell通道
    env_file:
      - .env
    image: ${NVXDB_IMAGE}
    container_name: dahua-db-dev
    privileged: true
    network_mode: host
    ports:
      - 33306:3306
    environment:
       TZ: Asia/Shanghai
       MYSQL_PORT: 33306
    command: 
      - sh
      - -c 
      - |
          /shell/enset.sh
          /shell/init_start.sh
          /shell/end_mysql.sh
          /shell/install-jdk.sh
    volumes:
      - ./shell:/shell
    restart: always
```