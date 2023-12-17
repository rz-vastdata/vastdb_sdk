# automatically generated by the FlatBuffers compiler, do not modify

# namespace: flatbuf

import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

# Date is either a 32-bit or 64-bit signed integer type representing an
# elapsed time since UNIX epoch (1970-01-01), stored in either of two units:
#
# * Milliseconds (64 bits) indicating UNIX time elapsed since the epoch (no
#   leap seconds), where the values are evenly divisible by 86400000
# * Days (32 bits) since the UNIX epoch
class Date(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = Date()
        x.Init(buf, n + offset)
        return x

    @classmethod
    def GetRootAsDate(cls, buf, offset=0):
        """This method is deprecated. Please switch to GetRootAs."""
        return cls.GetRootAs(buf, offset)
    # Date
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # Date
    def Unit(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int16Flags, o + self._tab.Pos)
        return 1

def Start(builder): builder.StartObject(1)
def DateStart(builder):
    """This method is deprecated. Please switch to Start."""
    return Start(builder)
def AddUnit(builder, unit): builder.PrependInt16Slot(0, unit, 1)
def DateAddUnit(builder, unit):
    """This method is deprecated. Please switch to AddUnit."""
    return AddUnit(builder, unit)
def End(builder): return builder.EndObject()
def DateEnd(builder):
    """This method is deprecated. Please switch to End."""
    return End(builder)