# 3. 在 Linux C 编程中使用 Unicode 和 UTF-8

目前各种 Linux 发行版都支持 UTF-8 编码，当前系统的语言和字符编码设置保存在一些环境变量中，可以通过 `locale` 命令查看：

```text
$ locale
LANG=en_US.UTF-8
LC_CTYPE="en_US.UTF-8"
LC_NUMERIC="en_US.UTF-8"
LC_TIME="en_US.UTF-8"
LC_COLLATE="en_US.UTF-8"
LC_MONETARY="en_US.UTF-8"
LC_MESSAGES="en_US.UTF-8"
LC_PAPER="en_US.UTF-8"
LC_NAME="en_US.UTF-8"
LC_ADDRESS="en_US.UTF-8"
LC_TELEPHONE="en_US.UTF-8"
LC_MEASUREMENT="en_US.UTF-8"
LC_IDENTIFICATION="en_US.UTF-8"
LC_ALL=
```

常用汉字也都位于 BMP 中，所以一个汉字的存储通常占 3 个字节。例如编辑一个 C 程序：

```c
#include <stdio.h>

int main(void)
{
	printf("你好\n");
	return 0;
}
```

源文件是以 UTF-8 编码存储的：

```text
$ od -tc nihao.c
0000000   #   i   n   c   l   u   d   e       <   s   t   d   i   o   .
0000020   h   >  \n  \n   i   n   t       m   a   i   n   (   v   o   i
0000040   d   )  \n   {  \n  \t   p   r   i   n   t   f   (   " 344 275
0000060 240 345 245 275   \   n   "   )   ;  \n  \t   r   e   t   u   r
0000100   n       0   ;  \n   }  \n
0000107
```

其中八进制的 `344 375 240` （十六进制 `e4 bd a0` ）就是“你”的 UTF-8 编码，八进制的 `345 245 275` （十六进制 `e5 a5 bd` ）就是“好”。把它编译成目标文件， `"你好\n"` 这个字符串就成了这样一串字节： `e4 bd a0 e5 a5 bd 0a 00` ，汉字在其中仍然是 UTF-8 编码的，一个汉字占 3 个字节，这种字符在 C 语言中称为多字节字符（Multibyte Character）。运行这个程序相当于把这一串字节 `write` 到当前终端的设备文件。如果当前终端的驱动程序能够识别 UTF-8 编码就能打印出汉字，如果当前终端的驱动程序不能识别 UTF-8 编码（比如一般的字符终端）就打印不出汉字。也就是说，像这种程序，识别汉字的工作既不是由 C 编译器做的也不是由 `libc` 做的，C 编译器原封不动地把源文件中的 UTF-8 编码复制到目标文件中， `libc` 只是当作以 0 结尾的字符串原封不动地 `write` 给内核，识别汉字的工作是由终端的驱动程序做的。

但是仅有这种程度的汉字支持是不够的，有时候我们需要在 C 程序中操作字符串里的字符，比如求字符串 `"你好\n"` 中有几个汉字或字符，用 `strlen` 就不灵了，因为 `strlen` 只看结尾的 0 字节而不管字符串里存的是什么，求出来的是字节数 7。为了在程序中操作 Unicode 字符，C 语言定义了宽字符（Wide Character）类型 `wchar_t` 和一些库函数。在字符常量或字符串字面值前面加一个 L 就表示宽字符常量或宽字符串，例如定义 `wchar_t c = L'你';` ，变量 `c` 的值就是汉字“你”的 31 位 UCS 编码，而 `L"你好\n"` 就相当于 `{L'你', L'好', L'\n', 0}` ， `wcslen` 函数就可以取宽字符串中的字符个数。看下面的程序：

```c
#include <stdio.h>
#include <locale.h>

int main(void)
{
	if (!setlocale(LC_CTYPE, "")) {
		fprintf(stderr, "Can't set the specified locale! "
			"Check LANG, LC_CTYPE, LC_ALL.\n");
		return 1;
	}
	printf("%ls", L"你好\n");
	return 0;
}
```

宽字符串 `L"你好\n"` 在源代码中当然还是存成 UTF-8 编码的，但编译器会把它变成 4 个 UCS 编码 `0x00004f60 0x0000597d 0x0000000a 0x00000000` 保存在目标文件中，按小端存储就是 `60 4f 00 00 7d 59 00 00 0a 00 00 00 00 00 00 00` ，用 `od` 命令查看目标文件应该能找到这些字节。

```text
$ gcc hihao.c
$ od -tx1 a.out
```

`printf ` 的`%ls ` 转换说明表示把后面的参数按宽字符串解释，不是见到 0 字节就结束，而是见到 UCS 编码为 0 的字符才结束，但是要`write ` 到终端仍然需要以多字节编码输出，这样终端驱动程序才能识别，所以`printf ` 在内部把宽字符串转换成多字节字符串再`write ` 出去。事实上，C 标准并没有规定多字节字符必须以 UTF-8 编码，也可以使用其它的多字节编码，在运行时根据环境变量确定当前系统的编码，所以在程序开头需要调用`setlocale ` 获取当前系统的编码设置，如果当前系统是 UTF-8 的，`printf ` 就把 UCS 编码转换成 UTF-8 编码的多字节字符串再`write` 出去。一般来说，程序在做内部计算时通常以宽字符编码，如果要存盘或者输出给别的程序，或者通过网络发给别的程序，则采用多字节编码。

关于 Unicode 和 UTF-8 本节只介绍了最基本的概念，部分内容出自[\[Unicode FAQ\]](bi01.md#bibli.unicodefaq)，读者可进一步参考这篇文章。
