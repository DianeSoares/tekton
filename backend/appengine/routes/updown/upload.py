# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from backend.appengine.routes import updown
from blob_app import blob_facade
from tekton import router
from tekton.gae.middleware.redirect import RedirectResponse
from gaepermission.decorator import login_not_required

@login_not_required
def index(_handler, _logged_user, files):
    blob_infos = _handler.get_uploads('files[]')
    cmd = blob_facade.save_blob_files_cmd(blob_infos, _logged_user)
    cmd.execute()
    path = router.to_path(updown)
    return RedirectResponse(path)