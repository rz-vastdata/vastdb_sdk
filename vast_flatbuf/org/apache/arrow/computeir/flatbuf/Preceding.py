# automatically generated by the FlatBuffers compiler, do not modify

# namespace: flatbuf

import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

# Boundary is preceding rows, determined by the contained expression
class Preceding(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = Preceding()
        x.Init(buf, n + offset)
        return x

    @classmethod
    def GetRootAsPreceding(cls, buf, offset=0):
        """This method is deprecated. Please switch to GetRootAs."""
        return cls.GetRootAs(buf, offset)
    # Preceding
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # Preceding
    def ImplType(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint8Flags, o + self._tab.Pos)
        return 0

    # Preceding
    def Impl(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            from flatbuffers.table import Table
            obj = Table(bytearray(), 0)
            self._tab.Union(obj, o)
            return obj
        return None

def Start(builder): builder.StartObject(2)
def PrecedingStart(builder):
    """This method is deprecated. Please switch to Start."""
    return Start(builder)
def AddImplType(builder, implType): builder.PrependUint8Slot(0, implType, 0)
def PrecedingAddImplType(builder, implType):
    """This method is deprecated. Please switch to AddImplType."""
    return AddImplType(builder, implType)
def AddImpl(builder, impl): builder.PrependUOffsetTRelativeSlot(1, flatbuffers.number_types.UOffsetTFlags.py_type(impl), 0)
def PrecedingAddImpl(builder, impl):
    """This method is deprecated. Please switch to AddImpl."""
    return AddImpl(builder, impl)
def End(builder): return builder.EndObject()
def PrecedingEnd(builder):
    """This method is deprecated. Please switch to End."""
    return End(builder)