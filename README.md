# Japanese Text Generator

[![Build Status](https://travis-ci.org/nerophung/jpn-text-gen.svg?branch=develop)](https://travis-ci.org/nerophung/jpn-text-gen)
[![Documentation Status](https://readthedocs.org/projects/jpn-text-gen/badge/?version=latest)](https://jpn-text-gen.readthedocs.io/en/latest/?badge=latest)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://github.com/nerophung/jpn-text-gen/blob/master/LICENSE.txt)

Generate Japanese General Text for OCR Engine

This **jpngentext** is a Python package that generates general text for OCR engine training dataset such as address, name, ... The others field is updating!

See the [documentation](https://jpn-text-gen.readthedocs.io/en/latest/).

### Pip Installation

```
pip install jpntextgen
```

### 

### Usage

Use `jpntextgen.Engine()` to create text data.

```
from jpntextgen import Engine

engine = Engine()

print(engine.get_full_name())
# '長崎県南島原市深江町甲' 
print(engine.get_address())
# '柵謹 鋲套吐饅'
```

Each time you call the method `engine.get_full_name()`, it will return the randomly results.
```
for _ in range(10):
    print(engine.get_full_name())

# '藻蛍 施浮'
# '菰帆 工椀含'
# '箱誓 鉄再'
# '疑妓 藪弦竣'
# '濫成跨 家鵤'
# '孝餘 限剰'
# '繋蛋氾 効祗侵'
# '鈑耽 靱燧'
# '頂拘臣 祐双'
# '羊通莨果 癌恩特蚫'
```

### License
The **JapaneseTextGenerator** is released under the MIT License. See the bundled [LICENSE](https://github.com/nerophung/jpn-text-gen/blob/develop/LICENSE.txt) file for details.