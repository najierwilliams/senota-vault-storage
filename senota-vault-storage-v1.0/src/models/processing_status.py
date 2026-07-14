from enum import Enum
class ProcessingStatus(str,Enum):
    UPLOADED="uploaded"
    PROCESSING="processing"
    COMPLETED="completed"
    FAILED="failed"
