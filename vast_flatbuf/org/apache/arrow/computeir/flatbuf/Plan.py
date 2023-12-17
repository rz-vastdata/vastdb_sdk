# automatically generated by the FlatBuffers compiler, do not modify

# namespace: flatbuf

import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

# A specification of a query.
class Plan(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = Plan()
        x.Init(buf, n + offset)
        return x

    @classmethod
    def GetRootAsPlan(cls, buf, offset=0):
        """This method is deprecated. Please switch to GetRootAs."""
        return cls.GetRootAs(buf, offset)
    # Plan
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # One or more output relations.
    # Plan
    def Sinks(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            x = self._tab.Vector(o)
            x += flatbuffers.number_types.UOffsetTFlags.py_type(j) * 4
            x = self._tab.Indirect(x)
            from vast_flatbuf.org.apache.arrow.computeir.flatbuf.Relation import Relation
            obj = Relation()
            obj.Init(self._tab.Bytes, x)
            return obj
        return None

    # Plan
    def SinksLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # Plan
    def SinksIsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        return o == 0

def Start(builder): builder.StartObject(1)
def PlanStart(builder):
    """This method is deprecated. Please switch to Start."""
    return Start(builder)
def AddSinks(builder, sinks): builder.PrependUOffsetTRelativeSlot(0, flatbuffers.number_types.UOffsetTFlags.py_type(sinks), 0)
def PlanAddSinks(builder, sinks):
    """This method is deprecated. Please switch to AddSinks."""
    return AddSinks(builder, sinks)
def StartSinksVector(builder, numElems): return builder.StartVector(4, numElems, 4)
def PlanStartSinksVector(builder, numElems):
    """This method is deprecated. Please switch to Start."""
    return StartSinksVector(builder, numElems)
def End(builder): return builder.EndObject()
def PlanEnd(builder):
    """This method is deprecated. Please switch to End."""
    return End(builder)