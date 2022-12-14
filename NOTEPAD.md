# 大华数据库
## 1、准备原始启动my.cnf重命名为：my.cnf.default，然后挂载到容器:/etc/my.cnf.default
```java
// com/nvxclouds/nvxdbserver/service/impl/ServerConfigServiceImpl.java:143
// TODO rollback to default my.cnf
File my_cnf_default = new File("/etc/my.cnf.default");
InputStream resourceAsStream = new FileInputStream(my_cnf_default);
FileUtils.copyInputStreamToFile(resourceAsStream, new File("/etc/my.cnf"));
```