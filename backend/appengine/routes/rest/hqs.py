# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from google.appengine.ext import ndb
from categoria.categoria_model import HQsForm, HQs
from gaecookie.decorator import no_csrf
from gaepermission.decorator import login_not_required
from tekton.gae.middleware.json_middleware import JsonUnsecureResponse


@login_not_required
@no_csrf
def apagar(hq_id):
    key = ndb.Key(HQs, int(hq_id))
    key.delete()
    return JsonUnsecureResponse('') # para setar cabeçalho para aplpication/json


@login_not_required
@no_csrf
def listar():
    form = HQsForm()
    hqs = HQs.query_ordenada_por_nome().fetch()
    hqs = [form.fill_with_model(p) for p in hqs]
    return JsonUnsecureResponse(hqs)


@login_not_required
@no_csrf
def salvar(_resp, **propriedades):
    form = HQsForm(**propriedades)
    erros = form.validate()
    if not erros:
        hq = form.fill_model()
        hq.put()
        dct = form.fill_with_model(hq)
        return JsonUnsecureResponse(dct)
    _resp.set_status(400)
    return JsonUnsecureResponse(erros)