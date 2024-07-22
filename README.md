# adofaihelper

- [adofaihelper](#adofaihelper)
  - [用法](#用法)
  - [函数](#函数)
    - [`adofai` 读取adofai文件并转化为ADOFAI类](#adofai-读取adofai文件并转化为adofai类)
      - [参数](#参数)
      - [返回值](#返回值)
    - [`ADOFAI_read` 读取adofai文件](#adofai_read-读取adofai文件)
      - [参数](#参数-1)
      - [返回值](#返回值-1)
    - [`ADOFAI_print` 输出adofai文件](#adofai_print-输出adofai文件)
      - [参数](#参数-2)
      - [返回值](#返回值-2)
    - [`AskForPath` 获取adofai文件路径](#askforpath-获取adofai文件路径)
      - [参数](#参数-3)
      - [返回值](#返回值-3)
    - [`SaveAsPath` 获取adofai文件保存路径](#saveaspath-获取adofai文件保存路径)
      - [参数](#参数-4)
      - [返回值](#返回值-4)
    - [`path_split` 拆分文件路径](#path_split-拆分文件路径)
      - [参数](#参数-5)
      - [返回值](#返回值-5)
    - [`pathData_to_angleData` 将旧版pathData转化为新版angleData](#pathdata_to_angledata-将旧版pathdata转化为新版angledata)
      - [参数](#参数-6)
      - [返回值](#返回值-6)
    - [`SortActions` 将actions重新排序](#sortactions-将actions重新排序)
      - [参数](#参数-7)
      - [返回值](#返回值-7)
    - [`clearFormat` 清除字符串的格式](#clearformat-清除字符串的格式)
      - [参数](#参数-8)
      - [返回值](#返回值-8)
    - [`boolean` 布尔值转换](#boolean-布尔值转换)
      - [参数](#参数-9)
      - [返回值](#返回值-9)

## 用法

放在<项目文件夹>/adofaihelper中，可以当做模组使用

```python
import adofaihelper
```

## 函数

### `adofai` 读取adofai文件并转化为ADOFAI类

#### 参数

| 字段名 | 数据类型 | 默认值 | 说明 |
| ----- | ------- | ----- | --- |
| `FILE_PATH` | string | - | 文件路径 |

#### 返回值

| 字段名 | 数据类型 | 默认值 | 说明 |
| ----- | ------- | ----- | --- |
| `level` | ADOFAI | - | adofai关卡的ADOFAI类 |

### `ADOFAI_read` 读取adofai文件

#### 参数

| 字段名 | 数据类型 | 默认值 | 说明 |
| ----- | ------- | ----- | --- |
| `FILE_PATH` | string | - | 文件路径 |

#### 返回值

| 字段名 | 数据类型 | 默认值 | 说明 |
| ----- | ------- | ----- | --- |
| `adofai_content` | dict | - | adofai文件内容 |

### `ADOFAI_print` 输出adofai文件

#### 参数

| 字段名 | 数据类型 | 默认值 | 说明 |
| ----- | ------- | ----- | --- |
| `level` | ADOFAI | - | 关卡文件的ADOFAI类 |
| `FILE_PATH` | string | - | 要输出的文件路径 |
| `info` | boolean | - | 是否对覆盖已有文件提示 |

#### 返回值

无

### `AskForPath` 获取adofai文件路径

#### 参数

无

#### 返回值

（唤起tk窗口）adofai文件路径

### `SaveAsPath` 获取adofai文件保存路径

#### 参数

无

#### 返回值

（唤起tk窗口）adofai文件保存路径

### `path_split` 拆分文件路径

#### 参数

| 字段名 | 数据类型 | 默认值 | 说明 |
| ----- | ------- | ----- | --- |
| `FILE_PATH` | string | - | 文件路径 |


#### 返回值

| 字段名 | 数据类型 | 说明 |
| ----- | ------- | --- |
| `level_dir` | string | 文件夹路径 |
| `level_name` | string | 文件名 |
| `extension` | string | 文件拓展名 |

### `pathData_to_angleData` 将旧版pathData转化为新版angleData

#### 参数

| 字段名 | 数据类型 | 默认值 | 说明 |
| ----- | ------- | ----- | --- |
| `pathData` | string | - | pathData |

#### 返回值

| 字段名 | 数据类型 | 默认值 | 说明 |
| ----- | ------- | ----- | --- |
| `angleData` | array | - | angleData |

### `SortActions` 将actions重新排序

#### 参数

| 字段名         | 数据类型  | 说明   |
| ------------ | ----- | ------ |
| `actions` | array | adofai文件中`"actions"`对应的值 |

#### 返回值

| 字段名         | 数据类型    | 说明       |
| ------------ | ------- | ---------- |
| `actions` | array | 按`"floor"`一项从小到大从新排序后的actions |

### `clearFormat` 清除字符串的格式

#### 参数

| 字段名 | 数据类型 | 默认值 | 说明 |
| ----- | ------- | ----- | --- |
| `content` | string | - | 需要清除格式的字符串 |

#### 返回值

| 字段名 | 数据类型 | 默认值 | 说明 |
| ----- | ------- | ----- | --- |
| `content` | string | - | 清除格式后的字符串 |

### `boolean` 布尔值转换

#### 参数

| 字段名 | 数据类型 | 默认值 | 说明 |
| ----- | ------- | ----- | --- |
| `value` | string或boolean | - | 旧版的"Enabled"/"Disabled"或新版的true/false |

#### 返回值

| 字段名 | 数据类型 | 默认值 | 说明 |
| ----- | ------- | ----- | --- |
| `value` | boolean | - | true/false |

<hr>
