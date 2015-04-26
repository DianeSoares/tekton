# -*- coding: utf-8 -*-
from backend.appengine.categoria.categoria_model import HQsForm, HQs
from backend.appengine.config.template_middleware import TemplateResponse
from backend.appengine.routes import hqs
from tekton.gae.middleware.redirect import RedirectResponse


def salvar(**kwargs):
    form = HQsForm(**kwargs)
    erros=form.validate()
    if not erros:
        valores_normalizados=form.normalize()
        categoria = HQs(**valores_normalizados)
        categoria.put()
        return RedirectResponse(hqs)
    else:
        ctx={'categoria':kwargs,'erros':erros}
        return TemplateResponse(ctx,'hqs/hqs_form.html')
