# coding:utf-8
from django.db import models
from django.contrib import admin


class Article(models.Model):
	title = models.CharField(u'标题', max_length=256)
	content = models.TextField(u'内容')
	pub_date = models.DateTimeField(u'发表时间', auto_now_add=True, editable=True)
	update_time = models.DateTimeField(u'更新时间', auto_now=True, null=True)
	class Meta:
		verbose_name_plural = '博文'

class Publisher(models.Model):
	name = models.CharField(u'标题',max_length=30)
	address = models.CharField(u'添加',max_length=50)
	city = models.CharField(u'城市',max_length=60)
	state_privince = models.CharField(u'省',max_length=30)
	country = models.CharField(u'国家',max_length=50)
	website = models.URLField(u'网站')
	class Meta:
		verbose_name_plural = '地区'

class Author(models.Model):
	first_name = models.CharField(max_length=30)
	last_name = models.CharField(max_length=40)
	email = models.EmailField(u'邮箱')

class Book(models.Model):
	title2 = models.CharField(max_length=100)
	authors = models.ManyToManyField(Author)
	publisher = models.ForeignKey(Publisher)
	publication_date = models.DateField()

class ArticleAdmin(admin.ModelAdmin):
	list_display = ('title','pub_date')


admin.site.register(Article,ArticleAdmin)
admin.site.register(Author)
admin.site.register(Publisher)
admin.site.register(Book)