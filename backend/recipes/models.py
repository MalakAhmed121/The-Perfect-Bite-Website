from django.db import models


# ده "الجدول" اللي هيتخزن فيه وصفات الـ Healthy
class HealthyRecipe(models.Model):
    # خيارات نوع الدايت عشان تختار منها في لوحة التحكم[cite: 11]
    DIET_CHOICES = [
        ('keto', 'Keto Friendly'),
        ('vegan', 'Vegan / Vegetarian'),
        ('protein', 'High Protein'),
        ('gluten-free', 'Gluten-Free'),
    ]
    
    title = models.CharField(max_length=200) # عنوان الوجبة
    description = models.TextField() # وصف قصير
    ingredients = models.TextField() # المكونات (هنكتبها ونفصل بينها بفصلة)
    preparation_steps = models.TextField() # طريقة التحضير
    calories = models.IntegerField() # السعرات الحرارية
    prep_time = models.IntegerField() # وقت التحضير بالدقائق
    diet_type = models.CharField(max_length=20, choices=DIET_CHOICES) # نوع الدايت
    image = models.ImageField(upload_to='healthy_photos/') # صورة الوجبة

    def __str__(self):
        return self.title # عشان لما تظهر في لوحة التحكم تظهر باسمها