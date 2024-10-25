# ouc接龙管家自动晚打卡

ouc信院晚上打卡，采用python requests和青龙面板

前几天闲来无事，在github上面搜到[ExistoT01](https://github.com/ExistoT01/auto-checkin-script)学长的自动打卡脚本，突然心生想法，用青龙面板来实现定时打卡。

**注意：仅供学习交流之用，请勿用作商业用途**

大佬说`authorization` 可能三天左右更换一次，刚写第一天，不知道现在啥情况，过几天我再看一下。

## 实现思路

requests模拟发出请求，携带data和authorization。

### 思路来源

近几天整理东西，发现来学校报到时带的两个wifi棒子ufi001c，

~~心生歹念~~，给它来个爆改。

### 具体操作

先给wifi棒子刷了一个debian包，这个网上一找就有，刷好之后出现了第一个问题：**<u>adb读不出来，只能使用ssh连接，但在ssh连接情况下，不能操控设备重新连接其他wifi。</u>**

这里有两个可行的方案：

​	1.卸载adb驱动之后重装，将驱动换为`网络适配器`-->`microsoft`-->`基于远程NDIS的Internet共享设备`（我也不知道原理）

​	2.曹哥：理论上说你可以写个脚本调nmcli然后让他后台跑给热点关了然后再连，但我觉得这要是寄了那就真寄了。  （照抄的原话  ~~二方案感觉可行但我没去试~~）



连上网之后就可以安装docker和青龙面板了，不详述。

打开青龙面板，在定时任务中添加以下内容，时间和文件名称按照自己的来![屏幕截图 2024-10-25 111933](https://github.com/user-attachments/assets/34194dea-1232-45d6-87be-dd5b21536890)


然后在进入脚本管理-->新建文件-->将脚本内容复制进去-->保存![屏幕截图 2024-10-25 112221](https://github.com/user-attachments/assets/5eaa3cc3-3dbf-458c-b3fd-2c5bbecdd2fe)


第一次写，有说不清楚的地方请谅解
