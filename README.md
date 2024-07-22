# adofaihelper

- [adofaihelper](#adofaihelper)
  - [用法](#用法)
  - [公开函数](#公开函数)
    - [`AskForPath` 获取adofai文件路径](#askforpath-获取adofai文件路径)
      - [参数](#参数)
      - [返回值](#返回值)
    - [`SaveAsPath` 获取adofai文件保存路径](#saveaspath-获取adofai文件保存路径)
      - [参数](#参数-1)
      - [返回值](#返回值-1)
    - [`path_split` 拆分文件路径](#path_split-拆分文件路径)
      - [参数](#参数-2)
      - [返回值](#返回值-2)
    - [`pathData_to_angleData` 将旧版pathData转化为新版angleData](#pathdata_to_angledata-将旧版pathdata转化为新版angledata)
      - [参数](#参数-3)
      - [返回值](#返回值-3)
    - [`SortActions` 将actions重新排序](#sortactions-将actions重新排序)
      - [参数](#参数-4)
      - [返回值](#返回值-4)
  - [`get_forward_msg` 获取合并转发消息](#get_forward_msg-获取合并转发消息)
    - [参数](#参数-5)
    - [返回值](#返回值-5)
  - [`send_like` 发送好友赞](#send_like-发送好友赞)
    - [参数](#参数-6)
    - [返回值](#返回值-6)
  - [`set_group_kick` 群组踢人](#set_group_kick-群组踢人)
    - [参数](#参数-7)
    - [返回值](#返回值-7)
  - [`set_group_ban` 群组单人禁言](#set_group_ban-群组单人禁言)
    - [参数](#参数-8)
    - [返回值](#返回值-8)
  - [`set_group_anonymous_ban` 群组匿名用户禁言](#set_group_anonymous_ban-群组匿名用户禁言)
    - [参数](#参数-9)
    - [返回值](#返回值-9)
  - [`set_group_whole_ban` 群组全员禁言](#set_group_whole_ban-群组全员禁言)
    - [参数](#参数-10)
    - [返回值](#返回值-10)
  - [`set_group_admin` 群组设置管理员](#set_group_admin-群组设置管理员)
    - [参数](#参数-11)
    - [返回值](#返回值-11)
  - [`set_group_anonymous` 群组匿名](#set_group_anonymous-群组匿名)
    - [参数](#参数-12)
    - [返回值](#返回值-12)
  - [`set_group_card` 设置群名片（群备注）](#set_group_card-设置群名片群备注)
    - [参数](#参数-13)
    - [返回值](#返回值-13)
  - [`set_group_name` 设置群名](#set_group_name-设置群名)
    - [参数](#参数-14)
    - [返回值](#返回值-14)
  - [`set_group_leave` 退出群组](#set_group_leave-退出群组)
    - [参数](#参数-15)
    - [返回值](#返回值-15)
  - [`set_group_special_title` 设置群组专属头衔](#set_group_special_title-设置群组专属头衔)
    - [参数](#参数-16)
    - [返回值](#返回值-16)
  - [`set_friend_add_request` 处理加好友请求](#set_friend_add_request-处理加好友请求)
    - [参数](#参数-17)
    - [返回值](#返回值-17)
  - [`set_group_add_request` 处理加群请求／邀请](#set_group_add_request-处理加群请求邀请)
    - [参数](#参数-18)
    - [返回值](#返回值-18)
  - [`get_login_info` 获取登录号信息](#get_login_info-获取登录号信息)
    - [参数](#参数-19)
    - [返回值](#返回值-19)
  - [`get_stranger_info` 获取陌生人信息](#get_stranger_info-获取陌生人信息)
    - [参数](#参数-20)
    - [返回值](#返回值-20)
  - [`get_friend_list` 获取好友列表](#get_friend_list-获取好友列表)
    - [参数](#参数-21)
    - [返回值](#返回值-21)
  - [`get_group_info` 获取群信息](#get_group_info-获取群信息)
    - [参数](#参数-22)
    - [返回值](#返回值-22)
  - [`get_group_list` 获取群列表](#get_group_list-获取群列表)
    - [参数](#参数-23)
    - [返回值](#返回值-23)
  - [`get_group_member_info` 获取群成员信息](#get_group_member_info-获取群成员信息)
    - [参数](#参数-24)
    - [返回值](#返回值-24)
  - [`get_group_member_list` 获取群成员列表](#get_group_member_list-获取群成员列表)
    - [参数](#参数-25)
    - [返回值](#返回值-25)
  - [`get_group_honor_info` 获取群荣誉信息](#get_group_honor_info-获取群荣誉信息)
    - [参数](#参数-26)
    - [返回值](#返回值-26)
  - [`get_cookies` 获取 Cookies](#get_cookies-获取-cookies)
    - [参数](#参数-27)
    - [返回值](#返回值-27)
  - [`get_csrf_token` 获取 CSRF Token](#get_csrf_token-获取-csrf-token)
    - [参数](#参数-28)
    - [返回值](#返回值-28)
  - [`get_credentials` 获取 QQ 相关接口凭证](#get_credentials-获取-qq-相关接口凭证)
    - [参数](#参数-29)
    - [返回值](#返回值-29)
  - [`get_record` 获取语音](#get_record-获取语音)
    - [参数](#参数-30)
    - [返回值](#返回值-30)
  - [`get_image` 获取图片](#get_image-获取图片)
    - [参数](#参数-31)
    - [返回值](#返回值-31)
  - [`can_send_image` 检查是否可以发送图片](#can_send_image-检查是否可以发送图片)
    - [参数](#参数-32)
    - [返回值](#返回值-32)
  - [`can_send_record` 检查是否可以发送语音](#can_send_record-检查是否可以发送语音)
    - [参数](#参数-33)
    - [返回值](#返回值-33)
  - [`get_status` 获取运行状态](#get_status-获取运行状态)
    - [参数](#参数-34)
    - [返回值](#返回值-34)
  - [`get_version_info` 获取版本信息](#get_version_info-获取版本信息)
    - [参数](#参数-35)
    - [返回值](#返回值-35)
  - [`set_restart` 重启 OneBot 实现](#set_restart-重启-onebot-实现)
    - [参数](#参数-36)
    - [返回值](#返回值-36)
  - [`clean_cache` 清理缓存](#clean_cache-清理缓存)
    - [参数](#参数-37)
    - [返回值](#返回值-37)


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

