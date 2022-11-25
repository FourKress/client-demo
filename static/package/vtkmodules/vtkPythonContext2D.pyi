from typing import overload, Any, Callable, TypeVar, Union
from typing import Tuple, List, Sequence, MutableSequence

Callback = Union[Callable[..., None], None]
Buffer = TypeVar('Buffer')
Pointer = TypeVar('Pointer')
Template = TypeVar('Template')

import vtkmodules.vtkCommonCore
import vtkmodules.vtkRenderingContext2D

class vtkPythonItem(vtkmodules.vtkRenderingContext2D.vtkContextItem):
    def GetNumberOfGenerationsFromBase(self, type:str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type:str) -> int: ...
    def IsA(self, type:str) -> int: ...
    @staticmethod
    def IsTypeOf(type:str) -> int: ...
    def NewInstance(self) -> 'vtkPythonItem': ...
    def Paint(self, painter:'vtkContext2D') -> bool: ...
    @staticmethod
    def SafeDownCast(o:'vtkObjectBase') -> 'vtkPythonItem': ...
    def SetPythonObject(self, obj:'PyObject') -> None: ...

