from m3.actions.results import OperationResult

from objectpack.actions import BaseAction
from objectpack.actions import ObjectPack
from objectpack.actions import SelectorWindowAction
from objectpack.filters import ColumnFilterEngine
from objectpack.filters import FilterByField
from objectpack.slave_object_pack.actions import SlavePack
from objectpack.tools import extract_int_list
from objectpack.ui import ModelEditWindow

from m3_ext.ui import all_components as ext

from . import models
from . import ui
from .controller import observer

from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.models import User
from django.contrib.auth.models import Group
from django.contrib.auth.models import Permission


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
    edit_window = add_window  = ui.DjangoUserAddWindow
    
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
    add_window =  ModelEditWindow.fabricate(
        model=Group, 
        model_register=observer,
    )
    edit_window = ui.DjangoUserEditWindow
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
    
    #parents = ['content_type']
    add_to_menu = True
    add_to_desktop = True

    add_window = edit_window = ui.DjangoPermissionEditWindow


class DjangoUserGroupsPack(SlavePack):
    model = User

    parents = ['groups']
    can_delete = True

    add_to_menu = add_to_desktop = True
    add_window = edit_window = ui.DjangoUserEditWindow
    
    def __init__(self):
        super(DjangoUserGroupsPack,self).__init__()
        
        self.save_user_groups_action = SaveUserGroupsAction()
        self.select_group_action = SelectGroupAction()
        
        self.replace_action('new_window_action', self.select_group_action)
        self.actions.append(self.save_user_groups_action)
        #self.model._meta.verbose_name= u'UserGroup'

    
class SaveUserGroupsAction(BaseAction):
    
    url = r'/save_user_groups$'
    
    def run(self, request, context):
        ids = extract_int_list(request, 'id')
        for i in ids:
            #obj = Group(group_id=i)
            obj = Group.objects.get(pk=i)
            self.parent.save_row(obj, True, request, context)
        return OperationResult()
    

class SelectGroupAction(SelectorWindowAction):
    
    def configure_action(self, request, context):
        self.callback_url = self.parent.save_user_groups_action.get_absolute_url()
        self.data_pack = self.parent._get_model_pack('Group')
    
    #ModelEditWindow.fabricate(
        #model        = Permission)
        # , 
        # content_type = ext.ExtDictSelectField(
            # label=u'Тип контента',
            # _pack=DjangoContentTypePack
        # )
    # )
"""   
    def create_edit_window(self, create_new, request, context):
        win = super(DjangoPermissionPack,self).create_edit_window(
            create_new, request, context)
        # def _init_components(_self):
            # super(win.__class__, _self)._init_components()
            # _self.field__content_type = ext.ExtDictSelectField(
                # label   = u'Тип контента',
            # )
        # win.field__content_type.configure_by_dictpack(DjangoContentTypePack)
        # win._init_components
    
    def get_edit_window_params(self, params, request, context):
        params = super(DjangoPermissionPack, self).get_edit_window_params(
            params, request, context)
        # params.update({
            # 'content_type': request.content_type,
            # })
        return params
"""


#=================================================================#

class QuestionPack(ObjectPack):
    model = models.Question
    add_to_menu = add_to_desktop = True
    add_window = edit_window = ModelEditWindow.fabricate(
        model=models.Question,
        model_register=observer,
    )
    
class AnswerPack(ObjectPack):
    model = models.Answer
    add_to_menu = add_to_desktop = True
    add_window = edit_window = ui.AnswerEditWindow #ModelEditWindow.fabricate(model=models.Answer)