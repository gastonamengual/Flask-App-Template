from dataclasses import dataclass

from abc import ABC, abstractmethod
from typing import Generic, List, Optional, TypeVar

from app.models.models import Entity


@dataclass
class AbstractDatabaseConfig(ABC):
    ...

T = TypeVar('T', bound=AbstractDatabaseConfig)

@dataclass
class AbstractDatabase(ABC, Generic[T]):

    config: T 

    @abstractmethod
    def create(self, entity: Entity) -> Entity:
        ...

    @abstractmethod
    def get_by_id(self, entity: Entity) -> Optional[Entity]:
        pass

    @abstractmethod
    def get_all(self) -> List[Entity]:
        pass

    @abstractmethod
    def update_by_id(self, entity: Entity) -> Entity:
        pass

    @abstractmethod
    def delete_by_id(self, entity: Entity) -> None:
        pass
