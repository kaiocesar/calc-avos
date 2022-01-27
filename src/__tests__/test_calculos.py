from datetime import datetime

from src.utils import calcular_avos, ferias


# https://www.calculorescisao.com.br/calcular-rescisao-online.php

def test_calc_ferias_zero_avos():
    dt_begin = datetime.strptime('2019-10-01', '%Y-%m-%d')
    dt_end = datetime.strptime('2019-10-14', '%Y-%m-%d')

    assert calcular_avos(dt_begin, dt_end, ferias) == 0


def test_calc_ferias_successful_same_year_1avo():
    dt_begin = datetime.strptime('2019-10-25', "%Y-%m-%d")
    dt_end = datetime.strptime('2019-11-24', '%Y-%m-%d')

    assert calcular_avos(dt_begin, dt_end, ferias) == 1


def test_calc_ferias_successful_same_year_2avos():
    dt_begin = datetime.strptime('2019-12-15', '%Y-%m-%d')
    dt_end = datetime.strptime('2020-02-14', '%Y-%m-%d')

    assert calcular_avos(dt_begin, dt_end, ferias) == 2


def test_calc_ferias_successful_two_year_5avos():
    dt_begin = datetime.strptime('2019-08-19', "%Y-%m-%d")
    dt_end = datetime.strptime('2020-01-04', '%Y-%m-%d')

    assert calcular_avos(dt_begin, dt_end, ferias) == 5


def test_calc_ferias_successful_two_year_6avos():
    dt_begin = datetime.strptime('2011-03-25', "%Y-%m-%d")
    dt_end = datetime.strptime('2011-09-10', '%Y-%m-%d')

    assert calcular_avos(dt_begin, dt_end, ferias) == 6


def test_calc_ferias_successful_two_year_7avos():
    dt_begin = datetime.strptime('2018-08-11', '%Y-%m-%d')
    dt_end = datetime.strptime('2019-03-24', '%Y-%m-%d')

    assert calcular_avos(dt_begin, dt_end, ferias) == 7


def test_calc_ferias_successful_8avos():
    dt_begin = datetime.strptime('2019-08-11', '%Y-%m-%d')
    dt_end = datetime.strptime('2020-03-25', '%Y-%m-%d')

    assert calcular_avos(dt_begin, dt_end, ferias) == 8


def test_calc_ferias_successful_same_year_10avo():
    dt_begin = datetime.strptime('2019-03-15', "%Y-%m-%d")
    dt_end = datetime.strptime('2020-01-21', '%Y-%m-%d')

    assert calcular_avos(dt_begin, dt_end, ferias) == 10


def test_calc_ferias_successful_same_year_12avo():
    dt_begin = datetime.strptime('2019-10-25', "%Y-%m-%d")
    dt_end = datetime.strptime('2020-10-09', '%Y-%m-%d')
    # dt_end_maior = datetime.strptime('2020-10-25', '%Y-%m-%d')
    
    assert calcular_avos(dt_begin, dt_end, ferias) == 12
    # assert calcular_avos(dt_begin, dt_end_maior, ferias) == 12
