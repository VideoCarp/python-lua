
"""
READ AND INSTALL ONLY.
DO NOT COPY AND RELEASE AS YOUR OWN.
If you want to improve it, fork and contribute, or write from scratch.
"""

tkmsg.showinfo("Compile", "Compiling. This may take some time.")
toParse = text_box.get(1.0, END)
lineBreak = """
""" # This functions.
parse_dict = {
      "True": "true",
      "False": "false",
      "#end": "end",
      "#class": "}",
      "def": "local function",
      "None": "nil",
      "str(": "tostring(",
      "int(": "tonumber(",
      "!=": "~=",
      "#": "--",
      "eval(": "loadstring(",
      "exec(": "loadstring(",
      " + ": " .. ",
      "elif": "elseif",
      "time.sleep(": "wait(",
      "random.randint(": "math.random(",
      "random.randrange(": "math.random(",
      ".replace(": ":gsub("
    }
# All above this are transpiled with NO condition.
parser2 = {"prtonumber": "print"} # Second parsing with NO condition, done after the first.
# SPLIT
split_array = toParse.split(lineBreak)
split_length = len(split_array)

finished = text_box.get(1.0, END)
for k, v in parse_dict.items():
    finished = finished.replace(k, v)

for k,v in parser2.items():
    finished = finished.replace(k, v)

# SPLIT
split_array = finished.split(lineBreak)
result_array = []
for line in split_array:
    if "#exclude" not in line:
        if "while" in line:
            result_array.append(line.replace(":", " do"))
        elif "if" in line:
              result_array.append(line.replace(":", " then"))
        elif "class" in line:
              result_array.append(line.replace("class ", "local ").replace(":", " = {"))
        elif " = " in line and "  " not in line and "  " not in line: # doublespace and tab.
              result_array.append(line.replace(line, "local " + line)\
              .replace("[", "{").replace("]", "}"))

        elif "else:" in line:
              result_array.append(line.replace(":", ""))
        elif "max(" in line and ")" in line:
              result_array.append(line.replace("max(", "math.max("))
        elif "min(" in line and ")" in line:
              result_array.append(line.replace("min(", "math.min("))
        elif "lamba" in line and ":" in line and " " in line:
              result_array.append(line.replace("lamda", "function").replace(" ", "(").replace(":", ")"))
        elif "lambda" in line and ":" in line and " " not in line:
              result_array.append(line.replace("lambda", "function").replace(":", "()"))
        elif "for " in line and ":" in line:
              result_array.append(line.replace(":", " do"))
        else:
            result_array.append(line)
        text_box.delete(1.0, END)
        text_box.insert(1.0, '-- Result:\n' + "\n".join(result_array))
        
        """Optional to write file directly in dir."""
        #newFile = open("result.txtl", "+w")
        #newFile.write('\n'.join(result_array))
