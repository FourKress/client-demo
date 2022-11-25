from typing import overload, Any, Callable, TypeVar, Union
from typing import Tuple, List, Sequence, MutableSequence

Callback = Union[Callable[..., None], None]
Buffer = TypeVar('Buffer')
Pointer = TypeVar('Pointer')
Template = TypeVar('Template')

import vtkmodules.vtkCommonCore
import vtkmodules.vtkCommonExecutionModel
import vtkmodules.vtkIOCore
import vtkmodules.vtkIOGeometry
import vtkmodules.vtkIOImage
import vtkmodules.vtkIOLegacy

class vtkEnSightWriter(vtkmodules.vtkIOCore.vtkWriter):
    def GetBaseName(self) -> str: ...
    def GetBlockIDs(self) -> Pointer: ...
    def GetFileName(self) -> str: ...
    def GetGhostLevel(self) -> int: ...
    def GetInput(self) -> 'vtkUnstructuredGrid': ...
    def GetNumberOfBlocks(self) -> int: ...
    def GetNumberOfGenerationsFromBase(self, type:str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type:str) -> int: ...
    def GetPath(self) -> str: ...
    def GetProcessNumber(self) -> int: ...
    def GetTimeStep(self) -> int: ...
    def GetTransientGeometry(self) -> bool: ...
    def IsA(self, type:str) -> int: ...
    @staticmethod
    def IsTypeOf(type:str) -> int: ...
    def NewInstance(self) -> 'vtkEnSightWriter': ...
    @staticmethod
    def SafeDownCast(o:'vtkObjectBase') -> 'vtkEnSightWriter': ...
    def SetBaseName(self, _arg:str) -> None: ...
    def SetBlockIDs(self, val:MutableSequence[int]) -> None: ...
    def SetFileName(self, _arg:str) -> None: ...
    def SetGhostLevel(self, _arg:int) -> None: ...
    def SetInputData(self, input:'vtkUnstructuredGrid') -> None: ...
    def SetNumberOfBlocks(self, _arg:int) -> None: ...
    def SetPath(self, _arg:str) -> None: ...
    def SetProcessNumber(self, _arg:int) -> None: ...
    def SetTimeStep(self, _arg:int) -> None: ...
    def SetTransientGeometry(self, _arg:bool) -> None: ...
    def WriteCaseFile(self, TotalTimeSteps:int) -> None: ...
    def WriteSOSCaseFile(self, NumProcs:int) -> None: ...

class vtkMultiBlockPLOT3DReader(vtkmodules.vtkCommonExecutionModel.vtkParallelReader):
    FILE_BIG_ENDIAN:int
    FILE_LITTLE_ENDIAN:int
    def AddFunction(self, functionNumber:int) -> None: ...
    def AddFunctionName(self, name:str) -> None: ...
    def AutoDetectFormatOff(self) -> None: ...
    def AutoDetectFormatOn(self) -> None: ...
    def BinaryFileOff(self) -> None: ...
    def BinaryFileOn(self) -> None: ...
    def CanReadBinaryFile(self, fname:str) -> int: ...
    def DoublePrecisionOff(self) -> None: ...
    def DoublePrecisionOn(self) -> None: ...
    def ForceReadOff(self) -> None: ...
    def ForceReadOn(self) -> None: ...
    def GetAutoDetectFormat(self) -> int: ...
    def GetBinaryFile(self) -> int: ...
    def GetByteOrder(self) -> int: ...
    def GetByteOrderAsString(self) -> str: ...
    def GetController(self) -> 'vtkMultiProcessController': ...
    def GetDoublePrecision(self) -> int: ...
    @overload
    def GetFileName(self) -> str: ...
    @overload
    def GetFileName(self, i:int) -> str: ...
    def GetForceRead(self) -> int: ...
    def GetFunctionFileName(self) -> str: ...
    def GetGamma(self) -> float: ...
    def GetHasByteCount(self) -> int: ...
    def GetIBlanking(self) -> int: ...
    def GetMultiGrid(self) -> int: ...
    def GetNumberOfGenerationsFromBase(self, type:str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type:str) -> int: ...
    @overload
    def GetOutput(self) -> 'vtkMultiBlockDataSet': ...
    @overload
    def GetOutput(self, __a:int) -> 'vtkMultiBlockDataSet': ...
    def GetPreserveIntermediateFunctions(self) -> bool: ...
    def GetQFileName(self) -> str: ...
    def GetR(self) -> float: ...
    def GetScalarFunctionNumber(self) -> int: ...
    def GetTwoDimensionalGeometry(self) -> int: ...
    def GetVectorFunctionNumber(self) -> int: ...
    def GetXYZFileName(self) -> str: ...
    def HasByteCountOff(self) -> None: ...
    def HasByteCountOn(self) -> None: ...
    def IBlankingOff(self) -> None: ...
    def IBlankingOn(self) -> None: ...
    def IsA(self, type:str) -> int: ...
    @staticmethod
    def IsTypeOf(type:str) -> int: ...
    def MultiGridOff(self) -> None: ...
    def MultiGridOn(self) -> None: ...
    def NewInstance(self) -> 'vtkMultiBlockPLOT3DReader': ...
    def PreserveIntermediateFunctionsOff(self) -> None: ...
    def PreserveIntermediateFunctionsOn(self) -> None: ...
    def ReadArrays(self, piece:int, npieces:int, nghosts:int, timestep:int, output:'vtkDataObject') -> int: ...
    def ReadMesh(self, piece:int, npieces:int, nghosts:int, timestep:int, output:'vtkDataObject') -> int: ...
    def ReadMetaData(self, metadata:'vtkInformation') -> int: ...
    def ReadPoints(self, piece:int, npieces:int, nghosts:int, timestep:int, output:'vtkDataObject') -> int: ...
    def RemoveAllFunctions(self) -> None: ...
    def RemoveFunction(self, __a:int) -> None: ...
    @staticmethod
    def SafeDownCast(o:'vtkObjectBase') -> 'vtkMultiBlockPLOT3DReader': ...
    def SetAutoDetectFormat(self, _arg:int) -> None: ...
    def SetBinaryFile(self, _arg:int) -> None: ...
    def SetByteOrder(self, _arg:int) -> None: ...
    def SetByteOrderToBigEndian(self) -> None: ...
    def SetByteOrderToLittleEndian(self) -> None: ...
    def SetController(self, c:'vtkMultiProcessController') -> None: ...
    def SetDoublePrecision(self, _arg:int) -> None: ...
    def SetFileName(self, name:str) -> None: ...
    def SetForceRead(self, _arg:int) -> None: ...
    def SetFunctionFileName(self, _arg:str) -> None: ...
    def SetGamma(self, _arg:float) -> None: ...
    def SetHasByteCount(self, _arg:int) -> None: ...
    def SetIBlanking(self, _arg:int) -> None: ...
    def SetMultiGrid(self, _arg:int) -> None: ...
    def SetPreserveIntermediateFunctions(self, _arg:bool) -> None: ...
    def SetQFileName(self, name:str) -> None: ...
    def SetR(self, _arg:float) -> None: ...
    def SetScalarFunctionNumber(self, num:int) -> None: ...
    def SetTwoDimensionalGeometry(self, _arg:int) -> None: ...
    def SetVectorFunctionNumber(self, num:int) -> None: ...
    def SetXYZFileName(self, __a:str) -> None: ...
    def TwoDimensionalGeometryOff(self) -> None: ...
    def TwoDimensionalGeometryOn(self) -> None: ...

class vtkPChacoReader(vtkmodules.vtkIOGeometry.vtkChacoReader):
    def GetController(self) -> 'vtkMultiProcessController': ...
    def GetNumberOfGenerationsFromBase(self, type:str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type:str) -> int: ...
    def IsA(self, type:str) -> int: ...
    @staticmethod
    def IsTypeOf(type:str) -> int: ...
    def NewInstance(self) -> 'vtkPChacoReader': ...
    @staticmethod
    def SafeDownCast(o:'vtkObjectBase') -> 'vtkPChacoReader': ...
    def SetController(self, c:'vtkMultiProcessController') -> None: ...

class vtkPDataSetReader(vtkmodules.vtkCommonExecutionModel.vtkDataSetAlgorithm):
    def CanReadFile(self, filename:str) -> int: ...
    def GetDataType(self) -> int: ...
    def GetFileName(self) -> str: ...
    def GetNumberOfGenerationsFromBase(self, type:str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type:str) -> int: ...
    def IsA(self, type:str) -> int: ...
    @staticmethod
    def IsTypeOf(type:str) -> int: ...
    def NewInstance(self) -> 'vtkPDataSetReader': ...
    @staticmethod
    def SafeDownCast(o:'vtkObjectBase') -> 'vtkPDataSetReader': ...
    def SetFileName(self, _arg:str) -> None: ...

class vtkPDataSetWriter(vtkmodules.vtkIOLegacy.vtkDataSetWriter):
    def GetController(self) -> 'vtkMultiProcessController': ...
    def GetEndPiece(self) -> int: ...
    def GetFilePattern(self) -> str: ...
    def GetGhostLevel(self) -> int: ...
    def GetNumberOfGenerationsFromBase(self, type:str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type:str) -> int: ...
    def GetNumberOfPieces(self) -> int: ...
    def GetStartPiece(self) -> int: ...
    def GetUseRelativeFileNames(self) -> int: ...
    def IsA(self, type:str) -> int: ...
    @staticmethod
    def IsTypeOf(type:str) -> int: ...
    def NewInstance(self) -> 'vtkPDataSetWriter': ...
    @staticmethod
    def SafeDownCast(o:'vtkObjectBase') -> 'vtkPDataSetWriter': ...
    def SetController(self, __a:'vtkMultiProcessController') -> None: ...
    def SetEndPiece(self, _arg:int) -> None: ...
    def SetFilePattern(self, _arg:str) -> None: ...
    def SetGhostLevel(self, _arg:int) -> None: ...
    def SetNumberOfPieces(self, num:int) -> None: ...
    def SetStartPiece(self, _arg:int) -> None: ...
    def SetUseRelativeFileNames(self, _arg:int) -> None: ...
    def UseRelativeFileNamesOff(self) -> None: ...
    def UseRelativeFileNamesOn(self) -> None: ...
    def Write(self) -> int: ...

class vtkPImageWriter(vtkmodules.vtkIOImage.vtkImageWriter):
    def GetMemoryLimit(self) -> int: ...
    def GetNumberOfGenerationsFromBase(self, type:str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type:str) -> int: ...
    def IsA(self, type:str) -> int: ...
    @staticmethod
    def IsTypeOf(type:str) -> int: ...
    def NewInstance(self) -> 'vtkPImageWriter': ...
    @staticmethod
    def SafeDownCast(o:'vtkObjectBase') -> 'vtkPImageWriter': ...
    def SetMemoryLimit(self, _arg:int) -> None: ...

class vtkPOpenFOAMReader(vtkmodules.vtkIOGeometry.vtkOpenFOAMReader):
    class caseType(int): ...
    DECOMPOSED_CASE:'caseType'
    RECONSTRUCTED_CASE:'caseType'
    def GetCaseType(self) -> 'caseType': ...
    def GetController(self) -> 'vtkMultiProcessController': ...
    def GetNumberOfGenerationsFromBase(self, type:str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type:str) -> int: ...
    def IsA(self, type:str) -> int: ...
    @staticmethod
    def IsTypeOf(type:str) -> int: ...
    def NewInstance(self) -> 'vtkPOpenFOAMReader': ...
    @staticmethod
    def SafeDownCast(o:'vtkObjectBase') -> 'vtkPOpenFOAMReader': ...
    def SetCaseType(self, t:int) -> None: ...
    def SetController(self, __a:'vtkMultiProcessController') -> None: ...

class vtkPlot3DMetaReader(vtkmodules.vtkCommonExecutionModel.vtkMultiBlockDataSetAlgorithm):
    def GetFileName(self) -> str: ...
    def GetNumberOfGenerationsFromBase(self, type:str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type:str) -> int: ...
    def IsA(self, type:str) -> int: ...
    @staticmethod
    def IsTypeOf(type:str) -> int: ...
    def NewInstance(self) -> 'vtkPlot3DMetaReader': ...
    @staticmethod
    def SafeDownCast(o:'vtkObjectBase') -> 'vtkPlot3DMetaReader': ...
    def SetFileName(self, _arg:str) -> None: ...

