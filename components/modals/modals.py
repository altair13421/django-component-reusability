from django_viewcomponent import component
from django_viewcomponent.fields import RendersOneField


@component.register("modal")
class ModalComponent(component.Component):
    modal_trigger = RendersOneField()
    modal_body = RendersOneField(required=True)
    modal_footer = RendersOneField(required=True)

    template_name = "modals/modals.html"

    def __init__(self, modal_id, modal_title, **kwargs):
        self.modal_id = modal_id
        self.modal_title = modal_title