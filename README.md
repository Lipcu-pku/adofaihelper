# adofaihelper

- [adofaihelper](#adofaihelper)
  - [用法](#用法)
  - [函数](#函数)
    - [`AskForPath` 获取adofai文件路径](#askforpath-获取adofai文件路径)
      - [参数](#参数)
      - [返回值](#返回值)
    - [`SaveAsPath` 获取adofai文件保存路径](#saveaspath-获取adofai文件保存路径)
      - [参数](#参数-1)
      - [返回值](#返回值-1)
    - [`pathData_to_angleData` 将旧版pathData转化为新版angleData](#pathdata_to_angledata-将旧版pathdata转化为新版angledata)
      - [参数](#参数-2)
      - [返回值](#返回值-2)
  - [ADOFAI类](#adofai类)
    - [ADOFAI.load](#adofaiload)
      - [参数](#参数-3)
      - [返回值](#返回值-3)
    - [ADOFAI.loads](#adofailoads)
      - [参数](#参数-4)
      - [返回值](#返回值-4)
    - [.value](#value)
      - [返回值](#返回值-5)
    - [.as\_adofai](#as_adofai)
      - [返回值](#返回值-6)
    - [.dump](#dump)
      - [参数](#参数-5)
      - [返回值](#返回值-7)
    - [.add\_action](#add_action)
      - [参数](#参数-6)
      - [返回值](#返回值-8)
    - [.add\_decoration](#add_decoration)
      - [参数](#参数-7)
  - [SETTINGS类](#settings类)
    - [.value](#value-1)
      - [返回值](#返回值-9)
  - [ACTION类](#action类)
    - [load](#load)
      - [参数](#参数-8)
      - [返回值](#返回值-10)
    - [.value](#value-2)
      - [返回值](#返回值-11)
  - [DECORATION类](#decoration类)
    - [load](#load-1)
      - [参数](#参数-9)
      - [返回值](#返回值-12)
    - [.value](#value-3)
      - [返回值](#返回值-13)

## 用法

已上传至PyPI: [adofaihelper](https://pypi.org/project/adofaihelper/1.1.4/)

```bash
pip install adofaihelper
```

```python
import adofaihelper
```

## 函数

### `AskForPath` 获取adofai文件路径

#### 参数

无

#### 返回值

| 变量名 | 数据类型 | 说明 |
| ----- | ------- | --- |
| `FILE_PATH` | string | （唤起tk窗口）adofai文件路径 |

### `SaveAsPath` 获取adofai文件保存路径

#### 参数

| 变量名 | 数据类型 | 默认值 | 说明 |
| ----- | ------- | ----- | --- |
| `default_name` | string | - | 默认文件名 |

#### 返回值

| 变量名 | 数据类型 | 说明 |
| ----- | ------- | --- |
| `FILE_PATH` | string | （唤起tk窗口）adofai文件保存路径 |

### `pathData_to_angleData` 将旧版pathData转化为新版angleData

#### 参数

| 变量名 | 数据类型 | 默认值 | 说明 |
| ----- | ------- | ----- | --- |
| `pathData` | string | - | pathData |

#### 返回值

| 变量名 | 数据类型 | 说明 |
| ----- | ------- |  --- |
| `angleData` | array | angleData |

## ADOFAI类

### ADOFAI.load

#### 参数

| 变量名 | 数据类型 | 默认值 | 说明 |
| ----- | ----- | ----- | ----- |
| `FILE_PATH` | string | - | .adofai文件路径 | 

#### 返回值

| 变量名 | 数据类型 | 说明 |
| ----- | ------- |  --- |
| `level` | ADOFAI | .adofai文件读取内容 |

### ADOFAI.loads

#### 参数

| 变量名 | 数据类型 | 默认值 | 说明 |
| ----- | ----- | ----- | ----- |
| `adofai_string` | string | - | .adofai型字符串 | 

#### 返回值

| 变量名 | 数据类型 | 说明 |
| ----- | ------- |  --- |
| `level` | ADOFAI | .adofai文件读取内容 |

### .value

#### 返回值

| 变量名 | 数据类型 | 说明 |
| ----- | ----- | ----- | 
| `adofai_dict` | dict | ADOFAI输出为字典格式 | 

### .as_adofai

#### 返回值

| 变量名 | 数据类型 | 说明 |
| ----- | ------- |  --- |
| `adofai_string` | string | ADOFAI输出为字符串格式 |

### .dump

#### 参数

| 变量名 | 数据类型 | 默认值 | 说明 |
| ----- | ----- | ----- | ----- |
| `FILE_PATH` | string | - | .adofai文件保存路径 | 
| `file_replace_warning` | bool | True | 文件覆盖提醒 |

#### 返回值

无

### .add_action

#### 参数

| 变量名 | 数据类型 | 默认值 | 说明 |
| ----- | ----- | ----- | ----- |
| `floor` | int | None | 事件所在砖块数 | 
| `eventType` | str/EventType | None | 事件类型 |
| `**kwargs` | **dict | None | 事件的其他参数 |

#### 返回值

无

### .add_decoration

#### 参数

| 变量名 | 数据类型 | 默认值 | 说明 |
| ----- | ----- | ----- | ----- |
| `eventType` | str/EventType | None | 事件类型 |
| `**kwargs` | **dict | None | 事件的其他参数 |

## SETTINGS类

### .value

#### 返回值

| 变量名 | 数据类型 | 说明 |
| ----- | ----- | ----- |
| `settings_dict` | dict | 设置对应字典型 |

## ACTION类

### load

#### 参数

| 变量名 | 数据类型 | 默认值 | 说明 |
| ----- | ----- | ----- | ----- |
| `floor` | int | None | 事件所在砖块数 | 
| `eventType` | str/EventType | None | 事件类型 |
| `**kwargs` | **dict | None | 事件的其他参数 |

#### 返回值

| 变量名 | 数据类型 | 说明 |
| ----- | ------- |  --- |
| `action` | Action | 对应事件类型 |

### .value

#### 返回值

| 变量名 | 数据类型 | 说明 |
| ----- | ----- | ----- |
| `action_dict` | dict | 事件对应字典型 |

## DECORATION类

### load

#### 参数

| 变量名 | 数据类型 | 默认值 | 说明 |
| ----- | ----- | ----- | ----- |
| `eventType` | str/EventType | None | 添加装饰类型 |
| `**kwargs` | **dict | None | 添加装饰事件的其他参数 |

#### 返回值

| 变量名 | 数据类型 | 说明 |
| ----- | ------- |  --- |
| `decoration` | Decoration | 添加装饰事件对应类型 |

### .value

#### 返回值

| 变量名 | 数据类型 | 说明 |
| ----- | ----- | ----- |
| `decoration_dict` | dict | 添加装饰事件对应字典型 |


帮我把这段markdown翻译为英文

<hr>
