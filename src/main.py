from kivymd.app import MDApp
from kivy.lang.builder import Builder
from kivymd.uix.button import MDFlatButton
from helpers import screen_helper
from kivy.core.window import Window
from kivymd.uix.dialog import MDDialog
from kivy.uix.screenmanager import SwapTransition, SlideTransition
import webbrowser
from kivy.uix.scrollview import ScrollView
from kivy.properties import StringProperty


class ScrolllabelLabel(ScrollView):
    text = StringProperty('')

class CaseInApp(MDApp):

    def build(self):
        self.no = True
        self.theme_cls.primary_palette = "Indigo"
        self.theme_cls.primary_hue = "700"
        self.train_dict = {'home_train': False, 'messenger_train': False, 'map_train': False,
                           'profile_train': False, 'tasks_train': False}
        screen = Builder.load_string(screen_helper)
        return screen

    def open_link(self, link):
        webbrowser.open(link)

    def training(self, screen):
        if not self.train_dict[screen] and not self.no:
            self.root.ids.manager.transition = SwapTransition()
            self.root.ids.navigator.opacity = 0
            self.root.ids.manager.current = screen
            self.dialog.dismiss()
            self.root.ids.navigator.disabled = True
            self.train_dict[screen] = True
        else:
            pass

    def switch(self, screen):
        self.no = False
        self.training(screen)

    def done(self, screen):
        if screen == 'video':
            self.root.ids.video.secondary_text = ' '
            self.root.ids.video_icon.icon = 'check'
            self.root.ids.video_player.state = 'pause'
        elif screen == 'reading':
            self.root.ids.reading.secondary_text = ' '
            self.root.ids.read_icon.icon = 'check'
        elif screen == 'add':
            self.root.ids.cov.secondary_text = ' '
            self.root.ids.cov_icon.icon = 'check'
        self.root.ids.manager.current = 'tasks'

    def exit_training(self, screen):
        self.root.ids.manager.transition = SlideTransition()
        self.root.ids.manager.current = screen
        self.root.ids.navigator.opacity = 1
        self.root.ids.navigator.disabled = False


    def open_doc(self):
        webbrowser.open('https://drive.google.com/file/d/1KvGlyXc5FFb2O1RUtM-Of8IWqy8-tjjQ/view')
        self.dialog.dismiss()

    def back(self):
        self.root.ids.video_player.state = 'pause'
        self.root.ids.manager.current = 'tasks'

    def documentation(self):
        self.dialog = MDDialog(title='Хотите просмотреть документацию?',
                          size_hint=(0.8, 1),
                          buttons=[MDFlatButton(text='Да', on_release=lambda x: self.open_doc()),
                                    MDFlatButton(text='Нет', on_release=lambda x: self.dialog.dismiss())]
                          )
        self.dialog.open()

    def login(self):
        logins = {'user': 'user', 'admin': 'admin'}
        if self.root.ids.login.text in logins and self.root.ids.password.text == logins[self.root.ids.login.text]:
            self.root.ids.manager.current = 'home'
            self.root.ids.navigator.opacity = 1
            self.root.ids.atom.opacity = 1
            self.root.ids.top_bar.opacity = 1
            self.root.ids.navigator.disabled = False
            self.root.ids.top_bar.disabled = False
            if self.root.ids.login.text == 'user':
                self.dialog = MDDialog(title='Приветствуем в OnBoard! Включить режим обучения?',
                                       size_hint=(0.8, 1),
                                       buttons=[MDFlatButton(text='Да', text_color=self.theme_cls.primary_color,
                                                             on_release=lambda x: self.switch('home_train')),
                                                MDFlatButton(text='Нет', on_release=lambda x: self.dialog.dismiss())]
                                       )
                self.dialog.open()
            if not self.root.ids.check1.active:
                self.root.ids.password.text = ''
        # elif not self.root.ids.login.text:
        #     self.root.ids.top_bar.disabled = False
        #     self.root.ids.manager.current = 'home'
        #     self.root.ids.navigator.opacity = 1
        #     self.root.ids.navigator.disabled = False
        #     self.root.ids.atom.opacity = 1
        #     self.root.ids.top_bar.opacity = 1
        #     # self.dialog = MDDialog(title='Приветствуем в OnBoard! Включить режим обучения?',
        #     #                        size_hint=(0.8, 1),
        #     #                        buttons=[MDFlatButton(text='Да', text_color=self.theme_cls.primary_color,
        #     #                                              on_release=lambda x: self.switch('home_train')),
        #     #                                 MDFlatButton(text='Нет', on_release=lambda x: self.dialog.dismiss())]
        #     #                        )
        #     # self.dialog.open()
        #     self.root.ids.login.hint_text = 'Введите логин'


        else:
            dialog = MDDialog(title='Неправильный логин или пароль. Попробуйте \n user: user \n admin: admin',
                                   size_hint=(0.8, 1),
                                   buttons=[MDFlatButton(text='Close', on_release=lambda x: dialog.dismiss())]
                                   )
            dialog.open()

    def exit(self):
        self.dialog = MDDialog(title='Вы действительно хотите выйти?',
                          size_hint=(0.8, 1),
                          buttons=[MDFlatButton(text='Да', on_release=lambda x: self.logout()),
                                   MDFlatButton(text='Нет', on_release=lambda x: self.dialog.dismiss())]
                          )
        self.dialog.open()

    def progress(self):
        self.root.ids.manager.current = 'tasks'
        self.root.ids.navigator.switch_tab('tasks_item')

    def logout(self):
        self.root.ids.navigator.switch_tab('home_item')
        self.root.ids.manager.transition = SlideTransition()
        self.root.ids.manager.current = 'auth'
        self.root.ids.navigator.opacity = 0
        self.root.ids.atom.opacity = 0
        self.root.ids.top_bar.opacity = 0
        self.no = True
        self.train_dict = {'home_train': False, 'messenger_train': False, 'map_train': False,
                           'profile_train': False, 'tasks_train': False}
        self.dialog.dismiss()
        self.root.ids.scroll_home.scroll_y = 1
        self.root.ids.scroll_messenger.scroll_y = 1
        self.root.ids.scroll_tasks.scroll_y = 1
        self.root.ids.scroll_map.scroll_y = 1
        self.root.ids.scroll_profile.scroll_y = 1
        self.root.ids.top_bar.disabled = True
        self.root.ids.navigator.disabled = True


if __name__ == '__main__':
    CaseInApp().run()
