# adofaihelper

put it into your `<Python Install Path>/Lib/adofaihelper` or `<Project Path>/adofaihelper` so you can use it as a module

---

A module to help with reading and processing `.adofai` files (in the rhythm game 'A Dance Of Fire And Ice'). 

Author: [Lipcu](https://github.com/Lipcu-pku)

Check Updates on https://github.com/Lipcu-pku/adofaihelper/tree/main

---

Examples: 

Use `adofai(path)` to directly read the level at `path` and convert to a `ADOFAI` class. 

There are several parameters in the `ADOFAI` class: `pathData`, `angleData`, `settings`, `settings_dict`, `actions`, `decorations`.

As for the difference between `settings` and `settings_dict`, the former one have further parameters like `version`, `artist` and so on. The Latter one is just the `dict` of settings. 

For lines in `actions` you can also use `action = ACTION(_action)` to get its further parameters, so does the `decorations`. 

You can just use `AskForPath()` to show a window of opening the level. 

You can use `SortActions()` to sort the actions in the order of the floor, as you can see in the default `.adofai` file. 

You can use `ADOFAIprint()` to directly output the level in the `.adofai` format, except for the random extra commas in the actions.
