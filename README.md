![gp](https://camo.githubusercontent.com/1a0976983f732f3a3713173670c9843d4eb27c420b5844b13378aaadb28ce0b9/68747470733a2f2f726561646d652d747970696e672d7376672e6865726f6b756170702e636f6d2f3f6c696e65733d6770436f6c6f722b213b4d4144452b42592b4752414e4450412b454a213b5445524d494e414c2b434f4c4f522b574954482b5247422b414e442b4845582b434f44452b4645415455524521)
# gpColor

gpColor is a Python module for applying ANSI, RGB and HEX colors in terminal output.

## Installation
<b>install via pip</b>
```bash
pip install gpColor
```
```bash
git clone https://github.com/gpbot-org/gpColor
cd gpColor

python setup.py install
```
## Usage

```python
from gpColor import colorize as color

'''how to use text color'''
print(color("This is bright red text", font='bright_red'))
print(color("This is RGB text", font=(255, 0, 0)))
print(color("This is HEX text", font='#FF5733'))

'''
>_ How to use background color with text color

text       : font
background : back
'''
print(color("This is blue text with yellow background", font='blue', back='yellow'))
print(color("This is RGB text", font=(255, 0, 0), back=(255,255,255))
print(color("This is HEX text", font='#FF5733', back='#FFFFFF'))
```
