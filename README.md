# Python to Lua
This transpiler compiles Python to Lua automatically.<br>
It also supports usage of normal Lua functions in the scripts you're transpiling, such as `string.gsub` in Lua.<br>
`end`s are placed manually, with `#end`, `class` becomes a `table` (end with `#class`).<br>

The aim of this transpiler is to allow a Python syntax while using Lua functions, whenever you need a specifically Lua script.<br>
All variable declarations automatically become `local` in the output, which if outside any expression, will be equivalent to a global.<br>

# Installation
Installing this transpiler is simple, and any device that can run Python can install it, so macOS, Linux, and Windows are all probably able to do it, Windows has been tested and works successfully.<br>
Here are some steps on how to install it:
* Download Python 3.8.x or higher<br>
Other Python versions (such as 3.5, 3.4, etc) may work, but have not been tested
if you already have an older version, use that. If an error occurs, upgrade.
* Download the scripts<br>
You can clone this repository, or install the `main` folder.<br>
No compilation is necessary, Python is interpreted.
* Run `compiler.py`<br>
You will have now ran the compiler.

# Usage
There are a lot of things you need to be mindful of when using the compiler, to compile, press 'Menu', click 'open', find your file, open it, then press 'Menu' again and select 'Compile'.<br>

Here is also a list of things you need to know:
* Lua built-in functions are to be used.<br>

Use Lua functions, don't use Python ones, think of this as Lua with a Python syntax.

* Indentation doesn't add `end`<br>

Always add `#end` as you would in Lua, at the end of an expression, a function, etc.
We're planning to make indentation automatically add `end` but currently it's unavailable.<br>

* Classes become Tables<br>

Lua has no classes, therefore declaring a Python class creates a Lua table, which is basically a dictionary, which is referred
to the same way as classes (eg: `tablename.tablevalue`). You need to end each class/table with `#class`.<br>
Lua tables normally do carry functions, however if you want to add one to your `class`, please use `name = function() ... #end`.

* Dictionaries are to be written with `=`<br>


You need to write each dictionary with `=`, not `"key": "value"` rather `key = "value"`
