# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from google.appengine.ext import ndb
from categoria.categoria_model import Categoria
from config.template_middleware import TemplateResponse
from gaecookie.decorator import no_csrf
from routes.categorias import edit
from routes.categorias.new import salvar
from tekton.gae.middleware.redirect import RedirectResponse
from tekton.router import to_path


@no_csrf
def index():
    query = Categoria.query_ordenada_por_nome()
    categorias = query.fetch()
    edit_path_base = to_path(edit)
    deletar_path_base = to_path(deletar)

    for cat in categorias:
        key = cat.key
        id = key.id()
        cat.edit_path=to_path(edit_path_base, id)
        cat.deletar_path=to_path(deletar_path_base, id)

    salvar_path = to_path(salvar)
    ctx = {'salvar_path': salvar_path,
           'categorias': categorias}
    return TemplateResponse(ctx, 'categorias/categoria_home.html')

def deletar(categoria_id):
    key= ndb.Key(Categoria, int(categoria_id))
    key.delete()
    return RedirectResponse(index)