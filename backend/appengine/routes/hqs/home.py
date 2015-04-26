# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from categoria.categoria_model import Categoria, HQsForm, HQs
from config.template_middleware import TemplateResponse
from google.appengine.ext import ndb
from backend.appengine.routes import hqs
from gaecookie.decorator import no_csrf
from tekton.gae.middleware.redirect import RedirectResponse
from tekton.router import to_path


@no_csrf
def index(categoria_selecionada=None):

    query = HQs.query_ordenada_por_nome()
    hqs = query.fetch()
    edit_path_base = to_path(edit)
    deletar_path_base = to_path(deletar)

    for hq in hqs:
        key = hq.key
        id = key.id()
        hq.edit_path=to_path(edit_path_base, id)
        hq.deletar_path=to_path(deletar_path_base, id)

    ctx={'categorias':Categoria.query_ordenada_por_nome().fetch(),
         'salvar_path':to_path(salvar),
         'allhqs': hqs,
         'pesquisar_path': to_path(index)}
    if categoria_selecionada is None:
        ctx['hqs']=HQs.query_ordenada_por_nome().fetch()
        ctx['allhqs']=hqs
        ctx['categoria_selecionada']= None
    else:
        ctx['categoria_selecionada']=Categoria.get_by_id(int(categoria_selecionada))
        ctx['hqs']=HQs.query_por_categoria_ordenados_por_nome(categoria_selecionada).fetch()
    return TemplateResponse(ctx, 'hqs/hqs_home.html')

def deletar(hq_id):
    key= ndb.Key(HQs, int(hq_id))
    key.delete()
    return RedirectResponse(index)

def salvar(**propriedades):
    form = HQsForm(**propriedades)
    erros = form.validate()
    if not erros:
        hqs = form.fill_model()
        hqs.put()
    return RedirectResponse(index)

@no_csrf
def edit(hq_id):
    hqs=HQs.get_by_id(int(hq_id))
    ctx={'hqs':hqs,
         'salvar_path':to_path(save)}
    return TemplateResponse(ctx,'hqs/hqs_form.html')

def save(hq_id, nome):
    hqs=HQs.get_by_id(int(hq_id))
    hqs.nome=nome
    hqs.put()
    return RedirectResponse(index)

