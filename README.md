# pliscal
A plain markdown list calender.

## Sample

```terminal
$ python pliscal.py -y 2017
```

[2017.md](2017.md)

## Requirement
- Python2.7

## How to customize
Please edit the customization area of [pliscal.py](pliscal.py).

```python
...
#  ---- [ Customization Area ----
format_filename = '%d.md'
format_section  = '# %Y/%m'
format_line     = '- %y%m%d'
dows            = ["mon","tue","wed","thu","fri","sat","SUN"]
#  ---- Customization Area ] ----
...
```

## License
[MIT License](LICENSE)

## Author
[stakiran](https://github.com/stakiran)
