import builtins

from utils._assert import Assert
builtins.Assert = Assert

from utils._print import print as Print
builtins.print = Print

import json as json
builtins.json = json

from pygments import highlight, lexers, formatters
builtins.highlight = highlight
builtins.lexers = lexers
builtins.formatters = formatters

from utils.to_Hz import to_Hz
builtins.to_Hz = to_Hz

from utils.Sub import sub
builtins.sub = sub

# import numpy as np
