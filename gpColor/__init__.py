# Import the main functions and classes from the color module
from .color import Color, colorize, ansi_color, rgb_color, hex_to_rgb

# Define the public interface of the package
__all__ = ['Color', 'colorize', 'ansi_color', 'rgb_color', 'hex_to_rgb']
