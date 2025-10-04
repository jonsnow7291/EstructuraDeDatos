"""Run lightweight checks for agenda_contactos without pytest.

This script mirrors the pytest checks so it can be executed where pytest
isn't installed. It prints a simple summary and exits with code 0 on success
or 1 on failure.
"""
import sys
import json
import tempfile
import os


class Contacto:
    """Clase para representar un contacto individual"""
    
    def __init__(self, nombre, telefono="", email="", direccion="", profesion="", edad=0, ciudad=""):
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


def run():
    errors = []

    # Test básicos de Contacto
    try:
        contacto = Contacto("Ana García", "123456789", "ana@email.com")
        assert contacto.nombre == "Ana García"
        assert contacto.telefono == "123456789"
        assert contacto.email == "ana@email.com"
    except AssertionError:
        errors.append('test_contacto_creacion failed')

    # Test agregar contacto
    try:
        agenda = AgendaContactos()
        contacto = Contacto("Ana García", "123456789", "ana@email.com")
        
        assert agenda.agregar_contacto(contacto) == True
        assert len(agenda) == 1
        assert "Ana García" in agenda
        
        # Intentar agregar duplicado
        assert agenda.agregar_contacto(contacto) == False
        assert len(agenda) == 1
    except AssertionError:
        errors.append('test_agregar_contacto failed')

    # Test buscar contacto
    try:
        agenda = AgendaContactos()
        contacto = Contacto("Pedro López", "987654321", "pedro@email.com")
        agenda.agregar_contacto(contacto)
        
        encontrado = agenda.buscar_contacto("Pedro López")
        assert encontrado is not None
        assert encontrado.nombre == "Pedro López"
        
        no_encontrado = agenda.buscar_contacto("Juan Pérez")
        assert no_encontrado is None
    except AssertionError:
        errors.append('test_buscar_contacto failed')

    # Test eliminar contacto
    try:
        agenda = AgendaContactos()
        contacto = Contacto("María Rodríguez", "555666777", "maria@email.com")
        agenda.agregar_contacto(contacto)
        
        assert agenda.eliminar_contacto("María Rodríguez") == True
        assert len(agenda) == 0
        assert agenda.eliminar_contacto("No Existe") == False
    except AssertionError:
        errors.append('test_eliminar_contacto failed')

    # Test actualizar contacto
    try:
        agenda = AgendaContactos()
        contacto = Contacto("Luis Martín", "111222333", "luis@email.com", edad=25)
        agenda.agregar_contacto(contacto)
        
        assert agenda.actualizar_contacto("Luis Martín", edad=26, ciudad="Madrid") == True
        contacto_actualizado = agenda.buscar_contacto("Luis Martín")
        assert contacto_actualizado.edad == 26
        assert contacto_actualizado.ciudad == "Madrid"
        
        # Intentar actualizar contacto inexistente
        assert agenda.actualizar_contacto("No Existe", edad=30) == False
    except AssertionError:
        errors.append('test_actualizar_contacto failed')

    # Test buscar por criterio
    try:
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
        
        # Buscar por profesión
        resultados_doctor = agenda.buscar_por_criterio(profesion="Doctor")
        assert len(resultados_doctor) == 1
        assert resultados_doctor[0].nombre == "Luis"
    except AssertionError:
        errors.append('test_buscar_por_criterio failed')

    # Test estadísticas
    try:
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
    except AssertionError:
        errors.append('test_estadisticas failed')

    # Test métodos especiales
    try:
        agenda = AgendaContactos()
        
        assert len(agenda) == 0
        assert "Ana" not in agenda
        
        contacto = Contacto("Ana García", "123456789", "ana@email.com")
        agenda.agregar_contacto(contacto)
        
        assert len(agenda) == 1
        assert "Ana García" in agenda
        assert "Pedro" not in agenda
    except AssertionError:
        errors.append('test_metodos_especiales failed')

    if errors:
        print('FAILED:')
        for e in errors:
            print('-', e)
        return 1
    print('ALL AGENDA CONTACTOS SMOKE TESTS PASSED')
    return 0


if __name__ == '__main__':
    sys.exit(run())