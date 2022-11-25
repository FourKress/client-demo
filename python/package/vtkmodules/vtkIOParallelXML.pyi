from typing import overload, Any, Callable, TypeVar, Union
from typing import Tuple, List, Sequence, MutableSequence

Callback = Union[Callable[..., None], None]
Buffer = TypeVar('Buffer')
Pointer = TypeVar('Pointer')
Template = TypeVar('Template')

import vtkmodules.vtkCommonCore
import vtkmodules.vtkIOXML

class vtkXMLCompositeDataSetWriterHelper(vtkmodules.vtkCommonCore.vtkObject):
    def GetNumberOfGenerationsFromBase(self, type:str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type:str) -> int: ...
    def GetWriter(self) -> 'vtkXMLWriterBase': ...
    def IsA(self, type:str) -> int: ...
    @staticmethod
    def IsTypeOf(type:str) -> int: ...
    def NewInstance(self) -> 'vtkXMLCompositeDataSetWriterHelper': ...
    @staticmethod
    def SafeDownCast(o:'vtkObjectBase') -> 'vtkXMLCompositeDataSetWriterHelper': ...
    def SetWriter(self, writer:'vtkXMLWriterBase') -> None: ...
    def WriteDataSet(self, path:str, prefix:str, data:'vtkDataObject') -> str: ...

class vtkXMLDataWriterHelper(vtkmodules.vtkIOXML.vtkXMLWriter):
    def AddGlobalFieldData(self, dataset:'vtkCompositeDataSet') -> bool: ...
    def AddXML(self, xmlElement:'vtkXMLDataElement') -> bool: ...
    def BeginWriting(self) -> bool: ...
    def EndWriting(self) -> bool: ...
    def GetDefaultFileExtension(self) -> str: ...
    def GetNumberOfGenerationsFromBase(self, type:str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type:str) -> int: ...
    def GetWriter(self) -> 'vtkXMLWriter2': ...
    def IsA(self, type:str) -> int: ...
    @staticmethod
    def IsTypeOf(type:str) -> int: ...
    def NewInstance(self) -> 'vtkXMLDataWriterHelper': ...
    def OpenFile(self) -> bool: ...
    @staticmethod
    def SafeDownCast(o:'vtkObjectBase') -> 'vtkXMLDataWriterHelper': ...
    def SetDataSetName(self, name:str) -> None: ...
    def SetDataSetVersion(self, major:int, minor:int) -> None: ...
    def SetWriter(self, __a:'vtkXMLWriter2') -> None: ...

class vtkXMLPDataObjectWriter(vtkmodules.vtkIOXML.vtkXMLWriter):
    def GetController(self) -> 'vtkMultiProcessController': ...
    def GetEndPiece(self) -> int: ...
    def GetGhostLevel(self) -> int: ...
    def GetNumberOfGenerationsFromBase(self, type:str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type:str) -> int: ...
    def GetNumberOfPieces(self) -> int: ...
    def GetStartPiece(self) -> int: ...
    def GetUseSubdirectory(self) -> bool: ...
    def GetWriteSummaryFile(self) -> int: ...
    def IsA(self, type:str) -> int: ...
    @staticmethod
    def IsTypeOf(type:str) -> int: ...
    def NewInstance(self) -> 'vtkXMLPDataObjectWriter': ...
    @staticmethod
    def SafeDownCast(o:'vtkObjectBase') -> 'vtkXMLPDataObjectWriter': ...
    def SetController(self, __a:'vtkMultiProcessController') -> None: ...
    def SetEndPiece(self, _arg:int) -> None: ...
    def SetGhostLevel(self, _arg:int) -> None: ...
    def SetNumberOfPieces(self, _arg:int) -> None: ...
    def SetStartPiece(self, _arg:int) -> None: ...
    def SetUseSubdirectory(self, _arg:bool) -> None: ...
    def SetWriteSummaryFile(self, flag:int) -> None: ...
    def WriteSummaryFileOff(self) -> None: ...
    def WriteSummaryFileOn(self) -> None: ...

class vtkXMLPDataWriter(vtkXMLPDataObjectWriter):
    def GetNumberOfGenerationsFromBase(self, type:str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type:str) -> int: ...
    def IsA(self, type:str) -> int: ...
    @staticmethod
    def IsTypeOf(type:str) -> int: ...
    def NewInstance(self) -> 'vtkXMLPDataWriter': ...
    @staticmethod
    def SafeDownCast(o:'vtkObjectBase') -> 'vtkXMLPDataWriter': ...

class vtkXMLPDataSetWriter(vtkXMLPDataWriter):
    def GetInput(self) -> 'vtkDataSet': ...
    def GetNumberOfGenerationsFromBase(self, type:str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type:str) -> int: ...
    def IsA(self, type:str) -> int: ...
    @staticmethod
    def IsTypeOf(type:str) -> int: ...
    def NewInstance(self) -> 'vtkXMLPDataSetWriter': ...
    @staticmethod
    def SafeDownCast(o:'vtkObjectBase') -> 'vtkXMLPDataSetWriter': ...

class vtkXMLPUniformGridAMRWriter(vtkmodules.vtkIOXML.vtkXMLUniformGridAMRWriter):
    def GetController(self) -> 'vtkMultiProcessController': ...
    def GetNumberOfGenerationsFromBase(self, type:str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type:str) -> int: ...
    def IsA(self, type:str) -> int: ...
    @staticmethod
    def IsTypeOf(type:str) -> int: ...
    def NewInstance(self) -> 'vtkXMLPUniformGridAMRWriter': ...
    @staticmethod
    def SafeDownCast(o:'vtkObjectBase') -> 'vtkXMLPUniformGridAMRWriter': ...
    def SetController(self, __a:'vtkMultiProcessController') -> None: ...
    def SetWriteMetaFile(self, flag:int) -> None: ...

class vtkXMLPHierarchicalBoxDataWriter(vtkXMLPUniformGridAMRWriter):
    def GetNumberOfGenerationsFromBase(self, type:str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type:str) -> int: ...
    def IsA(self, type:str) -> int: ...
    @staticmethod
    def IsTypeOf(type:str) -> int: ...
    def NewInstance(self) -> 'vtkXMLPHierarchicalBoxDataWriter': ...
    @staticmethod
    def SafeDownCast(o:'vtkObjectBase') -> 'vtkXMLPHierarchicalBoxDataWriter': ...

class vtkXMLPHyperTreeGridWriter(vtkXMLPDataObjectWriter):
    def GetDefaultFileExtension(self) -> str: ...
    def GetInput(self) -> 'vtkHyperTreeGrid': ...
    def GetNumberOfGenerationsFromBase(self, type:str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type:str) -> int: ...
    def IsA(self, type:str) -> int: ...
    @staticmethod
    def IsTypeOf(type:str) -> int: ...
    def NewInstance(self) -> 'vtkXMLPHyperTreeGridWriter': ...
    @staticmethod
    def SafeDownCast(o:'vtkObjectBase') -> 'vtkXMLPHyperTreeGridWriter': ...

class vtkXMLPStructuredDataWriter(vtkXMLPDataWriter):
    def GetNumberOfGenerationsFromBase(self, type:str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type:str) -> int: ...
    def IsA(self, type:str) -> int: ...
    @staticmethod
    def IsTypeOf(type:str) -> int: ...
    def NewInstance(self) -> 'vtkXMLPStructuredDataWriter': ...
    @staticmethod
    def SafeDownCast(o:'vtkObjectBase') -> 'vtkXMLPStructuredDataWriter': ...

class vtkXMLPImageDataWriter(vtkXMLPStructuredDataWriter):
    def GetDefaultFileExtension(self) -> str: ...
    def GetInput(self) -> 'vtkImageData': ...
    def GetNumberOfGenerationsFromBase(self, type:str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type:str) -> int: ...
    def IsA(self, type:str) -> int: ...
    @staticmethod
    def IsTypeOf(type:str) -> int: ...
    def NewInstance(self) -> 'vtkXMLPImageDataWriter': ...
    @staticmethod
    def SafeDownCast(o:'vtkObjectBase') -> 'vtkXMLPImageDataWriter': ...

class vtkXMLPMultiBlockDataWriter(vtkmodules.vtkIOXML.vtkXMLMultiBlockDataWriter):
    def GetController(self) -> 'vtkMultiProcessController': ...
    def GetNumberOfGenerationsFromBase(self, type:str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type:str) -> int: ...
    def GetNumberOfPieces(self) -> int: ...
    def GetStartPiece(self) -> int: ...
    def IsA(self, type:str) -> int: ...
    @staticmethod
    def IsTypeOf(type:str) -> int: ...
    def NewInstance(self) -> 'vtkXMLPMultiBlockDataWriter': ...
    @staticmethod
    def SafeDownCast(o:'vtkObjectBase') -> 'vtkXMLPMultiBlockDataWriter': ...
    def SetController(self, __a:'vtkMultiProcessController') -> None: ...
    def SetNumberOfPieces(self, _arg:int) -> None: ...
    def SetStartPiece(self, _arg:int) -> None: ...
    def SetWriteMetaFile(self, flag:int) -> None: ...

class vtkXMLWriter2(vtkmodules.vtkIOXML.vtkXMLWriterBase):
    def GetController(self) -> 'vtkMultiProcessController': ...
    def GetNumberOfGenerationsFromBase(self, type:str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type:str) -> int: ...
    def GetNumberOfGhostLevels(self) -> int: ...
    def GetNumberOfGhostLevelsMaxValue(self) -> int: ...
    def GetNumberOfGhostLevelsMinValue(self) -> int: ...
    def IsA(self, type:str) -> int: ...
    @staticmethod
    def IsTypeOf(type:str) -> int: ...
    def NewInstance(self) -> 'vtkXMLWriter2': ...
    @staticmethod
    def SafeDownCast(o:'vtkObjectBase') -> 'vtkXMLWriter2': ...
    def SetController(self, controller:'vtkMultiProcessController') -> None: ...
    def SetNumberOfGhostLevels(self, _arg:int) -> None: ...

class vtkXMLPartitionedDataSetWriter(vtkXMLWriter2):
    def GetDefaultFileExtension(self) -> str: ...
    def GetNumberOfGenerationsFromBase(self, type:str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type:str) -> int: ...
    def IsA(self, type:str) -> int: ...
    @staticmethod
    def IsTypeOf(type:str) -> int: ...
    def NewInstance(self) -> 'vtkXMLPartitionedDataSetWriter': ...
    @staticmethod
    def SafeDownCast(o:'vtkObjectBase') -> 'vtkXMLPartitionedDataSetWriter': ...
    def SetInputData(self, pd:'vtkPartitionedDataSet') -> None: ...

class vtkXMLPPartitionedDataSetWriter(vtkXMLPartitionedDataSetWriter):
    def GetNumberOfGenerationsFromBase(self, type:str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type:str) -> int: ...
    def GetNumberOfPieces(self) -> int: ...
    def GetStartPiece(self) -> int: ...
    def IsA(self, type:str) -> int: ...
    @staticmethod
    def IsTypeOf(type:str) -> int: ...
    def NewInstance(self) -> 'vtkXMLPPartitionedDataSetWriter': ...
    @staticmethod
    def SafeDownCast(o:'vtkObjectBase') -> 'vtkXMLPPartitionedDataSetWriter': ...
    def SetNumberOfPieces(self, _arg:int) -> None: ...
    def SetStartPiece(self, _arg:int) -> None: ...
    def SetWriteMetaFile(self, __a:int) -> None: ...

class vtkXMLPUnstructuredDataWriter(vtkXMLPDataWriter):
    def GetNumberOfGenerationsFromBase(self, type:str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type:str) -> int: ...
    def IsA(self, type:str) -> int: ...
    @staticmethod
    def IsTypeOf(type:str) -> int: ...
    def NewInstance(self) -> 'vtkXMLPUnstructuredDataWriter': ...
    @staticmethod
    def SafeDownCast(o:'vtkObjectBase') -> 'vtkXMLPUnstructuredDataWriter': ...

class vtkXMLPPolyDataWriter(vtkXMLPUnstructuredDataWriter):
    def GetDefaultFileExtension(self) -> str: ...
    def GetInput(self) -> 'vtkPolyData': ...
    def GetNumberOfGenerationsFromBase(self, type:str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type:str) -> int: ...
    def IsA(self, type:str) -> int: ...
    @staticmethod
    def IsTypeOf(type:str) -> int: ...
    def NewInstance(self) -> 'vtkXMLPPolyDataWriter': ...
    @staticmethod
    def SafeDownCast(o:'vtkObjectBase') -> 'vtkXMLPPolyDataWriter': ...

class vtkXMLPRectilinearGridWriter(vtkXMLPStructuredDataWriter):
    def GetDefaultFileExtension(self) -> str: ...
    def GetInput(self) -> 'vtkRectilinearGrid': ...
    def GetNumberOfGenerationsFromBase(self, type:str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type:str) -> int: ...
    def IsA(self, type:str) -> int: ...
    @staticmethod
    def IsTypeOf(type:str) -> int: ...
    def NewInstance(self) -> 'vtkXMLPRectilinearGridWriter': ...
    @staticmethod
    def SafeDownCast(o:'vtkObjectBase') -> 'vtkXMLPRectilinearGridWriter': ...

class vtkXMLPStructuredGridWriter(vtkXMLPStructuredDataWriter):
    def GetDefaultFileExtension(self) -> str: ...
    def GetInput(self) -> 'vtkStructuredGrid': ...
    def GetNumberOfGenerationsFromBase(self, type:str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type:str) -> int: ...
    def IsA(self, type:str) -> int: ...
    @staticmethod
    def IsTypeOf(type:str) -> int: ...
    def NewInstance(self) -> 'vtkXMLPStructuredGridWriter': ...
    @staticmethod
    def SafeDownCast(o:'vtkObjectBase') -> 'vtkXMLPStructuredGridWriter': ...

class vtkXMLPTableWriter(vtkXMLPDataObjectWriter):
    def GetDefaultFileExtension(self) -> str: ...
    def GetInput(self) -> 'vtkTable': ...
    def GetNumberOfGenerationsFromBase(self, type:str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type:str) -> int: ...
    def IsA(self, type:str) -> int: ...
    @staticmethod
    def IsTypeOf(type:str) -> int: ...
    def NewInstance(self) -> 'vtkXMLPTableWriter': ...
    @staticmethod
    def SafeDownCast(o:'vtkObjectBase') -> 'vtkXMLPTableWriter': ...

class vtkXMLPUnstructuredGridWriter(vtkXMLPUnstructuredDataWriter):
    def GetDefaultFileExtension(self) -> str: ...
    def GetInput(self) -> 'vtkUnstructuredGridBase': ...
    def GetNumberOfGenerationsFromBase(self, type:str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type:str) -> int: ...
    def IsA(self, type:str) -> int: ...
    @staticmethod
    def IsTypeOf(type:str) -> int: ...
    def NewInstance(self) -> 'vtkXMLPUnstructuredGridWriter': ...
    @staticmethod
    def SafeDownCast(o:'vtkObjectBase') -> 'vtkXMLPUnstructuredGridWriter': ...

class vtkXMLPartitionedDataSetCollectionWriter(vtkXMLWriter2):
    def GetDefaultFileExtension(self) -> str: ...
    def GetNumberOfGenerationsFromBase(self, type:str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type:str) -> int: ...
    def IsA(self, type:str) -> int: ...
    @staticmethod
    def IsTypeOf(type:str) -> int: ...
    def NewInstance(self) -> 'vtkXMLPartitionedDataSetCollectionWriter': ...
    @staticmethod
    def SafeDownCast(o:'vtkObjectBase') -> 'vtkXMLPartitionedDataSetCollectionWriter': ...
    def SetInputData(self, pd:'vtkPartitionedDataSetCollection') -> None: ...
