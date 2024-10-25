![Typing SVG](https://readme-typing-svg.herokuapp.com/?lines=gpColor+!;MADE+BY+GRANDPA+EJ!;TERMINAL+COLOR+WITH+RGB+AND+HEX+CODE+FEATURE!)
# gpColor

gpColor is a Python module for applying ANSI, RGB and HEX colors in terminal output.

## Installation

```bash
❌pip install gpColor
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
