from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html
from .models import Post, Category, Tag

# superuser
# name: miniyang9
# email: 20136261@cqu.edu.cn
# password: zhangyang


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'status', 'is_nav', 'created_time', 'post_count')    # 显示的属性
    fields = ('name', 'status', 'is_nav')                                   # 输入的属性

    def post_count(self, obj):
        return obj.post_set.count()
    post_count.short_description = "文章数量"

    def save_model(self, request, obj, form, change):                       # save函数将request.user传给owner
        obj.owner = request.user                                            # 实现控制owner选择的目的
        return super(CategoryAdmin, self).save_model(request, obj, form, change)


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('name', 'status', 'created_time')
    fields = ('name', 'status')

    def save_model(self, request, obj, form, change):
        obj.owner = request.user
        return super(TagAdmin, self).save_model(request, obj, form, change)


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'status', 'created_time', 'operator')
    list_display_links = []
    list_filter = ['category', ]
    search_fields = ['title', 'category__name']

    actions_on_top = True
    actions_on_bottom = True

    save_on_top = True

    fields = (('category', 'title'), 'desc', 'status', 'content', 'tag')

    def operator(self, obj):
        return format_html('<a href="{}">编辑</a>', reverse('admin:blog_post_change', args=(obj.id, )))
    operator.short_description = '操作'

    def save_model(self, request, obj, form, change):
        obj.owner = request.user
        print(f"request: {request}")
        print(f"obj: {obj}")
        print(f"form: {form}")
        print(f"change: {change}")
        return super(PostAdmin, self).save_model(self, obj, form, change)
