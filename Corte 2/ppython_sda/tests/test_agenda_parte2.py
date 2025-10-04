import pytest
import json
import tempfile
import os
from typing import Dict, Any, List
from datetime import datetime


class AgendaContactosParte2:
    """Agenda de contactos usando diccionarios anidados"""
    
    def __init__(self):
        self.agenda = {}
        self.campos_requeridos = {'telefono', 'email', 'direccion'}
        self.campos_opcionales = {'edad', 'profesion', 'ciudad', 'empresa', 'notas'}
        self.estadisticas = {
            'total_contactos': 0,
            'operaciones_lectura': 0,
            'operaciones_escritura': 0,
            'ultima_modificacion': None
        }
    
    def agregar_contacto(self, nombre: str, datos: Dict[str, Any]) -> bool:
        if not nombre or not isinstance(nombre, str):
            return False
            
        if not all(campo in datos for campo in self.campos_requeridos):
            missing = self.campos_requeridos - set(datos.keys())
            raise ValueError(f"Faltan campos requeridos: {missing}")
        
        if nombre in self.agenda:
            return False
            
        contacto_datos = {}
        campos_validos = self.campos_requeridos | self.campos_opcionales
        
        for campo, valor in datos.items():
            if campo in campos_validos:
                contacto_datos[campo] = valor
        
        self.agenda[nombre] = contacto_datos
        self.estadisticas['total_contactos'] += 1
        self.estadisticas['operaciones_escritura'] += 1
        self._actualizar_timestamp()
        return True
    
    def obtener_contacto(self, nombre: str):
        self.estadisticas['operaciones_lectura'] += 1
        return self.agenda.get(nombre)
    
    def obtener_campo(self, nombre: str, campo: str):
        self.estadisticas['operaciones_lectura'] += 1
        contacto = self.agenda.get(nombre)
        if contacto:
            return contacto.get(campo)
        return None
    
    def actualizar_contacto(self, nombre: str, **campos) -> bool:
        if nombre not in self.agenda:
            return False
            
        campos_validos = self.campos_requeridos | self.campos_opcionales
        
        for campo, valor in campos.items():
            if campo in campos_validos:
                self.agenda[nombre][campo] = valor
        
        self.estadisticas['operaciones_escritura'] += 1
        self._actualizar_timestamp()
        return True
    
    def actualizar_campo(self, nombre: str, campo: str, valor: Any) -> bool:
        return self.actualizar_contacto(nombre, **{campo: valor})
    
    def eliminar_contacto(self, nombre: str) -> bool:
        if nombre in self.agenda:
            del self.agenda[nombre]
            self.estadisticas['total_contactos'] -= 1
            self.estadisticas['operaciones_escritura'] += 1
            self._actualizar_timestamp()
            return True
        return False
    
    def eliminar_campo(self, nombre: str, campo: str) -> bool:
        if nombre in self.agenda and campo in self.agenda[nombre]:
            if campo in self.campos_requeridos:
                return False
            del self.agenda[nombre][campo]
            self.estadisticas['operaciones_escritura'] += 1
            self._actualizar_timestamp()
            return True
        return False
    
    def buscar_por_campo(self, campo: str, valor: Any, exacto: bool = True) -> List[str]:
        self.estadisticas['operaciones_lectura'] += 1
        resultados = []
        
        for nombre, datos in self.agenda.items():
            if campo in datos:
                valor_contacto = datos[campo]
                if exacto:
                    if valor_contacto == valor:
                        resultados.append(nombre)
                else:
                    if (isinstance(valor_contacto, str) and isinstance(valor, str) and
                        valor.lower() in valor_contacto.lower()):
                        resultados.append(nombre)
        
        return resultados
    
    def listar_contactos(self, ordenar_por: str = 'nombre') -> List[tuple]:
        self.estadisticas['operaciones_lectura'] += 1
        
        if ordenar_por == 'nombre':
            return [(nombre, datos) for nombre, datos in sorted(self.agenda.items())]
        else:
            contactos = []
            for nombre, datos in self.agenda.items():
                valor_orden = datos.get(ordenar_por, '')
                contactos.append((valor_orden, nombre, datos))
            
            contactos.sort(key=lambda x: x[0])
            return [(nombre, datos) for _, nombre, datos in contactos]
    
    def obtener_campos_disponibles(self) -> Dict[str, int]:
        self.estadisticas['operaciones_lectura'] += 1
        campos_count = {}
        
        for datos in self.agenda.values():
            for campo in datos.keys():
                campos_count[campo] = campos_count.get(campo, 0) + 1
        
        return campos_count
    
    def _actualizar_timestamp(self):
        self.estadisticas['ultima_modificacion'] = datetime.now().isoformat()
    
    def obtener_estadisticas(self) -> Dict[str, Any]:
        return {
            **self.estadisticas,
            'contactos_actuales': len(self.agenda),
            'campos_disponibles': self.obtener_campos_disponibles(),
            'memoria_estimada_kb': len(str(self.agenda)) / 1024
        }
    
    def __len__(self) -> int:
        return len(self.agenda)
    
    def __contains__(self, nombre: str) -> bool:
        return nombre in self.agenda


# Tests básicos para AgendaContactosParte2
def test_agregar_contacto_basico():
    """Prueba agregar contacto básico"""
    agenda = AgendaContactosParte2()
    datos = {
        'telefono': '123456789',
        'email': 'ana@email.com',
        'direccion': 'Calle Mayor 1'
    }
    
    assert agenda.agregar_contacto('Ana García', datos) == True
    assert len(agenda) == 1
    assert 'Ana García' in agenda


def test_agregar_contacto_campos_faltantes():
    """Prueba agregar contacto con campos faltantes"""
    agenda = AgendaContactosParte2()
    datos_incompletos = {
        'telefono': '123456789',
        'email': 'ana@email.com'
        # Falta 'direccion'
    }
    
    with pytest.raises(ValueError):
        agenda.agregar_contacto('Ana García', datos_incompletos)


def test_agregar_contacto_duplicado():
    """Prueba agregar contacto duplicado"""
    agenda = AgendaContactosParte2()
    datos = {
        'telefono': '123456789',
        'email': 'ana@email.com',
        'direccion': 'Calle Mayor 1'
    }
    
    assert agenda.agregar_contacto('Ana García', datos) == True
    assert agenda.agregar_contacto('Ana García', datos) == False
    assert len(agenda) == 1


def test_obtener_contacto_completo():
    """Prueba obtener contacto completo"""
    agenda = AgendaContactosParte2()
    datos = {
        'telefono': '987654321',
        'email': 'pedro@email.com',
        'direccion': 'Av. Principal 2',
        'edad': 30,
        'profesion': 'Ingeniero'
    }
    
    agenda.agregar_contacto('Pedro López', datos)
    
    contacto = agenda.obtener_contacto('Pedro López')
    assert contacto is not None
    assert contacto['telefono'] == '987654321'
    assert contacto['edad'] == 30
    assert contacto['profesion'] == 'Ingeniero'


def test_obtener_campo_especifico():
    """Prueba obtener campo específico"""
    agenda = AgendaContactosParte2()
    datos = {
        'telefono': '555666777',
        'email': 'maria@email.com',
        'direccion': 'Plaza Central 3',
        'ciudad': 'Madrid'
    }
    
    agenda.agregar_contacto('María Rodríguez', datos)
    
    assert agenda.obtener_campo('María Rodríguez', 'email') == 'maria@email.com'
    assert agenda.obtener_campo('María Rodríguez', 'ciudad') == 'Madrid'
    assert agenda.obtener_campo('María Rodríguez', 'campo_inexistente') is None
    assert agenda.obtener_campo('Contacto Inexistente', 'email') is None


def test_actualizar_contacto_multiple():
    """Prueba actualizar múltiples campos"""
    agenda = AgendaContactosParte2()
    datos = {
        'telefono': '111222333',
        'email': 'luis@email.com',
        'direccion': 'Calle Test 1'
    }
    
    agenda.agregar_contacto('Luis Martín', datos)
    
    assert agenda.actualizar_contacto('Luis Martín', edad=25, ciudad='Madrid', profesion='Doctor') == True
    
    contacto = agenda.obtener_contacto('Luis Martín')
    assert contacto['edad'] == 25
    assert contacto['ciudad'] == 'Madrid'
    assert contacto['profesion'] == 'Doctor'
    assert contacto['telefono'] == '111222333'  # Campo original mantenido


def test_actualizar_campo_individual():
    """Prueba actualizar campo individual"""
    agenda = AgendaContactosParte2()
    datos = {
        'telefono': '444555666',
        'email': 'carmen@email.com',
        'direccion': 'Av. Test 2'
    }
    
    agenda.agregar_contacto('Carmen Sánchez', datos)
    
    assert agenda.actualizar_campo('Carmen Sánchez', 'edad', 28) == True
    assert agenda.obtener_campo('Carmen Sánchez', 'edad') == 28
    
    # Intentar actualizar contacto inexistente
    assert agenda.actualizar_campo('No Existe', 'edad', 30) == False


def test_eliminar_contacto():
    """Prueba eliminar contacto completo"""
    agenda = AgendaContactosParte2()
    datos = {
        'telefono': '777888999',
        'email': 'test@email.com',
        'direccion': 'Test Address'
    }
    
    agenda.agregar_contacto('Test User', datos)
    assert len(agenda) == 1
    
    assert agenda.eliminar_contacto('Test User') == True
    assert len(agenda) == 0
    assert agenda.eliminar_contacto('No Existe') == False


def test_eliminar_campo():
    """Prueba eliminar campo específico"""
    agenda = AgendaContactosParte2()
    datos = {
        'telefono': '111111111',
        'email': 'test2@email.com',
        'direccion': 'Test Address 2',
        'edad': 40,
        'profesion': 'Tester'
    }
    
    agenda.agregar_contacto('Test User 2', datos)
    
    # Eliminar campo opcional
    assert agenda.eliminar_campo('Test User 2', 'edad') == True
    assert agenda.obtener_campo('Test User 2', 'edad') is None
    
    # Intentar eliminar campo requerido (debería fallar)
    assert agenda.eliminar_campo('Test User 2', 'telefono') == False
    assert agenda.obtener_campo('Test User 2', 'telefono') == '111111111'
    
    # Intentar eliminar campo de contacto inexistente
    assert agenda.eliminar_campo('No Existe', 'edad') == False


def test_buscar_por_campo_exacto():
    """Prueba búsqueda exacta por campo"""
    agenda = AgendaContactosParte2()
    
    contactos = [
        ('Ana García', {'telefono': '111', 'email': 'ana@test.com', 'direccion': 'Madrid', 'profesion': 'Ingeniera'}),
        ('Luis Martín', {'telefono': '222', 'email': 'luis@test.com', 'direccion': 'Barcelona', 'profesion': 'Doctor'}),
        ('Pedro Sánchez', {'telefono': '333', 'email': 'pedro@test.com', 'direccion': 'Madrid', 'profesion': 'Profesor'})
    ]
    
    for nombre, datos in contactos:
        agenda.agregar_contacto(nombre, datos)
    
    # Búsqueda exacta por dirección
    resultados_madrid = agenda.buscar_por_campo('direccion', 'Madrid', exacto=True)
    assert len(resultados_madrid) == 2
    assert 'Ana García' in resultados_madrid
    assert 'Pedro Sánchez' in resultados_madrid
    
    # Búsqueda exacta por profesión
    resultados_doctor = agenda.buscar_por_campo('profesion', 'Doctor', exacto=True)
    assert len(resultados_doctor) == 1
    assert 'Luis Martín' in resultados_doctor


def test_buscar_por_campo_parcial():
    """Prueba búsqueda parcial por campo"""
    agenda = AgendaContactosParte2()
    
    contactos = [
        ('Ana García', {'telefono': '111', 'email': 'ana@empresa.com', 'direccion': 'Madrid'}),
        ('Luis Martín', {'telefono': '222', 'email': 'luis@corporacion.com', 'direccion': 'Barcelona'}),
        ('Pedro Sánchez', {'telefono': '333', 'email': 'pedro@empresa.com', 'direccion': 'Valencia'})
    ]
    
    for nombre, datos in contactos:
        agenda.agregar_contacto(nombre, datos)
    
    # Búsqueda parcial por email
    resultados_empresa = agenda.buscar_por_campo('email', 'empresa', exacto=False)
    assert len(resultados_empresa) == 2
    assert 'Ana García' in resultados_empresa
    assert 'Pedro Sánchez' in resultados_empresa


def test_listar_contactos_ordenados():
    """Prueba listar contactos ordenados"""
    agenda = AgendaContactosParte2()
    
    contactos = [
        ('Carlos Pérez', {'telefono': '111', 'email': 'carlos@test.com', 'direccion': 'Madrid', 'edad': 30}),
        ('Ana García', {'telefono': '222', 'email': 'ana@test.com', 'direccion': 'Barcelona', 'edad': 25}),
        ('Bruno López', {'telefono': '333', 'email': 'bruno@test.com', 'direccion': 'Valencia', 'edad': 35})
    ]
    
    for nombre, datos in contactos:
        agenda.agregar_contacto(nombre, datos)
    
    # Ordenar por nombre (default)
    lista_nombre = agenda.listar_contactos('nombre')
    nombres_ordenados = [nombre for nombre, _ in lista_nombre]
    assert nombres_ordenados == ['Ana García', 'Bruno López', 'Carlos Pérez']
    
    # Ordenar por edad
    lista_edad = agenda.listar_contactos('edad')
    edades_ordenadas = [datos['edad'] for _, datos in lista_edad]
    assert edades_ordenadas == [25, 30, 35]


def test_obtener_campos_disponibles():
    """Prueba obtener estadísticas de campos"""
    agenda = AgendaContactosParte2()
    
    contactos = [
        ('Ana', {'telefono': '111', 'email': 'ana@test.com', 'direccion': 'Madrid', 'edad': 25}),
        ('Luis', {'telefono': '222', 'email': 'luis@test.com', 'direccion': 'Barcelona', 'profesion': 'Doctor'}),
        ('Pedro', {'telefono': '333', 'email': 'pedro@test.com', 'direccion': 'Valencia', 'edad': 30, 'profesion': 'Profesor'})
    ]
    
    for nombre, datos in contactos:
        agenda.agregar_contacto(nombre, datos)
    
    campos = agenda.obtener_campos_disponibles()
    
    # Campos que aparecen en todos los contactos
    assert campos['telefono'] == 3
    assert campos['email'] == 3
    assert campos['direccion'] == 3
    
    # Campos que aparecen en algunos contactos
    assert campos['edad'] == 2
    assert campos['profesion'] == 2


def test_estadisticas():
    """Prueba obtener estadísticas de la agenda"""
    agenda = AgendaContactosParte2()
    
    # Estado inicial
    stats_inicial = agenda.obtener_estadisticas()
    assert stats_inicial['total_contactos'] == 0
    assert stats_inicial['operaciones_lectura'] == 1  # La llamada a obtener_campos_disponibles
    assert stats_inicial['operaciones_escritura'] == 0
    assert stats_inicial['contactos_actuales'] == 0
    
    # Agregar contacto
    datos = {'telefono': '123456789', 'email': 'test@email.com', 'direccion': 'Test Address'}
    agenda.agregar_contacto('Test User', datos)
    
    stats_despues = agenda.obtener_estadisticas()
    assert stats_despues['total_contactos'] == 1
    assert stats_despues['operaciones_escritura'] == 1
    assert stats_despues['contactos_actuales'] == 1
    assert stats_despues['ultima_modificacion'] is not None
    
    # Realizar búsqueda
    agenda.obtener_contacto('Test User')
    
    stats_final = agenda.obtener_estadisticas()
    assert stats_final['operaciones_lectura'] > stats_despues['operaciones_lectura']


def test_metodos_especiales():
    """Prueba métodos especiales (__len__, __contains__)"""
    agenda = AgendaContactosParte2()
    
    assert len(agenda) == 0
    assert 'Ana García' not in agenda
    
    datos = {'telefono': '123456789', 'email': 'ana@email.com', 'direccion': 'Test Address'}
    agenda.agregar_contacto('Ana García', datos)
    
    assert len(agenda) == 1
    assert 'Ana García' in agenda
    assert 'Pedro López' not in agenda


def test_validacion_nombre_vacio():
    """Prueba validación de nombre vacío o inválido"""
    agenda = AgendaContactosParte2()
    datos = {'telefono': '123456789', 'email': 'test@email.com', 'direccion': 'Test Address'}
    
    # Nombre vacío
    assert agenda.agregar_contacto('', datos) == False
    assert agenda.agregar_contacto(None, datos) == False
    
    # Tipo incorrecto para nombre
    assert agenda.agregar_contacto(123, datos) == False


def test_campos_invalidos_ignorados():
    """Prueba que campos inválidos son ignorados"""
    agenda = AgendaContactosParte2()
    datos = {
        'telefono': '123456789',
        'email': 'test@email.com',
        'direccion': 'Test Address',
        'campo_valido': 'profesion',  # Este debería ser ignorado
        'edad': 25,  # Este es válido
        'campo_invalido': 'valor'  # Este debería ser ignorado
    }
    
    agenda.agregar_contacto('Test User', datos)
    contacto = agenda.obtener_contacto('Test User')
    
    # Campos requeridos deben estar
    assert 'telefono' in contacto
    assert 'email' in contacto
    assert 'direccion' in contacto
    
    # Campo opcional válido debe estar
    assert 'edad' in contacto
    
    # Campos inválidos no deben estar
    assert 'campo_valido' not in contacto
    assert 'campo_invalido' not in contacto