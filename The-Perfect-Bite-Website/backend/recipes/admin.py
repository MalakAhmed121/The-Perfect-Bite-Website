from django.contrib import admin
from .models import Recipe, Category, Favorite

# 1. تخصيص عرض التصنيفات (Categories)
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'get_recipes_count') # عرض الاسم وعدد الوصفات في التصنيف
    search_fields = ('name',)

    # ميثود إضافية لبيان عدد الوصفات في كل تصنيف
    def get_recipes_count(self, obj):
        return obj.recipes.count()
    get_recipes_count.short_description = 'Number of Recipes'


# 2. تخصيص عرض الوصفات (Recipes) - النسخة المطورة
@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    # الأعمدة التي ستظهر في الجدول الرئيسي للأدمن
    list_display = ('title', 'category', 'diet_type', 'author', 'prep_time', 'calories', 'created_at')
    
    # فلاتر جانبية ذكية للوصول السريع
    list_filter = ('category', 'diet_type', 'author', 'created_at')
    
    # إمكانية البحث بالعنوان، المكونات، أو الوصف
    search_fields = ('title', 'ingredients', 'description')
    
    # جعل الـ Slug يتولد تلقائياً بمجرد كتابة العنوان (SEO Friendly)
    prepopulated_fields = {'slug': ('title',)}
    
    # ترتيب الحقول داخل صفحة إضافة/تعديل الوصفة بشكل منظم (Fieldsets)
    fieldsets = (
        ('Basic Information', {
            'fields': ('title', 'slug', 'category', 'author', 'image')
        }),
        ('Healthy Details', {
            'description': 'Specific info for the Healthy Food page',
            'fields': ('diet_type', 'prep_time', 'calories'),
        }),
        ('Content Details', {
            'fields': ('description', 'ingredients', 'instructions'),
            'classes': ('collapse',), # تجعل القسم قابلاً للطي لتقليل الزحمة
        }),
        ('Metadata', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',),
        }),
    )
    
    # حقول للقراءة فقط (لا يمكن للأدمن تعديل وقت الإنشاء يدوياً)
    readonly_fields = ('created_at', 'updated_at')

# 3. تخصيص عرض المفضلة (Favorites)
@admin.register(Favorite)
class FavoriteAdmin(admin.ModelAdmin):
    list_display = ('user', 'recipe', 'added_at')
    list_filter = ('user', 'added_at')
    