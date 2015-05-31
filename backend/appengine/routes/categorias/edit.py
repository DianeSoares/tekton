# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from categoria.categoria_model import Categoria
from config.template_middleware import TemplateResponse
from gaecookie.decorator import no_csrf
from routes import categorias
from gaepermission.decorator import login_not_required
from tekton.gae.middleware.redirect import RedirectResponse
from tekton.router import to_path

@login_not_required
@no_csrf
def index(categoria_id):
    categoria=Categoria.get_by_id(int(categoria_id))
    ctx={'categoria':categoria,
         'salvar_path':to_path(salvar)}
    return TemplateResponse(ctx,'categorias/categoria_form.html')

@login_not_required
def salvar(categoria_id, nome,imagem):
    categoria=Categoria.get_by_id(int(categoria_id))
    categoria.nome=nome
    categoria.imagem=imagem
    categoria.put()
    return RedirectResponse(categorias)

