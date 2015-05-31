# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from google.appengine.ext import ndb
from categoria.categoria_model import CategoriaForm, Categoria
from gaecookie.decorator import no_csrf
from gaepermission.decorator import login_not_required
from tekton.gae.middleware.json_middleware import JsonUnsecureResponse
@login_not_required
@no_csrf
def index():
    form = CategoriaForm()
    categorias = Categoria.query_ordenada_por_nome().fetch()
    categorias = [form.fill_with_model(p) for p in categorias]
    return JsonUnsecureResponse(categorias)

@login_not_required
@no_csrf
def apagar(categoria_id):
    key = ndb.Key(Categoria, int(categoria_id))
    key.delete()
    return JsonUnsecureResponse('') # para setar cabeçalho para aplpication/json


@login_not_required
@no_csrf
def listar():
    form = CategoriaForm()
    categorias = Categoria.query_ordenada_por_nome().fetch()
    categorias = [form.fill_with_model(p) for p in categorias]
    return JsonUnsecureResponse(categorias)


@login_not_required
@no_csrf
def salvar(_resp, **propriedades):
    form = CategoriaForm(**propriedades)
    erros = form.validate()
    if not erros:
        categoria = form.fill_model()
        categoria.put()
        dct = form.fill_with_model(categoria)
        return JsonUnsecureResponse(dct)
    _resp.set_status(400)
    return JsonUnsecureResponse(erros)