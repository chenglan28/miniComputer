# MiniComputer
欢迎使用MiniComputer，这是一个由橙蓝自主研发的命令行系统
## 如何使用
在掌控版下方有 P Y T H O N 六个按键

按 P 键输出编码0

按 Y 键输出编码1

八个 0/1编码 即可构成一个字符

按 T 键删除上一个编码

按 H 键键入编码所选的字符


例如输入一个“P”

查表可知，“P”前四位的编码是“0000”，
后四位是“1111”，
结合起来就是“00001111”，
为了方便，在最前面的0都省略不写，
所以可以写成“1111”，
也就是说，我们按四次 P 键，再按一次H键即可键入一个“P”


附表：编码对照
<table>
    <tr>
        <td>前/后</td>
        <td>0000</td>
        <td>0001</td>
        <td>0010</td>
        <td>0011</td>
        <td>0100</td>
        <td>0101</td>
        <td>0110</td>
        <td>0111</td>
        <td>1000</td>
        <td>1001</td>
        <td>1010</td>
        <td>1011</td>
        <td>1100</td>
        <td>1101</td>
        <td>1110</td>
        <td>1111</td>
    </tr>
    <tr>
        <td>0000</td>
        <td>A</td>
        <td>B</td>
        <td>C</td>
        <td>D</td>
        <td>E</td>
        <td>F</td>
        <td>G</td>
        <td>H</td>
        <td>I</td>
        <td>J</td>
        <td>K</td>
        <td>L</td>
        <td>M</td>
        <td>N</td>
        <td>O</td>
        <td>P</td>
    </tr>
    <tr>
        <td>0001</td>
        <td>Q</td>
        <td>R</td>
        <td>S</td>
        <td>T</td>
        <td>U</td>
        <td>V</td>
        <td>W</td>
        <td>X</td>
        <td>Y</td>
        <td>Z</td>
        <td>a</td>
        <td>b</td>
        <td>c</td>
        <td>d</td>
        <td>e</td>
        <td>f</td>
    </tr>
    <tr>
        <td>0010</td>
        <td>g</td>
        <td>h</td>
        <td>i</td>
        <td>j</td>
        <td>k</td>
        <td>l</td>
        <td>m</td>
        <td>n</td>
        <td>o</td>
        <td>p</td>
        <td>q</td>
        <td>r</td>
        <td>s</td>
        <td>t</td>
        <td>u</td>
        <td>v</td>
    </tr>
    <tr>
        <td>0011</td>
        <td>w</td>
        <td>x</td>
        <td>y</td>
        <td>z</td>
        <td>0</td>
        <td>1</td>
        <td>2</td>
        <td>3</td>
        <td>4</td>
        <td>5</td>
        <td>6</td>
        <td>7</td>
        <td>8</td>
        <td>9</td>
        <td>~</td>
        <td>!</td>
    </tr>
    <tr>
        <td>0100</td>
        <td>@</td>
        <td>#</td>
        <td>$</td>
        <td>%</td>
        <td>^</td>
        <td>&</td>
        <td>*</td>
        <td>(</td>
        <td>)</td>
        <td>_</td>
        <td>+</td>
        <td>`</td>
        <td>-</td>
        <td>=</td>
        <td>{</td>
        <td>}</td>
    </tr>
    <tr>
        <td>0101</td>
        <td>|</td>
        <td>:</td>
        <td>"</td>
        <td><</td>
        <td>></td>
        <td>?</td>
        <td>[</td>
        <td>]</td>
        <td>\\</td>
        <td>;</td>
        <td>'</td>
        <td>,</td>
        <td>.</td>
        <td>/</td>
        <td>空格</td>
        <td>Del(退格)</td>
    </tr>
    <tr>
        <td>0110</td>
        <td>Get(执行)</td>
        <td>Clock(详见“快捷指令:Clock”)</td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
    </tr>
    <tr>
        <td>0111</td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
    </tr>
    <tr>
        <td>1000</td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
    </tr>
    <tr>
        <td>1001</td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
    </tr>
    <tr>
        <td>1010</td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
    </tr>
    <tr>
        <td>1011</td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
    </tr>
    <tr>
        <td>1100</td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
    </tr>
    <tr>
        <td>1101</td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
    </tr>
    <tr>
        <td>1110</td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
    </tr>
    <tr>
        <td>1111</td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
    </tr>
</table>
## 指令
### sudo
执行 python 代码
语法:
sudo [代码]
### print
打印信息
语法:
print [内容]
### link
连接网络
语法:
link [SSID(网络名)] [password(密码)]
### alarm
设定一个闹钟，闹钟响铃时按A键关闭，且关闭后需要重新设定

如果想要在响铃前关闭，请输入"alarm -1 -1"
语法:
alarm [hour(时)] [minute(分)]
### 快捷指令
为了方便，我们将一些常用指令添加到了编译表中
#### Clock
打开时钟界面

## 更新历程
### 1.0
+ 正式上线
+ 支持 sudo , print
### 1.2
+ 新增快捷指令: clock
+ 新增指令: link
+ 新增指令: alarm