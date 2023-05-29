# termcolor-whl
Colorize your console output.

This is a fork of `termcolor`, originally created so it would have a wheel package.

 
Note that handling of nested colour tokens has been removed in this package. This is to save on an import of a large package (`re`) and since this is actually not a common usage case.

## Example

```python
import sys
from termcolor import colored, cprint

text = colored('Hello, World!', 'red', attrs=['reverse', 'blink'])
print(text)
cprint('Hello, World!', 'green', 'on_red')

print_red_on_cyan = lambda x: cprint(x, 'red', 'on_cyan')
print_red_on_cyan('Hello, World!')
print_red_on_cyan('Hello, Universe!')

for i in range(10):
    cprint(i, 'magenta', end=' ')


cprint("Attention!", 'red', attrs=['bold'], file=sys.stderr)
```


## Disabling
Any value in the environment variable `ANSI_COLORS_DISABLED` will disable colors.


## Text Properties
Text colors:

> -   grey
> -   red
> -   green
> -   yellow
> -   blue
> -   magenta
> -   cyan
> -   white

Text highlights:
> -   on\_grey
> -   on\_red
> -   on\_green
> -   on\_yellow
> -   on\_blue
> -   on\_magenta
> -   on\_cyan
> -   on\_white

Attributes:
> -   bold
> -   dark
> -   underline
> -   blink
> -   reverse
> -   concealed


## Terminal properties

    Terminal       bold      dark   underline   blink        reverse   concealed
    -------------- --------- ------ ----------- ------------ --------- -----------
    xterm          yes       no     yes         bold         yes       yes
    linux          yes       yes    bold        yes          yes       no
    rxvt           yes       no     yes         bold/black   yes       no
    dtterm         yes       yes    yes         reverse      yes       yes
    teraterm       reverse   no     yes         rev/red      yes       no
    aixterm        normal    no     yes         no           yes       yes
    PuTTY          color     no     yes         no           yes       no
    Windows        no        no     no          no           yes       no
    Cygwin SSH     yes       no     color       color        color     yes
    Mac Terminal   yes       no     yes         yes          yes       yes


## License and Authorship
Original author: Konstantin Lepa <konstantin.lepa@gmail.com>, Copyright (c) 2008-2011 Volvox Development Team
Original license: MIT.

Original source code repository no longer available, this is a fork of the artifacts published to pypi


## Documents
- [Changes](https://github.com/matthewdeanmartin/termcolor/blob/main/docs/CHANGES.MD)