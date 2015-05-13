import string
import sublime
import sublime_plugin
import zlib

class GzdecodeCommand(Transformer):
    transformer = lambda s: zlib.decompress(s),
