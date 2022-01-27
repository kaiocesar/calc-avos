from datetime import datetime


def calcular_avos(
    dt_begin: datetime,
    dt_end: datetime, Beneficio: object)-> int:
    return Beneficio(dt_begin, dt_end)


def ferias(dt_begin, dt_end) -> int:
    months = (dt_end.year - dt_begin.year) * 12 + (dt_end.month - dt_begin.month)
    if months > 1:
        acquisition_day = (dt_begin.day - 1) \
            if dt_begin.day > 1 else dt_begin.day
        acquisition_day = abs(acquisition_day - dt_end.day)
        return months + 1 if acquisition_day > 14 else months
    return months


def decimo_terceiro(dt_begin, dt_end) -> int:
    return None
