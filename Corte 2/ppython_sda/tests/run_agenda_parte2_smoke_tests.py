#!/usr/bin/env python3
"""
Script de pruebas de humo para la Agenda de Contactos Parte 2 (Diccionarios Anidados)
Este script verifica que las funcionalidades básicas estén funcionando sin usar pytest.
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


def test_result(test_name: str, condition: bool, error_msg: str = "") -> bool:
    """Helper para mostrar resultados de pruebas"""
    status = "✓ PASS" if condition else "✗ FAIL"
    print(f"  {status} {test_name}")
    if not condition and error_msg:
        print(f"    Error: {error_msg}")
    return condition


def run_smoke_tests():
    """Ejecuta todas las pruebas de humo"""
    print("🧪 Ejecutando pruebas de humo para AgendaContactosParte2...")
    print("=" * 60)
    
    tests_passed = 0
    tests_failed = 0
    
    try:
        # Test 1: Crear agenda vacía
        print("\n📝 Test 1: Creación de agenda")
        agenda = AgendaContactosParte2()
        if test_result("Crear agenda vacía", len(agenda) == 0):
            tests_passed += 1
        else:
            tests_failed += 1
        
        # Test 2: Agregar contacto básico
        print("\n📝 Test 2: Agregar contacto")
        datos_ana = {
            'telefono': '123456789',
            'email': 'ana@email.com',
            'direccion': 'Calle Mayor 1'
        }
        
        resultado_add = agenda.agregar_contacto('Ana García', datos_ana)
        if test_result("Agregar contacto válido", resultado_add and len(agenda) == 1):
            tests_passed += 1
        else:
            tests_failed += 1
        
        if test_result("Contacto existe en agenda", 'Ana García' in agenda):
            tests_passed += 1
        else:
            tests_failed += 1
        
        # Test 3: Obtener contacto
        print("\n📝 Test 3: Obtener contacto")
        contacto = agenda.obtener_contacto('Ana García')
        if test_result("Obtener contacto existente", contacto is not None):
            tests_passed += 1
        else:
            tests_failed += 1
        
        if test_result("Datos del contacto correctos", contacto['email'] == 'ana@email.com'):
            tests_passed += 1
        else:
            tests_failed += 1
        
        # Test 4: Agregar contacto con campos opcionales
        print("\n📝 Test 4: Contacto con campos opcionales")
        datos_pedro = {
            'telefono': '987654321',
            'email': 'pedro@email.com',
            'direccion': 'Av. Principal 2',
            'edad': 30,
            'profesion': 'Ingeniero',
            'ciudad': 'Madrid'
        }
        
        resultado_pedro = agenda.agregar_contacto('Pedro López', datos_pedro)
        if test_result("Agregar contacto con campos opcionales", resultado_pedro):
            tests_passed += 1
        else:
            tests_failed += 1
        
        # Test 5: Obtener campo específico
        print("\n📝 Test 5: Obtener campo específico")
        edad_pedro = agenda.obtener_campo('Pedro López', 'edad')
        if test_result("Obtener edad de Pedro", edad_pedro == 30):
            tests_passed += 1
        else:
            tests_failed += 1
        
        telefono_ana = agenda.obtener_campo('Ana García', 'telefono')
        if test_result("Obtener teléfono de Ana", telefono_ana == '123456789'):
            tests_passed += 1
        else:
            tests_failed += 1
        
        # Test 6: Actualizar contacto
        print("\n📝 Test 6: Actualizar contacto")
        resultado_update = agenda.actualizar_contacto('Ana García', edad=25, ciudad='Barcelona')
        if test_result("Actualizar campos de Ana", resultado_update):
            tests_passed += 1
        else:
            tests_failed += 1
        
        edad_ana = agenda.obtener_campo('Ana García', 'edad')
        if test_result("Verificar edad actualizada", edad_ana == 25):
            tests_passed += 1
        else:
            tests_failed += 1
        
        # Test 7: Buscar por campo
        print("\n📝 Test 7: Buscar por campo")
        resultados_madrid = agenda.buscar_por_campo('ciudad', 'Madrid')
        if test_result("Buscar contactos en Madrid", 'Pedro López' in resultados_madrid):
            tests_passed += 1
        else:
            tests_failed += 1
        
        # Test 8: Buscar parcial
        print("\n📝 Test 8: Búsqueda parcial")
        resultados_email = agenda.buscar_por_campo('email', 'email.com', exacto=False)
        if test_result("Búsqueda parcial por email", len(resultados_email) == 2):
            tests_passed += 1
        else:
            tests_failed += 1
        
        # Test 9: Listar contactos ordenados
        print("\n📝 Test 9: Listar contactos")
        lista_contactos = agenda.listar_contactos('nombre')
        nombres_ordenados = [nombre for nombre, _ in lista_contactos]
        if test_result("Listar contactos ordenados por nombre", 
                      nombres_ordenados == ['Ana García', 'Pedro López']):
            tests_passed += 1
        else:
            tests_failed += 1
        
        # Test 10: Eliminar campo
        print("\n📝 Test 10: Eliminar campo")
        resultado_del_campo = agenda.eliminar_campo('Pedro López', 'ciudad')
        if test_result("Eliminar campo opcional", resultado_del_campo):
            tests_passed += 1
        else:
            tests_failed += 1
        
        ciudad_pedro = agenda.obtener_campo('Pedro López', 'ciudad')
        if test_result("Verificar campo eliminado", ciudad_pedro is None):
            tests_passed += 1
        else:
            tests_failed += 1
        
        # Test 11: No eliminar campo requerido
        print("\n📝 Test 11: Protección de campos requeridos")
        resultado_del_telefono = agenda.eliminar_campo('Pedro López', 'telefono')
        if test_result("No puede eliminar campo requerido", not resultado_del_telefono):
            tests_passed += 1
        else:
            tests_failed += 1
        
        # Test 12: Estadísticas
        print("\n📝 Test 12: Estadísticas")
        stats = agenda.obtener_estadisticas()
        if test_result("Estadísticas - contactos actuales", stats['contactos_actuales'] == 2):
            tests_passed += 1
        else:
            tests_failed += 1
        
        if test_result("Estadísticas - operaciones de escritura", stats['operaciones_escritura'] > 0):
            tests_passed += 1
        else:
            tests_failed += 1
        
        # Test 13: Campos disponibles
        print("\n📝 Test 13: Campos disponibles")
        campos = agenda.obtener_campos_disponibles()
        if test_result("Campos disponibles - teléfono", campos.get('telefono', 0) == 2):
            tests_passed += 1
        else:
            tests_failed += 1
        
        # Test 14: Eliminar contacto
        print("\n📝 Test 14: Eliminar contacto")
        resultado_del_contacto = agenda.eliminar_contacto('Pedro López')
        if test_result("Eliminar contacto existente", resultado_del_contacto):
            tests_passed += 1
        else:
            tests_failed += 1
        
        if test_result("Verificar contacto eliminado", len(agenda) == 1):
            tests_passed += 1
        else:
            tests_failed += 1
        
        # Test 15: Validación de campos faltantes
        print("\n📝 Test 15: Validación de campos")
        datos_invalidos = {
            'telefono': '111222333',
            'email': 'test@email.com'
            # Falta 'direccion'
        }
        
        try:
            agenda.agregar_contacto('Test Invalid', datos_invalidos)
            if test_result("Detectar campos faltantes", False, "Debería haber lanzado ValueError"):
                tests_passed += 1
            else:
                tests_failed += 1
        except ValueError:
            if test_result("Detectar campos faltantes correctamente", True):
                tests_passed += 1
            else:
                tests_failed += 1
        except Exception as e:
            if test_result("Detectar campos faltantes", False, f"Error inesperado: {e}"):
                tests_passed += 1
            else:
                tests_failed += 1
        
        # Test 16: Contacto duplicado
        print("\n📝 Test 16: Contacto duplicado")
        resultado_duplicado = agenda.agregar_contacto('Ana García', datos_ana)
        if test_result("Rechazar contacto duplicado", not resultado_duplicado):
            tests_passed += 1
        else:
            tests_failed += 1
        
    except Exception as e:
        print(f"\n❌ Error inesperado durante las pruebas:")
        print(f"   {str(e)}")
        print(f"\n📊 Stack trace:")
        traceback.print_exc()
        tests_failed += 1
    
    # Resumen final
    print("\n" + "=" * 60)
    print("📊 RESUMEN DE PRUEBAS")
    print("=" * 60)
    
    total_tests = tests_passed + tests_failed
    success_rate = (tests_passed / total_tests * 100) if total_tests > 0 else 0
    
    print(f"✅ Pruebas exitosas: {tests_passed}")
    print(f"❌ Pruebas fallidas: {tests_failed}")
    print(f"📈 Tasa de éxito: {success_rate:.1f}%")
    
    if tests_failed == 0:
        print("\n🎉 ¡Todas las pruebas de humo pasaron exitosamente!")
        print("   La implementación básica de AgendaContactosParte2 está funcionando correctamente.")
        return True
    else:
        print(f"\n⚠️  Se encontraron {tests_failed} problemas en las pruebas.")
        print("   Revisa la implementación antes de continuar.")
        return False


if __name__ == "__main__":
    print("🚀 Iniciando pruebas de humo para AgendaContactosParte2 (Diccionarios Anidados)")
    print(f"🐍 Python {sys.version}")
    print(f"📅 {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    
    success = run_smoke_tests()
    
    if success:
        print("\n✨ Sistema listo para usar!")
        sys.exit(0)
    else:
        print("\n🔧 Se necesitan correcciones.")
        sys.exit(1)