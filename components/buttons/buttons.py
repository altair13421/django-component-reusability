from django_viewcomponent import component


@component.register("button")
class ButtonComponent(component.Component):
    template = '<button class="btn {{ self.extra_css }}" type="button">{{ self.content }}</button>'

    size_map = {
        "sm": "btn-sm",
        "lg": "btn-lg",
    }

    variant_map = {
        "primary": "btn-primary",
        "secondary": "btn-secondary",
        "success": "btn-success",
        "danger": "btn-danger",
        "warning": "btn-warning",
        "info": "btn-info",
        "light": "btn-light",
        "dark": "btn-dark",
    }

    def __init__(self, variant="primary", size=None, **kwargs):
        self.variant = variant
        self.extra_css = kwargs.get("extra_css", "")
        self.content = kwargs.get("content", "")

        if self.variant and self.variant in self.variant_map:
            self.extra_css += f" {self.variant_map[self.variant]}"

        # append css class to the extra_css
        if size and size in self.size_map:
            self.extra_css += f" {self.size_map[size]}"
