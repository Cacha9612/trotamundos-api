from datos import Datos


class Negocios:
    async def getusuario(self, payload):
        _datos = Datos()
        user_list = await _datos.inicio_sesion(payload)
        if user_list and len(user_list) > 0:
            return user_list[0]  # Retorna el primer usuario si hay resultados
        return None  # Devuelve None si no hay usuarios