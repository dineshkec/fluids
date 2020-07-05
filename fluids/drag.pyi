# DO NOT EDIT - AUTOMATICALLY GENERATED BY tests/make_test_stubs.py!
from numpy import ndarray
from typing import (
    List,
    Optional,
    Tuple,
    Union,
)


def Almedeij(Re: float) -> float: ...


def Barati(Re: Union[int, ndarray, float]) -> float: ...


def Barati_high(Re: float) -> float: ...


def Ceylan(Re: float) -> float: ...


def Cheng(Re: float) -> float: ...


def Clift(Re: float) -> float: ...


def Clift_Gauvin(Re: float) -> float: ...


def Engelund_Hansen(Re: float) -> float: ...


def Flemmer_Banks(Re: float) -> float: ...


def Graf(Re: float) -> float: ...


def Haider_Levenspiel(Re: float) -> float: ...


def Khan_Richardson(Re: float) -> float: ...


def Mikhailov_Freire(Re: float) -> float: ...


def Morrison(Re: float) -> float: ...


def Morsi_Alexander(Re: float) -> float: ...


def Rouse(Re: float) -> float: ...


def Song_Xu(Re: float, sphericity: float = ..., S: float = ...) -> float: ...


def Stokes(Re: float) -> float: ...


def Swamee_Ojha(Re: float) -> float: ...


def Terfous(Re: float) -> float: ...


def Yen(Re: float) -> float: ...


def _v_terminal_err(V: float, Method: None, Re_almost: float, main: float) -> float: ...


def drag_sphere(
    Re: Union[int, ndarray, float],
    Method: Optional[str] = ...,
    AvailableMethods: bool = ...
) -> Union[List[str], float]: ...


def drag_sphere_methods(Re: float, check_ranges: bool = ...) -> List[str]: ...


def integrate_drag_sphere(
    D: float,
    rhop: float,
    rho: float,
    mu: float,
    t: float,
    V: int = ...,
    Method: Optional[str] = ...,
    distance: bool = ...
) -> Union[Tuple[float, float], float]: ...


def time_v_terminal_Stokes(D: float, rhop: float, rho: float, mu: float, V0: int, tol: float = ...) -> float: ...


def v_terminal(D: float, rhop: float, rho: float, mu: float, Method: Optional[str] = ...) -> float: ...

__all__: List[str]