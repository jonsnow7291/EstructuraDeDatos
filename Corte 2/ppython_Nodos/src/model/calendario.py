"""Modelo sencillo de calendario del mes actual.
No usa librerías avanzadas (solo datetime). Feriados y fases se ponen manual/estimado.
"""
from __future__ import annotations
import datetime as _dt
from typing import List, Dict

# Feriados ejemplo (puedes ajustar): lista de (mes, dia)
_FERIADOS_FIJOS = {
    (1,1): "Año Nuevo",
    (5,1): "Día del Trabajo",
    (7,20): "Independencia",
    (12,25): "Navidad",
}

# Fases lunares (simple estimación: cada ~7 días a partir de una fecha base)
# Tomamos una fecha base conocida de luna nueva (aprox) y calculamos offsets
_BASE_LUNA_NUEVA = _dt.date(2025, 1, 29)  # ejemplo aproximado
_LUNAR_CYCLE = 29.53

# Pesca: asignamos un "nivel" (0-3) según fase aproximada (solo para ejemplo)
# 3 = excelente (luna nueva / llena), 2 = buena (cuartos), 1 = normal, 0 = mala

class CalendarioMes:
    def __init__(self, hoy: _dt.date | None = None):
        self.hoy = hoy or _dt.date.today()
        self.year = self.hoy.year
        self.month = self.hoy.month
        # Precalcular días del mes
        first = _dt.date(self.year, self.month, 1)
        if self.month == 12:
            next_first = _dt.date(self.year + 1, 1, 1)
        else:
            next_first = _dt.date(self.year, self.month + 1, 1)
        self.num_dias = (next_first - first).days

    def dia_actual(self):
        """Devuelve (numero_dia, nombre_semana)."""
        nombres = ["Lunes","Martes","Miércoles","Jueves","Viernes","Sábado","Domingo"]
        wd = self.hoy.weekday()  # 0 lunes
        return self.hoy.day, nombres[wd]

    def feriados(self) -> Dict[int, str]:
        out = {}
        for (m,d), nombre in _FERIADOS_FIJOS.items():
            if m == self.month:
                out[d] = nombre
        return out

    def _dias_del_mes(self) -> List[_dt.date]:
        return [_dt.date(self.year, self.month, d) for d in range(1, self.num_dias+1)]

    def fases_luna(self):
        """Devuelve dict con claves 'luna_nueva','luna_llena','cuarto_creciente','cuarto_menguante' -> lista de días.
        Cálculo muy aproximado: se busca el día del mes más cercano a offsets dentro del ciclo.
        """
        dias = self._dias_del_mes()
        resultado = {"luna_nueva": [], "luna_llena": [], "cuarto_creciente": [], "cuarto_menguante": []}
        for fecha in dias:
            # días desde base
            delta = (fecha - _BASE_LUNA_NUEVA).days
            # fase fraccional 0..1
            fase = (delta % _LUNAR_CYCLE) / _LUNAR_CYCLE
            # Clasificación grosera por rangos
            if fase < 0.05 or fase > 0.95:  # alrededor de nueva
                resultado["luna_nueva"].append(fecha.day)
            elif 0.45 < fase < 0.55:  # llena
                resultado["luna_llena"].append(fecha.day)
            elif 0.20 < fase < 0.30:  # creciente
                resultado["cuarto_creciente"].append(fecha.day)
            elif 0.70 < fase < 0.80:  # menguante
                resultado["cuarto_menguante"].append(fecha.day)
        return resultado

    def pesca(self):
        """Devuelve dict dia->nivel (0-3) usando fases para asignar nivel simple."""
        fases = self.fases_luna()
        niveles = {}
        especiales = set()
        for k, lvl in (("luna_nueva",3),("luna_llena",3),("cuarto_creciente",2),("cuarto_menguante",2)):
            for d in fases[k]:
                niveles[d] = lvl
                especiales.add(d)
        # resto
        for d in range(1, self.num_dias+1):
            if d not in niveles:
                niveles[d] = 1  # normal
        return niveles
