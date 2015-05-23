# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from categoria.categoria_model import Categoria, HQsForm, HQs
from config.template_middleware import TemplateResponse
from google.appengine.ext import ndb
from backend.appengine.routes import hqs
from gaecookie.decorator import no_csrf
from tekton.gae.middleware.redirect import RedirectResponse
from tekton.router import to_path

from gaepermission.decorator import login_not_required
@login_not_required
@no_csrf
def index(categoria_selecionada=None):

    ctx={'categorias':Categoria.query_ordenada_por_nome().fetch(),
         'salvar_path':to_path(salvar),
         'pesquisar_path': to_path(index)}
    if categoria_selecionada is None:
        ctx['categoria_selecionada']= None
    else:
        ctx['categoria_selecionada']=Categoria.get_by_id(int(categoria_selecionada))
    return TemplateResponse(ctx, 'hqs/hqs_home.html')

@login_not_required
def salvar(**propriedades):
    form = HQsForm(**propriedades)
    erros = form.validate()
    if not erros:
        hqs = form.fill_model()
        hqs.put()
    return RedirectResponse(index)


