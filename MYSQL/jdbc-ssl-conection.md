方案一：JDK导入证书（部署到本机）

```
 在cmd命令中直接执行该命令
```

keytool -import -trustcacerts -v -alias Mysql -file "C:\\ProgramData\\MySQL\\MySQL Server 8.0\\Data\\ca.pem" -keystore "C:\\Program Files\\Java\\jdk1.8.0\_192\\jre\\lib\\security\\cacerts"

方案二：证书导入证书库（多台服务器共享）

```
  现在的生产系统一般都是分布式，N台机器部署，每台机器都需要执行一次导入证书命令，N台机器就要执行N次命令。
```

如果数据库换个证书，那么所有的机器都要执行一次导入证书命令。

在cmd命令中直接执行该命令

keytool -import -trustcacerts -v -alias Mysql -file "C:\\ProgramData\\MySQL\\MySQL Server 8.0\\Data\\ca.pem" -keystore "mysql.ks"

注意：生成mysql.ks的过程中需要设置密码（trustCertificateKeyStorePassword），生成的mysql.ks文件一般放在C盘的用户文件夹下。

然后将证书放http服务器上，或ftp服务器上。

连接字符串里配置 trustCertificateKeyStoreUrl=http://localhost:8080/static/mysql.ks

密码 trustCertificateKeyStorePassword=123456

最终的连接字符串为

jdbc:mysql://localhost:3306/test-ssl?useUnicode=true&useSSL=true&trustCertificateKeyStorePassword=123456&trustCertificateKeyStoreUrl=http://localhost:8080/static/mysql.ks&serverTimezone=Asia/Shanghai

https://www.bbsmax.com/A/xl56AOpoJr/