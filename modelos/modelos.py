from typing import Optional, List
from pydantic import BaseModel, Field

class ResponseModel(BaseModel):
    id_resultado : int
    respuesta : str

class ModificarVehiculo(BaseModel):
    ID : int
    Activo : int
class SaveCliente(BaseModel):
    Facturar_a : Optional[str] = ""
    Nombre : str
    Calle: Optional[str] = ""
    Colonia: Optional[str] = ""
    Ciudad: Optional[str] = ""
    Estado: Optional[str] = ""
    No_int : int
    Tel : str
    Cel : str
    Email : Optional[str] = ""
    RFC : Optional[str] = ""
    Id_empleado: int

class GetCliente(SaveCliente):
    ID : int

class SaveOrden(BaseModel):
    ID : int
    No_orden : int
    Fecha_recepcion : str
    Fecha_entrega : str
    Hora_de_compromiso : str
    Hora_de_entrega : str
    Motivo_de_visita : str
    Medio : str

class GetOrden(SaveOrden):
    ID : int
class VehiculoV2(BaseModel):
    ID: int
    Id_Cliente: int
    Id_Empleado: int
    Marca: str
    Modelo: str
    Color: str
    No_serie: str
    Placa: str
    Tipo: str
    Motor: str
    Kms: str
    MotorVehiculo: int
    Acumulador: int
    Espejo_retrovisor: int
    Espejo_izquierdo: int
    Espejo_derecho: int
    Antena: int
    Tapones_ruedas: int
    Radio: int
    Encendedor: int
    Gato: int
    Herramienta: int
    Llanta_refaccion: int
    Limpiadores: int
    Pintura_rayada: int
    Cristales_rotos: int
    Golpes: int
    Tapetes: int
    Extintor: int
    Tapones_gasolina: int
    Calaveras_rotas: int
    Molduras_completas: int
    MotorVehiculo_foto: List[str]
    Acumulador_foto: List[str]
    Espejo_retrovisor_foto: List[str]
    Espejo_izquierdo_foto: List[str]
    Espejo_derecho_foto: List[str]
    Antena_foto: List[str]
    Tapones_ruedas_foto: List[str]
    Radio_foto: List[str]
    Encendedor_foto: List[str]
    Gato_foto: List[str]
    Herramienta_foto: List[str]
    Llanta_refaccion_foto: List[str]
    Limpiadores_foto: List[str]
    Pintura_rayada_foto: List[str]
    Cristales_rotos_foto: List[str]
    Golpes_foto: List[str]
    Tapetes_foto: List[str]
    Extintor_foto: List[str]
    Tapones_gasolina_foto: List[str]
    Calaveras_rotas_foto: List[str]
    Molduras_completas_foto: List[str]
    MotorVehiculo_video: List[str]
    Acumulador_video: List[str]
    Espejo_retrovisor_video: List[str]
    Espejo_izquierdo_video: List[str]
    Espejo_derecho_video: List[str]
    Antena_video: List[str]
    Tapones_ruedas_video: List[str]
    Radio_video: List[str]
    Encendedor_video: List[str]
    Gato_video: List[str]
    Herramienta_video: List[str]
    Llanta_refaccion_video: List[str]
    Limpiadores_video: List[str]
    Pintura_rayada_video: List[str]
    Cristales_rotos_video: List[str]
    Golpes_video: List[str]
    Tapetes_video: List[str]
    Extintor_video: List[str]
    Tapones_gasolina_video: List[str]
    Calaveras_rotas_video: List[str]
    Molduras_completas_video: List[str]
    IdFlotilla: int
    IdOrdenServicio: int
    Activo: int
class Vehiculo(BaseModel):
    Id_Empleado: int
    Marca: str
    Modelo: str
    Color: str
    No_serie: str
    Placa: str
    Tipo: str
    Motor: str
    Kms: str
    MotorVehiculo: int
    Acumulador: int
    Espejo_retrovisor: int
    Espejo_izquierdo: int
    Espejo_derecho: int
    Antena: int
    Tapones_ruedas: int
    Radio: int
    Encendedor: int
    Gato: int
    Herramienta: int
    Llanta_refaccion: int
    Limpiadores: int
    Pintura_rayada: int
    Cristales_rotos: int
    Golpes: int
    Tapetes: int
    Extintor: int
    Tapones_gasolina: int
    Calaveras_rotas: int
    Molduras_completas: int
    Panel_instrumentos: int
    Lado_izquierdo: int
    Lado_izquierdo_inf: int
    Lado_derecho:int
    Lado_derecho_inf: int
    Tablero:int
    Guantera:int
    Consola:int
    LadoFrontal:int
    LadoTrasero:int
    Cajuela:int
    NumeroEconomico: Optional[str] = ""
    MotorVehiculo_foto: List[str]
    Acumulador_foto: List[str]
    Espejo_retrovisor_foto: List[str]
    Espejo_izquierdo_foto: List[str]
    Espejo_derecho_foto: List[str]
    Antena_foto: List[str]
    Tapones_ruedas_foto: List[str]
    Radio_foto: List[str]
    Encendedor_foto: List[str]
    Gato_foto: List[str]
    Herramienta_foto: List[str]
    Llanta_refaccion_foto: List[str]
    Limpiadores_foto: List[str]
    Pintura_rayada_foto: List[str]
    Cristales_rotos_foto: List[str]
    Golpes_foto: List[str]
    Tapetes_foto: List[str]
    Extintor_foto: List[str]
    Tapones_gasolina_foto: List[str]
    Calaveras_rotas_foto: List[str]
    Molduras_completas_foto: List[str]
    Panel_instrumentos_foto :List[str]
    Lado_izquierdo_foto: List[str]
    Lado_izquierdo_inf_foto: List[str]
    Lado_derecho_foto:List[str]
    Lado_derecho_inf_foto: List[str]
    Tablero_foto:List[str]
    Guantera_foto:List[str]
    Consola_foto:List[str]
    LadoFrontal_foto:List[str]
    LadoTrasero_foto:List[str]
    Cajuela_foto:List[str]
    NumeroEconomico_foto:List[str]
    MotorVehiculo_video: List[str]
    Acumulador_video: List[str]
    Espejo_retrovisor_video: List[str]
    Espejo_izquierdo_video: List[str]
    Espejo_derecho_video: List[str]
    Antena_video: List[str]
    Tapones_ruedas_video: List[str]
    Radio_video: List[str]
    Encendedor_video: List[str]
    Gato_video: List[str]
    Herramienta_video: List[str]
    Llanta_refaccion_video: List[str]
    Limpiadores_video: List[str]
    Pintura_rayada_video: List[str]
    Cristales_rotos_video: List[str]
    Golpes_video: List[str]
    Tapetes_video: List[str]
    Extintor_video: List[str]
    Tapones_gasolina_video: List[str]
    Calaveras_rotas_video: List[str]
    Molduras_completas_video: List[str]
    Panel_instrumentos_video :List[str]
    Lado_izquierdo_video: List[str]
    Lado_izquierdo_inf_video: List[str]
    Lado_derecho_video:List[str]
    Lado_derecho_inf_video: List[str]
    Tablero_video:List[str]
    Guantera_video:List[str]
    Consola_video:List[str]
    LadoFrontal_video:List[str]
    LadoTrasero_video:List[str]
    Cajuela_video:List[str]
    NumeroEconomico_video:List[str]
    IdFlotilla: int
    IdOrdenServicio: int
    Activo: int


class saveVehiculo(Vehiculo):
    Id_Cliente: int

class GetVehiculo(Vehiculo):
    ID : int
    Id_Cliente : int
    Id_Empleado : int
    MotorVehiculo_foto: List[str]
    Acumulador_foto: List[str]
    Espejo_retrovisor_foto: List[str]
    Espejo_izquierdo_foto: List[str]
    Espejo_derecho_foto: List[str]
    Antena_foto: List[str]
    Tapones_ruedas_foto: List[str]
    Radio_foto: List[str]
    Encendedor_foto: List[str]
    Gato_foto: List[str]
    Herramienta_foto: List[str]
    Llanta_refaccion_foto: List[str]
    Limpiadores_foto: List[str]
    Pintura_rayada_foto: List[str]
    Cristales_rotos_foto: List[str]
    Golpes_foto: List[str]
    Tapetes_foto: List[str]
    Extintor_foto: List[str]
    Tapones_gasolina_foto: List[str]
    Calaveras_rotas_foto: List[str]
    Molduras_completas_foto: List[str]
    Lado_izquierdo_foto: List[str]
    Lado_izquierdo_inf_foto: List[str]
    Lado_derecho_foto:List[str]
    Lado_derecho_inf_foto: List[str]
    Tablero_foto:List[str]
    Guantera_foto:List[str]
    Consola_foto:List[str]
    NumeroEconomico_foto:List[str]
    MotorVehiculo_video: List[str]
    Acumulador_video: List[str]
    Espejo_retrovisor_video: List[str]
    Espejo_izquierdo_video: List[str]
    Espejo_derecho_video: List[str]
    Antena_video: List[str]
    Tapones_ruedas_video: List[str]
    Radio_video: List[str]
    Encendedor_video: List[str]
    Gato_video: List[str]
    Herramienta_video: List[str]
    Llanta_refaccion_video: List[str]
    Limpiadores_video: List[str]
    Pintura_rayada_video: List[str]
    Cristales_rotos_video: List[str]
    Golpes_video: List[str]
    Tapetes_video: List[str]
    Extintor_video: List[str]
    Tapones_gasolina_video: List[str]
    Calaveras_rotas_video: List[str]
    Molduras_completas_video: List[str]
    Lado_izquierdo_video: List[str]
    Lado_izquierdo_inf_video: List[str]
    Lado_derecho_video:List[str]
    Lado_derecho_inf_video: List[str]
    Tablero_video:List[str]
    Guantera_video:List[str]
    Consola_video:List[str]
    NumeroEconomico:List[str]
    IdFlotilla: int
    IdOrdenServicio: int
    Activo: int


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: Optional[str] = None
class DatosLogin(BaseModel):
    usuario: str = Field(
        ...,
        min_length=1
    )
    contrasena: str = Field(
        ...,
        min_length=1
    )

class OrdenCompleta(Vehiculo, SaveOrden, SaveCliente):
    Id_empleado: int

class Roles(BaseModel):
    Id_Rol: int
    Descripcion: str
    Estatus: int

class Estatus(BaseModel):
    Id_Estatus: int
    Descripcion: str

class SaveUsuario(BaseModel):
    Nombre: str
    Password: str
    Rol: int
    Estatus: int

class ImageData(BaseModel):
    tags: List[str]
    description: List[str]
class OrdenServicio(BaseModel):
        IdOrden:int
        IdCliente:int
        IdEmpleado:int
class SaveOrdenServicio(OrdenServicio):
    Nombre:str
    Calle:str
    Colonia:str
    Ciudad:str
    Estado:str
    Tel:str
    Cel:str
    Email:str
    RFC:str
    No_int:str
    Usuario:str
    Facturar_a:str
    Marca:str
    Modelo:str
    Color:str
    No_serie:str
    Placa:str
    Tipo:str
    Motor:str
    Kms:str
    Espejo_retrovisor:str
    Espejo_izquierdo:str
    Antena:str
    Tapones_ruedas:str
    Radio:str
    Encendedor:str
    Gato:str
    Herramienta:str
    Llanta_refaccion:str
    Limpiadores:str
    Pintura_rayada:str
    Cristales_rotos:str
    Golpes:str
    Tapetes:str
    Extintor:str
    Tapones_gasolina:str
    Calaveras_rotas:str
    Molduras_completas:str
class OrdenService(BaseModel):
    IdCliente:int
    IdEmpleado:int
class Empleado(BaseModel):
    Idusuario: int
    Nombre: str
    Rol: int
    Estatus: int

class CheckListHistorico(BaseModel):
    IdChecklist: int
    IdVehiculo: int
    IdEmpleado: int
    Fecha: str
    TiempoTranscurrido: int
    Estado :str

class Flotillas(BaseModel):
    IdFlotilla: int
    NamesFlotillas: str
    Encargado: str

class Checklist(BaseModel):
    lectura_codigos: Optional[int] = None
    lectura_codigos_observacion: Optional[str] = None
    lectura_codigos_foto: Optional[str] = None

    servofreno: Optional[int] = None
    servofreno_observacion: Optional[str] = None
    servofreno_foto: Optional[str] = None

    pedal_freno: Optional[int] = None
    pedal_freno_observacion: Optional[str] = None
    pedal_freno_foto: Optional[str] = None

    pedal_estacionamiento: Optional[int] = None
    pedal_estacionamiento_observacion: Optional[str] = None
    pedal_estacionamiento_foto: Optional[str] = None

    cinturon_seguridad: Optional[int] = None
    cinturon_seguridad_observacion: Optional[str] = None
    cinturon_seguridad_foto: Optional[str] = None

    cuadro_instrumentos: Optional[int] = None
    cuadro_instrumentos_observacion: Optional[str] = None
    cuadro_instrumentos_foto: Optional[str] = None

    aire_acondicionado: Optional[int] = None
    aire_acondicionado_observacion: Optional[str] = None
    aire_acondicionado_foto: Optional[str] = None

    bocina_claxon: Optional[int] = None
    bocina_claxon_observacion: Optional[str] = None
    bocina_claxon_foto: Optional[str] = None

    iluminacion_interior: Optional[int] = None
    iluminacion_interior_observacion: Optional[str] = None
    iluminacion_interior_foto: Optional[str] = None

    iluminacion_externa: Optional[int] = None
    iluminacion_externa_observacion: Optional[str] = None
    iluminacion_externa_foto: Optional[str] = None

    limpiaparabrisas: Optional[int] = None
    limpiaparabrisas_observacion: Optional[str] = None
    limpiaparabrisas_foto: Optional[str] = None

    limpia_medallon: Optional[int] = None
    limpia_medallon_observacion: Optional[str] = None
    limpia_medallon_foto: Optional[str] = None

    neumaticos_friccion: Optional[int] = None
    neumaticos_friccion_observacion: Optional[str] = None
    neumaticos_friccion_foto: Optional[str] = None

    otros_vehiculo_en_piso: Optional[int] = None
    otros_vehiculo_en_piso_observacion: Optional[str] = None
    otros_vehiculo_en_piso_foto: Optional[str] = None

    estado_fugas_aceite: Optional[int] = None
    estado_fugas_aceite_observacion: Optional[str] = None
    estado_fugas_aceite_foto: Optional[str] = None

    estado_nivel_calidad_lubricante_transmision: Optional[int] = None
    estado_nivel_calidad_lubricante_transmision_observacion: Optional[str] = None
    estado_nivel_calidad_lubricante_transmision_foto: Optional[str] = None

    estado_nivel_calidad_lubricante_diferencial: Optional[int] = None
    estado_nivel_calidad_lubricante_diferencial_observacion: Optional[str] = None
    estado_nivel_calidad_lubricante_diferencial_foto: Optional[str] = None

    cubrepolvos_flechas: Optional[int] = None
    cubrepolvos_flechas_observacion: Optional[str] = None
    cubrepolvos_flechas_foto: Optional[str] = None

    componentes_direccion: Optional[int] = None
    componentes_direccion_observacion: Optional[str] = None
    componentes_direccion_foto: Optional[str] = None

    componentes_suspesion: Optional[int] = None
    componentes_suspesion_observacion: Optional[str] = None
    componentes_suspesion_foto: Optional[str] = None

    sistema_escape_completo: Optional[int] = None
    sistema_escape_completo_observacion: Optional[str] = None
    sistema_escape_completo_foto: Optional[str] = None

    sistema_alimentacion_combustible: Optional[int] = None
    sistema_alimentacion_combustible_observacion: Optional[str] = None
    sistema_alimentacion_combustible_foto: Optional[str] = None

    filtro_combustible: Optional[int] = None
    filtro_combustible_observacion: Optional[str] = None
    filtro_combustible_foto: Optional[str] = None

    control_fugas_direccion_hidraulica: Optional[int] = None
    control_fugas_direccion_hidraulica_observacion: Optional[str] = None
    control_fugas_direccion_hidraulica_foto: Optional[str] = None

    otros_altura_total: Optional[int] = None
    otros_altura_total_observacion: Optional[str] = None
    otros_altura_total_foto: Optional[str] = None

    rodamiento_mazas_rueda: Optional[int] = None
    rodamiento_mazas_rueda_observacion: Optional[str] = None
    rodamiento_mazas_rueda_foto: Optional[str] = None

    holgura_partes_suspension_rueda: Optional[int] = None
    holgura_partes_suspension_rueda_observacion: Optional[str] = None
    holgura_partes_suspension_rueda_foto: Optional[str] = None

    control_neumaticos_desgaste_presion: Optional[int] = None
    control_neumaticos_desgaste_presion_observacion: Optional[str] = None
    control_neumaticos_desgaste_presion_foto: Optional[str] = None

    profundidad: Optional[int] = None
    profundidad_observacion: Optional[str] = None
    profundidad_foto: Optional[str] = None

    presion: Optional[int] = None
    presion_observacion: Optional[str] = None
    presion_foto: Optional[str] = None

    otros_altura_media: Optional[int] = None
    otros_altura_media_observacion: Optional[str] = None
    otros_altura_media_foto: Optional[str] = None

    nivel_calidad_aceite_motor: Optional[int] = None
    nivel_calidad_aceite_motor_observacion: Optional[str] = None
    nivel_calidad_aceite_motor_foto: Optional[str] = None

    filtro_aire: Optional[int] = None
    filtro_aire_observacion: Optional[str] = None
    filtro_aire_foto: Optional[str] = None

    filtro_polen: Optional[int] = None
    filtro_polen_observacion: Optional[str] = None
    filtro_polen_foto: Optional[str] = None

    filtro_pcv: Optional[int] = None
    filtro_pcv_observacion: Optional[str] = None
    filtro_pcv_foto: Optional[str] = None

    valvula_pcv: Optional[int] = None
    valvula_pcv_observacion: Optional[str] = None
    valvula_pcv_foto: Optional[str] = None

    bujias_encendido: Optional[int] = None
    bujias_encendido_observacion: Optional[str] = None
    bujias_encendido_foto: Optional[str] = None

    cables_bujias_bobinas_ignicion: Optional[int] = None
    cables_bujias_bobinas_ignicion_observacion: Optional[str] = None
    cables_bujias_bobinas_ignicion_foto: Optional[str] = None

    nivel_anticongenlante: Optional[int] = None
    nivel_anticongenlante_observacion: Optional[str] = None
    nivel_anticongenlante_foto: Optional[str] = None

    tapon_radiador: Optional[int] = None
    tapon_radiador_observacion: Optional[str] = None
    tapon_radiador_foto: Optional[str] = None

    mangueras_sistema: Optional[int] = None
    mangueras_sistema_observacion: Optional[str] = None
    mangueras_sistema_foto: Optional[str] = None

    desempeño_ventilador: Optional[int] = None
    desempeño_ventilador_observacion: Optional[str] = None
    desempeño_ventilador_foto: Optional[str] = None

    calidad_liquido_limpiaparabrisas: Optional[int] = None
    calidad_liquido_limpiaparabrisas_observacion: Optional[str] = None
    calidad_liquido_limpiaparabrisas_foto: Optional[str] = None

    calidad_aceite_direccion_hidraulica: Optional[int] = None
    calidad_aceite_direccion_hidraulica_observacion: Optional[str] = None
    calidad_aceite_direccion_hidraulica_foto: Optional[str] = None

    calidad_aceite_transmision_bayoneta: Optional[int] = None
    calidad_aceite_transmision_bayoneta_observacion: Optional[str] = None
    calidad_aceite_transmision_bayoneta_foto: Optional[str] = None

    liquido_bateria_condiciones: Optional[int] = None
    liquido_bateria_condiciones_observacion: Optional[str] = None
    liquido_bateria_condiciones_foto: Optional[str] = None

    bandas_poly_v: Optional[int] = None
    bandas_poly_v_observacion: Optional[str] = None
    bandas_poly_v_foto: Optional[str] = None

    poleas_banda: Optional[int] = None
    poleas_banda_observacion: Optional[str] = None
    poleas_banda_foto: Optional[str] = None

    banda_tiempo: Optional[int] = None
    banda_tiempo_observacion: Optional[str] = None
    banda_tiempo_foto: Optional[str] = None

    otros_habitaculo_motor: Optional[int] = None
    otros_habitaculo_motor_observacion: Optional[str] = None
    otros_habitaculo_motor_foto: Optional[str] = None

    reset_intervalo_servicio: Optional[int] = None
    reset_intervalo_servicio_observacion: Optional[str] = None
    reset_intervalo_servicio_foto: Optional[str] = None

    ajuste_tornillos_neumaticos_torquimetro: Optional[int] = None
    ajuste_tornillos_neumaticos_torquimetro_observacion: Optional[str] = None
    ajuste_tornillos_neumaticos_torquimetro_foto: Optional[str] = None

    limpiar_libricar_puertas_cerraduras: Optional[int] = None
    limpiar_libricar_puertas_cerraduras_observacion: Optional[str] = None
    limpiar_libricar_puertas_cerraduras_foto: Optional[str] = None

    completar_plan_mantenimiento: Optional[int] = None
    completar_plan_mantenimiento_observacion: Optional[str] = None
    completar_plan_mantenimiento_foto: Optional[str] = None

    Fecha: str
    IdEmpleado: Optional[int] = None
    IdVehiculo: Optional[int] = None
    Id_ordendeservicio: Optional[int] = None
    NumeroSerie: str
    TiempoTranscurrido: str
    id: Optional[int] = None
    id_checklist: Optional[int] = None
    Activo: Optional[int] = None
    #NuevasVariables

class Tecnicos(BaseModel):
    IdUsuario : int
    Nombre : str
    Estatus : int

class AsignarOrden(BaseModel):
    IdOrden : int
    IdTecnico : int

class ReporteVentas(BaseModel):
    Id: Optional[int] = None  # Haciendo que Id sea opcional
    date: str
    service_order_id: int
    vehicle_id: int
    credit: Optional[str] = None
    initial_service: Optional[str] = None
    finalized: int
    reception: bool
    entry: bool
    repair: bool
    checklist: bool
    technician: Optional[str] = None
    quotation: bool
    authorization: bool
    additional: bool
    washing: bool
    delivery: bool
    comments: Optional[str] = None