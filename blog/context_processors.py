# カウントさせる
from django.db.models import Count, Q

from blog.models import Category,Tag

def common(request):
    context = {
        # キーとvaluの設定 anotateは新しく情報を追加できる。カウントの設定
        'categories':Category.objects.annotate(
            # postの数で公開すみになっているものだけ取得する
            # Qオブジェクトは条件の絞り込み
            count = Count('post',Q(post__is_published=True))
        ),
        # タグは全て取得する
        'tags': Tag.objects.all(),
    }
    return context