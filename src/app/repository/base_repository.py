from db.connection import connect
from app.utils.fetch_all import fetch_all
from app.utils.fetch_one import fetch_one

class BaseRepository:
    def __enter__(self):
        # Se ejecuta al momento de abrir la conexión y crea la conexión y el cursor. Retorna el DAO
        self.connection = connect()
        self.cursor = self.connection.cursor()
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        # Se ejecuta siempre al cierre de la operación; en caso de éxito hace commit, sino hace rollback. Para finalizar cierra conexión y cursor.
        if exc_type:
            self.connection.rollback()
        else:
            self.connection.commit()
        self.cursor.close()
        self.connection.close()

    def _execute_query(self, query, params=None, mode=None):
        """
        Ejecuta una consulta SQL.

        # Params:
        - query: la consulta SQL.
        - params: los parámetros para la consulta.
        - mode: 'one' para fetchone, 'all' para fetchall, None para operaciones tipo INSERT/UPDATE/DELETE.
        """
        try:
            if params is None:
                self.cursor.execute(query)
            else:
                self.cursor.execute(query, params)

            if mode == "one":
                return fetch_one(self.cursor)
            elif mode == "all":
                return fetch_all(self.cursor)
            elif mode is None:
                return {"rowcount": self.cursor.rowcount, "lastrowid": self.cursor.lastrowid}
        except:
            raise