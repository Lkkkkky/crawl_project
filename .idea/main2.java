import java.util.Base64;

/**
* 利用盐值和多次加密的方式
*/
public class Base64SaltTest {
private static final String SALT = "helloKitty";
private static final int REPEAT = 5;

/**
* 加密处理
* @param str 要加密的字符串，需要与盐值整合
* @return 加密后的数据
*/
public static String encode(String str) {
                                        // 加盐处理
String temp = str + "{" + SALT + "}";
byte data[] = temp.getBytes();
for (int i = 0; i < REPEAT; i++) {
                                 // 重复加密
data = Base64.getEncoder().encode(data);
}
return new String(data);
}

/**
* 解密处理
  * @param str 需要解密的内容
               * @return 解密后的原始数据
*/
public static String decode(String str) {
                                        // 获取加密的内容
byte data[] = str.getBytes();
for (int i = 0; i < REPEAT; i++) {
                                 // 多次解密
data = Base64.getDecoder().decode(data);
}
// 删除盐值格式
return new String(data).replaceAll("\\{\\w+\\}", "");
}

public static void main(String[] args) {
String str = encode("www.hello.com");
System.out.println("解密：" + decode(str));
}

}