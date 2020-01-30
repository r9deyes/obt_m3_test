from objectpack.ui import BaseEditWindow, make_combo_box, _create_dict_select_field, ObjectTab, TabbedEditWindow, ObjectGridTab
from m3_ext.ui import all_components as ext
from django.db import models as django_models
from django.contrib.auth.models import Group
from . import controller
from . import models


class DjangoUserCRUWindow(BaseEditWindow):

    def _init_components(self):
        """
        Здесь следует инициализировать компоненты окна и складывать их в
        :attr:`self`.
        """
        super(DjangoUserCRUWindow, self)._init_components()
        self.model_register=controller.observer
        self.field__username = ext.ExtStringField(
            label=u'Логин',
            name='username',
            allow_blank=False,
            anchor='100%')

        self.field__password = ext.ExtStringField(
            label=u'Пароль',
            name='password',
            allow_blank=False,
            input_type="password",
            anchor='100%')            
            
        self.field__first_name = ext.ExtStringField(
            label=u'Имя',
            name='first_name',
            allow_blank=True,
            anchor='100%')      

        self.field__last_name = ext.ExtStringField(
            label=u'Фамилия',
            name='last_name',
            allow_blank=True,
            anchor='100%')

        self.field__email = ext.ExtStringField(
            label=u'E-mail',
            name='email',
            allow_blank=True,
            anchor='100%')

        self.field__is_staff = ext.ExtCheckBox(
            label=u'Администрация',
            name='is_staff',
            anchor='100%',
            checked = False)
            
        self.field__is_active= ext.ExtCheckBox(
            label=u'Активен',
            name='is_active',
            anchor='100%',
            checked = True)


    def _do_layout(self):
        """
        Здесь размещаем компоненты в окне
        """
        super(DjangoUserCRUWindow, self)._do_layout()
        self.form.items.extend((
            self.field__username,
            self.field__password,
            self.field__first_name,
            self.field__last_name,
            self.field__email,
            self.field__is_staff,
            self.field__is_active,           
        ))

    def set_params(self, params):
        """
        Установка параметров окна

        :params: Словарь с параметрами, передается из пака
        """
        super(DjangoUserCRUWindow, self).set_params(params)
        self.height = 'auto'


class DjangoUserAddWindow(DjangoUserCRUWindow):
    
    def _init_components(self):
        super(DjangoUserAddWindow,self)._init_components()
    
    def _do_layout(self):
        super(DjangoUserAddWindow,self)._do_layout()
    
    def set_params(self, params):
        super(DjangoUserAddWindow, self).set_params(params)


class DjangoGroupTab(ObjectTab.fabricate(
        model=Group, field_list=('name',))):
    
    def init_components(self, *args, **kwargs):
        super(DjangoGroupTab, self).init_components(*args, **kwargs)
        self.field__user = ext.ExtMultiSelectField(
            label=u'Пользователи'
        )
        self._controls.append(self.field__user)
        self.model_register=controller.observer
    
    def set_params(self, *args, **kwargs):
        super(DjangoGroupTab, self).set_params(*args, **kwargs)
        self.field__user.pack = 'app.actions.DjangoUserPack'
        self.field__user.display_field = 'username'


class DjangoUserEditWindow(TabbedEditWindow):
    
    tabs = [
        DjangoGroupTab,
        ObjectGridTab.fabricate_from_pack(
            pack_name = 'app.actions.DjangoUserPack',
            pack_register = controller.observer
        ),
    ]

class DjangoPermissionEditWindow(BaseEditWindow):   

    def _init_components(self):
        """
        Здесь следует инициализировать компоненты окна и складывать их в
        :attr:`self`.
        """
        super(DjangoPermissionEditWindow, self)._init_components()
        self.model_register=controller.observer
        self.field__name = ext.ExtStringField(
            label=u'Название',
            name='name',
            allow_blank=False,
            anchor='100%')
        
        self.field__content_type = ext.ExtDictSelectField(
            label=u'Тип контента',)

        
        self.field__codename = ext.ExtStringField(
            label=u'Кодовое имя',
            name='codename',
            allow_blank=False,
            anchor='100%')
    
    def _do_layout(self):
        """
        Здесь размещаем компоненты в окне
        """
        super(DjangoPermissionEditWindow, self)._do_layout()
        self.form.items.extend((
            self.field__name,
            self.field__content_type,
            self.field__codename,   
        ))

    def set_params(self, params):
        """
        Установка параметров окна

        :params: Словарь с параметрами, передается из пака
        """
        super(DjangoPermissionEditWindow, self).set_params(params)
        self.field__content_type.pack='app.actions.DjangoContentTypePack'
        self.field__content_type.display_field= '__unicode__'
        self.height = 'auto'


#================================================================================#

class AnswerEditWindow(BaseEditWindow):
    def _init_components(self):
        super(AnswerEditWindow,self)._init_components()
        self.model_register=controller.observer   
        self.field__text = ext.ExtStringField(
            label=u'Ответ',
            name='text',
            allow_blank=False,
            anchor='100%',
        )
        
        self.field__is_correct = ext.ExtCheckBox(
            label=u'Правильный',
            name='is_correct',
            anchor='100%',
            checked = False,
        )
        
        # for f in models.Answer._meta.fields:
            # if isinstance(f, django_models.ForeignKey):
        self.field__question = ext.ExtDictSelectField(#_create_dict_select_field(
            models.Answer._meta.get_field('question'), 
            model_register=controller.observer,
            label=u'Вопрос',
            name='question',
            anchor='100%',
        )
        
        
    
    def _do_layout(self):
        super(AnswerEditWindow,self)._do_layout()
        self.form.items.extend((
            self.field__text,
            self.field__is_correct,
            self.field__question,
        ))
    
    def set_params(self, params):
        super(AnswerEditWindow, self).set_params(params)
        self.height='auto'
