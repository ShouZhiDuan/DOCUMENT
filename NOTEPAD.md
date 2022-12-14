# 1、准备原始启动my.cnf重命名为：my.cnf.default，然后挂载到容器:/etc/my.cnf.default
```java
// com/nvxclouds/nvxdbserver/service/impl/ServerConfigServiceImpl.java:143
// TODO rollback to default my.cnf
File my_cnf_default = new File("/etc/my.cnf.default");
InputStream resourceAsStream = new FileInputStream(my_cnf_default);
FileUtils.copyInputStreamToFile(resourceAsStream, new File("/etc/my.cnf"));
```
# 2、大华图片加密
```text
1、私钥利用。(已完成)
2、CSR动态生成。(已完成)
3、tink图片加密改造。(已完成)
4、大华token校验。(已完成)
5、加密、解密性能测试。(进行中。。。。。)
6、DEK持久或者动态获取。(已完成)
```