from django.db import models

# Create your models here.
class Category(models.Model):
  name = models.CharField(verbose_name="カテゴリー",max_length=255)
  # URLを保存するフィールド（英数字とハイフン、アンダースコアの使用が可能）※重複があるとまずいのでuniqueをTrueにする
  slug = models.SlugField(verbose_name="URL",unique=True)
  def __str__(self):
    return self.name

class Tag(models.Model):
  name = models.CharField(verbose_name="タグ",max_length=255)
  # URLを保存するフィールド（英数字とハイフン、アンダースコアの使用が可能）※重複があるとまずいのでuniqueをTrueにする
  slug = models.SlugField(verbose_name="URL",unique=True)
  def __str__(self):
    return self.name

class Post(models.Model):
  # ブログ記事のタイトル（200文字制限）
  title = models.CharField(verbose_name="タイトル",max_length=200)
  # ブログ記事の内容
  content = models.TextField(verbose_name="本文",blank=True)
  # 作成日時 auto_now_add=Trueでインスタンスの作成(DBにINSERT)する度に更新される
  created_at = models.DateTimeField(verbose_name="作成日",auto_now_add=True)
  # 更新日時 auto_now=Trueの場合はモデルインスタンスを保存する度に現在の時間で更新
  updated_at = models.DateTimeField(verbose_name="更新日",auto_now=True)
  # boolean型の真偽値（記事の公開設定）
  is_published = models.BooleanField(verbose_name="公開設定",default=False)

  # 1対Nの関係　カテゴリ1に対しPoatがN ※on_deleteは削除したいカテゴリにPostが存在した場合削除させない
  category = models.ForeignKey(
      Category, 
      verbose_name="カテゴリー", 
      on_delete=models.PROTECT, 
      null=True, 
      blank=True
    )
  
  # 多 対 多の関係はManyToManyField
  tag = models.ManyToManyField(Tag, verbose_name="タグ", blank=True)

  # 管理画面で記事のタイトルを表示させる
  def __str__(self):
    return self.title