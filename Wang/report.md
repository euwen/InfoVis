## 职员关系与邮件来往分析 - Email-header数据和staff数据：力学图
### 数据来源
1. 所有邮件的头信息，包含发送者，接收者，时间和邮件主题的csv文件
1. 所有职员的简历，xlsx表文件，包含每个人的姓名、性别、出生日期、出生地点、国籍、居住地、任职信息等

### 数据预处理
1. 使用python读入邮件头信息，根据发送 - 接收关系整理出人与人之间的关系，统计出两两之间的收发次数，以
```json
link { source: 发送者邮箱 target: 接受者邮箱 time: 收发次数 }
```
结构存储。
1. 使用python读入xlsx表文件，按照不同属性将职员进行分类，保存成json格式

### 数据可视化
  - 一个表示邮件收发关系的力学图，边表示邮件的收发关系，收发次数多的边比较粗
  - 节点表示人物，节点按照某项属性进行分组，同一组的节点颜色相同
  - 可以在页面上方选择分组的关键属性，改变关键属性会导致图的重绘
  - 鼠标经过节点的时候会浮动显示该人物的基本信息，同时高亮该人物的邮件收发的边

## POK的发展历程时间线：Events Chart
### 数据来源
来自柴神的以人物分类的事件发展时间线信息

### 数据可视化
  - 根据分析「关键文章」的结果，得到一些关键人物
  - 通过自动筛选，在「关键文章」中得到与人物相关的描述文章
  - 根据这些文章的事件顺序，整理出POK发展历程的大致时间线
  - 视图包含多条时间线，每条时间线表示某个特定的人物参与的事件的时间线
  - 视图上每个点代表一个事件，鼠标移动到事件上是会出现该事件的摘要信息

## 脚本及数据文件解释

|         文件名        |                                  用途                                       |
|-----------------------|-----------------------------------------------------------------------------|
| csv2json.py           | 将csv文件转化为json格式                                                     |
| xlsx2json.py          | 将xlsx表格转化为json格式                                                    |
| jsonsplit.py          | 将邮件信息文件和职员简历文件整理成一个统一的「节点 - 边」信息，按照属性分类 |
| EmployeeRecords.xlsx  | 原始的人员信息文件                                                          |
| Employee Records.json | 转化后的人员信息文件                                                        |
| email header.csv      | 原始的邮件头信息                                                            |
| email.json            | 转化后的邮件头信息                                                          |
| content.json          | 整合后的「节点 - 边」信息文件                                               |
| events.json           | 柴神给的事件数据文件                                                        |

## 感想
虽然邮件信息的分析花费了一定精力且没有收获比较有价值的信息，但这不失为一次有价值的尝试，至少帮我们排除了这些相对无关的信息。而POK的按人物的发展时间线在一定程度上帮我们理清了思路，尽管用处也不是太大。
经过这一次相对失败的尝试，我也掌握了不少关于数据可视化的知识，相信今后会有机会运用到这些知识。