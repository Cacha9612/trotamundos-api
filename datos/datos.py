from sqlalchemy import text
from database import engine
import pandas as pd  # Importa Pandas
from modelos import DatosLogin
from utils import utilsclass
from loguru import logger

class Datos():
    async def inicio_sesion(self, payload: DatosLogin):
        conn = engine.connect()
        query = f"select * from seguridad.Usuarios where nombre = '{payload.usuario}'"
        try:
            roles_df = pd.read_sql(query, engine)
            result = roles_df.to_dict(orient="records")
            if(len(result) == 0):
                return False
            hashed_password = result[0]['Password']
            if not await utilsclass.verify_password(payload.contrasena, hashed_password):
                return False
            return result
        except Exception as error:
            logger.error(error)
        finally:
            conn.close()
        pass