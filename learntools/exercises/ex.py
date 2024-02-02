import pandas as pd

from learntools.core import *

usuarios = pd.read_csv('./u.user', sep='|', index_col='user_id')

class Ejercicio1(EqualityCheckProblem):
    _var = 'p1'
    _expected = (
            usuarios.head(),
    )

class Ejercicio2(EqualityCheckProblem):
    _var = 'p2'
    _expected = (
            usuarios.iloc[:, 2],
    )

class Ejercicio3(EqualityCheckProblem):
    _var = 'p3'
    _expected = (
            usuarios.loc[usuarios['occupation'] == 'administrator'],
    )

class Ejercicio4(EqualityCheckProblem):
    _var = 'p4'
    _expected = (
            usuarios.loc[usuarios['occupation'].notnull()],
    )

class Ejercicio5(EqualityCheckProblem):
    _var = 'p5'
    _expected = (
            usuarios.groupby('gender').age.mean(),
    )

class Ejercicio6(EqualityCheckProblem):
    _var = 'p6'
    _expected = (
            usuarios['occupation'].replace("educator", "teacher"),
    )

class Ejercicio7(EqualityCheckProblem):
    _var = 'p7'
    _expected = (
            usuarios.isnull().sum(),
    )

class Ejercicio8(EqualityCheckProblem):
    _var = 'p8'
    _expected = (
            usuarios.dropna(),
    )

class Ejercicio9(EqualityCheckProblem):
    _var = 'p9'
    _expected = (
            usuarios['occupation'].fillna('unknown'),
    )

class Ejercicio10(EqualityCheckProblem):
    _var = 'p10'
    _expected = (
            pd.to_datetime(usuarios['birth_date'], format='%d-%m-%Y'),
    )

qvars = bind_exercises(globals(), [
    Ejercicio1,
    Ejercicio2,
    Ejercicio3,
    Ejercicio4,
    Ejercicio5,
    Ejercicio6,
    Ejercicio7,
    Ejercicio8,
    Ejercicio9,
    Ejercicio10,
    ],
    var_format='q{n}',
    )
__all__ = list(qvars)