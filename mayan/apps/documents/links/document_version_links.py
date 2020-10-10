from django.utils.translation import ugettext_lazy as _

from mayan.apps.navigation.classes import Link

from ..icons import (
    icon_document_version_create, icon_document_version_delete,
    icon_document_version_edit, icon_document_version_list,
    icon_document_version_return_document, icon_document_version_return_list,
    icon_document_version_preview
)
from ..permissions import (
    permission_document_version_create, permission_document_version_delete,
    permission_document_version_edit, permission_document_version_view,
    permission_document_view
)

link_document_version_create = Link(
    args='resolved_object.pk', icon_class=icon_document_version_create,
    permissions=(permission_document_version_create,),
    text=_('Create document version'),
    view='documents:document_version_create'
)
link_document_version_delete = Link(
    args='resolved_object.pk',
    icon_class=icon_document_version_delete,
    permissions=(permission_document_version_delete,), tags='dangerous',
    text=_('Delete'), view='documents:document_version_delete'
)
link_document_version_edit = Link(
    args='resolved_object.pk', icon_class=icon_document_version_edit,
    permissions=(permission_document_version_edit,),
    text=_('Edit'), view='documents:document_version_edit'
)
link_document_version_multiple_delete = Link(
    icon_class=icon_document_version_delete, tags='dangerous',
    text=_('Delete'), view='documents:document_version_multiple_delete'
)
link_document_version_list = Link(
    args='resolved_object.pk', icon_class=icon_document_version_list,
    permissions=(permission_document_version_view,), text=_('Versions'),
    view='documents:document_version_list'
)
#link_document_version_download = Link(
#    args='resolved_object.pk',
#    icon_class_path='mayan.apps.documents.icons.icon_document_version_download',
#    permissions=(permission_document_file_download,), text=_('Download version'),
#    view='documents:document_version_download_form'
#)
link_document_version_return_to_document = Link(
    args='resolved_object.document.pk',
    icon_class=icon_document_version_return_document,
    permissions=(permission_document_view,), text=_('Document'),
    view='documents:document_preview'
)
link_document_version_return_list = Link(
    args='resolved_object.document.pk',
    icon_class=icon_document_version_return_list,
    permissions=(permission_document_version_view,), text=_('Versions'),
    view='documents:document_version_list'
)
link_document_version_preview = Link(
    args='resolved_object.pk', icon_class=icon_document_version_preview,
    permissions=(permission_document_version_view,),
    text=_('Preview'), view='documents:document_version_preview'
)