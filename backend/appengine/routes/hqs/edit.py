from backend.appengine.categoria.categoria_model import HQs
from backend.appengine.config.template_middleware import TemplateResponse
from backend.appengine.routes import hqs
from gaecookie.decorator import no_csrf
from tekton.gae.middleware.redirect import RedirectResponse
from tekton.router import to_path



@no_csrf
def index(hq_id):
    hq=HQs.get_by_id(int(hq_id))
    ctx={'hq':hq,
         'salvar_path':to_path(salvar)}
    return TemplateResponse(ctx,'hqs/hqs_form.html')

def salvar(hq_id, nome):
    hq=HQs.get_by_id(int(hq_id))
    hq.nome=nome
    hq.put()
    return RedirectResponse(hqs)

