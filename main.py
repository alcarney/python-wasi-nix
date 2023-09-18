import sys

from lsprotocol.converters import get_converter
from lsprotocol import types

print(f"{sys.platform=}")

converter = get_converter()
print(converter.unstructure(types.Position(line=1, character=42)))
