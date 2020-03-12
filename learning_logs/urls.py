"""Определяет схемы URL для learning_logs."""

from django.urls import path

from .views import index, topics, topic, new_topic, new_entry, edit_entry

app_name = 'learning_logs'
urlpatterns = [
    #Домашняя страница
    path('', index, name='index'),
    #Вывод всех тем.
    path('topics/', topics, name='topics'),
    #Страница с подробной информацией по отдельной теме
    path('topics/<int:topic_id>/', topic, name='topic'),
    #Страница для добавления новой темы
    path('new_topic/', new_topic, name='new_topic'),
    #Страница для добавления новой записи
    path('new_entry/<int:topic_id>/', new_entry, name='new_entry'),
    #Страница редактирования записи
    path('edit_entry/<int:entry_id>/', edit_entry, name ='edit_entry')
]
