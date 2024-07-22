# adofaihelper

- [adofaihelper](#adofaihelper)
  - [Usage](#usage)
  - [Functions](#functions)
    - [`adofai` Read the .adofai file and convert to an ADOFAI class](#adofai-read-the-adofai-file-and-convert-to-an-adofai-class)
      - [Params](#params)
      - [Returns](#returns)
    - [`ADOFAI_read` Reading the .adofai file](#adofai_read-reading-the-adofai-file)
      - [Params](#params-1)
      - [Returns](#returns-1)
    - [`ADOFAI_print` Output the .adofai file](#adofai_print-output-the-adofai-file)
      - [Params](#params-2)
      - [Returns](#returns-2)
    - [`AskForPath` Get .adofai file path](#askforpath-get-adofai-file-path)
      - [Params](#params-3)
      - [Returns](#returns-3)
    - [`SaveAsPath` Get .adofai saving path](#saveaspath-get-adofai-saving-path)
      - [Params](#params-4)
      - [Returns](#returns-4)
    - [`path_split` Splitting the file path](#path_split-splitting-the-file-path)
      - [Params](#params-5)
      - [Returns](#returns-5)
    - [`pathData_to_angleData` Converting the pathData to angleData](#pathdata_to_angledata-converting-the-pathdata-to-angledata)
      - [Params](#params-6)
      - [Returns](#returns-6)
    - [`SortActions` Sort the actions](#sortactions-sort-the-actions)
      - [Params](#params-7)
      - [Returns](#returns-7)
    - [`clearFormat` Clear the format of the string](#clearformat-clear-the-format-of-the-string)
      - [Params](#params-8)
      - [Returns](#returns-8)
    - [`boolean` Boolean value converting](#boolean-boolean-value-converting)
      - [Params](#params-9)
      - [Returns](#returns-9)

## Usage

Put it in [ProjectDir]/adofaihelper, then you can use it as a module. 

```python
import adofaihelper
```

## Functions

### `adofai` Read the .adofai file and convert to an ADOFAI class

#### Params

| Name | Type | Default | Description |
| ----- | ------- | ----- | --- |
| `FILE_PATH` | string | - | the path of the .adofai file |

#### Returns

| Name | Type | Description |
| ----- | ------- | --- |
| `level` | ADOFAI | ADOFAI of the .adofai file |

### `ADOFAI_read` Reading the .adofai file

#### Params

| Name | Type | Default | Description |
| ----- | ------- | ----- | --- |
| `FILE_PATH` | string | - | the path of the .adofai file |

#### Returns

| Name | Type | Description |
| ----- | ------- | --- |
| `adofai_content` | dict | .adofai content |

### `ADOFAI_print` Output the .adofai file

#### Params

| Name | Type | Default | Description |
| ----- | ------- | ----- | --- |
| `level` | ADOFAI | - | ADOFAI of the level |
| `FILE_PATH` | string | - | file path to output to |
| `info` | boolean | - | whether to prompt when overwriting existing file |

#### Returns

None

### `AskForPath` Get .adofai file path

#### Params

None

#### Returns

| Name | Type | Description |
| ----- | ------- | --- |
| `FILE_PATH` | string | (call a tk window and select) the .adofai file path |

### `SaveAsPath` Get .adofai saving path

#### Params

None

#### Returns

| Name | Type | Description |
| ----- | ------- | --- |
| `FILE_PATH` | string | (call a tk window and select) the .adofai file saving path |

### `path_split` Splitting the file path

#### Params

| Name | Type | Default | Description |
| ----- | ------- | ----- | --- |
| `FILE_PATH` | string | - | the path of the .adofai file |


#### Returns

| Name | Type | Description |
| ----- | ------- | --- |
| `level_dir` | string | folder path of the file |
| `level_name` | string | file name of the file |
| `extension` | string | file extension name |

### `pathData_to_angleData` Converting the pathData to angleData

#### Params

| Name | Type | Default | Description |
| ----- | ------- | ----- | --- |
| `pathData` | string | - | pathData |

#### Returns

| Name | Type | Description |
| ----- | ------- | --- |
| `angleData` | array | angleData |

### `SortActions` Sort the actions

#### Params

| Name | Type | Default | Description |
| ----- | ------- | ----- | --- |
| `actions` | array | - | the value to `"actions"` in the .adofai |

#### Returns

| Name | Type | Description |
| ----- | ------- | ----- |
| `actions` | array | actions sorted by `"floor"` |

### `clearFormat` Clear the format of the string

#### Params

| Name | Type | Default | Description |
| ----- | ------- | ----- | --- |
| `content` | string | - | string to clear format |

#### Returns

| Name | Type | Description |
| ----- | ------- | --- |
| `content` | string | clear formatted string |

### `boolean` Boolean value converting

#### Params

| Name | Type | Default | Description |
| ----- | ------- | ----- | --- |
| `value` | string or boolean | - | "Enabled"/"Disabled" or true/false |

#### Returns

| Name | Type | Description |
| ----- | ------- | --- |
| `value` | boolean |  true/false |

<hr>
