from django.conf.urls import url
from objectpack import desktop
from app.controller import controller

from . import actions
#from . import controller

def register_urlpatterns():
  """
  Регистрация конфигурации урлов для приложения
  """
  return [url(*controller.urlpattern)]

def register_actions():
  """
  Регистрация экшен-паков

   """
  return controller.packs.extend([

    actions.DjangoContentTypePack(),
    actions.DjangoUserPack(),
    actions.DjangoGroupPack(),
    actions.DjangoPermissionPack(),
    actions.DjangoUserGroupsPack(),
    actions.QuestionPack(),
    actions.AnswerPack(),

   ])

def register_desktop_menu():
  """
  регистрация элементов рабочего стола
  """
  desktop.uificate_the_controller(
      controller,
      menu_root=desktop.MainMenu.SubMenu('App')
  )