from django.http import HttpResponse
from pandas import DataFrame

from grant_app.getting_data import get_champ_data


def gd(request: DataFrame) -> HttpResponse:
    coeffs_t = get_champ_data()
    return HttpResponse(coeffs_t.to_html())
