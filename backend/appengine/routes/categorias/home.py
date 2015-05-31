# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from google.appengine.ext import ndb
from categoria.categoria_model import Categoria
from config.template_middleware import TemplateResponse
from gaecookie.decorator import no_csrf
from routes.rest.categorias import salvar
from routes.rest.categorias import index
'''from routes.categorias.new import salvar'''
from routes.rest.categorias import apagar
from gaepermission.decorator import login_not_required
from tekton.gae.middleware.redirect import RedirectResponse
from tekton.router import to_path
from tekton.gae.middleware.json_middleware import JsonUnsecureResponse

@login_not_required
@no_csrf
def index():
    '''edit_path_base = to_path(edit)
    deletar_path_base = to_path(deletar)

    for cat in categorias:
        key = cat.key
        id = key.id()
        cat.edit_path=to_path(edit_path_base, id)
        cat.deletar_path=to_path(deletar_path_base, id)
    '''
    salvar_path = to_path(salvar)
    listar_path = to_path(index)
    apagar_path = to_path(apagar)

    ctx = {'salvar_path': salvar_path,
           'apagar_path': apagar_path,
           'listar_path': listar_path}

    return TemplateResponse(ctx, 'categorias/categoria_home.html')

@login_not_required
def deletar(categoria_id):
    key= ndb.Key(Categoria, int(categoria_id))
    key.delete()
    return RedirectResponse(index)

