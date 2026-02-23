# Summary

[历史](pr01.md)

[前言](pr02.md)

---
## 部分 I. C 语言入门
- [程序的基本概念](ch01.md)

    - [程序和编程语言](intro.program.md)

    - [自然语言和形式语言](intro.naturalformal.md)

    - [程序的调试](ch01s03.md)

    - [第一个程序](intro.helloworld.md)

- [常量、变量和表达式](ch02.md)

    - [继续 Hello World](ch02s01.md)

    - [常量](ch02s02.md)

    - [变量](expr.variable.md)

    - [赋值](ch02s04.md)

    - [表达式](expr.expression.md)

    - [字符类型与字符编码](ch02s06.md)

- [简单函数](ch03.md)

    - [数学函数](ch03s01.md)

    - [自定义函数](ch03s02.md)

    - [形参和实参](ch03s03.md)

    - [全局变量、局部变量和作用域](ch03s04.md)

- [分支语句](ch04.md)

    - [if 语句](ch04s01.md)

    - [if/else 语句](ch04s02.md)

    - [布尔代数](ch04s03.md)

    - [switch 语句](ch04s04.md)

- [深入理解函数](ch05.md)

    - [return 语句](ch05s01.md)

    - [增量式开发](ch05s02.md)

    - [递归](ch05s03.md)

- [循环语句](ch06.md)

    - [while 语句](ch06s01.md)

    - [do/while 语句](ch06s02.md)

    - [for 语句](ch06s03.md)

    - [break 和 continue 语句](ch06s04.md)

    - [嵌套循环](ch06s05.md)

    - [goto 语句和标号](ch06s06.md)

- [结构体](ch07.md)

    - [复合类型与结构体](ch07s01.md)

    - [数据抽象](ch07s02.md)

    - [数据类型标志](ch07s03.md)

    - [嵌套结构体](ch07s04.md)

- [数组](ch08.md)

    - [数组的基本概念](ch08s01.md)

    - [数组应用实例：统计随机数](ch08s02.md)

    - [数组应用实例：直方图](ch08s03.md)

    - [字符串](ch08s04.md)

    - [多维数组](ch08s05.md)

- [编码风格](ch09.md)

    - [缩进和空白](ch09s01.md)

    - [注释](ch09s02.md)

    - [标识符命名](ch09s03.md)

    - [函数](ch09s04.md)

    - [indent 工具](ch09s05.md)

- [gdb](ch10.md)

    - [单步执行和跟踪函数调用](ch10s01.md)

    - [断点](ch10s02.md)

    - [观察点](ch10s03.md)

    - [段错误](ch10s04.md)

- [排序与查找](ch11.md)

    - [算法的概念](ch11s01.md)

    - [插入排序](ch11s02.md)

    - [算法的时间复杂度分析](ch11s03.md)

    - [归并排序](ch11s04.md)

    - [线性查找](ch11s05.md)

    - [折半查找](ch11s06.md)

- [栈与队列](ch12.md)

    - [数据结构的概念](ch12s01.md)

    - [堆栈](ch12s02.md)

    - [深度优先搜索](ch12s03.md)

    - [队列与广度优先搜索](ch12s04.md)

    - [环形队列](ch12s05.md)

- [本阶段总结](ch13.md)

---
## 部分 II. C 语言本质
- [计算机中数的表示](ch14.md)

    - [为什么计算机用二进制计数](ch14s01.md)

    - [不同进制之间的换算](ch14s02.md)

    - [整数的加减运算](ch14s03.md)

    - [浮点数](ch14s04.md)

- [数据类型详解](ch15.md)

    - [整型](ch15s01.md)

    - [浮点型](ch15s02.md)

    - [类型转换](ch15s03.md)

- [运算符详解](ch16.md)

    - [位运算](ch16s01.md)

    - [其它运算符](ch16s02.md)

    - [Side Effect 与 Sequence Point](ch16s03.md)

    - [运算符总结](ch16s04.md)

- [计算机体系结构基础](ch17.md)

    - [内存与地址](ch17s01.md)

    - [CPU](ch17s02.md)

    - [设备](ch17s03.md)

    - [MMU](ch17s04.md)

    - [Memory Hierarchy](ch17s05.md)

- [x86 汇编程序基础](ch18.md)

    - [最简单的汇编程序](ch18s01.md)

    - [x86 的寄存器](ch18s02.md)

    - [第二个汇编程序](ch18s03.md)

    - [寻址方式](ch18s04.md)

    - [ELF 文件](ch18s05.md)

- [汇编与 C 之间的关系](ch19.md)

    - [函数调用](ch19s01.md)

    - [main 函数和启动例程](ch19s02.md)

    - [变量的存储布局](ch19s03.md)

    - [结构体和联合体](ch19s04.md)

    - [C 内联汇编](ch19s05.md)

    - [volatile 限定符](ch19s06.md)

- [链接详解](ch20.md)

    - [多目标文件的链接](ch20s01.md)

    - [定义和声明](ch20s02.md)

    - [静态库](ch20s03.md)

    - [共享库](ch20s04.md)

    - [虚拟内存管理](ch20s05.md)

- [预处理](ch21.md)

    - [预处理的步骤](ch21s01.md)

    - [宏定义](ch21s02.md)

    - [条件预处理指示](ch21s03.md)

    - [其它预处理特性](ch21s04.md)

- [Makefile 基础](ch22.md)

    - [基本规则](ch22s01.md)

    - [隐含规则和模式规则](ch22s02.md)

    - [变量](ch22s03.md)

    - [自动处理头文件的依赖关系](ch22s04.md)

    - [常用的 make 命令行选项](ch22s05.md)

- [指针](ch23.md)

    - [指针的基本概念](ch23s01.md)

    - [指针类型的参数和返回值](ch23s02.md)

    - [指针与数组](ch23s03.md)

    - [指针与 const 限定符](ch23s04.md)

    - [指针与结构体](ch23s05.md)

    - [指向指针的指针与指针数组](ch23s06.md)

    - [指向数组的指针与多维数组](ch23s07.md)

    - [函数类型和函数指针类型](ch23s08.md)

    - [不完全类型和复杂声明](ch23s09.md)

- [函数接口](ch24.md)

    - [本章的预备知识](ch24s01.md)

    - [传入参数与传出参数](ch24s02.md)

    - [两层指针的参数](ch24s03.md)

    - [返回值是指针的情况](ch24s04.md)

    - [回调函数](ch24s05.md)

    - [可变参数](ch24s06.md)

- [C 标准库](ch25.md)

    - [字符串操作函数](ch25s01.md)

    - [标准 I/O 库函数](ch25s02.md)

    - [数值字符串转换函数](ch25s03.md)

    - [分配内存的函数](ch25s04.md)

- [链表、二叉树和哈希表](ch26.md)

    - [链表](ch26s01.md)

    - [二叉树](ch26s02.md)

    - [哈希表](ch26s03.md)

- [本阶段总结](ch27.md)

---
### 部分 III. Linux 系统编程
- [文件与 I/O](ch28.md)

    - [汇编程序的 Hello world](ch28s01.md)

    - [C 标准 I/O 库函数与 Unbuffered I/O 函数](ch28s02.md)

    - [open/close](ch28s03.md)

    - [read/write](ch28s04.md)

    - [lseek](ch28s05.md)

    - [fcntl](ch28s06.md)

    - [ioctl](ch28s07.md)

    - [mmap](ch28s08.md)

- [文件系统](ch29.md)

    - [引言](ch29s01.md)

    - [ext2 文件系统](ch29s02.md)

    - [VFS](ch29s03.md)

- [进程](ch30.md)

    - [引言](ch30s01.md)

    - [环境变量](ch30s02.md)

    - [进程控制](ch30s03.md)

    - [进程间通信](ch30s04.md)

    - [练习：实现简单的 Shell](ch30s05.md)

- [Shell 脚本](ch31.md)

    - [Shell 的历史](ch31s01.md)

    - [Shell 如何执行命令](ch31s02.md)

    - [Shell 的基本语法](ch31s03.md)

    - [bash 启动脚本](ch31s04.md)

    - [Shell 脚本语法](ch31s05.md)

    - [Shell 脚本的调试方法](ch31s06.md)

- [正则表达式](ch32.md)

    - [引言](ch32s01.md)

    - [基本语法](ch32s02.md)

    - [sed](ch32s03.md)

    - [awk](ch32s04.md)

    - [练习：在 C 语言中使用正则表达式](ch32s05.md)

- [信号](ch33.md)

    - [信号的基本概念](ch33s01.md)

    - [产生信号](ch33s02.md)

    - [阻塞信号](ch33s03.md)

    - [捕捉信号](ch33s04.md)

- [终端、作业控制与守护进程](ch34.md)

    - [终端](ch34s01.md)

    - [作业控制](ch34s02.md)

    - [守护进程](ch34s03.md)

- [线程](ch35.md)

    - [线程的概念](ch35s01.md)

    - [线程控制](ch35s02.md)

    - [线程间同步](ch35s03.md)

    - [编程练习](ch35s04.md)

- [TCP/IP 协议基础](ch36.md)

    - [TCP/IP 协议栈与数据包封装](ch36s01.md)

    - [以太网(RFC 894)帧格式](ch36s02.md)

    - [ARP 数据报格式](ch36s03.md)

    - [IP 数据报格式](ch36s04.md)

    - [IP 地址与路由](ch36s05.md)

    - [UDP 段格式](ch36s06.md)

    - [TCP 协议](ch36s07.md)

- [socket 编程](ch37.md)

    - [预备知识](ch37s01.md)

    - [基于 TCP 协议的网络程序](ch37s02.md)

    - [基于 UDP 协议的网络程序](ch37s03.md)

    - [UNIX Domain Socket IPC](ch37s04.md)

    - [练习：实现简单的 Web 服务器](ch37s05.md)

---

- [附录 A. 字符编码](apa.md)

    - [ASCII 码](apas01.md)

    - [Unicode 和 UTF-8](apas02.md)

    - [在 Linux C 编程中使用 Unicode 和 UTF-8](apas03.md)

[附录 B. GNU Free Documentation License](apb.md)

[参考书目](bi01.md)

[索引](ix01.md)
