from backend.appengine.categoria.categoria_model import HQs
from backend.appengine.config.template_middleware import TemplateResponse
from backend.appengine.routes import hqs
from gaecookie.decorator import no_csrf
from tekton.gae.middleware.redirect import RedirectResponse
from tekton.router import to_path
from gaepermission.decorator import login_not_required

@login_not_required
@no_csrf
def index(hq_id):
    hq=HQs.get_by_id(int(hq_id))
    ctx={'hqs':hqs,
         'salvar_path':to_path(salvar)}
    return TemplateResponse(ctx,'hqs/hqs_form.html')
@login_not_required
def salvar(hq_id, nome):
    hq=HQs.get_by_id(int(hq_id))
    hq.nome=nome
    hq.put()
    return RedirectResponse(hqs)

