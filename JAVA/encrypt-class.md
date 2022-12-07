# Maven依赖
```xml
<build>
        <finalName>nvx-db-server-1.1.0</finalName>
        <plugins>
            <plugin>
                <groupId>org.springframework.boot</groupId>
                <artifactId>spring-boot-maven-plugin</artifactId>
            </plugin>
            <plugin>
                <groupId>com.idea-aedi</groupId>
                <artifactId>class-winter-maven-plugin</artifactId>
                <version>2.5.0</version>
                <configuration>
                    <!--<debug>true</debug>-->
                    <tips>锘崴机密@2022</tips>
                    <!--输出加密后的JAR包-->
                    <finalName>nvx-db-server-1.1.0</finalName>
                    <!--需要加密的包-->
                    <includePrefix>com.nvxclouds</includePrefix>
                    <!--密码，这个会在启动JAR的时候需要-->
                    <password>NVXCLOUDS@2022</password>
                    <!--禁止运行中dump-->
                    <jvmArgCheck>-XX:+DisableAttachMechanism</jvmArgCheck>
                </configuration>
                <executions>
                    <execution>
                        <phase>package</phase>
                        <goals>
                            <goal>class-winter</goal>
                        </goals>
                    </execution>
                </executions>
            </plugin>
        </plugins>
    </build>
```
# 启动
```shell
nohub java -javaagent:./encryted-test.jar=passwordFromFile=./pwd.txt -XX:+DisableAttachMechanism -jar ./encryted-test.jar > /dev/null 2>&1 &
```
```shell
java -javaagent:/app/db.jar=password=NVXCLOUDS@2022 -XX:+DisableAttachMechanism -jar /app/db.jar
```
