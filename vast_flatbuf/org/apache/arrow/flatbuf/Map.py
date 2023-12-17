# automatically generated by the FlatBuffers compiler, do not modify

# namespace: flatbuf

import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

# A Map is a logical nested type that is represented as
#
# List<entries: Struct<key: K, value: V>>
#
# In this layout, the keys and values are each respectively contiguous. We do
# not constrain the key and value types, so the application is responsible
# for ensuring that the keys are hashable and unique. Whether the keys are sorted
# may be set in the metadata for this field.
#
# In a field with Map type, the field has a child Struct field, which then
# has two children: key type and the second the value type. The names of the
# child fields may be respectively "entries", "key", and "value", but this is
# not enforced.
#
# Map
# ```text
#   - child[0] entries: Struct
#     - child[0] key: K
#     - child[1] value: V
# ```
# Neither the "entries" field nor the "key" field may be nullable.
#
# The metadata is structured so that Arrow systems without special handling
# for Map can make Map an alias for List. The "layout" attribute for the Map
# field must have the same contents as a List.
class Map(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = Map()
        x.Init(buf, n + offset)
        return x

    @classmethod
    def GetRootAsMap(cls, buf, offset=0):
        """This method is deprecated. Please switch to GetRootAs."""
        return cls.GetRootAs(buf, offset)
    # Map
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # Set to true if the keys within each value are sorted
    # Map
    def KeysSorted(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return bool(self._tab.Get(flatbuffers.number_types.BoolFlags, o + self._tab.Pos))
        return False

def Start(builder): builder.StartObject(1)
def MapStart(builder):
    """This method is deprecated. Please switch to Start."""
    return Start(builder)
def AddKeysSorted(builder, keysSorted): builder.PrependBoolSlot(0, keysSorted, 0)
def MapAddKeysSorted(builder, keysSorted):
    """This method is deprecated. Please switch to AddKeysSorted."""
    return AddKeysSorted(builder, keysSorted)
def End(builder): return builder.EndObject()
def MapEnd(builder):
    """This method is deprecated. Please switch to End."""
    return End(builder)