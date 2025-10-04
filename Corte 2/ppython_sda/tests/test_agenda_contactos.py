import pytest
import json
import tempfile
import os
from datetime import datetime


class Contacto:
    """Clase para representar un contacto individual"""
    
    def __init__(self, nombre: str, telefono: str = "", email: str = "", 
                 direccion: str = "", profesion: str = "", edad: int = 0, ciudad: str = ""):
        self.nombre = nombre
        self.telefono = telefono
        self.email = email
        self.direccion = direccion
        self.profesion = profesion
        self.edad = edad
        self.ciudad = ciudad
    
    def to_dict(self):
        return {
            'nombre': self.nombre,
            'telefono': self.telefono,
            'email': self.email,
            'direccion': self.direccion,
            'profesion': self.profesion,
            'edad': self.edad,
            'ciudad': self.ciudad
        }
    
    def __str__(self):
        return f"{self.nombre} ({self.telefono}) - {self.email}"


class AgendaContactos:
    """Agenda de contactos usando diccionario como estructura base"""
    
    def __init__(self):
        self.contactos = {}
        self.estadisticas = {
            'total_contactos': 0,
            'busquedas_realizadas': 0,
            'modificaciones': 0
        }
    
    def agregar_contacto(self, contacto):
        if contacto.nombre in self.contactos:
            return False
        
        self.contactos[contacto.nombre] = contacto
        self.estadisticas['total_contactos'] += 1
        self.estadisticas['modificaciones'] += 1
        return True
    
    def buscar_contacto(self, nombre):
        self.estadisticas['busquedas_realizadas'] += 1
        return self.contactos.get(nombre)
    
    def eliminar_contacto(self, nombre):
        if nombre in self.contactos:
            del self.contactos[nombre]
            self.estadisticas['total_contactos'] -= 1
            self.estadisticas['modificaciones'] += 1
            return True
        return False
    
    def actualizar_contacto(self, nombre, **kwargs):
        if nombre not in self.contactos:
            return False
        
        contacto = self.contactos[nombre]
        for key, value in kwargs.items():
            if hasattr(contacto, key):
                setattr(contacto, key, value)
        
        self.estadisticas['modificaciones'] += 1
        return True
    
    def listar_contactos(self, ordenar_por='nombre'):
        contactos = list(self.contactos.values())
        
        if ordenar_por == 'nombre':
            return sorted(contactos, key=lambda c: c.nombre)
        elif ordenar_por == 'edad':
            return sorted(contactos, key=lambda c: c.edad)
        elif ordenar_por == 'ciudad':
            return sorted(contactos, key=lambda c: c.ciudad)
        else:
            return contactos
    
    def buscar_por_criterio(self, **criterios):
        resultados = []
        for contacto in self.contactos.values():
            cumple_criterios = True
            for key, value in criterios.items():
                if hasattr(contacto, key):
                    if getattr(contacto, key).lower() != str(value).lower():
                        cumple_criterios = False
                        break
            if cumple_criterios:
                resultados.append(contacto)
        
        self.estadisticas['busquedas_realizadas'] += 1
        return resultados
    
    def cargar_desde_json(self, archivo_path):
        try:
            with open(archivo_path, 'r', encoding='utf-8') as file:
                personas_data = json.load(file)
                
            for persona in personas_data:
                contacto = Contacto(
                    nombre=persona.get('nombre', ''),
                    telefono=persona.get('telefono', ''),
                    email=persona.get('email', ''),
                    direccion=persona.get('direccion', ''),
                    profesion=persona.get('profesion', ''),
                    edad=persona.get('edad', 0),
                    ciudad=persona.get('ciudad', '')
                )
                self.agregar_contacto(contacto)
            return True
        except (FileNotFoundError, json.JSONDecodeError, KeyError):
            return False
    
    def exportar_a_json(self, archivo_path):
        try:
            datos = [contacto.to_dict() for contacto in self.contactos.values()]
            with open(archivo_path, 'w', encoding='utf-8') as file:
                json.dump(datos, file, indent=2, ensure_ascii=False)
            return True
        except Exception:
            return False
    
    def obtener_estadisticas(self):
        return {
            **self.estadisticas,
            'contactos_actuales': len(self.contactos),
            'memoria_estimada_kb': len(str(self.contactos)) / 1024
        }
    
    def __len__(self):
        return len(self.contactos)
    
    def __contains__(self, nombre):
        return nombre in self.contactos


# Tests para Contacto
def test_contacto_creacion():
    """Prueba creación de contacto"""
    contacto = Contacto("Ana García", "123456789", "ana@email.com")
    assert contacto.nombre == "Ana García"
    assert contacto.telefono == "123456789"
    assert contacto.email == "ana@email.com"


def test_contacto_to_dict():
    """Prueba conversión a diccionario"""
    contacto = Contacto("Pedro López", "987654321", "pedro@email.com", 
                       "Calle Mayor 1", "Ingeniero", 30, "Madrid")
    dict_contacto = contacto.to_dict()
    
    assert dict_contacto['nombre'] == "Pedro López"
    assert dict_contacto['edad'] == 30
    assert dict_contacto['ciudad'] == "Madrid"


def test_contacto_str():
    """Prueba representación string"""
    contacto = Contacto("María", "555666777", "maria@email.com")
    str_contacto = str(contacto)
    assert "María" in str_contacto
    assert "555666777" in str_contacto
    assert "maria@email.com" in str_contacto


# Tests para AgendaContactos
def test_agregar_contacto():
    """Prueba agregar contactos"""
    agenda = AgendaContactos()
    contacto = Contacto("Ana García", "123456789", "ana@email.com")
    
    assert agenda.agregar_contacto(contacto) == True
    assert len(agenda) == 1
    assert "Ana García" in agenda
    
    # Intentar agregar duplicado
    assert agenda.agregar_contacto(contacto) == False
    assert len(agenda) == 1


def test_buscar_contacto():
    """Prueba buscar contactos"""
    agenda = AgendaContactos()
    contacto = Contacto("Pedro López", "987654321", "pedro@email.com")
    agenda.agregar_contacto(contacto)
    
    encontrado = agenda.buscar_contacto("Pedro López")
    assert encontrado is not None
    assert encontrado.nombre == "Pedro López"
    
    no_encontrado = agenda.buscar_contacto("Juan Pérez")
    assert no_encontrado is None


def test_eliminar_contacto():
    """Prueba eliminar contactos"""
    agenda = AgendaContactos()
    contacto = Contacto("María Rodríguez", "555666777", "maria@email.com")
    agenda.agregar_contacto(contacto)
    
    assert agenda.eliminar_contacto("María Rodríguez") == True
    assert len(agenda) == 0
    assert agenda.eliminar_contacto("No Existe") == False


def test_actualizar_contacto():
    """Prueba actualizar información de contactos"""
    agenda = AgendaContactos()
    contacto = Contacto("Luis Martín", "111222333", "luis@email.com", edad=25)
    agenda.agregar_contacto(contacto)
    
    assert agenda.actualizar_contacto("Luis Martín", edad=26, ciudad="Madrid") == True
    contacto_actualizado = agenda.buscar_contacto("Luis Martín")
    assert contacto_actualizado.edad == 26
    assert contacto_actualizado.ciudad == "Madrid"
    
    # Intentar actualizar contacto inexistente
    assert agenda.actualizar_contacto("No Existe", edad=30) == False


def test_listar_contactos():
    """Prueba listar contactos ordenados"""
    agenda = AgendaContactos()
    contactos = [
        Contacto("Carlos", "111", "carlos@email.com", edad=30),
        Contacto("Ana", "222", "ana@email.com", edad=25),
        Contacto("Bruno", "333", "bruno@email.com", edad=35)
    ]
    
    for contacto in contactos:
        agenda.agregar_contacto(contacto)
    
    # Ordenar por nombre
    lista_nombre = agenda.listar_contactos('nombre')
    assert lista_nombre[0].nombre == "Ana"
    assert lista_nombre[1].nombre == "Bruno"
    assert lista_nombre[2].nombre == "Carlos"
    
    # Ordenar por edad
    lista_edad = agenda.listar_contactos('edad')
    assert lista_edad[0].edad == 25
    assert lista_edad[1].edad == 30
    assert lista_edad[2].edad == 35


def test_buscar_por_criterio():
    """Prueba búsqueda por criterios"""
    agenda = AgendaContactos()
    contactos = [
        Contacto("Ana", "123", "ana@email.com", ciudad="Madrid", profesion="Ingeniera"),
        Contacto("Luis", "456", "luis@email.com", ciudad="Barcelona", profesion="Doctor"),
        Contacto("Pedro", "789", "pedro@email.com", ciudad="Madrid", profesion="Profesor")
    ]
    
    for contacto in contactos:
        agenda.agregar_contacto(contacto)
    
    # Buscar por ciudad
    resultados_madrid = agenda.buscar_por_criterio(ciudad="Madrid")
    assert len(resultados_madrid) == 2
    nombres_madrid = [c.nombre for c in resultados_madrid]
    assert "Ana" in nombres_madrid
    assert "Pedro" in nombres_madrid
    
    # Buscar por profesión
    resultados_doctor = agenda.buscar_por_criterio(profesion="Doctor")
    assert len(resultados_doctor) == 1
    assert resultados_doctor[0].nombre == "Luis"


def test_cargar_exportar_json():
    """Prueba cargar y exportar desde/hacia JSON"""
    agenda = AgendaContactos()
    
    # Crear datos de prueba
    contactos_test = [
        {"nombre": "Ana", "email": "ana@test.com", "edad": 25, "ciudad": "Madrid"},
        {"nombre": "Pedro", "email": "pedro@test.com", "edad": 30, "ciudad": "Barcelona"}
    ]
    
    # Crear archivo temporal
    with tempfile.NamedTemporaryFile(mode='w', suffix='.json', delete=False) as f:
        json.dump(contactos_test, f)
        temp_filename = f.name
    
    try:
        # Cargar desde JSON
        assert agenda.cargar_desde_json(temp_filename) == True
        assert len(agenda) == 2
        assert "Ana" in agenda
        assert "Pedro" in agenda
        
        # Exportar a JSON
        output_file = tempfile.NamedTemporaryFile(mode='w', suffix='.json', delete=False)
        output_filename = output_file.name
        output_file.close()
        
        assert agenda.exportar_a_json(output_filename) == True
        
        # Verificar contenido exportado
        with open(output_filename, 'r') as f:
            datos_exportados = json.load(f)
        
        assert len(datos_exportados) == 2
        nombres_exportados = [d['nombre'] for d in datos_exportados]
        assert "Ana" in nombres_exportados
        assert "Pedro" in nombres_exportados
        
        # Limpiar archivos temporales
        os.unlink(output_filename)
        
    finally:
        os.unlink(temp_filename)


def test_estadisticas():
    """Prueba obtener estadísticas"""
    agenda = AgendaContactos()
    contacto = Contacto("Test User", "123456789", "test@email.com")
    
    # Estado inicial
    stats_inicial = agenda.obtener_estadisticas()
    assert stats_inicial['total_contactos'] == 0
    assert stats_inicial['busquedas_realizadas'] == 0
    assert stats_inicial['modificaciones'] == 0
    
    # Después de agregar
    agenda.agregar_contacto(contacto)
    stats_agregar = agenda.obtener_estadisticas()
    assert stats_agregar['total_contactos'] == 1
    assert stats_agregar['modificaciones'] == 1
    assert stats_agregar['contactos_actuales'] == 1
    
    # Después de buscar
    agenda.buscar_contacto("Test User")
    stats_buscar = agenda.obtener_estadisticas()
    assert stats_buscar['busquedas_realizadas'] == 1


def test_agenda_len_contains():
    """Prueba métodos especiales __len__ y __contains__"""
    agenda = AgendaContactos()
    
    assert len(agenda) == 0
    assert "Ana" not in agenda
    
    contacto = Contacto("Ana García", "123456789", "ana@email.com")
    agenda.agregar_contacto(contacto)
    
    assert len(agenda) == 1
    assert "Ana García" in agenda
    assert "Pedro" not in agenda


def test_cargar_json_archivo_inexistente():
    """Prueba cargar desde archivo inexistente"""
    agenda = AgendaContactos()
    assert agenda.cargar_desde_json("archivo_inexistente.json") == False


def test_exportar_json_directorio_inexistente():
    """Prueba exportar a directorio inexistente"""
    agenda = AgendaContactos()
    contacto = Contacto("Test", "123", "test@email.com")
    agenda.agregar_contacto(contacto)
    
    assert agenda.exportar_a_json("/directorio/inexistente/archivo.json") == False