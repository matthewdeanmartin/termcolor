# Usage

`colored(text, color=None, on_color=None, attrs=None)` returns a string. `cprint()` accepts the same color arguments and passes additional keyword arguments, such as `file` or `end`, to `print()`.

```python
from termcolor import colored, cprint

message = colored('Ready', 'green', attrs=['bold'])
print(message)
cprint('Attention!', 'red', attrs=['underline'])
```

Foreground colors are `grey`, `red`, `green`, `yellow`, `blue`, `magenta`, `cyan`, and `white`. Each has an `on_` background highlight, such as `on_cyan`. Text attributes are `bold`, `dark`, `underline`, `blink`, `reverse`, and `concealed`.

Set `ANSI_COLORS_DISABLED` to a nonempty value to return uncolored text:

```bash
ANSI_COLORS_DISABLED=1 python -m termcolor
```

The built-in demo prints sample colors, highlights, and attributes. Appearance depends on terminal support. Nested color tokens are not handled by this fork.
