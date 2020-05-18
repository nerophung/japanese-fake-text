# Japanese Text Generator

It generates general text for OCR engine training dataset such as address, name, ... The others field is updating!

> Support for Python 3.6

## Installation

See [Installation](https://pypi.org/project/jpntextgen/)

## Providers

We split the text class to 4 main providers:
* General Provider
* Name Provider
* Date Provider
* Address Provider

## General Provider

This provider provide the fake text about email, url, katakana name, phone, ...

### Usage

**Get Email, Urls**

```
from jpntextgen import Engine

engine = Engine()

general_provider = engine.get_general_provider()

print(general_provider.get_email())
print(engine.get_email()

# menya1@ps.kurabo-grp.com
# okubo-k@marubeni.com

print(general_provider.get_url())
print(engine.get_url())

# www.designpocket.co.jp
# www.agrex.co.jp
```

**Get Katakana - English**

```
print(general_provider.get_eng_katakana())
# ホィラヒヌ
```

**Get Phone Number**

```
print(general_provider.get_phone_number())
# 546-5640-974
```

For more code, see [Source code](https://github.com/nerophung/jpn-text-gen/blob/master/jpntextgen/general_provider.py)

## Name Provider

This provider provide human name in Kanji and Hiragana.

### Usage

```
from jpntextgen import Engine

engine = Engine()

name_provider = engine.get_name_provider()

print(name_provider.get_full_name())

# 丘謂 用抓
```

For more code, see [Source code](https://github.com/nerophung/jpn-text-gen/blob/master/jpntextgen/name_provider.py)

## Date Provider

This provider provide date using Popular Japanese Date Format.

### Usage

```
from jpntextgen import Engine

engine = Engine()

date_provider = engine.get_date_provider()

print(date_provider.get_date())

# 大永24.24.09
```

For more code, see [Source code](https://github.com/nerophung/jpn-text-gen/blob/master/jpntextgen/date_provider.py)

## Address Provider

This provider provide real Japanese address such as city, district and fake building name, floor number.

### Usage

```
from jpntextgen import Engine

engine = Engine()

address_provider = engine.get_address_provider()

print(address_provider.get_address())

# 大永24.24.09
```

For more code, see [Source code](https://github.com/nerophung/jpn-text-gen/blob/master/jpntextgen/address_provider.py)
