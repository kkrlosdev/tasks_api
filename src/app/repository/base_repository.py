from enum import StrEnum
from types import TracebackType
from typing import Iterable, Any, Mapping, Type

from app.utils.fetch_all import fetch_all
from app.utils.fetch_one import fetch_one
from db.connection import connect

SQLParams = Iterable[Any] | Mapping[str, Any]

class ExecuteMode(StrEnum):
    ALL = "all"
    ONE = "one"

class BaseRepository:
    def __enter__(self):
        # Se ejecuta al momento de abrir la conexión y crea la conexión y el cursor.
        self.connection = connect()
        self._configure_connection()
        self.cursor = self.connection.cursor()
        return self

    def __exit__(
            self,
            exc_type: Type[BaseException] | None,
            _exc_value: BaseException | None,
            traceback: TracebackType | None
        ) -> None:
        # Se ejecuta siempre al cierre de la operación; en caso de éxito hace commit, sino hace rollback.
        if exc_type:
            self.connection.rollback()
        else:
            self.connection.commit()

        self.cursor.close()
        self.connection.close()

    def _configure_connection(self):
        """
        Método para establecer las propiedades de una conexión.
        Por el momento, activa las restricciones de llaves foráneas.
        """
        self.connection.execute("PRAGMA foreign_keys = ON;")

    def _execute_query(
            self,
            query: str,
            params: SQLParams | None = None,
            mode: ExecuteMode | None = None
        ) -> Any:
        """
        Ejecuta una consulta SQL.

        # Params:
        - query: la consulta SQL.
        - params: los parámetros para la consulta.
        - mode: ExecuteMode.ONE para fetchone, ExecuteMode.ALL para fetchall, None para consultas tipo INSERT / UPDATE / DELETE
        """
        if params is None:
            self.cursor.execute(query)
        else:
            self.cursor.execute(query, params) # type: ignore

        match mode:
            case ExecuteMode.ONE:
                return fetch_one(self.cursor)
            case ExecuteMode.ALL:
                return fetch_all(self.cursor)
            case _:
                return {
                    "rowcount": self.cursor.rowcount,
                    "lastrowid": self.cursor.lastrowid
                }