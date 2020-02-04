from objectpack.ui import BaseEditWindow, make_combo_box, _create_dict_select_field
from m3_ext.ui import all_components as ext

from django.contrib.auth.models import Group, Permission
from django.utils import timezone
from . import controller
from . import models


class DjangoUserEditWindow(BaseEditWindow):

    def _init_components(self):
        super(DjangoUserEditWindow, self)._init_components()
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

        self.field__date_joined = ext.ExtDateField(
            label=u'Дата создания',
            name='date_joined',
            anchor='100%',
            value={'default':timezone.now(),'format':'d m, Y',},
            format = 'd m, Y',
            )

        self.field__last_login = ext.ExtDateField(
            label=u'Последний вход',
            name='last_login',
            anchor='100%',
            )
        
        self.field__is_superuser = ext.ExtCheckBox(
            label=u'Суперпользователь',
            name='is_superuser',
            anchor='100%',
            )
    


    def _do_layout(self):
        super(DjangoUserEditWindow, self)._do_layout()
        self.form.items.extend((
            self.field__username,
            self.field__password,
            self.field__first_name,
            self.field__last_name,
            self.field__email,
            self.field__date_joined,
            self.field__is_staff,
            self.field__is_superuser,
            self.field__is_active,  
            self.field__last_login,
        ))

    def set_params(self, params):
        super(DjangoUserEditWindow, self).set_params(params)
        self.height = 'auto'


class DjangoPermissionEditWindow(BaseEditWindow):   

    def _init_components(self):
        
        super(DjangoPermissionEditWindow, self)._init_components()
        self.model_register=controller.observer
        self.field__name = ext.ExtStringField(
            label=u'Название',
            name='name',
            allow_blank=False,
            anchor='100%')
        
        self.field__content_type = _create_dict_select_field(
            Permission._meta.get_field('content_type'), 
            model_register=controller.observer,
            label=u'Тип контента',
            name='content_type',
            anchor='100%',
        )

        
        self.field__codename = ext.ExtStringField(
            label=u'Кодовое имя',
            name='codename',
            allow_blank=False,
            anchor='100%')
    
    def _do_layout(self):
        super(DjangoPermissionEditWindow, self)._do_layout()
        self.form.items.extend((
            self.field__name,
            self.field__content_type,
            self.field__codename,   
        ))

    def set_params(self, params):
        super(DjangoPermissionEditWindow, self).set_params(params)
        #elf.field__content_type.pack='app.actions.DjangoContentTypePack'
        #self.field__content_type.display_field= '__unicode__'
        self.height = 'auto'
