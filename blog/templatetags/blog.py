from django import template

register = template.Library()

# テンプレートタグだよという証
@register.simple_tag
def replace(request, key, value):
    #  request.GETで取得した値は配列になっている
    url_dict = request.GET.copy()
    url_dict[key] = value

    return url_dict.urlencode()