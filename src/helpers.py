
screen_helper = """
#:import SlideTransition kivy.uix.screenmanager.SlideTransition
#:import ScrolllabelLabel main.ScrolllabelLabel
<ScrolllabelLabel>:
    MDLabel:
        text: root.text
        halign: 'left'
        text_size: self.width, None
        size_hint_y: None
        height: self.texture_size[1]
<Check@MDCheckbox>:
    group: 'group'
    size_hint: None, None
    size: dp(24), dp(24)
<Check1@MDCheckbox>:
    group: 'group1'
    size_hint: None, None
    size: dp(24), dp(24)
<Check2@MDCheckbox>:
    group: 'group2'
    size_hint: None, None
    size: dp(24), dp(24)
<Check3@MDCheckbox>:
    group: 'group3'
    size_hint: None, None
    size: dp(24), dp(24)
<Check4@MDCheckbox>:
    group: 'group4'
    size_hint: None, None
    size: dp(24), dp(24)
AnchorLayout:
    anchor_x: 'left'
    anchor_y: 'top'
    
    BoxLayout:
    
        orientation:'vertical'
        MDToolbar:
            
            title: '                       OnBoard'
            
            opacity: 0
            disabled: True
            id: top_bar
            md_bg_color: (1, 1, 1, 1)
            specific_text_color: (0, 0, 0, 1)
            
            right_action_items: [["file-document-box-search", lambda x: app.documentation()], ["exit-to-app", lambda x: app.exit()]]
            elevation:8
        
        ScreenManager:
            
            id: manager
            
            Screen:
                name: 'auth'
                id: auth
                MDTextField:
                    id: login 
                    hint_text: "Логин"
                    helper_text: ""
                    helper_text_mode: "on_focus"
                    icon_right: "account"
                    icon_right_color: app.theme_cls.primary_color
                    pos_hint:{'center_x': 0.5, 'center_y': 0.6}
                    size_hint_x:None
                    width:auth.width / 1.5
                    
                MDTextField:
                    id: password
                    password: True
                    hint_text: "Пароль"
                    helper_text: ""
                    icon_right: "textbox-password"
                    helper_text_mode: "on_focus"
                    icon_right_color: app.theme_cls.primary_color
                    pos_hint:{'center_x': 0.5, 'center_y': 0.5}
                    size_hint_x:None
                    width:auth.width / 1.5
                MDCheckbox:
                    id: check1
                    size_hint: None, None
                    size: dp(48), dp(48)
                    pos_hint: {'center_x': .3, 'center_y': .4}
                    
                MDLabel:
                    pos_hint: {'center_x': .85, 'center_y': .4}
                    text: 'Запомнить пароль'
                    font_style: 'Body2'
                    theme_text_color: 'Custom'
                    text_color: (68/255, 68/255, 68/255, 1)
                MDRectangleFlatButton:
                    text: 'Войти'
                    pos_hint:{'center_x': 0.5, 'center_y': 0.3}
                    on_release: app.login()
                   
            Screen:
                name: 'home'
                BoxLayout:
                    padding: 10
                    ScrollView:
                        MDList:
                            
                            MDList:
                                OneLineIconListItem:         
                                    text: 'Задачи на сегодня'
                                    theme_text_color: 'Custom'
                                    halign: 'center'
                                    font_style: 'H5'
                                    text_color: (1, 1, 1, 1)
                                    background_color: 9/255, 105/255, 161/255, 1
                                    canvas.before:
                                        Color:
                                            rgba: self.background_color
                                        RoundedRectangle:
                                            radius: [7]
                                            size: self.size[0], self.size[1] + 10
                                            pos: self.pos
                                    
                                    
                                    
                                OneLineIconListItem:
                                    text: 'Прохождение VR-задания'
                                    bg_color: (55/255, 197/255, 219/255, 1)
                                    IconLeftWidget:
                                        icon:'information-outline'
                                    
                                OneLineIconListItem:
                                    text: 'Общение с ментором'
                                    bg_color: (55/255, 197/255, 219/255, 1)
                                    
                                    IconLeftWidget:
                                        icon:'information-outline'
                            MDList:
                                OneLineIconListItem:         
                                    text: 'Расписание'
                                    theme_text_color: 'Custom'
                                    halign: 'center'
                                    font_style: 'H5'
                                    text_color: (1, 1, 1, 1)
                                    background_color: 9/255, 105/255, 161/255, 1
                                    canvas.before:
                                        Color:
                                            rgba: self.background_color
                                        RoundedRectangle:
                                            radius: [7]        
                                            size: self.size[0], self.size[1] + 10
                                            pos: self.pos
                                    
                                    
                                TwoLineIconListItem:
                                    secondary_text: 'Практика в VR-лаборатории'
                                    text: '11.30 - 12.00'
                                    theme_text_color: 'Custom'
                                    text_color: 1, 1, 1, 1
                                    bg_color: (41/255, 160/255, 229/255,1)
                                    
                                    IconLeftWidget:
                                        icon:'clock-outline'
                                TwoLineIconListItem:
                                    secondary_text: 'Обед'
                                    theme_text_color: 'Custom'
                                    text_color: 1, 1, 1, 1
                                    text: '12.00 - 13.00'
                                    
                                    bg_color: (41/255, 160/255, 229/255,1)
                                   
                                    IconLeftWidget:
                                        icon:'clock-outline'
                                TwoLineIconListItem:
                                    secondary_text: 'Общение с ментором'
                                    text: '13.00 - 14.00'
                                    theme_text_color: 'Custom'
                                    text_color: 1, 1, 1, 1
                                    bg_color: (41/255, 160/255, 229/255,1)
                                    
                                    IconLeftWidget:
                                        icon:'clock-outline'
                                MDFlatButton:         
                                    text: 'Прогресс недели:'
                                    theme_text_color: "Custom"
                                    text_color: 0/255, 0/255, 0/255, 1
                                    italic: True
                                    font_size: "18"
                                    size_hint: None, None
                                    halign: 'center'
                                    on_press: app.progress()
                                ProgressBar:
                                    max:100
                                    
                                    value: 76
                
                            GridLayout:
                                size_hint_y: None
                                cols:2
                                   
                                GridLayout:
                                    cols: 2
                                    rows:2
                                    MDIconButton:
                                        halign: "center"
                                        icon: "vk"
                                        on_press: app.open_link('https://vk.com/rosatomru')
                                    MDIconButton:
                                        halign: "center"
                                        icon: "instagram"
                                        on_press: app.open_link('https://www.instagram.com/rosatom_ru')
                                    MDIconButton:
                                        halign: "center"
                                        icon: "twitter"
                                        on_press: app.open_link('https://twitter.com/rosatom?ref_src=twsrc%5Egoogle%7Ctwcamp%5Eserp%7Ctwgr%5Eauthor')
                                    MDIconButton:
                                        halign: "center"
                                        icon: "facebook"
                                        on_press: app.open_link('https://www.facebook.com/rosatom.ru/')
                                BoxLayout:
                                    spacing: 10
                                    orientation: 'vertical'
                                    
                                    MDRoundFlatButton:         
                                        text: 'Новости компании'
                                        theme_text_color: "Custom"
                                        text_color: 1, 1, 1, 1
                                        md_bg_color: 9/255, 105/255, 161/255, 1
                                        line_color: 0, 0, 0, 1
                                        on_press: app.open_link('https://rosatom.ru/')
                                        width: auth.width / 3
                                        halign: 'center'
                                    MDRoundFlatButton:         
                                        text: 'Covid-19'
                                        theme_text_color: "Custom"
                                        text_color: 1, 1, 1, 1
                                        md_bg_color: 55/255, 197/255, 219/255, 1
                                        on_press: app.open_link('https://covid19.rosminzdrav.ru/')
                                        font_size: "24"
                                        width: auth.width / 3
                                        halign: 'center'
            Screen:
                name: 'messenger'
                on_pre_enter: app.training('messenger_train')
                FloatLayout:
                    Image:
                        source: 'unname1d.png'
                BoxLayout:
                    padding: 10
                    ScrollView:
                        MDList:
                            MDList:
                                OneLineIconListItem:         
                                    text: 'Каналы'
                                    theme_text_color: 'Custom'
                                    halign: 'center'
                                    font_style: 'H6'
                                    text_color: (1, 1, 1, 1)
                                    background_color: 6/255, 72/255, 105/255, 1
                                    canvas.before:
                                        Color:
                                            rgba: self.background_color
                                        RoundedRectangle:
                                            radius: [7]        
                                            size: self.size
                                            pos: self.pos
                                    IconLeftWidget:
                                        icon:'plus-thick'
                                OneLineIconListItem:
                                    
                                    text: 'новости'
                                    theme_text_color: 'Custom'
                                    text_color: 1, 1, 1, 1
                                    bg_color: (0/255, 143/255, 226/255,1)
                                    
                                    IconLeftWidget:
                                        icon:'wechat'
                                OneLineIconListItem:
                                    
                                    theme_text_color: 'Custom'
                                    text_color: 1, 1, 1, 1
                                    text: 'знакомства'
                                
                                    bg_color: (14/255, 204/255, 225/255,1)
                                    
                                    IconLeftWidget:
                                        icon:'wechat'
                                OneLineIconListItem:
                                    
                                    text: 'неделя_1'
                                    theme_text_color: 'Custom'
                                    text_color: 1, 1, 1, 1
                                    bg_color: (0/255, 143/255, 226/255,1)
                                    
                                    IconLeftWidget:
                                        icon:'wechat'
                                
                            MDList:
                                OneLineIconListItem:         
                                    text: 'Личные сообщения'
                                    theme_text_color: 'Custom'
                                    halign: 'center'
                                    font_style: 'H6'
                                    text_color: (1, 1, 1, 1)
                                    background_color: 6/255, 72/255, 105/255, 1
                                    canvas.before:
                                        Color:
                                            rgba: self.background_color
                                        RoundedRectangle:
                                            radius: [7]        
                                            size: self.size
                                            pos: self.pos
                                    size_hint: 1, None
                                    
                                OneLineIconListItem:
                                    
                                    text: 'OnBoard_bot'
                                    theme_text_color: 'Custom'
                                    text_color: 1, 1, 1, 1
                                    bg_color: (0/255, 143/255, 226/255,1)
                                    
                                    IconLeftWidget:
                                        icon:'qqchat'
                                OneLineIconListItem:
                                    
                                    theme_text_color: 'Custom'
                                    text_color: 1, 1, 1, 1
                                    text: 'Юлия (ментор)'
        
                                    bg_color: (55/255, 197/255, 219/255,1)
                                    
                                    IconLeftWidget:
                                        icon:'chat'
                                OneLineIconListItem:
                                    
                                    text: 'Новый диалог'
                                    theme_text_color: 'Custom'
                                    text_color: 1, 1, 1, 1
                                    bg_color: (0/255, 143/255, 226/255,1)
                                    
                                    IconLeftWidget:
                                        icon:'plus'
                        
                        
                        
               
            Screen:
                
                name: 'tasks'
                on_pre_enter: app.training('tasks_train')
                BoxLayout:
                    padding: 10
                    ScrollView:
                        MDList:
                            MDLabel:
                                text: 'Неделя 1: Знакомство с рабочим местом'
                                theme_text_color: 'Custom'
                                halign: 'center'
                                font_style: 'H5'
                                text_color: (1, 1, 1, 1)
                                background_color: 9/255, 105/255, 161/255, 1
                                canvas.before:
                                    Color:
                                        rgba: self.background_color
                                    RoundedRectangle:
                                        radius: [7]        
                                        size: self.size[0], self.size[1] + 30
                                        pos: self.pos
                                size_hint: 1, None
                                
                                
                            MDList:
                                MDLabel:
                                    text: 'Материалы для подготовки'
                                    theme_text_color: 'Custom'
                                    halign: 'center'
                                    font_style: 'H5'
                                    text_color: (1, 1, 1, 1)
                                    background_color: 9/255, 105/255, 161/255, 1
                                    canvas.before:
                                        Color:
                                            rgba: self.background_color
                                        RoundedRectangle:
                                            radius: [7]        
                                            size: self.size
                                            pos: self.pos
                                    size_hint: 1, None
                                    
                                    
                                    
                                TwoLineIconListItem:
                                    id : video
                                    text: 'Видео'
                                    theme_text_color: 'Custom'
                                    text_color: 1, 1, 1, 1
                                    bg_color: (41/255, 160/255, 229/255,1)
                                    secondary_text: 'Осталось 4 мин'
                                    on_press: manager.current= "video"
                                    IconLeftWidget:
                                        id: video_icon
                                        icon:'clock-outline'
                                TwoLineIconListItem:
                                    id : reading
                                    secondary_text: 'Осталось 10 мин'
                                    theme_text_color: 'Custom'
                                    text_color: 1, 1, 1, 1
                                    text: 'Материалы для чтения'
                                    on_press: manager.current= "text"
                                    bg_color: (41/255, 160/255, 229/255,1)
                                    
                                    IconLeftWidget:
                                        id: read_icon
                                        icon:'clock-outline'
                                TwoLineIconListItem:
                                    id: cov
                                    secondary_text: 'Осталось 2 мин'
                                    text: 'Дополнительно'
                                    theme_text_color: 'Custom'
                                    text_color: 1, 1, 1, 1
                                    on_press: manager.current= "add"
                                    bg_color: (41/255, 160/255, 229/255,1)
                                    
                                    IconLeftWidget:
                                        id: cov_icon
                                        icon:'clock-outline'
                            
                            MDList:
                                MDLabel:
                                    text: 'Необходимо выполнить:'
                                    theme_text_color: 'Custom'
                                    halign: 'center'
                                    font_style: 'H5'
                                    text_color: (1, 1, 1, 1)
                                    background_color: 9/255, 105/255, 161/255, 1
                                    canvas.before:
                                        Color:
                                            rgba: self.background_color
                                        RoundedRectangle:
                                            radius: [7]        
                                            size: self.size
                                            pos: self.pos
                                    size_hint: 1, None
                                    
                                    
                                TwoLineIconListItem:
                                    secondary_text: 'Последняя оценка: 100%'
                                    text: 'Тест "Техника безопасности"'
                                    theme_text_color: 'Custom'
                                    text_color: 1, 1, 1, 1
                                    on_press: manager.current= "test1"
                                    bg_color: (41/255, 160/255, 229/255,1)
                                    
                                    IconLeftWidget:
                                        icon:'check-circle'
                                TwoLineIconListItem:
                                    secondary_text: 'Последняя оценка: 50%'
                                    text: 'Тест "Тех процесс"'
                                    theme_text_color: 'Custom'
                                    text_color: 1, 1, 1, 1
                                    on_press: manager.current= "test2"
                                   
                                    bg_color: (41/255, 160/255, 229/255,1)
                                    
                                    IconLeftWidget:
                                        icon:'alert-circle'
                                OneLineIconListItem:
                                    secondary_text: ''
                                    text: 'VR-практика'
                                    theme_text_color: 'Custom'
                                    text_color: 1, 1, 1, 1
                                    bg_color: (41/255, 160/255, 229/255,1)
                                  
                                    IconLeftWidget:
                                        icon:'sunglasses'
                            AnchorLayout:
                                size_hint_y: None
                                anchor_x: 'center'
                                anchor_y: 'top'
                                MDRoundFlatButton:         
                                    text: 'Поставить оценку ментору'
                                    theme_text_color: "Custom"
                                    text_color: 76/255, 19/255, 209/255, 1
                                    
                                    line_color: 0, 0, 0, 1
                                    
                                    
                                    halign: 'center'
            
            Screen:
                on_pre_enter: app.training('map_train')
                name: 'map'
                ScrollView:
                    FitImage:
                        source: 'map.jpg'
                    
                    
                   
               
            Screen:
                name: 'profile'
                on_pre_enter: app.training('profile_train')
                FloatLayout:
                    FitImage:
                        source: 'back1.jpg'
                GridLayout:
                    cols:1
                    padding: 10
                    
                    ScrollView:
                        
                        MDList:
                            pos_hint: {'center_y': .5}
                            GridLayout:
                                cols: 2
                                spacing: 20
                                size_hint_y:None
                                Image:
                                    source: '2.png'
                                    
    
                                MDLabel:
                                    text: 'Инеженеров Иван Геннадьевич'
                                    theme_text_color: 'Custom'
                                    halign: 'center'
                                    font_style: 'H6'
                                    text_color: (1, 1, 1, 1)
                                    background_color: 0, 0, 0,1
                                    
                                    canvas.before:
                                        Color:
                                            rgba: self.background_color
                                        RoundedRectangle:
                                            radius: [7]        
                                            size: self.size
                                            pos: self.pos

                          
                                
                            MDList:
                                OneLineListItem:
                                    text: 'АКМЭ-инжинириг, АО'
                                    theme_text_color: 'Custom'
                                    
                                    font_style: 'Subtitle2'
                                    text_color: (1, 1, 1, 1)
                                    background_color: 0, 0, 0,1
                                    canvas.before:
                                        Color:
                                            rgba: self.background_color
                                        Rectangle:
                                            size: self.size
                                            pos: self.pos
                                    
                                    
                                OneLineListItem:
                                    text: 'Отдел: Заготовительный'
                                    theme_text_color: 'Custom'
                                    
                                    font_style: 'Subtitle1'
                                    text_color: (1, 1, 1, 1)
                                    background_color: 9/255, 105/255, 161/255, 1
                                    canvas.before:
                                        Color:
                                            rgba: self.background_color
                                        Rectangle:
                            
                                            size: self.size
                                            pos: self.pos
                                    size_hint: 1, None
                                   
                                OneLineListItem:
                                    text: 'Должность: Технолог'
                                    theme_text_color: 'Custom'
                                    
                                    font_style: 'Subtitle2'
                                    text_color: (1, 1, 1, 1)
                                    background_color: 9/255, 105/255, 161/255, 1
                                    canvas.before:
                                        Color:
                                            rgba: self.background_color
                                        Rectangle:
                            
                                            size: self.size
                                            pos: self.pos
                                OneLineListItem:
                                    text: 'Контакты: +79726486137, evrika@mail.ru'
                                    theme_text_color: 'Custom'
                                    
                                    font_style: 'Subtitle2'
                                    text_color: (1, 1, 1, 1)
                                    background_color: 9/255, 105/255, 161/255, 1
                                    canvas.before:
                                        Color:
                                            rgba: self.background_color
                                        Rectangle:
                                        
                                            size: self.size
                                            pos: self.pos
                            MDList:
                        
                                MDFlatButton:         
                                    text: 'Общий прогресс адаптации:'
                                    theme_text_color: "Custom"
                                    text_color: 0/255, 0/255, 0/255, 1
                                    italic: True
                                    font_size: "18"
                                    size_hint: None, None
                                    halign: 'center'
                                    on_press: app.progress()
                                ProgressBar:
                                    max:100
                                    value: 24
                            MDList:
                                OneLineIconListItem:
                                    
                                    text: 'Мои бонусы: 24/100(7.500р)'
                                    theme_text_color: 'Custom'
                                    text_color: 1, 1, 1, 1
                                    bg_color: (41/255, 160/255, 229/255,1)
                                    
                                    IconLeftWidget:
                                        icon:'sticker-plus'
                                TwoLineIconListItem:
                                    secondary_text: '4 место'
                                    text: 'Мой рейтинг в общем зачете:'
                                    theme_text_color: 'Custom'
                                    text_color: 1, 1, 1, 1
                                    
                                    
                                    bg_color: (41/255, 160/255, 229/255,1)
                                   
                                    IconLeftWidget:
                                        icon:'account-multiple'
                            
            Screen:
                name: 'home_train'
                ScrollView:
                    id: scroll_home
                    do_scroll_x: False
                    BoxLayout:
                        padding: 10
                        spacing: 10
                        orientation: 'vertical'
                        height: self.minimum_height
                        size_hint_y: None
                        MDCard:
                            orientation: 'vertical'
                            pos_hint: {'center_x': .5, 'center_y': .7}
                            size_hint: .7, None
                            height: 1100
                            Image:
                                source: 'home.png'
                        MDCard:
                            orientation: 'vertical'
                            pos_hint: {'center_x': .5, 'center_y': .7}
                            size_hint: .7, None
                            height: 1100
                            Image:
                                source: 'home1.png'
                        MDCard:
                            orientation: 'vertical'
                            pos_hint: {'center_x': .5, 'center_y': .7}
                            size_hint: .7, None
                            height: 1100
                            Image:
                                source: 'home2.png'
                        MDCard:
                            orientation: 'vertical'
                            pos_hint: {'center_x': .5, 'center_y': .7}
                            size_hint: .7, None
                            height: 1100
                            Image:
                                source: 'home3.png'
                        MDLabel:
                            text: 'Не устали? Продолжим!'
                            theme_text_color: 'Custom'
                            halign: 'center'
                            font_style: 'H6'
                            text_color: (1, 1, 1, 1)
                            background_color: 6/255, 72/255, 105/255,1
                            canvas.before:
                                Color:
                                    rgba: self.background_color
                                RoundedRectangle:
                                    radius: [7]        
                                    size: self.size
                                    pos: self.pos
                            size_hint: 1, None
                        MDCard:
                            orientation: 'vertical'
                            pos_hint: {'center_x': .5, 'center_y': .7}
                            size_hint: .7, None
                            height: 1100
                            Image:
                                source: 'home4.png'
                        MDCard:
                            orientation: 'vertical'
                            pos_hint: {'center_x': .5, 'center_y': .7}
                            size_hint: .7, None
                            height: 1100
                            Image:
                                source: 'home5.png'
                        MDCard:
                            orientation: 'vertical'
                            pos_hint: {'center_x': .5, 'center_y': .7}
                            size_hint: .7, None
                            height: 1100
                            Image:
                                source: 'home6.png'
                        MDRectangleFlatButton:         
                            text: 'ОК'
                            theme_text_color: "Custom"
                            text_color: 1, 1, 1, 1
                            md_bg_color: 9/255, 105/255, 161/255, 1
                            line_color: 0, 0, 0, 1
                            pos_hint:{'center_x' : 0.5, 'center_y' : 0.5}
                            halign: 'center'
                            size_hint: None, None
                            on_press: app.exit_training('home')
                            width: auth.width / 3
            Screen:
                name: 'messenger_train'
                ScrollView:
                    id: scroll_messenger
                    do_scroll_x: False
                    BoxLayout:
                        padding: 10
                        spacing: 10
                        orientation: 'vertical'
                        height: self.minimum_height
                        size_hint_y: None
                        MDCard:
                            orientation: 'vertical'
                            pos_hint: {'center_x': .5, 'center_y': .7}
                            size_hint: .7, None
                            height: 1100
                            Image:
                                source: 'chat.png'
                        MDCard:
                            orientation: 'vertical'
                            pos_hint: {'center_x': .5, 'center_y': .7}
                            size_hint: .7, None
                            height: 1100
                            Image:
                                source: 'chat1.png'
                        MDCard:
                            orientation: 'vertical'
                            pos_hint: {'center_x': .5, 'center_y': .7}
                            size_hint: .7, None
                            height: 1100
                            Image:
                                source: 'chat2.png'
                        
                        MDRectangleFlatButton:         
                            text: 'ОК'
                            theme_text_color: "Custom"
                            text_color: 1, 1, 1, 1
                            md_bg_color: 9/255, 105/255, 161/255, 1
                            line_color: 0, 0, 0, 1
                            pos_hint:{'center_x' : 0.5, 'center_y' : 0.5}
                            halign: 'center'
                            size_hint: None, None
                            on_press: app.exit_training('messenger')
                            width: auth.width / 3
            Screen:
                name: 'tasks_train'
                ScrollView:
                    id: scroll_tasks
                    do_scroll_x: False
                    BoxLayout:
                        padding: 10
                        spacing: 10
                        orientation: 'vertical'
                        height: self.minimum_height
                        size_hint_y: None
                        MDCard:
                            orientation: 'vertical'
                            pos_hint: {'center_x': .5, 'center_y': .7}
                            size_hint: .7, None
                            height: 1100
                            Image:
                                source: 'tasks.png'
                        MDCard:
                            orientation: 'vertical'
                            pos_hint: {'center_x': .5, 'center_y': .7}
                            size_hint: .7, None
                            height: 1100
                            Image:
                                source: 'tasks1.png'
                        MDCard:
                            orientation: 'vertical'
                            pos_hint: {'center_x': .5, 'center_y': .7}
                            size_hint: .7, None
                            height: 1100
                            Image:
                                source: 'tasks2.png'
                        MDLabel:
                            text: 'Осталось еще немного...'
                            theme_text_color: 'Custom'
                            halign: 'center'
                            font_style: 'H6'
                            text_color: (1, 1, 1, 1)
                            background_color: 6/255, 72/255, 105/255,1
                            canvas.before:
                                Color:
                                    rgba: self.background_color
                                RoundedRectangle:
                                    radius: [7]        
                                    size: self.size
                                    pos: self.pos
                            size_hint: 1, None
                        MDCard:
                            orientation: 'vertical'
                            pos_hint: {'center_x': .5, 'center_y': .7}
                            size_hint: .7, None
                            height: 1100
                            Image:
                                source: 'tasks3.png'
                        
                        MDCard:
                            orientation: 'vertical'
                            pos_hint: {'center_x': .5, 'center_y': .7}
                            size_hint: .7, None
                            height: 1100
                            Image:
                                source: 'tasks4.png'
            
                        MDRectangleFlatButton:         
                            text: 'ОК'
                            theme_text_color: "Custom"
                            text_color: 1, 1, 1, 1
                            md_bg_color: 9/255, 105/255, 161/255, 1
                            line_color: 0, 0, 0, 1
                            pos_hint:{'center_x' : 0.5, 'center_y' : 0.5}
                            halign: 'center'
                            size_hint: None, None
                            on_press: app.exit_training('tasks')
                            width: auth.width / 3
            Screen:
                name: 'map_train'
                ScrollView:
                    id: scroll_map
                    do_scroll_x: False
                    BoxLayout:
                        padding: 10
                        spacing: 10
                        orientation: 'vertical'
                        height: self.minimum_height
                        size_hint_y: None
                        MDCard:
                            orientation: 'vertical'
                            pos_hint: {'center_x': .5, 'center_y': .7}
                            size_hint: .7, None
                            height: 1100
                            Image:
                                source: 'mapp.png'
                        MDCard:
                            orientation: 'vertical'
                            pos_hint: {'center_x': .5, 'center_y': .7}
                            size_hint: .7, None
                            height: 1100
                            Image:
                                source: 'map1.png'
                        MDRectangleFlatButton:         
                            text: 'ОК'
                            theme_text_color: "Custom"
                            text_color: 1, 1, 1, 1
                            md_bg_color: 9/255, 105/255, 161/255, 1
                            line_color: 0, 0, 0, 1
                            pos_hint:{'center_x' : 0.5, 'center_y' : 0.5}
                            halign: 'center'
                            size_hint: None, None
                            on_press: app.exit_training('map')
                            width: auth.width / 3
            Screen:
                name: 'profile_train'
                ScrollView:
                    id: scroll_profile
                    do_scroll_x: False
                    BoxLayout:
                        padding: 10
                        spacing: 10
                        orientation: 'vertical'
                        height: self.minimum_height
                        size_hint_y: None
                        MDCard:
                            orientation: 'vertical'
                            pos_hint: {'center_x': .5, 'center_y': .7}
                            height: 1100
                            size_hint: .7, None
                            Image:
                                source: 'profile.png'
                        MDCard:
                            orientation: 'vertical'
                            pos_hint: {'center_x': .5, 'center_y': .7}
                            size_hint: .7, None
                            height: 1100
                            Image:
                                source: 'profile1.png'
                        MDLabel:
                            text: 'Почти закончили...'
                            theme_text_color: 'Custom'
                            halign: 'center'
                            font_style: 'H6'
                            text_color: (1, 1, 1, 1)
                            background_color: 6/255, 72/255, 105/255,1
                            canvas.before:
                                Color:
                                    rgba: self.background_color
                                RoundedRectangle:
                                    radius: [7]        
                                    size: self.size
                                    pos: self.pos
                            size_hint: 1, None
                        MDCard:
                            orientation: 'vertical'
                            pos_hint: {'center_x': .5, 'center_y': .7}
                            size_hint: .7, None
                            height: 1100
                            Image:
                                source: 'profile2.png'
                        
                        MDCard:
                            orientation: 'vertical'
                            pos_hint: {'center_x': .5, 'center_y': .7}
                            size_hint: .7, None
                            height: 1100
                            Image:
                                source: 'profile3.png'
                        MDLabel:
                            text: 'И напоследок:'
                            theme_text_color: 'Custom'
                            halign: 'center'
                            font_style: 'H6'
                            text_color: (1, 1, 1, 1)
                            background_color: 6/255, 72/255, 105/255,1
                            canvas.before:
                                Color:
                                    rgba: self.background_color
                                RoundedRectangle:
                                    radius: [7]        
                                    size: self.size
                                    pos: self.pos
                            size_hint: 1, None
                        
                        MDCard:
                            orientation: 'vertical'
                            pos_hint: {'center_x': .5, 'center_y': .7}
                            size_hint: .7, None
                            height: 1100
                            Image:
                                source: 'exit.png'
            
                        MDRectangleFlatButton:         
                            text: 'ОК'
                            theme_text_color: "Custom"
                            text_color: 1, 1, 1, 1
                            md_bg_color: 9/255, 105/255, 161/255, 1
                            line_color: 0, 0, 0, 1
                            pos_hint:{'center_x' : 0.5, 'center_y' : 0.5}
                            halign: 'center'
                            size_hint: None, None
                            on_press: app.exit_training('profile')
                            width: auth.width / 3
                        
            Screen:
                name: 'text'
                id : text
                GridLayout:
                    padding: 10
                    row_force_default: True
                    row_default_height: auth.height / 1.1
                    cols: 1
                    ScrolllabelLabel:
                        text: 'Тепловыделя́ющий элеме́нт (ТВЭЛ) — главный конструктивный элемент активной зоны гетерогенного ядерного реактора, содержащий ядерное топливо. В ТВЭЛах происходит деление тяжёлых ядер 235U или 239Pu, сопровождающееся выделением тепловой энергии, которая затем передаётся теплоносителю. ТВЭЛ должен обеспечить отвод тепла от топлива к теплоносителю и препятствовать распространению радиоактивных продуктов из топлива в теплоноситель.Справа ТВС, большинство ее трубок — ТВЭЛы. Слева ТВЭЛ, оболочка вскрыта и видны топливные таблетки. ТВЭЛ состоит из топливного сердечника, оболочки и установочных деталей. Несколько ТВЭЛов и крепёжно-установочные элементы объединяются в единую конструкцию, которая называется тепловыделяющая сборка (ТВС). Конструкция и материалы ТВЭЛа определяются конструкцией реактора: гидродинамикой и химическим составом теплоносителя, температурными режимами, требованиями к нейтронному потоку. В большинстве реакторов ТВЭЛ представляет собой герметичную трубку из стали или циркониевых сплавов внешним диаметром около сантиметра и длиной десятки — сотни сантиметров, заполненную таблетками ядерного топлива.'
                    GridLayout:
                        rows: 1
                        row_force_default: True
                        row_default_height: auth.height * 0.06
                        spacing: 15
                        
                       
                        MDRectangleFlatButton:         
                            text: 'Назад'
                            theme_text_color: "Custom"
                            text_color: 1, 1, 1, 1
                            md_bg_color: 9/255, 105/255, 161/255, 1
                            line_color: 0, 0, 0, 1
                            
                            halign: 'center'
                            size_hint: 1, 1
                            on_press: manager.current = 'tasks'
                            
                        MDRectangleFlatButton:         
                            text: 'Готово'
                            theme_text_color: "Custom"
                            text_color: 1, 1, 1, 1
                            md_bg_color: 9/255, 105/255, 161/255, 1
                            line_color: 0, 0, 0, 1
                            
                            halign: 'center'
                            size_hint: 1, 1
                            on_press: app.done('reading')
                            
            Screen:
                name: 'video'
                FloatLayout:
                    FitImage:
                        source: 'back2.png'
                GridLayout:
                    cols: 1
                    row_force_default: True
                    row_default_height: auth.height * 0.9
                    BoxLayout:
                        spacing: 20
                        padding: 10
                        orientation: 'vertical'
                        MDLabel:
                            text: 'Топливная компания ТВЭЛ'
                            theme_text_color: 'Custom'
                            halign: 'center'
                            font_style: 'H6'
                            text_color: (1, 1, 1, 1)
                            background_color: 6/255, 72/255, 105/255,1
                            canvas.before:
                                Color:
                                    rgba: self.background_color
                                RoundedRectangle:
                                    radius: [7]        
                                    size: self.size
                                    pos: self.pos
                            size_hint: 1, None
                            height: 70
                        VideoPlayer:
                            id: video_player
                            source: "video.mp4"
                    
                    GridLayout:
                        rows: 1
                        row_force_default: True
                        row_default_height: auth.height * 0.06  
                        spacing: 15
                        padding: 10
                       
                        MDRectangleFlatButton:         
                            text: 'Назад'
                            theme_text_color: "Custom"
                            text_color: 1, 1, 1, 1
                            md_bg_color: 9/255, 105/255, 161/255, 1
                            line_color: 0, 0, 0, 1
                            
                            halign: 'center'
                            size_hint: 1, 1
                            on_press: app.back()
                            
                        MDRectangleFlatButton:         
                            text: 'Готово'
                            theme_text_color: "Custom"
                            text_color: 1, 1, 1, 1
                            md_bg_color: 9/255, 105/255, 161/255, 1
                            line_color: 0, 0, 0, 1
                            
                            halign: 'center'
                            size_hint: 1, 1
                            on_press: app.done('video')
            Screen:
                name: 'add'
                BoxLayout:
                    orientation: 'vertical'
                    padding: 10
                    Image:
                        source: 'cov.jpg'
                    MDRectangleFlatButton:         
                        text: 'Готово'
                        theme_text_color: "Custom"
                        text_color: 1, 1, 1, 1
                        md_bg_color: 9/255, 105/255, 161/255, 1
                        line_color: 0, 0, 0, 1
                        
                        halign: 'center'
                        pos_hint:{'center_x' : 0.5, 'center_y' : 0.5}
                        on_press: app.done('add')
                        width: auth.width / 3
            Screen:
                name: 'test1'
                ScrollView:
                    BoxLayout:
                        padding: 10
                        spacing: 30
                        orientation: 'vertical'
                        height: self.minimum_height
                        size_hint_y: None
                         
                        MDList:
                            MDLabel:         
                                text: 'Предельно допустимая мощность внешнего облучения для 36-часовой рабочей недели?'
                                theme_text_color: 'Custom'
                                halign: 'center'
                                font_style: 'H6'
                                text_color: (0, 0, 0, 1)
                                background_color: 9/255, 105/255, 161/255, 1
                                canvas.before:
                                    Color:
                                        rgba: self.background_color
                                    RoundedRectangle:
                                        radius: [7]        
                                        size: self.size[0], self.size[1] + 30
                                        pos: self.pos
                                size_hint: 1, None
                                
                                size_hint: 1, None
                            BoxLayout:
                                size_hint_y: None
                                Check:
                                    id: check
                                    
                                MDLabel:
                                    text: ' 1,2 мбэр/ч.'
                                    theme_text_color: 'Custom'
                                    text_color: (0, 0, 0, 1)
                                    size_hint: 1, None
                                    height: check.height
                                    
                                    
                        
                            BoxLayout:
                                size_hint_y: None
                                Check:
                                   
                                MDLabel:
                                    text: ' 1,8 мбэр/ч.'
                                    theme_text_color: 'Custom'
                                    text_color: (0, 0, 0, 1)
                                    size_hint: 1, None
                                    height: check.height
                                    
                                   
                                
                            BoxLayout:
                                size_hint_y: None
                                Check:
                                  
                                MDLabel:
                                    text: ' 2,2 мбэр/ч.'
                                    theme_text_color: 'Custom'
                                    text_color: (0, 0, 0, 1)
                                    size_hint: 1, None
                                    height: check.height
                                    
                                    
                                
                            BoxLayout:
                                size_hint_y: None
                                Check:
                                    
                                MDLabel:
                                    text: ' 2,8 мбэр/ч.'
                                    theme_text_color: 'Custom'
                                    text_color: (0, 0, 0, 1)
                                    size_hint: 1, None
                                    height: check.height
                                    
                                   
                        MDList:
                            MDLabel:         
                                text: 'Что включает в себя управление запроектными авариями?'
                                theme_text_color: 'Custom'
                                halign: 'center'
                                font_style: 'H6'
                                text_color: (0, 0, 0, 1)
                                background_color: 9/255, 105/255, 161/255, 1
                                canvas.before:
                                    Color:
                                        rgba: self.background_color
                                    RoundedRectangle:
                                        radius: [7]        
                                        size: self.size[0], self.size[1] + 30
                                        pos: self.pos
                                size_hint: 1, None
                                
                            BoxLayout:
                                size_hint_y: None
                                Check1:
                                    
                                    
                                MDLabel:
                                    text: ' Предотвращение развития запроектных аварий.'
                                    theme_text_color: 'Custom'
                                    text_color: (0, 0, 0, 1)
                                    size_hint: 1, None
                                    height: check.height
                                    
                                   
                        
                            BoxLayout:
                                size_hint_y: None
                                Check1:
                                   
                                MDLabel:
                                    text: ' Защита герметичного ограждения от разрушения.'
                                    theme_text_color: 'Custom'
                                    text_color: (0, 0, 0, 1)
                                    size_hint: 1, None
                                    height: check.height
                                    
                                   
                                
                            BoxLayout:
                                size_hint_y: None
                                Check1:
                                  
                                MDLabel:
                                    text: ' Возвращение АС в контролируемое состояние.'
                                    theme_text_color: 'Custom'
                                    text_color: (0, 0, 0, 1)
                                    size_hint: 1, None
                                    height: check.height
                                    
                                    
                                
                            BoxLayout:
                                size_hint_y: None
                                Check1:
                                    
                                MDLabel:
                                    text: ' Все вышеуказанное.'
                                    theme_text_color: 'Custom'
                                    text_color: (0, 0, 0, 1)
                                    size_hint: 1, None
                                    height: check.height
                        MDList:
                            MDLabel:         
                                text: 'Нужно ли фиксировать погрешности измерений ядерных материалов?'
                                theme_text_color: 'Custom'
                                halign: 'center'
                                font_style: 'H6'
                                text_color: (0, 0, 0, 1)
                                background_color: 9/255, 105/255, 161/255, 1
                                canvas.before:
                                    Color:
                                        rgba: self.background_color
                                    RoundedRectangle:
                                        radius: [7]        
                                        size: self.size[0], self.size[1] + 30
                                        pos: self.pos
                                size_hint: 1, None
                               
                            BoxLayout:
                                size_hint_y: None
                                Check2:
                                    
                                    
                                MDLabel:
                                    text: 'Лишняя работа.'
                                    theme_text_color: 'Custom'
                                    text_color: (0, 0, 0, 1)
                                    size_hint: 1, None
                                    height: check.height
                                    
                                   
                        
                            BoxLayout:
                                size_hint_y: None
                                Check2:
                                   
                                MDLabel:
                                    text: ' По желанию.'
                                    theme_text_color: 'Custom'
                                    text_color: (0, 0, 0, 1)
                                    size_hint: 1, None
                                    height: check.height
                                    
                                   
                                
                            BoxLayout:
                                size_hint_y: None
                                Check2:
                                  
                                MDLabel:
                                    text: ' Обязательно.'
                                    theme_text_color: 'Custom'
                                    text_color: (0, 0, 0, 1)
                                    size_hint: 1, None
                                    height: check.height
                                    
                                    
                                
                            BoxLayout:
                                size_hint_y: None
                                Check2:
                                    
                                MDLabel:
                                    text: ' Зависит от ядерного материала.'
                                    theme_text_color: 'Custom'
                                    text_color: (0, 0, 0, 1)
                                    size_hint: 1, None
                                    height: check.height
                                                    
                        MDList:
                            MDLabel:         
                                text: 'Что такое радиоактивные вещества?'
                                theme_text_color: 'Custom'
                                halign: 'center'
                                font_style: 'H6'
                                text_color: (0, 0, 0, 1)
                                background_color: 9/255, 105/255, 161/255, 1
                                canvas.before:
                                    Color:
                                        rgba: self.background_color
                                    RoundedRectangle:
                                        radius: [7]        
                                        size: self.size[0], self.size[1] + 30
                                        pos: self.pos
                                size_hint: 1, None
                                
                            BoxLayout:
                                size_hint_y: None
                                Check3:
                                    
                                    
                                MDLabel:
                                    text: 'Вещества, испускающие ионизирующее излучение.'
                                    theme_text_color: 'Custom'
                                    text_color: (0, 0, 0, 1)
                                    size_hint: 1, None
                                    height: check.height
                                    
                                   
                        
                            BoxLayout:
                                size_hint_y: None
                                Check3:
                                   
                                MDLabel:
                                    text: ' Все ядерные материалы.'
                                    theme_text_color: 'Custom'
                                    text_color: (0, 0, 0, 1)
                                    size_hint: 1, None
                                    height: check.height
                                    
                                   
                                
                            BoxLayout:
                                size_hint_y: None
                                Check3:
                                  
                                MDLabel:
                                    text: ' Легкие элементы.'
                                    theme_text_color: 'Custom'
                                    text_color: (0, 0, 0, 1)
                                    size_hint: 1, None
                                    height: check.height
                                    
                                    
                                
                            BoxLayout:
                                size_hint_y: None
                                Check3:
                                    
                                MDLabel:
                                    text: ' Тяжелые элементы.'
                                    theme_text_color: 'Custom'
                                    text_color: (0, 0, 0, 1)
                                    size_hint: 1, None
                                    height: check.height
                        MDList:
                            MDLabel:         
                                text: 'Какое излучение обладает наибольшей проникающей способностью?'
                                theme_text_color: 'Custom'
                                halign: 'center'
                                font_style: 'H6'
                                text_color: (0, 0, 0, 1)
                                background_color: 9/255, 105/255, 161/255, 1
                                canvas.before:
                                    Color:
                                        rgba: self.background_color
                                    RoundedRectangle:
                                        radius: [7]        
                                        size: self.size[0], self.size[1] + 30
                                        pos: self.pos
                                size_hint: 1, None
                                
                            BoxLayout:
                                size_hint_y: None
                                Check4:
                                    
                                    
                                MDLabel:
                                    text: 'Альфа.'
                                    theme_text_color: 'Custom'
                                    text_color: (0, 0, 0, 1)
                                    size_hint: 1, None
                                    height: check.height
                                    
                                   
                        
                            BoxLayout:
                                size_hint_y: None
                                Check4:
                                   
                                MDLabel:
                                    text: ' Бета.'
                                    theme_text_color: 'Custom'
                                    text_color: (0, 0, 0, 1)
                                    size_hint: 1, None
                                    height: check.height
                                    
                                   
                                
                            BoxLayout:
                                size_hint_y: None
                                Check4:
                                  
                                MDLabel:
                                    text: ' Гамма.'
                                    theme_text_color: 'Custom'
                                    text_color: (0, 0, 0, 1)
                                    size_hint: 1, None
                                    height: check.height
                                    
                                    
                                
                            BoxLayout:
                                size_hint_y: None
                                Check4:
                                    
                                MDLabel:
                                    text: ' У всех излучений проникающая способность одинакова.'
                                    theme_text_color: 'Custom'
                                    text_color: (0, 0, 0, 1)
                                    size_hint: 1, None
                                    height: check.height
                                    
                        MDRectangleFlatButton:         
                            text: 'Готово'
                            theme_text_color: "Custom"
                            text_color: 1, 1, 1, 1
                            md_bg_color: 9/255, 105/255, 161/255, 1
                            line_color: 0, 0, 0, 1
                            pos_hint:{'center_x' : 0.5, 'center_y' : 0.5}
                            halign: 'center'
                            on_press: app.back()
                            width: auth.width / 3
            Screen:
                name: 'test2'
                ScrollView:
                    BoxLayout:
                        padding: 10
                        spacing: 30
                        orientation: 'vertical'
                        height: self.minimum_height
                        size_hint_y: None
                         
                        MDList:
                            MDLabel:         
                                text: 'Чему равна максимально допустимая скорость введения реактивности?'
                                theme_text_color: 'Custom'
                                halign: 'center'
                                font_style: 'H6'
                                text_color: (0, 0, 0, 1)
                                background_color: 9/255, 105/255, 161/255, 1
                                canvas.before:
                                    Color:
                                        rgba: self.background_color
                                    RoundedRectangle:
                                        radius: [7]        
                                        size: self.size[0], self.size[1] + 30
                                        pos: self.pos
                                size_hint: 1, None
                            BoxLayout:
                                size_hint_y: None
                                Check:
                                    id: check
                                    
                                MDLabel:
                                    text: ' 0,01 β/с.'
                                    theme_text_color: 'Custom'
                                    text_color: (0, 0, 0, 1)
                                    size_hint: 1, None
                                    height: check.height
                                    
                                    
                        
                            BoxLayout:
                                size_hint_y: None
                                Check:
                                   
                                MDLabel:
                                    text: ' 0,07 β/с'
                                    theme_text_color: 'Custom'
                                    text_color: (0, 0, 0, 1)
                                    size_hint: 1, None
                                    height: check.height
                                    
                                   
                                
                            BoxLayout:
                                size_hint_y: None
                                Check:
                                  
                                MDLabel:
                                    text: ' 0,10 β/с'
                                    theme_text_color: 'Custom'
                                    text_color: (0, 0, 0, 1)
                                    size_hint: 1, None
                                    height: check.height
                                    
                                    
                                
                            BoxLayout:
                                size_hint_y: None
                                Check:
                                    
                                MDLabel:
                                    text: ' 0,30 β/с'
                                    theme_text_color: 'Custom'
                                    text_color: (0, 0, 0, 1)
                                    size_hint: 1, None
                                    height: check.height
                                    
                                   
                        MDList:
                            MDLabel:         
                                text: 'Реакторная установка ВВЭР-1000. Укажите давление пара перед турбиной?'
                                theme_text_color: 'Custom'
                                halign: 'center'
                                font_style: 'H6'
                                text_color: (0, 0, 0, 1)
                                background_color: 9/255, 105/255, 161/255, 1
                                canvas.before:
                                    Color:
                                        rgba: self.background_color
                                    RoundedRectangle:
                                        radius: [7]        
                                        size: self.size[0], self.size[1] + 30
                                        pos: self.pos
                                size_hint: 1, None
                            BoxLayout:
                                size_hint_y: None
                                Check1:
                                    
                                    
                                MDLabel:
                                    text: ' 4 МПа'
                                    theme_text_color: 'Custom'
                                    text_color: (0, 0, 0, 1)
                                    size_hint: 1, None
                                    height: check.height
                                    
                                   
                        
                            BoxLayout:
                                size_hint_y: None
                                Check1:
                                   
                                MDLabel:
                                    text: ' 6 МПа'
                                    theme_text_color: 'Custom'
                                    text_color: (0, 0, 0, 1)
                                    size_hint: 1, None
                                    height: check.height
                                    
                                   
                                
                            BoxLayout:
                                size_hint_y: None
                                Check1:
                                  
                                MDLabel:
                                    text: ' 8 МПа'
                                    theme_text_color: 'Custom'
                                    text_color: (0, 0, 0, 1)
                                    size_hint: 1, None
                                    height: check.height
                                    
                                    
                                
                            BoxLayout:
                                size_hint_y: None
                                Check1:
                                    
                                MDLabel:
                                    text: ' 10 МПа'
                                    theme_text_color: 'Custom'
                                    text_color: (0, 0, 0, 1)
                                    size_hint: 1, None
                                    height: check.height
                        MDList:
                            MDLabel:         
                                text: 'На каком паре работает турбина АЭС с реактором типа РБМК?'
                                theme_text_color: 'Custom'
                                halign: 'center'
                                font_style: 'H6'
                                text_color: (0, 0, 0, 1)
                                background_color: 9/255, 105/255, 161/255, 1
                                canvas.before:
                                    Color:
                                        rgba: self.background_color
                                    RoundedRectangle:
                                        radius: [7]        
                                        size: self.size[0], self.size[1] + 30
                                        pos: self.pos
                                size_hint: 1, None
                            BoxLayout:
                                size_hint_y: None
                                Check2:
                                    
                                    
                                MDLabel:
                                    text: ' Насыщенном'
                                    theme_text_color: 'Custom'
                                    text_color: (0, 0, 0, 1)
                                    size_hint: 1, None
                                    height: check.height
                                    
                                   
                        
                            BoxLayout:
                                size_hint_y: None
                                Check2:
                                   
                                MDLabel:
                                    text: ' Перегретом'
                                    theme_text_color: 'Custom'
                                    text_color: (0, 0, 0, 1)
                                    size_hint: 1, None
                                    height: check.height
                                    
                                   
                                
                            BoxLayout:
                                size_hint_y: None
                                Check2:
                                  
                                MDLabel:
                                    text: ' Перенасыщенном'
                                    theme_text_color: 'Custom'
                                    text_color: (0, 0, 0, 1)
                                    size_hint: 1, None
                                    height: check.height
                                    
                                    
                                
                            BoxLayout:
                                size_hint_y: None
                                Check2:
                                    
                                MDLabel:
                                    text: ' Влажном'
                                    theme_text_color: 'Custom'
                                    text_color: (0, 0, 0, 1)
                                    size_hint: 1, None
                                    height: check.height
                                                    
                        MDList:
                            MDLabel:         
                                text: 'Какое из приведенных ядер будут делиться нейтронами любых энергий?'
                                theme_text_color: 'Custom'
                                halign: 'center'
                                font_style: 'H6'
                                text_color: (0, 0, 0, 1)
                                background_color: 9/255, 105/255, 161/255, 1
                                canvas.before:
                                    Color:
                                        rgba: self.background_color
                                    RoundedRectangle:
                                        radius: [7]        
                                        size: self.size[0], self.size[1] + 30
                                        pos: self.pos
                                size_hint: 1, None
                            BoxLayout:
                                size_hint_y: None
                                Check3:
                                    
                                    
                                MDLabel:
                                    text: '233U.'
                                    theme_text_color: 'Custom'
                                    text_color: (0, 0, 0, 1)
                                    size_hint: 1, None
                                    height: check.height
                                    
                                   
                        
                            BoxLayout:
                                size_hint_y: None
                                Check3:
                                   
                                MDLabel:
                                    text: ' 234U.'
                                    theme_text_color: 'Custom'
                                    text_color: (0, 0, 0, 1)
                                    size_hint: 1, None
                                    height: check.height
                                    
                                   
                                
                            BoxLayout:
                                size_hint_y: None
                                Check3:
                                  
                                MDLabel:
                                    text: ' 238U.'
                                    theme_text_color: 'Custom'
                                    text_color: (0, 0, 0, 1)
                                    size_hint: 1, None
                                    height: check.height
                                    
                                    
                                
                            BoxLayout:
                                size_hint_y: None
                                Check3:
                                    
                                MDLabel:
                                    text: ' 240Pu.'
                                    theme_text_color: 'Custom'
                                    text_color: (0, 0, 0, 1)
                                    size_hint: 1, None
                                    height: check.height
                        MDList:
                            MDLabel:         
                                text: 'Какой стратегии перегрузки следует придерживаться для уменьшения утечки нейтронов?'
                                theme_text_color: 'Custom'
                                halign: 'center'
                                font_style: 'H6'
                                text_color: (0, 0, 0, 1)
                                background_color: 9/255, 105/255, 161/255, 1
                                canvas.before:
                                    Color:
                                        rgba: self.background_color
                                    RoundedRectangle:
                                        radius: [7]        
                                        size: self.size[0], self.size[1] + 30
                                        pos: self.pos
                                size_hint: 1, None
                            BoxLayout:
                                size_hint_y: None
                                Check4:
                                    
                                    
                                MDLabel:
                                    text: 'От периферии к центру.'
                                    theme_text_color: 'Custom'
                                    text_color: (0, 0, 0, 1)
                                    size_hint: 1, None
                                    height: check.height
                                    
                                   
                        
                            BoxLayout:
                                size_hint_y: None
                                Check4:
                                   
                                MDLabel:
                                    text: ' От центра к периферии.'
                                    theme_text_color: 'Custom'
                                    text_color: (0, 0, 0, 1)
                                    size_hint: 1, None
                                    height: check.height
                                    
                                   
                                
                            BoxLayout:
                                size_hint_y: None
                                Check4:
                                  
                                MDLabel:
                                    text: ' Стратегия перегрузки не влияет на утечку нейтронов.'
                                    theme_text_color: 'Custom'
                                    text_color: (0, 0, 0, 1)
                                    size_hint: 1, None
                                    height: check.height
                                    
                                    
                                
                            BoxLayout:
                                size_hint_y: None
                                Check4:
                                    
                                MDLabel:
                                    text: ' Радиальной.'
                                    theme_text_color: 'Custom'
                                    text_color: (0, 0, 0, 1)
                                    size_hint: 1, None
                                    height: check.height
                                    
                        MDRectangleFlatButton:         
                            text: 'Готово'
                            theme_text_color: "Custom"
                            text_color: 1, 1, 1, 1
                            md_bg_color: 9/255, 105/255, 161/255, 1
                            line_color: 0, 0, 0, 1
                            pos_hint:{'center_x' : 0.5, 'center_y' : 0.5}
                            halign: 'center'
                            on_press: app.back()
                            width: auth.width / 3
                     
     
                        
        MDBottomNavigation:
            id: navigator
            size_hint: 1, None
            opacity: 0
            disabled: True
            panel_color: 1, 1, 1, 1
            MDBottomNavigationItem:
                name: 'home_item'
                icon: 'home'
                on_tab_press: manager.current= "home"
            MDBottomNavigationItem:
                name: 'messenger_item'
                icon: 'message'
                on_tab_press: manager.current= "messenger"
            MDBottomNavigationItem:
                name: 'tasks_item'
                icon: 'file-document-box-check'
                on_tab_press: manager.current= "tasks"
            MDBottomNavigationItem:
                name: 'map_item'
                icon: 'map-marker'
                on_tab_press: manager.current= "map"
            MDBottomNavigationItem:
                name: 'profile_item'
                icon: 'account-box'
                on_tab_press: manager.current= "profile"
    Image:
        id: atom
        source: 'atom.png'
        pos_hint: {'left': 1, 'top': 1}
        size_hint: None, None
        size: top_bar.height, top_bar.height
        opacity: 0            

            
"""
