# Japanese Text Generator

[![Documentation Status](https://readthedocs.org/projects/jpn-text-gen/badge/?version=latest)](https://jpn-text-gen.readthedocs.io/en/latest/?badge=latest)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://github.com/nerophung/jpn-text-gen/blob/master/LICENSE.txt)

Generate Japanese General Text for OCR Engine

### Pip Installation

```
pip install jpntextgen
```

### Usage

```
from jpntextgen import Engine

engine = Engine()

print(engine.get_full_name())
print(engine.get_address())
```