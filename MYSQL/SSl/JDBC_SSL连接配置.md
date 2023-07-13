# MySQL MariaDB SSL Connector (双向证书配置)

## 一、MySQL驱动配置（双向）
### 1、制作java证书库
- ca.pem：MySQL安装data目录下ca.pem、ca-key.pem、client-cert.pem、client-key.pem、server-cert.pem、server-key.pem等
- truststoremysql：将ca.pem导入后的证书库
- 123456：truststoremysql证书库密码

### 2、CA证书
```shell
keytool -importcert -alias Cacert -file ca.pem  -keystore truststoremysql -storepass 123456
```
### 3、客户端证书
```shell
openssl pkcs12 -export -in client-cert.pem -inkey client-key.pem -name "mysqlclient" -passout pass:123456 -out client-keystore.p12
keytool -importkeystore -srckeystore client-keystore.p12 -srcstoretype pkcs12 -srcstorepass 123456 -destkeystore keystoremysql -deststoretype JKS -deststorepass 123456
```
### 4、JDBC CONFIG
```text
username: root
password: 123456
driverClassName: com.mysql.cj.jdbc.Driver
url: jdbc:mysql://127.0.0.1:3306/test?useSSL=true&verifyServerCertificate=true&requireSSL=true&clientCertificateKeyStoreUrl=file:${ssl.cert.path}/keystoremysql&clientCertificateKeyStorePassword=123456&trustCertificateKeyStoreUrl=file:${ssl.cert.path}/truststoremysql&trustCertificateKeyStorePassword=123456&useUnicode=true&characterEncoding=utf8&autoReconnect=true&serverTimezone=Asia/Shanghai
```

## 二、MariaDB驱动配置（双向）

### 1、POM依赖
```xml
<dependency>
    <groupId>org.mariadb.jdbc</groupId>
    <artifactId>mariadb-java-client</artifactId>
</dependency>
```

### 2、参考文章
- https://mariadb.com/kb/en/about-mariadb-connector-j/
- https://mariadb.com/kb/en/using-tls-ssl-with-mariadb-java-connector/#mutual-2-way-authentication

### 3、制作java证书库(同上)

### 4、JDBC CONFIG

```text
username: root
password: 123456
driverClassName: org.mariadb.jdbc.Driver
url: jdbc:mysql://127.0.0.1:3306/test?sslMode=verify-ca&serverSslCert=${ssl.cert.path}/ca.pem&keyStore=${ssl.cert.path}/keystoremysql&keyStorePassword=123456
```

# 三、my.cnf配置
```text
[client]
port=3306

[mysqld]
#basedir=/mysql/basedir
#datadir=/mysql/datadir
max_connections=200
max_connect_errors=10
character-set-server=utf8

log-bin=/var/lib/mysql/mysql-bin
expire_logs_days=7
server-id=1

# 开启SSL（重点）
require_secure_transport=ON
ssl-ca=/var/lib/mysql/ca.pem
ssl-cert=/var/lib/mysql/server-cert.pem
ssl-key=/var/lib/mysql/server-key.pem

[mysql]
default-character-set=utf8
```