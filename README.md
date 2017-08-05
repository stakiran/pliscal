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

## (Example) My Ops
![pliscal_sample](https://user-images.githubusercontent.com/23325839/28999448-52ed9e22-7a82-11e7-82e8-e38a57696dc4.jpg)

My customization like this:

```python
#  ---- [ Customization Area ----
format_filename = '%d.md'
format_section  = '# %Y/%m'
format_line     = ' %y%m%d'
dows            = ["mon","tue","wed","thu","fri","sat","SUN"]
#  ---- Customization Area ] ----
```

And,

- Operating on my GitHub repo to use from my any machines.
- A line of first '-' mark expresses today.

## License
[MIT License](LICENSE)

## Author
[stakiran](https://github.com/stakiran)
