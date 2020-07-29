### <center> C++ Basic </center>
* __强类型语言__
* GCC:
    * <a href='https://blog.csdn.net/weixin_41143631/article/details/81221777'>程序编译过程</a>
        1. 预处理， 展开头文件/宏替换/去掉注释/条件编译 (test.i main .i)
        2. 编译，    检查语法，生成汇编    （ test.s  main .s）
        3. 汇编，   汇编代码转换机器码    (test.o main.o)
        4. 链接,     链接到一起生成可执行程序    a.out

    * g++ 有些系统默认是使用 C++98，我们可以指定使用 C++11 来编译 main.cpp 文件：
        ```C++
        g++ -g -Wall -std=c++11 main.cpp
        ```
    * g++ 常用命令选项
        |选项|解释|
        |-|-|
        |-ansi|	只支持 ANSI 标准的 C 语法。这一选项将禁止 GNU C 的某些特色， 例如 asm 或 typeof|关键|词。
        |-c|	只编译并生成目标文件。|
        |-DMACRO|	以字符串"1"定义 MACRO 宏。|
        |-DMACRO|=DEFN	以字符串"DEFN"定义 MACRO 宏。|
        |-E|	只运行 C 预编译器。|
        |-g|	生成调试信息。GNU 调试器可利用该信息。|
        |-IDIRECTORY|	指定额外的头文件搜索路径DIRECTORY。|
        |-LDIRECTORY|	指定额外的函数库搜索路径DIRECTORY。|
        |-lLIBRARY|	连接时搜索指定的函数库LIBRARY。|
        |-m486|	针对 486 进行代码优化。|
        |-o|	FILE 生成指定的输出文件。用在生成可执行文件时。|
        |-O0|	不进行优化处理。|
        |-O|	或 -O1 优化生成代码。|
        |-O2|	进一步优化。|
        |-O3|	比 -O2 更进一步优化，包括 inline 函数。|
        |-shared|	生成共享目标文件。通常用在建立共享库时。|
        |-static|	禁止使用共享连接。|
        |-UMACRO|	取消对 MACRO 宏的定义。|
        |-w|	不生成任何警告信息。|
        |-Wall|	生成所有警告信息。|
* <a href='https://www.runoob.com/w3cnote/cpp-keyword-intro.html'>关键字</a>
    * __const__:（常量的，constant）__所修饰的对象或变量不能被改变__，修饰函数时，该函数不能改变在该函数外面声明的变量也不能调用任何非const函数。在函数的声明与定义时都要加上const，放在函数参数列表的最后一个括号后。在 C++ 中，用 const 声明一个变量，意味着该变量就是一个带类型的常量，可以代替 #define，且比 #define 多一个类型信息，且它执行内链接，可放在头文件中声明；但在 C 中，其声明则必须放在源文件（即 .C 文件）中，在 C 中 const 声明一个变量，除了不能改变其值外，它仍是一具变量。
* 数据类型
    * ```typedef short int wchar_t; //宽字符型```
    * <a href='https://www.runoob.com/cplusplus/cpp-data-types.html'>数据类型及其字符大小</a>
    * 变量的大小会根据编译器和所使用的电脑而有所不同
    * 枚举类型：
        * ```enum color { red, green, blue } c; //enum 枚举名{ 标识符[=整型常数], ... } 枚举变量;```
        * 默认情况下，第一个名称的值为 0，第二个名称的值为 1，第三个名称的值为 2，以此类推。但是，您也可以给名称赋予一个特殊的值，只需要添加一个初始值即可。例如，在下面的枚举中，green 的值为 5。
        * ```enum color { red, green=5, blue };``` 在这里，blue 的值为 6，因为默认情况下，每个名称都会比它前面一个名称大 1，但 red 的值依然为 0。
    * 
* <a href='https://www.runoob.com/cplusplus/cpp-variable-scope.html'>变量作用域：</a>
    * 初始化局部变量和全局变量
        * __当局部变量被定义时，系统不会对其初始化，您必须自行对其初始化。定义全局变量时，系统会自动初始化为下列值__：

* 常量：
    * 常量是固定值，在程序执行期间不会改变。这些固定的值，又叫做 __字面量__
    * 以下是各种类型的整数常量的实例：注意 __后缀不能重复__
        ```C++
        85         // 十进制
        0213       // 八进制 
        0x4b       // 十六进制 
        30         // 整数 
        30u        // 无符号整数 
        30l        // 长整数 
        30ul       // 无符号长整数
        ```
    * 下面列举几个浮点常量的实例：
        ```C++
        3.14159       // 合法的 
        314159E-5L    // 合法的 
        510E          // 非法的：不完整的指数
        210f          // 非法的：没有小数或指数
        .e55          // 非法的：缺少整数或分数
        ```
* 修饰符：
    * 类型限定符
        |限定符|含义|
        |-|-|
        |const|	const 类型的对象在程序执行期间不能被修改改变。|
        |volatile|	修饰符 volatile 告诉编译器不需要优化volatile声明的变量，让程序可以直接从内存中读取变量。对于一般的变量编译器会对变量进行优化，将内存中的变量值放在寄存器中以加快读写效率。|
        |restrict|	由 restrict 修饰的指针是唯一一种访问它所指向的对象的方式。只有 C99 增加了新的类型限定符 restrict。|
        
* <a href='https://www.runoob.com/cplusplus/cpp-storage-classes.html'>存储类：</a>
    * 存储类定义 C++ 程序中变量/函数的范围（可见性）和生命周期。这些说明符放置在它们所修饰的类型之前。下面列出 C++ 程序中可用的存储类：auto、register、static、extern、mutable、thread_local (C++11)
    * 从 C++ 17 开始，auto 关键字不再是 C++ 存储类说明符，且 register 关键字被弃用。

* <a href='https://www.runoob.com/cplusplus/cpp-functions.html'>函数：</a>
    * 先声明，后使用
    * <a href='https://www.runoob.com/cplusplus/cpp-functions.html'>函数参数</a>：
        |调用类型|	描述|
        |-|-|
        |传值调用|	该方法把参数的实际值赋值给函数的形式参数。在这种情况下，修改函数内的形式参数对实际参数没有影响。
        |指针调用|	该方法把参数的地址赋值给形式参数。在函数内，该地址用于访问调用中要用到的实际参数。这意味着，修改形式参数会影响实际参数。
        |引用调用|	该方法把参数的引用赋值给形式参数。在函数内，该引用用于访问调用中要用到的实际参数。这意味着，修改形式参数会影响实际参数。
        * 区分指针调用和引用调用
            * 指针调用：
            ```C++
            // 函数声明
            void swap(int *x, int *y);
            
            // 函数调用
            int a = 100;
            int b = 200;
            /* 调用函数来交换值
                * &a 表示指向 a 的指针，即变量 a 的地址 
                * &b 表示指向 b 的指针，即变量 b 的地址 
                */
            swap(&a, &b);
            ```
            * 引用调用:
            ```C++
            // 函数声明
            void swap(int &x, int &y);

            // 函数调用
            int a = 100;
            int b = 200;
            swap(a, b);
            ```
    * 参数默认值：
        * 当定义一个函数，可以为参数列表中后边的每一个参数指定默认值。当调用函数时，如果实际参数的值留空，则使用这个默认值。
    * __lambda函数__(__函数式编程$\lambda$演算__)：
        * Lambda 表达式本质上与函数声明非常类似。Lambda 表达式具体形式如下:
            ```C++
            [capture](parameters)->return-type{body}
            //例如
            [](int x, int y){ return x < y ; }
            
            //如果没有返回值可以表示为：
            [capture](parameters){body}
            //例如
            []{ ++global_x; }

            //更复杂例子：
            [](int x, int y) -> int { int z = x + y; return z + x; }
            ```
        * 本例中，一个临时的参数 z 被创建用来存储中间结果。如同一般的函数，z 的值不会保留到下一次该不具名函数再次被调用时。
        * 如果 lambda 函数没有传回值（例如 void），其返回类型可被完全忽略。
        * 在Lambda表达式内可以访问当前作用域的变量，这是Lambda表达式的闭包（Closure）行为。 与JavaScript闭包不同，C++变量传递有传值和传引用的区别。可以通过前面的[]来指定：
            ```c++
            []      // 沒有定义任何变量。使用未定义变量会引发错误。
            [x, &y] // x以传值方式传入（默认），y以引用方式传入。
            [&]     // 任何被使用到的外部变量都隐式地以引用方式加以引用。
            [=]     // 任何被使用到的外部变量(即lambda所在范围内所有可见局部变量)都隐式地以传值方式加以引用。
            [&, x]  // x显式地以传值方式加以引用。其余变量以引用方式加以引用。
            [=, &z] // z显式地以引用方式加以引用。其余变量以传值方式加以引用。
            ```
            另外有一点需要注意。对于[=]或[&]的形式，lambda 表达式可以直接使用 this 指针。但是，对于[]的形式，如果要使用 this 指针，必须显式传入：
            ```C++
            [this]() { this->someFunc(); }();//最后一个()是调用，及时调用
            ```
        * mutable关键字用来对值传递的变量进行修改
            ```C++
            int m=10;
            [=]()mutable{m=100+10;cout<<m;}();//如果没有mutable，会报错提示m read-only
            ```

* 数字：
    * 数学函数库cmath：sin,cos,pow,log,sqrt,abs,floor
    * 随机数：在许多情况下，需要生成随机数。关于随机数生成器，有两个相关的函数。一个是 rand()，该函数只返回一个伪随机数。生成随机数之前必须先调用 srand() 函数来设置种子
* 数组：
    * 声明、赋值(初始化)、访问。
    * 初始化数组：
        ```c++
        double balance[5] = {1000.0, 2.0, 3.4, 7.0, 50.0};//大括号 { } 之间的值的数目不能大于我们在数组声明时在方括号 [ ] 中指定的元素数目。
        double balance[] = {1000.0, 2.0, 3.4, 7.0, 50.0};//如果您省略掉了数组的大小，数组的大小则为初始化时元素的个数。
        ```
    * 数组详解：
        |概念|	描述
        |-|-|
        |<a href='https://www.runoob.com/cplusplus/cpp-multi-dimensional-arrays.html'>多维数组</a>|C++ 支持多维数组。多维数组最简单的形式是二维数组。<br> __低维度可省略，高维不可省略__ <br><a href='https://blog.csdn.net/o707191418/article/details/81365895'>原因</a>：因为二维数组在内存中的地址排列方式是<span style='color:red;font-weight:bold'>【!按行】</span>排列的，第一行排列完之后再排列第二行，以此类推。因为，当给出数组的列数时，通过列数与行数的关系 $pointer=array + n * i + j$，对于这样一个数组，就能找找到特定的地址，从而找到值。更高维度以此类推|
        |<a href='https://www.runoob.com/cplusplus/cpp-pointer-to-an-array.html'>指向数组的指针</a>|您可以通过指定不带索引的数组名称来生成一个指向数组中第一个元素的指针。|
        |<a href='https://www.runoob.com/cplusplus/cpp-passing-arrays-to-functions.html'>传递数组给函数</a>|您可以通过指定不带索引的数组名称来给函数传递一个指向数组的指针。<br>三种方式：__(注意多维度时的传入)__<br>1. 指针方式：```void myFunction(int *param){}```<br>2. 形式参数是一个已定义大小的数组：```void myFunction(int param[10]){}```<br>3. 形式参数是一个未定义大小的数组：```void myFunction(int param[]){}```<br>就函数而言，数组的长度是无关紧要的，__因为 C++ 不会对形式参数执行边界检查，<span style='color:red;'>函数内可以对形参数组越界访问</span>__|
        |<a href='https://www.runoob.com/cplusplus/cpp-return-arrays-from-function.html'>从函数返回数组</a>|C++ 允许从函数返回数组。<br> C++ 不支持在函数外返回局部变量的地址，除非定义局部变量为 static 变量。<br>__原因__：函数压入栈中执行后，会自动释放内存，所以局部变量也就不存在了|
* 字符串：
    * 注意
        ```c++
        char greeting[6] = {'H', 'e', 'l', 'l', 'o', '\0'};//下面的声明和初始化创建了一个 "Hello" 字符串。由于在数组的末尾存储了空字符，所以字符数组的大小比单词 "Hello" 的字符数多一个
        char greeting[] = "Hello";//C++ 编译器会在初始化数组时，自动把 '\0' 放在字符串的末尾
    * 字符串常见函数：strcpy,strlen,strcat,strcmp,strchr,strstr
        * strchr(s1, ch); 返回一个指针，指向字符串 s1 中字符 ch 的第一次出现的位置。
        * strstr(s1, s2); 返回一个指针，指向字符串 s1 中字符串 s2 的第一次出现的位置。
    * C++ 标准库提供了 string 类类型，支持上述所有的操作
        ```c++
        #include <iostream>
        #include <string>
        
        using namespace std;
        
        int main ()
        {
        string str1 = "Hello";
        string str2 = "World";
        string str3;
        int  len ;
        
        // 复制 str1 到 str3
        str3 = str1;
        cout << "str3 : " << str3 << endl;
        
        // 连接 str1 和 str2
        str3 = str1 + str2;
        cout << "str1 + str2 : " << str3 << endl;
        
        // 连接后，str3 的总长度
        len = str3.size();
        cout << "str3.size() :  " << len << endl;
        
        return 0;
        }
        ```

* <a href='https://www.runoob.com/cplusplus/cpp-pointers.html'>指针：</a>
    * 通过指针，可以简化一些 C++ 编程任务的执行，还有一些任务，如动态内存分配，没有指针是无法执行的
    * 指针详解，见链接
* <a href='https://www.runoob.com/cplusplus/cpp-references.html'>引用</a>：
    * 引用变量是一个别名，也就是说，它是某个已存在变量的另一个名字。一旦把引用初始化为某个变量，就可以使用该引用名称或变量名称来指向变量。
    * 引用和指针 __区别__：
        * __不存在空引用__。引用必须连接到一块合法的内存。
        * __一旦引用被初始化为一个对象__，就不能被指向到另一个对象。指针可以在任何时候指向到另一个对象。
        * __引用必须在创建时被初始化__。指针可以在任何时间被初始化。
    * 试想变量名称是变量附属在内存位置中的标签，您可以把引用当成是变量附属在内存位置中的第二个标签。因此，您可以通过原始变量名称或引用来访问变量的内容
        ```c++
        // 声明简单的变量
        int    i;
        double d;
        
        // 声明引用变量
        int&    r = i;
        double& s = d;
        ```
    * 在这些声明中，__& 读作引用__。因此，第一个声明可以读作 "r 是一个初始化为 i 的整型引用"，第二个声明可以读作 "s 是一个初始化为 d 的 double 型引用"。下面的实例使用了 int 和 double 引用
    * <span style='color:red;font-weight:bold'>【&】</span>在C++中有两个方面的的应用，一个是作为取地址操作符，还有一个便是别名或者引用变量的声明
    * 两种应用：1.把引用作为参数 2.把引用作为返回值（参考指针）

* <a href='https://www.runoob.com/cplusplus/cpp-date-time.html'>时间：</a>
    ```C++
    /*
    struct tm {
    int tm_sec;   // 秒，正常范围从 0 到 59，但允许至 61
    int tm_min;   // 分，范围从 0 到 59
    int tm_hour;  // 小时，范围从 0 到 23
    int tm_mday;  // 一月中的第几天，范围从 1 到 31
    int tm_mon;   // 月，范围从 0 到 11
    int tm_year;  // 自 1900 年起的年数
    int tm_wday;  // 一周中的第几天，范围从 0 到 6，从星期日算起
    int tm_yday;  // 一年中的第几天，范围从 0 到 365，从 1 月 1 日算起
    int tm_isdst; // 夏令时
    }*/

    #include <iostream>
    #include <ctime>
    
    using namespace std;
    
    int main( )
    {
    // 基于当前系统的当前日期/时间
    time_t now = time(0);
    
    cout << "1970 到目前经过秒数:" << now << endl;
    
    tm *ltm = localtime(&now);
    
    // 输出 tm 结构的各个组成部分
    cout << "年: "<< 1900 + ltm->tm_year << endl;
    cout << "月: "<< 1 + ltm->tm_mon<< endl;
    cout << "日: "<<  ltm->tm_mday << endl;
    cout << "时间: "<< ltm->tm_hour << ":";
    cout << ltm->tm_min << ":";
    cout << ltm->tm_sec << endl;
    }
    ```
* 基本输入输出：
    * C++ 的 I/O 发生在流中，流是字节序列。如果字节流是从设备（如键盘、磁盘驱动器、网络连接等）流向内存，这叫做输入操作。如果字节流是从内存流向设备（如显示屏、打印机、磁盘驱动器、网络连接等），这叫做输出操作。
        |头文件|函数和描述|
        |-|-|
        |\<iostream>|	该文件定义了 cin、cout、cerr 和 clog 对象，分别对应于标准输入流、标准输出流、|非缓冲标准错误流和缓冲标准错误流。|
        |\<iomanip>|	该文件通过所谓的参数化的流操纵器（比如 setw 和 setprecision），来声明对执行标准|化 I/O 有用的服务。|
        |\<fstream>|	该文件为用户控制的文件处理声明服务。我们将在文件和流的相关章节讨论它的细节。|
* 数据结构：
    * <a href='https://www.runoob.com/cplusplus/cpp-data-structures.html'>结构体</a>

* 面向对象：
    * 注意对象的创建不用new
        * JAVA中是new Object();调用new关键字时，动态创建。注意new关键字用来在堆中动态申请内存
        * C++中是 Object object(p1,p2,p3);直接声明了一个对象的时候就创建了相应的内存，如果不创建，就定义指针
        * Python中则是 object=Object() 调用时创建

    * 类&对象详解
        |概念|	描述
        |-|-|
        |类成员函数|类的成员函数是指那些把定义和原型写在类定义内部的函数，就像类定义中的其他变量一样。<br>特点：__声明和定义可以分开__，在外部定义的时候格式：类名::方法名|
        |<a href='https://www.runoob.com/cplusplus/cpp-class-access-modifiers.html'>类访问修饰符</a>|	类成员可以被定义为 public、private 或 protected。默认情况下是定义为 private。<br>注意protected：保护成员变量或函数与私有成员十分相似，但有一点不同，保护成员在派生类（即子类）中是可访问的。<br>继承中的特点：<br>有public, protected, private三种继承方式，它们相应地改变了基类成员的访问属性。1.public 继承：基类 public 成员，protected 成员，private 成员的访问属性在派生类中分别变成：public, protected, private<br>            2.protected 继承：基类 public 成员，protected 成员，private 成员的访问属性在派生类中分别变成：protected, protected, private<br>3.private 继承：基类 public 成员，protected 成员，private 成员的访问属性在派生类中分别变成：private, private, private<br> 但无论哪种继承方式，上面两点都没有改变：<br>(1).private 成员只能被本类成员（类内）和友元访问，不能被派生类访问；    <br>(2).protected 成员可以被派生类访问。例如：```class B : public A{}```|
        |<a href='https://www.runoob.com/cplusplus/cpp-constructor-destructor.html'>构造函数 & 析构函数</a>|	类的构造函数是一种特殊的函数，在创建一个新的对象时调用。类的析构函数也是一种特殊的函数，在删除所创建的对象时调用。<br>使用初始化列表来初始化字段:<br>```Line::Line( double len): length(len){ cout << "Object is being created, length = " << len << endl;} // length是Line的属性```<br>注意父类构造函数初始化形式, 注意当复制的变量名相同时要: this->param=param;否则认不出来|
        |拷贝构造函数|	拷贝构造函数，是一种特殊的构造函数，它在创建对象时，是使用同一类中之前创建的对象来初始化新创建的对象。
        |友元函数|	友元函数（类）可以访问类的 private 和 protected 成员。<br>友元的声明必须在类中声明（这样类才知道谁是友元），其次友元的定义的定义不用加域限定符::|
        |<a href='https://www.runoob.com/cplusplus/cpp-inline-functions.html'>内联函数</a>|	通过内联函数，编译器试图在调用函数的地方扩展函数体中的代码。<br>__目的__：引入内联函数的目的是为了解决程序中函数调用的效率问题，这么说吧，程序在编译器编译的时候，编译器将程序中出现的内联函数的调用表达式用内联函数的函数体进行替换，而对于其他的函数，都是在运行时候才被替代。这其实就是个空间代价换时间的i节省|
        |this 指针|	每个对象都有一个特殊的 __指针 this__，它指向对象本身。<br>调用方式：this->attr(). 和JAVA一样在类内部调用可省略|
        |指向类的指针|	指向类的指针方式如同指向结构的指针。实际上，类可以看成是一个带有函数的结构。|
        |类的静态成员|	类的数据成员和函数成员都可以被声明为静态的。<br>用 static 关键字来把类成员定义为静态的。当我们声明类的成员为静态时，这意味着无论创建多少个类的对象，静态成员都只有一个副本。静态成员在类的所有对象中是共享的。如果不存在其他的初始化语句，在创建第一个对象时，所有的静态数据都会被初始化为零。我们不能把静态成员的初始化放置在类的定义中，但是可以在类的外部通过使用范围解析运算符 :: 来重新声明静态变量从而对它进行初始化，如下面的实例所示<br>静态成员函数与普通成员函数的 __区别__：<br>静态成员函数没有 this 指针，只能访问静态成员（包括静态成员变量和静态成员函数）。<br>普通成员函数有 this 指针，可以访问类中的任意成员；而静态成员函数没有 this 指针。|
* 继承：
    * 访问控制和继承
    * 多继承
* 重载运算符和重载函数
    * 函数重载
    * 运算符重载:```Box operator+(const Box&, const Box&);```
    * 可重载运算符/不可重载运算符
    * 运算符重载实例
* 多态：
    ```c++
    #include <iostream> 
    using namespace std;
    
    class Shape {
    protected:
        int width, height;
    public:
        Shape( int a=0, int b=0)
        {
            width = a;
            height = b;
        }
        int area()
        {
            cout << "Parent class area :" <<endl;
            return 0;
        }
    };
    class Rectangle: public Shape{
    public:
        Rectangle( int a=0, int b=0):Shape(a, b) { }
        int area ()
        {
            cout << "Rectangle class area :" <<endl;
            return (width * height); 
        }
    };
    class Triangle: public Shape{
    public:
        Triangle( int a=0, int b=0):Shape(a, b) { }
        int area ()
        { 
            cout << "Triangle class area :" <<endl;
            return (width * height / 2); 
        }
    };
    // 程序的主函数
    int main( )
    {
    Shape *shape;
    Rectangle rec(10,7);
    Triangle  tri(10,5);
    
    // 存储矩形的地址
    shape = &rec;
    // 调用矩形的求面积函数 area
    shape->area();
    
    // 存储三角形的地址
    shape = &tri;
    // 调用三角形的求面积函数 area
    shape->area();
    
    return 0;
    }
    ```
    结果报错：导致错误输出的原因是，调用函数 area() 被编译器设置为基类中的版本，这就是所谓的静态多态，或静态链接 - 函数调用在程序执行前就准备好了。有时候这也被称为早绑定，因为 area() 函数在程序编译期间就已经设置好了。

    但现在，让我们对程序稍作修改，在 Shape 类中，area() 的声明前放置关键字 virtual，如下所示：
    ```c++
    class Shape {
        protected:
            int width, height;
        public:
            Shape( int a=0, int b=0)
            {
                width = a;
                height = b;
            }
            virtual int area()
            {
                cout << "Parent class area :" <<endl;
                return 0;
            }
        };
    ```
    * 虚函数：
        * 虚函数 是在基类中使用关键字 virtual 声明的函数。在派生类中重新定义基类中定义的虚函数时，会告诉编译器不要静态链接到该函数。我们想要的是在程序中任意点可以根据所调用的对象类型来选择调用的函数，这种操作被称为动态链接，或后期绑定。
        * 纯虚函数 您可能想要在基类中定义虚函数，以便在派生类中重新定义该函数更好地适用于对象，但是您在基类中又不能对虚函数给出有意义的实现，这个时候就会用到纯虚函数。我们可以把基类中的虚函数 area() 改写如下：
            ```c++
            class Shape {
            protected:
                int width, height;
            public:
                Shape( int a=0, int b=0)
                {
                    width = a;
                    height = b;
                }
                // pure virtual function
                virtual int area() = 0;//= 0 告诉编译器，函数没有主体，上面的虚函数是纯虚函数。
            };
            ```

* 高级教程：
    * <a href='https://www.runoob.com/cplusplus/cpp-dynamic-memory.html'>动态内存：</a>
        * new 和 delete 运算符
* 资源库
