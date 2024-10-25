# gpColor

gpColor is a Python module for applying ANSI, RGB and HEX colors in terminal output.

## Installation

```bash
❌pip install gpColor
```
```bash
git clone https://github.com/gpbot-org/gpColor
cd gpColor

python setup.py
```
## Usage

```python
from gpColor import color

print(colorize("This is bright red text", font='bright_red'))
print(colorize("This is RGB text", font=(255, 0, 0)))
print(colorize("This is HEX text", font='#FF5733'))
```