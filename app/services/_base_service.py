from typing import Generic, TypeVar, Type, Optional, ClassVar

from pydantic import BaseModel
from sqlalchemy.orm import Session

AUTO = object()

_Entity = TypeVar('_Entity')

class BaseService(Generic[_Entity]):
    __entity_type__: ClassVar[_Entity]

    _DEFAULT_GET_LIMIT = 100

    def __init__(self, session: Session):
        self._session = session
        self._entity_type = self.__entity_type__

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)

    def get(self, entity_id: int) -> Optional[_Entity]:
        return self._session.get(self._entity_type, entity_id)

    def get_many(self, skip: int = 0, limit: int = _DEFAULT_GET_LIMIT) -> list[_Entity]:
        return self._session.query(self._entity_type).offset(skip).limit(limit).all()

    def add(self, entity_schema: BaseModel) -> _Entity:
        db_entity = self._convert_schema_to_db_model(entity_schema)
        self._validate_before_add(db_entity)
        self._session.add(db_entity)
        self._session.commit()
        self._session.refresh(db_entity)
        return db_entity

    def _convert_schema_to_db_model(self, entity_schema: BaseModel) -> _Entity:
        return self._entity_type(**entity_schema.dict())

    def _validate_before_add(self, entity: _Entity) -> None:
        """Overridable method to add validation before adding an object
         to the db."""
        pass