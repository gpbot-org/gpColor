import re

class Color:
    ANSI_COLORS = {
        'black': 30, 'red': 31, 'green': 32, 'yellow': 33, 'blue': 34, 'magenta': 35, 'cyan': 36, 'white': 37,
        'bright_black': 90, 'bright_red': 91, 'bright_green': 92, 'bright_yellow': 93, 'bright_blue': 94,
        'bright_magenta': 95, 'bright_cyan': 96, 'bright_white': 97
    }

    def __init__(self, text, font=None, back=None):
        """
        Initialize with text, font color, and background color.
        - font, back: Can be ANSI color names, RGB tuples, HEX strings, or RGBA.
        """
        self.text = text
        self.font = self.convert_color(font, foreground=True) if font else ''
        self.back = self.convert_color(back, foreground=False) if back else ''

    def apply(self):
        """
        Apply the color formatting and return the colored string.
        """
        return f'{self.font}{self.back}{self.text}\033[0m'

    @staticmethod
    def convert_color(color, foreground=True):
        """
        Convert a color specification to the corresponding ANSI escape code.
        - color: Can be a named ANSI color, an RGB tuple, HEX code, or RGBA.

        The First time i added RGBA 😁😁
        but it's not working for Terminal 😆😆
        """
        if isinstance(color, tuple) and len(color) == 3:  # RGB
            return Color.rgb_to_ansi(color, foreground)
        elif isinstance(color, tuple) and len(color) == 4:  # RGBA (ignore alpha)
            return Color.rgb_to_ansi(color[:3], foreground)
        elif isinstance(color, str) and re.match(r'^#(?:[0-9a-fA-F]{3}){1,2}$', color):  # HEX
            return Color.hex_to_ansi(color, foreground)
        elif isinstance(color, str) and color in Color.ANSI_COLORS:  # ANSI named color
            return Color.ansi_named_color(color, foreground)
        else:
            return ''  # Invalid color, no escape code

    @staticmethod
    def rgb_to_ansi(rgb, foreground=True):
        """
        Convert an RGB tuple (R, G, B) to an ANSI escape sequence.
        """
        r, g, b = rgb
        if foreground:
            return f'\033[38;2;{r};{g};{b}m'  # 38 for foreground
        else:
            return f'\033[48;2;{r};{g};{b}m'  # 48 for background

    @staticmethod
    def hex_to_ansi(hex_color, foreground=True):
        """
        Convert a HEX color string (e.g., "#RRGGBB") to an RGB tuple, then to an ANSI escape sequence.
        """
        hex_color = hex_color.lstrip('#')
        if len(hex_color) == 3:  # Short form (#RGB)
            hex_color = ''.join([c*2 for c in hex_color])
        rgb = tuple(int(hex_color[i:i + 2], 16) for i in (0, 2, 4))
        return Color.rgb_to_ansi(rgb, foreground)

    @staticmethod
    def ansi_named_color(name, foreground=True):
        """
        Get the ANSI code for a named ANSI color.
        """
        code = Color.ANSI_COLORS.get(name)
        if foreground:
            return f'\033[{code}m'
        else:
            return f'\033[{code + 10}m'  # Background code is foreground + 10

# Utility function for all in one 😆
def colorize(text, font=None, back=None):
    """
    Apply custom RGB/HEX/ANSI colors to text using the Color class.
    """
    return Color(text, font=font, back=back).apply()
