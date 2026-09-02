# abstract CloudStorage class and implement GoogleDrive, AWSStorage, and AzureStorage.
from abc import ABC, abstractmethod
class CloudStorage(ABC):
    @abstractmethod
    storage(self)
    0.