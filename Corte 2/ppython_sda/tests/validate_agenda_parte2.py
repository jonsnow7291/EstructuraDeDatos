#!/usr/bin/env python3
"""
Script de validación completa para AgendaContactosParte2
Ejecuta todas las pruebas sin dependencias externas
"""

import sys
import traceback
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


def assert_equal(actual, expected, message=""):
    """Helper para aserciones"""
    if actual != expected:
        raise AssertionError(f"{message}: Expected {expected}, got {actual}")


def assert_true(condition, message=""):
    """Helper para aserciones booleanas"""
    if not condition:
        raise AssertionError(f"{message}: Expected True, got False")


def assert_false(condition, message=""):
    """Helper para aserciones booleanas negativas"""
    if condition:
        raise AssertionError(f"{message}: Expected False, got True")


def assert_is_none(value, message=""):
    """Helper para verificar None"""
    if value is not None:
        raise AssertionError(f"{message}: Expected None, got {value}")


def assert_is_not_none(value, message=""):
    """Helper para verificar no None"""
    if value is None:
        raise AssertionError(f"{message}: Expected not None, got None")


def assert_in(item, container, message=""):
    """Helper para verificar pertenencia"""
    if item not in container:
        raise AssertionError(f"{message}: {item} not found in {container}")


def assert_not_in(item, container, message=""):
    """Helper para verificar no pertenencia"""
    if item in container:
        raise AssertionError(f"{message}: {item} found in {container}")


def run_test(test_func, test_name):
    """Ejecutar una prueba individual"""
    try:
        test_func()
        print(f"  ✓ PASS {test_name}")
        return True
    except Exception as e:
        print(f"  ✗ FAIL {test_name}")
        print(f"    Error: {str(e)}")
        return False


def test_agregar_contacto_basico():
    """Prueba agregar contacto básico"""
    agenda = AgendaContactosParte2()
    datos = {
        'telefono': '123456789',
        'email': 'ana@email.com',
        'direccion': 'Calle Mayor 1'
    }
    
    assert_true(agenda.agregar_contacto('Ana García', datos), "Debería agregar contacto válido")
    assert_equal(len(agenda), 1, "Longitud de agenda debería ser 1")
    assert_in('Ana García', agenda, "Ana García debería estar en la agenda")


def test_agregar_contacto_campos_faltantes():
    """Prueba agregar contacto con campos faltantes"""
    agenda = AgendaContactosParte2()
    datos_incompletos = {
        'telefono': '123456789',
        'email': 'ana@email.com'
        # Falta 'direccion'
    }
    
    try:
        agenda.agregar_contacto('Ana García', datos_incompletos)
        assert_true(False, "Debería haber lanzado ValueError")
    except ValueError:
        pass  # Comportamiento esperado


def test_agregar_contacto_duplicado():
    """Prueba agregar contacto duplicado"""
    agenda = AgendaContactosParte2()
    datos = {
        'telefono': '123456789',
        'email': 'ana@email.com',
        'direccion': 'Calle Mayor 1'
    }
    
    assert_true(agenda.agregar_contacto('Ana García', datos), "Primer contacto debería agregarse")
    assert_false(agenda.agregar_contacto('Ana García', datos), "Contacto duplicado no debería agregarse")
    assert_equal(len(agenda), 1, "Solo debería haber un contacto")


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
    assert_is_not_none(contacto, "Contacto debería existir")
    assert_equal(contacto['telefono'], '987654321', "Teléfono incorrecto")
    assert_equal(contacto['edad'], 30, "Edad incorrecta")
    assert_equal(contacto['profesion'], 'Ingeniero', "Profesión incorrecta")


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
    
    assert_equal(agenda.obtener_campo('María Rodríguez', 'email'), 'maria@email.com', "Email incorrecto")
    assert_equal(agenda.obtener_campo('María Rodríguez', 'ciudad'), 'Madrid', "Ciudad incorrecta")
    assert_is_none(agenda.obtener_campo('María Rodríguez', 'campo_inexistente'), "Campo inexistente debería ser None")
    assert_is_none(agenda.obtener_campo('Contacto Inexistente', 'email'), "Contacto inexistente debería retornar None")


def test_actualizar_contacto_multiple():
    """Prueba actualizar múltiples campos"""
    agenda = AgendaContactosParte2()
    datos = {
        'telefono': '111222333',
        'email': 'luis@email.com',
        'direccion': 'Calle Test 1'
    }
    
    agenda.agregar_contacto('Luis Martín', datos)
    
    assert_true(agenda.actualizar_contacto('Luis Martín', edad=25, ciudad='Madrid', profesion='Doctor'),
               "Actualización debería ser exitosa")
    
    contacto = agenda.obtener_contacto('Luis Martín')
    assert_equal(contacto['edad'], 25, "Edad no actualizada")
    assert_equal(contacto['ciudad'], 'Madrid', "Ciudad no actualizada")
    assert_equal(contacto['profesion'], 'Doctor', "Profesión no actualizada")
    assert_equal(contacto['telefono'], '111222333', "Campo original debería mantenerse")


def test_eliminar_contacto():
    """Prueba eliminar contacto completo"""
    agenda = AgendaContactosParte2()
    datos = {
        'telefono': '777888999',
        'email': 'test@email.com',
        'direccion': 'Test Address'
    }
    
    agenda.agregar_contacto('Test User', datos)
    assert_equal(len(agenda), 1, "Debería haber un contacto")
    
    assert_true(agenda.eliminar_contacto('Test User'), "Eliminación debería ser exitosa")
    assert_equal(len(agenda), 0, "No debería haber contactos")
    assert_false(agenda.eliminar_contacto('No Existe'), "No debería poder eliminar contacto inexistente")


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
    assert_true(agenda.eliminar_campo('Test User 2', 'edad'), "Debería poder eliminar campo opcional")
    assert_is_none(agenda.obtener_campo('Test User 2', 'edad'), "Campo eliminado debería ser None")
    
    # Intentar eliminar campo requerido (debería fallar)
    assert_false(agenda.eliminar_campo('Test User 2', 'telefono'), "No debería poder eliminar campo requerido")
    assert_equal(agenda.obtener_campo('Test User 2', 'telefono'), '111111111', "Campo requerido debería mantenerse")


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
    assert_equal(len(resultados_madrid), 2, "Debería encontrar 2 contactos en Madrid")
    assert_in('Ana García', resultados_madrid, "Ana García debería estar en los resultados")
    assert_in('Pedro Sánchez', resultados_madrid, "Pedro Sánchez debería estar en los resultados")


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
    assert_equal(len(resultados_empresa), 2, "Debería encontrar 2 contactos con 'empresa' en email")
    assert_in('Ana García', resultados_empresa, "Ana García debería estar en los resultados")
    assert_in('Pedro Sánchez', resultados_empresa, "Pedro Sánchez debería estar en los resultados")


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
    assert_equal(nombres_ordenados, ['Ana García', 'Bruno López', 'Carlos Pérez'], "Orden por nombre incorrecto")
    
    # Ordenar por edad
    lista_edad = agenda.listar_contactos('edad')
    edades_ordenadas = [datos['edad'] for _, datos in lista_edad]
    assert_equal(edades_ordenadas, [25, 30, 35], "Orden por edad incorrecto")


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
    assert_equal(campos['telefono'], 3, "Teléfono debería aparecer en 3 contactos")
    assert_equal(campos['email'], 3, "Email debería aparecer en 3 contactos")
    assert_equal(campos['direccion'], 3, "Dirección debería aparecer en 3 contactos")
    
    # Campos que aparecen en algunos contactos
    assert_equal(campos['edad'], 2, "Edad debería aparecer en 2 contactos")
    assert_equal(campos['profesion'], 2, "Profesión debería aparecer en 2 contactos")


def test_estadisticas():
    """Prueba obtener estadísticas de la agenda"""
    agenda = AgendaContactosParte2()
    
    # Agregar contacto
    datos = {'telefono': '123456789', 'email': 'test@email.com', 'direccion': 'Test Address'}
    agenda.agregar_contacto('Test User', datos)
    
    stats = agenda.obtener_estadisticas()
    assert_equal(stats['total_contactos'], 1, "Total de contactos incorrecto")
    assert_true(stats['operaciones_escritura'] >= 1, "Debería haber al menos 1 operación de escritura")
    assert_equal(stats['contactos_actuales'], 1, "Contactos actuales incorrecto")
    assert_is_not_none(stats['ultima_modificacion'], "Debería tener timestamp de modificación")


def test_metodos_especiales():
    """Prueba métodos especiales (__len__, __contains__)"""
    agenda = AgendaContactosParte2()
    
    assert_equal(len(agenda), 0, "Agenda vacía debería tener longitud 0")
    assert_not_in('Ana García', agenda, "Contacto no debería existir en agenda vacía")
    
    datos = {'telefono': '123456789', 'email': 'ana@email.com', 'direccion': 'Test Address'}
    agenda.agregar_contacto('Ana García', datos)
    
    assert_equal(len(agenda), 1, "Agenda con un contacto debería tener longitud 1")
    assert_in('Ana García', agenda, "Ana García debería estar en la agenda")
    assert_not_in('Pedro López', agenda, "Pedro López no debería estar en la agenda")


def test_validacion_nombre_vacio():
    """Prueba validación de nombre vacío o inválido"""
    agenda = AgendaContactosParte2()
    datos = {'telefono': '123456789', 'email': 'test@email.com', 'direccion': 'Test Address'}
    
    # Nombre vacío
    assert_false(agenda.agregar_contacto('', datos), "No debería aceptar nombre vacío")
    assert_false(agenda.agregar_contacto(None, datos), "No debería aceptar nombre None")
    
    # Tipo incorrecto para nombre
    assert_false(agenda.agregar_contacto(123, datos), "No debería aceptar nombre no string")


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
    assert_in('telefono', contacto, "Teléfono debería estar presente")
    assert_in('email', contacto, "Email debería estar presente")
    assert_in('direccion', contacto, "Dirección debería estar presente")
    
    # Campo opcional válido debe estar
    assert_in('edad', contacto, "Edad debería estar presente")
    
    # Campos inválidos no deben estar
    assert_not_in('campo_valido', contacto, "Campo inválido no debería estar presente")
    assert_not_in('campo_invalido', contacto, "Campo inválido no debería estar presente")


def run_all_tests():
    """Ejecuta todas las pruebas"""
    print("🧪 Ejecutando suite completa de pruebas para AgendaContactosParte2...")
    print("=" * 70)
    
    tests = [
        (test_agregar_contacto_basico, "Agregar contacto básico"),
        (test_agregar_contacto_campos_faltantes, "Validar campos faltantes"),
        (test_agregar_contacto_duplicado, "Rechazar contacto duplicado"),
        (test_obtener_contacto_completo, "Obtener contacto completo"),
        (test_obtener_campo_especifico, "Obtener campo específico"),
        (test_actualizar_contacto_multiple, "Actualizar múltiples campos"),
        (test_eliminar_contacto, "Eliminar contacto"),
        (test_eliminar_campo, "Eliminar campo específico"),
        (test_buscar_por_campo_exacto, "Búsqueda exacta por campo"),
        (test_buscar_por_campo_parcial, "Búsqueda parcial por campo"),
        (test_listar_contactos_ordenados, "Listar contactos ordenados"),
        (test_obtener_campos_disponibles, "Obtener campos disponibles"),
        (test_estadisticas, "Obtener estadísticas"),
        (test_metodos_especiales, "Métodos especiales"),
        (test_validacion_nombre_vacio, "Validar nombre vacío"),
        (test_campos_invalidos_ignorados, "Ignorar campos inválidos")
    ]
    
    passed = 0
    failed = 0
    
    for i, (test_func, test_name) in enumerate(tests, 1):
        print(f"\n📝 Test {i}: {test_name}")
        if run_test(test_func, test_name):
            passed += 1
        else:
            failed += 1
    
    # Resumen final
    print("\n" + "=" * 70)
    print("📊 RESUMEN DE PRUEBAS COMPLETAS")
    print("=" * 70)
    
    total_tests = passed + failed
    success_rate = (passed / total_tests * 100) if total_tests > 0 else 0
    
    print(f"✅ Pruebas exitosas: {passed}")
    print(f"❌ Pruebas fallidas: {failed}")
    print(f"📈 Tasa de éxito: {success_rate:.1f}%")
    
    if failed == 0:
        print("\n🎉 ¡Todas las pruebas pasaron exitosamente!")
        print("   La implementación de AgendaContactosParte2 está completamente funcional.")
        return True
    else:
        print(f"\n⚠️  Se encontraron {failed} problemas en las pruebas.")
        print("   Revisa la implementación antes de continuar.")
        return False


if __name__ == "__main__":
    print("🚀 Iniciando validación completa de AgendaContactosParte2")
    print(f"🐍 Python {sys.version}")
    print(f"📅 {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    
    success = run_all_tests()
    
    if success:
        print("\n✨ Sistema completamente validado!")
        sys.exit(0)
    else:
        print("\n🔧 Se necesitan correcciones.")
        sys.exit(1)