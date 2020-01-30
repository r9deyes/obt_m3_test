from objectpack.actions import ObjectPack
from objectpack.filters import ColumnFilterEngine
from objectpack.filters import FilterByField
from objectpack.ui import ModelEditWindow

from . import ui
from .controller import observer

from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.models import User, Group, Permission


class DjangoContentTypePack(ObjectPack):
    
    model = ContentType
    
    add_to_menu = True
    add_to_desktop = True
    add_window = edit_window = ModelEditWindow.fabricate(
        model=ContentType, 
        model_register=observer,
    )


class DjangoUserPack(ObjectPack):
    
    model = User
    add_to_menu = True
    add_to_desktop = True
    edit_window = add_window = ui.DjangoUserEditWindow
    
    columns = [
        {
            'data_index': 'username',
            'header': u'Имя пользователя',
        },
        {
            'data_index': 'email',
            'header': u'email',
        }
    ]


class DjangoGroupPack(ObjectPack):
    
    model = Group
    add_to_menu = True
    add_to_desktop = True
    add_window = edit_window = ModelEditWindow.fabricate(
        model=Group, 
        model_register=observer,
    )
    
    columns = [
        {
            'data_index': 'name',
            'header': u'Название группы',
        },
        {
            'data_index': 'permissions',
            'header': u'Права доступа',
        }
    ]


class DjangoPermissionPack(ObjectPack):
    
    model = Permission
    
    add_to_menu = add_to_desktop = True

    add_window = edit_window = ui.DjangoPermissionEditWindow
