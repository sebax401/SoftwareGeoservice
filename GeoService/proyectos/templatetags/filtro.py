from django import template

register = template.Library()

@register.filter
def formato_monto(valor):
    try:
        return f"{int(valor):,}".replace(",", ".")
    except (ValueError, TypeError):
        return valor