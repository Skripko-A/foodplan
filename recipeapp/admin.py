from django.contrib import admin

from recipeapp.models import Ingredient, Dish, RecipeItem, Menu


class RecipeItemInline(admin.TabularInline):
    model = RecipeItem
    extra = 5


@admin.register(Ingredient)
class IngredientAdmin(admin.ModelAdmin):
    search_fields = ('title',)
    list_display = ('title', 'units', 'price')


@admin.register(Dish)
class DishAdmin(admin.ModelAdmin):
    search_fields = ('title',)
    list_display = ('title',)
    inlines = [RecipeItemInline]


@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    list_display = ('breakfast', 'lunch', 'dinner', 'created_at')
