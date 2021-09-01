# hello world

```c++
#include <iostream>  //头文件
#include <Windows.h>

int main(void) {
	std::cout << "1.网站404攻击" << std::endl;
	std::cout << "2.网站篡改攻击" << std::endl;
	std::cout << "3.网站攻击记录" << std::endl;
	std::cout << "4.DNS攻击" << std::endl;
	std::cout << "5.服务器重启攻击" << std::endl;

	system("pause");
	return 0;
}
```

## 头文件

- 放在首行
- <>直接到项目默认头文件目录引入
- "" 优先当前文件目录，再默认

```c++
#include <iostream>  //头文件
#include "Windows.h"
```

## main 函数

- 

```c++
//返回类型 main (形参) {
int main(void) {
	std::cout << "1.网站404攻击" << std::endl;
	system("pause");
	return 0;
}
```