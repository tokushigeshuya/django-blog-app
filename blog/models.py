from django.db import models

# Create your models here.
class Post(models.Model):
  # ブログ記事のタイトル（200文字制限）
  title = models.CharField("タイトル",max_length=200)
  # ブログ記事の内容
  content = models.TextField("本文",blank=True)
  # 作成日時 auto_now_add=Trueでインスタンスの作成(DBにINSERT)する度に更新される
  created_at = models.DateTimeField("作成日",auto_now_add=True)
  # 更新日時 auto_now=Trueの場合はモデルインスタンスを保存する度に現在の時間で更新
  updated_at = models.DateTimeField("更新日",auto_now=True)
  # boolean型の真偽値（記事の公開設定）
  is_published = models.BooleanField("公開設定",default=False)

  # 管理画面で記事のタイトルを表示させる
  def __str__(self):
    return self.title