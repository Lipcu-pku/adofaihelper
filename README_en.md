# adofaihelper

- [adofaihelper](#adofaihelper)
  - [Usage](#usage)
  - [Functions](#functions)
    - [`AskForPath` Get .adofai file path](#askforpath-get-adofai-file-path)
      - [Params](#params)
      - [Returns](#returns)
    - [`SaveAsPath` Get .adofai saving path](#saveaspath-get-adofai-saving-path)
      - [Params](#params-1)
      - [Returns](#returns-1)
    - [`pathData_to_angleData` Converting the pathData to angleData](#pathdata_to_angledata-converting-the-pathdata-to-angledata)
      - [Params](#params-2)
      - [Returns](#returns-2)
  - [ADOFAI Class](#adofai-class)
    - [ADOFAI.load](#adofaiload)
      - [Parameters](#parameters)
      - [Return Value](#return-value)
    - [ADOFAI.loads](#adofailoads)
      - [Parameters](#parameters-1)
      - [Return Value](#return-value-1)
    - [.value](#value)
      - [Return Value](#return-value-2)
    - [.as\_adofai](#as_adofai)
      - [Return Value](#return-value-3)
    - [.dump](#dump)
      - [Parameters](#parameters-2)
      - [Return Value](#return-value-4)
    - [.add\_action](#add_action)
      - [Parameters](#parameters-3)
      - [Return Value](#return-value-5)
    - [.add\_decoration](#add_decoration)
      - [Parameters](#parameters-4)
  - [SETTINGS Class](#settings-class)
    - [.value](#value-1)
      - [Return Value](#return-value-6)
  - [ACTION Class](#action-class)
    - [load](#load)
      - [Parameters](#parameters-5)
      - [Return Value](#return-value-7)
    - [.value](#value-2)
      - [Return Value](#return-value-8)
  - [DECORATION Class](#decoration-class)
    - [load](#load-1)
      - [Parameters](#parameters-6)
      - [Return Value](#return-value-9)
    - [.value](#value-3)
      - [Return Value](#return-value-10)

## Usage

```bash
pip install adofaihelper
```

```python
import adofaihelper
```

## Functions

### `AskForPath` Get .adofai file path

#### Params

None

#### Returns

| Name | Type | Description |
| ----- | ------- | --- |
| `FILE_PATH` | string | (call a tk window and select) the .adofai file path |

### `SaveAsPath` Get .adofai saving path

#### Params

| Name | Type | Default | Description |
| ----- | ------- | ----- | --- |
| `default_name` | string | - | default saving file name |

#### Returns

| Name | Type | Description |
| ----- | ------- | --- |
| `FILE_PATH` | string | (call a tk window and select) the .adofai file saving path |

### `pathData_to_angleData` Converting the pathData to angleData

#### Params

| Name | Type | Default | Description |
| ----- | ------- | ----- | --- |
| `pathData` | string | - | pathData |

#### Returns

| Name | Type | Description |
| ----- | ------- | --- |
| `angleData` | array | angleData |

## ADOFAI Class

### ADOFAI.load

#### Parameters

| Variable Name | Data Type | Default Value | Description |
| ------------- | --------- | ------------- | ----------- |
| `FILE_PATH` | string | - | Path to the .adofai file |

#### Return Value

| Variable Name | Data Type | Description |
| ------------- | --------- | ----------- |
| `level` | ADOFAI | Contents of the loaded .adofai file |

### ADOFAI.loads

#### Parameters

| Variable Name | Data Type | Default Value | Description |
| ------------- | --------- | ------------- | ----------- |
| `adofai_string` | string | - | String in .adofai format |

#### Return Value

| Variable Name | Data Type | Description |
| ------------- | --------- | ----------- |
| `level` | ADOFAI | Contents of the loaded .adofai string |

### .value

#### Return Value

| Variable Name | Data Type | Description |
| ------------- | --------- | ----------- |
| `adofai_dict` | dict | ADOFAI output in dictionary format |

### .as_adofai

#### Return Value

| Variable Name | Data Type | Description |
| ------------- | --------- | ----------- |
| `adofai_string` | string | ADOFAI output in string format |

### .dump

#### Parameters

| Variable Name | Data Type | Default Value | Description |
| ------------- | --------- | ------------- | ----------- |
| `FILE_PATH` | string | - | Path to save the .adofai file |
| `file_replace_warning` | bool | True | File replacement warning |

#### Return Value

None

### .add_action

#### Parameters

| Variable Name | Data Type | Default Value | Description |
| ------------- | --------- | ------------- | ----------- |
| `floor` | int | None | Tile number where the event occurs |
| `eventType` | str/EventType | None | Event type |
| `**kwargs` | **dict | None | Other parameters for the event |

#### Return Value

None

### .add_decoration

#### Parameters

| Variable Name | Data Type | Default Value | Description |
| ------------- | --------- | ------------- | ----------- |
| `eventType` | str/EventType | None | Event type |
| `**kwargs` | **dict | None | Other parameters for the event |

## SETTINGS Class

### .value

#### Return Value

| Variable Name | Data Type | Description |
| ------------- | --------- | ----------- |
| `settings_dict` | dict | Corresponding settings dictionary |

## ACTION Class

### load

#### Parameters

| Variable Name | Data Type | Default Value | Description |
| ------------- | --------- | ------------- | ----------- |
| `floor` | int | None | Tile number where the event occurs |
| `eventType` | str/EventType | None | Event type |
| `**kwargs` | **dict | None | Other parameters for the event |

#### Return Value

| Variable Name | Data Type | Description |
| ------------- | --------- | ----------- |
| `action` | Action | Corresponding event type |

### .value

#### Return Value

| Variable Name | Data Type | Description |
| ------------- | --------- | ----------- |
| `action_dict` | dict | Corresponding event dictionary |

## DECORATION Class

### load

#### Parameters

| Variable Name | Data Type | Default Value | Description |
| ------------- | --------- | ------------- | ----------- |
| `eventType` | str/EventType | None | Decoration event type |
| `**kwargs` | **dict | None | Other parameters for the decoration event |

#### Return Value

| Variable Name | Data Type | Description |
| ------------- | --------- | ----------- |
| `decoration` | Decoration | Corresponding decoration event type |

### .value

#### Return Value

| Variable Name | Data Type | Description |
| ------------- | --------- | ----------- |
| `decoration_dict` | dict | Corresponding decoration event dictionary |

<hr>
