from kivy.config import Config
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.uix.screenmanager import SlideTransition
from kivy.uix.textinput import TextInput
from kivy.graphics import Color, Rectangle
from kivy.uix.popup import Popup
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.graphics import Color, Line
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.screenmanager import Screen
from kivy.uix.gridlayout import GridLayout


class LoginScreen(Screen):
    def __init__(self, **kwargs):
        super(LoginScreen, self).__init__(**kwargs)
        layout = BoxLayout(orientation='vertical', padding=20, spacing=20)
        username_label = Label(text='Username:')
        self.username_input = TextInput(multiline=False)
        password_label = Label(text='Password:')
        self.password_input = TextInput(multiline=False, password=True)
        login_button = Button(text='Log in', on_release=self.login)
        signup_button = Button(text='Sign up', on_release=self.signup)
        layout.add_widget(username_label)
        layout.add_widget(self.username_input)
        layout.add_widget(password_label)
        layout.add_widget(self.password_input)
        layout.add_widget(login_button)
        layout.add_widget(signup_button)

        with layout.canvas.before:
            Color(0.298, 0.686, 0.855, 1)
            self.rect = Rectangle(size=layout.size, pos=layout.pos)
        layout.bind(size=self._update_rect, pos=self._update_rect)

        self.add_widget(layout)

    def _update_rect(self, instance, value):
        self.rect.pos = instance.pos
        self.rect.size = instance.size

    def login(self, button):
        username = self.username_input.text
        password = self.password_input.text
        if username == 'hello' and password == 'world':
            self.parent.current = 'menu'
        else:
            self.password_input.text = ''
            self.password_input.focus = True

    def signup(self, button):
        self.parent.current = 'signup'


class MenuScreen(Screen):
    def __init__(self, **kwargs):
        super(MenuScreen, self).__init__(**kwargs)
        layout = BoxLayout(orientation='vertical', padding=20, spacing=20)
        label = Label(text='MENU', font_size=24, color=(1, 1, 1, 1))
        option1_button = Button(text='Report a crime scene', on_release=self.select_option1)
        option2_button = Button(text='Report an incident', on_release=self.select_option2)
        option3_button = Button(text='Communication', on_release=self.select_option3)
        option4_button = Button(text='Location', on_release=self.select_option4)
        logout_button = Button(text='Log out', on_release=self.logout)

        layout.add_widget(label)
        layout.add_widget(option1_button)
        layout.add_widget(option2_button)
        layout.add_widget(option3_button)
        layout.add_widget(option4_button)
        layout.add_widget(logout_button)

        with layout.canvas.before:
            Color(0.298, 0.686, 0.855, 1)
            self.rect = Rectangle(size=layout.size, pos=layout.pos)
        layout.bind(size=self._update_rect, pos=self._update_rect)

        self.add_widget(layout)

    def _update_rect(self, instance, value):
        self.rect.pos = instance.pos
        self.rect.size = instance.size

    def select_option1(self, button):
        self.parent.current = 'option1'

    def select_option2(self, button):
        self.parent.current = 'not_available'

    def select_option3(self, button):
        self.parent.current = 'not_available'

    def select_option4(self, button):
        self.parent.current = 'not_available'

    def logout(self, button):
        self.parent.current = 'login'


class Option1Screen(Screen):
    def __init__(self, **kwargs):
        super(Option1Screen, self).__init__(**kwargs)
        layout = BoxLayout(orientation='vertical', padding=20, spacing=20)
        label = Label(text='PERSONAL INFORMATION', font_size=20)
        text_input = TextInput(multiline=False, hint_text="Name")
        text_input_2 = TextInput(multiline=False, hint_text="Date dd/mm/yyy")
        text_input_3 = TextInput(multiline=False, hint_text="Time")
        text_input_4 = TextInput(multiline=False, hint_text="Location")
        next_button = Button(text='Next', on_release=self.go_to_options_screen)
        back_button = Button(text='Back', on_release=self.back_to_menu, size_hint=(0.2, 0.1), pos_hint={'x': 0.8, 'y': 0.0})

        layout.add_widget(label)
        layout.add_widget(text_input)
        layout.add_widget(text_input_2)
        layout.add_widget(text_input_3)
        layout.add_widget(text_input_4)
        layout.add_widget(next_button)
        layout.add_widget(back_button)

        with layout.canvas.before:
            Color(0.298, 0.686, 0.855, 1)
            self.rect = Rectangle(size=layout.size, pos=layout.pos)
        layout.bind(size=self._update_rect, pos=self._update_rect)

        self.add_widget(layout)

    def _update_rect(self, instance, value):
        self.rect.pos = instance.pos
        self.rect.size = instance.size

    def go_to_options_screen(self, button):
        self.parent.current = 'options_screen'

    def back_to_menu(self, button):
        self.parent.current = 'menu'


class OptionsScreen(Screen):
    def __init__(self, **kwargs):
        super(OptionsScreen, self).__init__(**kwargs)
        layout = BoxLayout(orientation='vertical', padding=20, spacing=20)
        label = Label(text='Report a crime scene', font_size=20)
        identify_button = Button(text='Identify', on_release=self.select_identify)  # Added button
        photography_button = Button(text='Photography', on_release=self.select_photography)
        notes_button = Button(text='Notes', on_release=self.select_notes)
        back_button = Button(text='Back', size_hint=(0.2, 0.1), pos_hint={'x': 0.8, 'y': 0.0}, on_release=self.back_to_option1)
        layout.add_widget(label)
        layout.add_widget(identify_button)
        layout.add_widget(photography_button)
        layout.add_widget(notes_button)
        layout.add_widget(back_button)

        # Achtergrondkleur instellen
        with layout.canvas.before:
            Color(0.298, 0.686, 0.855, 1)  # Blauwe kleur
            self.rect = Rectangle(size=layout.size, pos=layout.pos)
        layout.bind(size=self._update_rect, pos=self._update_rect)

        self.add_widget(layout)

    def _update_rect(self, instance, value):
        self.rect.pos = instance.pos
        self.rect.size = instance.size

    def select_identify(self, button):
        self.parent.current = 'identify'

    def select_photography(self, button):
        self.parent.current = 'photography'

    def select_notes(self, button):
        self.parent.current = 'notes'

    def back_to_option1(self, button):
        self.parent.current = 'option1'


class NotAvailableScreen(Screen):
    def __init__(self, **kwargs):
        super(NotAvailableScreen, self).__init__(**kwargs)
        layout = BoxLayout(orientation='vertical', padding=20, spacing=20)
        label = Label(text='Not available yet', font_size=20)
        back_button = Button(text='Back', on_release=self.back_to_menu)

        layout.add_widget(label)
        layout.add_widget(back_button)

        self.add_widget(layout)

        with layout.canvas.before:
            Color(0, 0, 0, 0)

    def back_to_menu(self, button):
        self.parent.current = 'menu'


class IdentifyScreen(Screen):
    def __init__(self, **kwargs):
        super(IdentifyScreen, self).__init__(**kwargs)
        layout = BoxLayout(orientation='vertical', padding=20, spacing=20)
        label = Label(text='Identify', font_size=20)
        next_button = Button(text='Next', on_release=self.animal_covering)
        back_button = Button(text='Back', on_release=self.back_to_options)
        layout.add_widget(label)
        layout.add_widget(next_button)
        layout.add_widget(back_button)

        with layout.canvas.before:
            Color(0.298, 0.686, 0.855, 1)  # Blauwe kleur
            self.rect = Rectangle(size=layout.size, pos=layout.pos)
        layout.bind(size=self._update_rect, pos=self._update_rect)

        self.add_widget(layout)

    def _update_rect(self, instance, value):
        self.rect.pos = instance.pos
        self.rect.size = instance.size

    def back_to_options(self, button):
        self.parent.current = 'options_screen'

    def animal_covering(self, button):
        self.parent.current = 'animal_covering_screen'


class Animal:
    def __init__(self, name, covering, color, size, special_features):
        self.name = name
        self.covering = covering
        self.color = color
        self.size = size
        self.special_features = special_features


class AnimalCoveringQuestionScreen(Screen):
    def __init__(self, **kwargs):
        super(AnimalCoveringQuestionScreen, self).__init__(**kwargs)
        self.name = 'animal_covering_screen'
        layout = BoxLayout(orientation='vertical')
        layout.add_widget(Label(text='What is the primary covering of the animal:', size_hint=(1, 0.4)))
        grid_layout = GridLayout(cols=2)
        grid_layout.add_widget(Button(text='Fur', on_press=self.select_covering))
        grid_layout.add_widget(Button(text='Feathers', on_press=self.select_covering))
        grid_layout.add_widget(Button(text='Scales', on_press=self.select_covering))
        grid_layout.add_widget(Button(text='Skin', on_press=self.select_covering))
        layout.add_widget(grid_layout)
        self.add_widget(layout)

    def select_covering(self, instance):
        covering = instance.text
        self.manager.get_screen('animal_list').filter_animals_by_covering(covering)
        self.manager.get_screen('animal_list').filter_animals_by_covering(covering)
        self.manager.current = 'animal_color_screen'


class AnimalColorQuestionScreen(Screen):
    def __init__(self, **kwargs):
        super(AnimalColorQuestionScreen, self).__init__(**kwargs)
        self.name = 'animal_color_screen'
        layout = BoxLayout(orientation='vertical')
        layout.add_widget(Label(text='What is the primary color of the animal:', size_hint=(1, 0.4)))
        grid_layout = GridLayout(cols=2)
        grid_layout.add_widget(Button(text='Red', on_press=self.select_color))
        grid_layout.add_widget(Button(text='Blue', on_press=self.select_color))
        grid_layout.add_widget(Button(text='Green', on_press=self.select_color))
        grid_layout.add_widget(Button(text='Yellow', on_press=self.select_color))
        grid_layout.add_widget(Button(text='Orange', on_press=self.select_color))
        grid_layout.add_widget(Button(text='Purple', on_press=self.select_color))
        grid_layout.add_widget(Button(text='Gray', on_press=self.select_color))
        grid_layout.add_widget(Button(text='Brown', on_press=self.select_color))
        grid_layout.add_widget(Button(text='White', on_press=self.select_color))
        grid_layout.add_widget(Button(text='Black', on_press=self.select_color))
        layout.add_widget(grid_layout)
        self.add_widget(layout)

    def select_color(self, instance):
        color = instance.text
        self.manager.get_screen('animal_list').filter_animals_by_color(color)
        self.manager.current = 'animal_size_screen'


class AnimalSizeQuestionScreen(Screen):
    def __init__(self, **kwargs):
        super(AnimalSizeQuestionScreen, self).__init__(**kwargs)
        self.name = 'animal_size_screen'
        layout = BoxLayout(orientation='vertical')
        layout.add_widget(Label(text='What is the approximate size of the animal', size_hint=(1, 0.4)))
        grid_layout = GridLayout(cols=2)
        grid_layout.add_widget(Button(text='Smaller than 40cm', on_press=self.select_size))
        grid_layout.add_widget(Button(text='Smaller than 80cm', on_press=self.select_size))
        grid_layout.add_widget(Button(text='Smaller than 150cm', on_press=self.select_size))
        grid_layout.add_widget(Button(text='Bigger than 150cm', on_press=self.select_size))
        layout.add_widget(grid_layout)
        self.add_widget(layout)

    def select_size(self, instance):
        size = instance.text
        self.manager.get_screen('animal_list').filter_animals_by_size(size)
        self.manager.current = 'animal_features_screen'


class SpecialFeaturesQuestionScreen(Screen):
    def __init__(self, **kwargs):
        super(SpecialFeaturesQuestionScreen, self).__init__(**kwargs)
        self.name = 'animal_features_screen'
        layout = BoxLayout(orientation='vertical')
        layout.add_widget(Label(text='Does the animal have any special features', size_hint=(1, 0.4)))
        grid_layout = GridLayout(cols=2)
        self.answer_buttons = []
        self.selected_options = []  # Added to store selected options

        # Create buttons and store references in answer_buttons list
        button_texts = ['Tail', 'Fin', 'Wings', 'Spines', 'Horn', 'Antlers', 'None']
        for text in button_texts:
            button = Button(text=text)
            button.bind(on_press=self.select_special_features)  # Bind on_press event handler
            self.answer_buttons.append(button)
            grid_layout.add_widget(button)

        layout.add_widget(grid_layout)
        self.add_widget(layout)

    def select_special_features(self, instance):
        option = instance.text

        # Toggle button state
        if option in self.selected_options:
            self.selected_options.remove(option)
            instance.background_color = (1, 1, 1, 1)  # Reset button color
        else:
            self.selected_options.append(option)
            instance.background_color = (0, 0.5, 1, 1)  # Set button color

        # Check if any option is selected
        if self.selected_options:
            self.manager.get_screen('animal_list').filter_animals_by_special_features(self.selected_options)
            self.manager.current = 'animal_list'
        else:
            # Handle case when no option is selected
            pass


class AnimalListScreen(Screen):
    def __init__(self, **kwargs):
        super(AnimalListScreen, self).__init__(**kwargs)
        self.name = 'animal_list'
        self.animals = [
            Animal('Hyrax', 'Fur', 'Brown', 'Smaller than 80cm', ['None']),
            Animal('Brown greater galago', 'Fur', 'Brown', 'Smaller than 40cm', ['Tail']),
            Animal('White throated monkey', 'Fur', ['White', 'Gray'], 'Smaller than 80cm', ['Tail']),
            Animal('Vervet monkey', 'Fur', ['Gray', 'White'], 'Smaller than 80cm', ['Tail']),
            Animal('Cape Baboon', 'Fur', ['Gray', 'Brown'], 'Smaller than 150cm', ['Tail']),
            Animal('Ground pangolin', 'Scales', ['Gray', 'Brown'], 'Smaller than 80cm', ['Tail']),
            Animal('Lion', 'Fur', 'Brown', 'Larger than 150cm', ['Tail']),
            Animal('African leopard', 'Fur', ['Yellow', 'Brown'], 'Larger than 150cm', ['Tail']),
            Animal('Southeast African cheetah', 'Fur', ['Yellow', 'Brown'], 'Larger than 150cm', ['Tail']),
            Animal('Caracal', 'Fur', 'Brown', 'Smaller than 80cm', ['Tail']),
            Animal('Serval', 'Fur', ['Yellow', 'Black'], 'Smaller than 80cm', ['Tail']),
            Animal('African civet', 'Fur', ['Gray', 'Black'], 'Smaller than 80cm', ['Tail']),
            Animal('Genet', 'Fur', ['Gray', 'Brown'], 'Smaller than 80cm', ['Tail']),
            Animal('Spotted hyena', 'Fur', ['Gray', 'Brown'], 'Smaller than 150cm', ['Tail']),
            Animal('Brown hyena', 'Fur', 'Brown', 'Smaller than 150cm', ['Tail']),
            Animal('Aardwolf', 'Fur', ['Gray', 'Brown'], 'Smaller than 80cm', 'Tail'),
            Animal('Cape fox', 'Fur', ['Gray', 'Brown'], 'Smaller than 80cm', 'Tail'),
            Animal('Jackal', 'Fur', ['Gray', 'Brown'], 'Smaller than 80cm', 'Tail'),
            Animal('Bat-eared fox', 'Fur', ['Gray', 'White'], 'Smaller than 80cm', 'Tail'),
            Animal('African wild dog', 'Fur', ['Yellow', 'Brown', 'Black'], 'Smaller than 80cm', 'Tail'),
            Animal('Striped polecat', 'Fur', ['White', 'Brown'], 'Smaller than 80cm', 'Tail'),
            Animal('African striped weasel', 'Fur', ['Black', 'White'], 'Smaller than 40cm', 'Tail'),
            Animal('Honey badger', 'Fur', ['Black', 'White'], 'Smaller than 40cm', 'Tail'),
            Animal('Otter', 'Fur', ['Brown', 'Gray'], 'Smaller than 150cm', 'Tail'),
            Animal('Zebra', 'Fur', ['Black', 'White'], 'Larger than 150cm', 'Tail'),
            Animal('Rhinoceros', 'Skin', 'Gray', 'Larger than 150cm', ['Horn', 'Tail']),
            Animal('Fallow deer', 'Fur', 'Brown', 'Larger than 150cm', ['Antlers', 'Tail']),
            Animal('Warthog', 'Fur', ['Brown', 'Gray'], 'Smaller than 150cm', ['Horn', 'Tail']),
            Animal('Bushpig', 'Fur', ['Brown', 'Gray'], 'Smaller than 150cm', 'Tail'),
            Animal('Hippopotamus', 'Skin', 'Gray', 'Larger than 150cm', 'Tail'),
            Animal('South African giraffe', 'Fur', ['Brown', 'Yellow'], 'Larger than 150cm', ['Antlers', 'None']),
            Animal('Red hartebeest', 'Fur', ['Red', 'Brown'], 'Larger than 150cm', ['Antlers', 'Tail']),
            Animal('Lichtenstein hartebeest', 'Fur', ['Brown', 'Yellow'], 'Larger than 150cm', ['Antlers', 'Tail']),
            Animal('Black wildebeest', 'Fur', ['Black', 'Brown'], 'Larger than 150cm', ['Antlers', 'Tail']),
            Animal('Blue wildebeest', 'Fur', 'Gray', 'Larger than 150cm', ['Antlers', 'Tail']),
            Animal('Bontebok', 'Fur', ['Brown', 'Gray', 'White'], 'Larger than 150cm', ['Antlers', 'Tail']),
            Animal('Common tsessebe', 'Fur', 'Gray', 'Larger than 150cm', ['Antlers', 'Tail']),
            Animal('Springbok antelope', 'Fur', ['Yellow', 'Brown'], 'Smaller than 80cm', ['Antlers', 'Tail']),
            Animal('Suni', 'Fur', 'Brown', 'Smaller than 40cm', ['Antlers', 'Tail']),
            Animal('Klipspringer', 'Fur', ['Gray', 'Brown'], 'Smaller than 80cm', 'Antlers'),
            Animal('Oribi', 'Fur', 'Brown', 'Smaller than 80cm', 'Antlers'),
            Animal('Steenbok', 'Fur', 'Brown', 'Smaller than 80cm', 'Antlers'),
            Animal('Cape grysbok', 'Fur', 'Brown', 'Smaller than 80cm', 'Antlers'),
            Animal('Sharpe grysbok', 'Fur', 'Brown', 'Smaller than 80cm', ['Antlers', 'None']),
            Animal('African buffalo', 'Fur', ['Black', 'Grey'], 'Larger than 150cm', ['Antlers', 'Tail']),
            Animal('Nyala', 'Fur', ['Gray', 'Brown'], 'Larger than 150cm', ['Antlers', 'Tail']),
            Animal('Common eland', 'Fur', ['Gray', 'Brown'], 'Larger than 150cm', ['Antlers', 'Tail']),
            Animal('Bushbuck', 'Fur', 'Brown', 'Smaller than 150cm', ['Antlers', 'Tail']),
            Animal('Greater kudu', 'Fur', ['Gray', 'Brown'], 'Larger than 150cm', ['Antlers', 'Tail']),
            Animal('Blue duiker', 'Fur', ['Gray', 'Blue'], 'Smaller than 40cm', 'None'),
            Animal('Red forest duiker', 'Fur', ['Red', 'Brown'], 'Smaller than 40cm', 'None'),
            Animal('Common duiker', 'Fur', ['Gray', 'Brown'], 'Smaller than 80cm', ['Antlers', 'Tail']),
            Animal('Roan antelope', 'Fur', 'Brown', 'Larger than 150cm', ['Antlers', 'Tail']),
            Animal('Reedbuck', 'Fur', ['Brown', 'Red'], 'Smaller than 80cm', ['Antlers', 'Tail']),
            Animal('Sable antelope', 'Fur', ['Black', 'Brown'], 'Larger than 150cm', ['Antlers', 'Tail']),
            Animal('Gemsbok', 'Fur', ['Gray', 'White'], 'Larger than 150cm', ['Antlers', 'Tail']),
            Animal('Grey rhebok', 'Fur', 'Gray', 'Smaller than 80cm', ['Antlers', 'Tail']),
            Animal('Impala', 'Fur', ['Brown', 'Yellow'], 'Larger than 80cm', ['Antlers', 'Tail']),
            Animal('Waterbuck', 'Fur', ['Brown', 'Gray'], 'Larger than 150cm', ['Antlers', 'Tail'])
        ]

        self.filtered_animals = self.animals

        layout = BoxLayout(orientation='vertical', padding=[50, 100, 50, 100])
        self.animal_labels = []
        for animal in self.filtered_animals:
            label = Label(text=animal.name, font_size=24, size_hint=(1, None), height=50)
            self.animal_labels.append(label)
            layout.add_widget(label)

        back_button = Button(text='Back', size_hint=(1, None), height=50)
        back_button.bind(on_press=self.go_to_menu_screen)
        layout.add_widget(back_button)

        self.add_widget(layout)

    def go_to_menu_screen(self, instance):
        self.manager.current = 'menu'

    def filter_animals_by_covering(self, covering):
        self.filtered_animals = [animal for animal in self.animals if animal.covering == covering]
        self.update_animal_labels()

    def filter_animals_by_color(self, color):
        self.filtered_animals = [animal for animal in self.filtered_animals if color in animal.color]
        self.update_animal_labels()

    def filter_animals_by_size(self, size):
        if size == 'Smaller than 20cm':
            self.filtered_animals = [animal for animal in self.filtered_animals if animal.size == size or
                                     animal.size == 'Smaller than 20cm' or animal.size == 'Smaller than 80cm' or
                                     animal.size == 'Smaller than 180cm']
        elif size == 'Smaller than 80cm':
            self.filtered_animals = [animal for animal in self.filtered_animals if animal.size == size or
                                     animal.size == 'Smaller than 80cm' or animal.size == 'Smaller than 180cm']
        elif size == 'Smaller than 180cm':
            self.filtered_animals = [animal for animal in self.filtered_animals if animal.size == size or
                                     animal.size == 'Smaller than 180cm']
        elif size == 'Bigger than 180cm':
            self.filtered_animals = [animal for animal in self.filtered_animals if animal.size == size]

        self.update_animal_labels()

    def filter_animals_by_special_features(self, special_features):
        if 'None' in special_features:
            self.filtered_animals = [animal for animal in self.filtered_animals if 'None' in animal.special_features]
        else:
            self.filtered_animals = [animal for animal in self.filtered_animals if
                                     all(feature in animal.special_features for feature in special_features)]

        self.update_animal_labels()

    def update_animal_labels(self):
        layout = self.children[0]
        layout.clear_widgets()

        if len(self.filtered_animals) == 0:
            label = Label(text="No match found", font_size=24, size_hint=(1, None), height=450)
            layout.add_widget(label)
            print()
        else:
            for animal in self.filtered_animals:
                label = Label(text=animal.name, font_size=24, size_hint=(1, None), height=50)
                layout.add_widget(label)
                print()

        back_button = Button(text='Back', size_hint=(1, None), height=50)
        back_button.bind(on_press=self.go_to_menu_screen)
        layout.add_widget(back_button)


Builder.load_string('''
<PhotographyScreen>:
    canvas.before:
        Color:
            rgba: 0, 0, 0, 0
        Line:
            rectangle: self.x, self.y, self.width, self.height
            width: 1
''')


class PhotographyScreen(Screen):
    def __init__(self, **kwargs):
        super(PhotographyScreen, self).__init__(**kwargs)
        layout = BoxLayout(orientation='vertical', padding=20, spacing=20)
        stappenplan_label = Label(text='Overall photography\n'
                                       'Keep the camera in landscape mode - ensure that the photos are sharp.\n'
                                    'Take overview photos from different angles.\n'
                                    'Take photos at eye level - as you yourself see the crime scene.\n'
                                    'Photograph the entire crime scene.\n'
                                    'If you need to move to see the complete picture, you will have to take multiple photos. \n'
                                       'Make sure that the photos overlap partially so that they can be placed side by side to provide a complete image.\n'
                                    'Also, take a photo showing the victim and the immediate surroundings',
                                font_size=16, color=(1, 1, 1, 1),
                                halign='center')
        upload_button = Button(text='Upload Photo', on_release=self.upload_photo)
        back_button = Button(text='Back', size_hint=(0.1, 0.1), pos_hint={'x': 0.0, 'y': 0.0}, on_release=self.back_to_options_screen)

        # "Terug"-knop linksonder
        back_button = Button(text='Terug', size_hint=(0.2, 0.1), pos_hint={'x': 0.0, 'y': 0.0},
                             on_release=self.back_to_options_screen)
        # "Next"-knop rechtsonder
        next_button = Button(text='Next', size_hint=(0.2, 0.1), pos_hint={'right': 1, 'y': 0.0},
                             on_release=self.go_to_next_screen)

        layout.add_widget(stappenplan_label)
        layout.add_widget(upload_button)
        layout.add_widget(back_button)
        layout.add_widget(next_button)

        with layout.canvas.before:
            Color(0.298, 0.686, 0.855, 1)
            self.rect = Rectangle(size=layout.size, pos=layout.pos)

        layout.bind(size=self._update_rect, pos=self._update_rect)
        self.add_widget(layout)

    def _update_rect(self, instance, value):
        self.rect.pos = instance.pos
        self.rect.size = instance.size

    def upload_photo(self, button):
        # Here, you can implement the logic to open a file browser and select a photo to upload
        # You can use libraries like kivy.garden.filebrowser or plyer for this purpose
        # Once the photo is selected, you can handle it accordingly (e.g., display it, save it, etc.)
        pass

    def back_to_options_screen(self, button):
        self.parent.current = 'options_screen'

    def go_to_next_screen(self, button):
        self.parent.current = 'closeup_photos'


class CloseupPhotosScreen(Screen):
    def __init__(self, **kwargs):
        super(CloseupPhotosScreen, self).__init__(**kwargs)
        layout = BoxLayout(orientation='vertical', padding=20, spacing=20)
        stappenplan_label = Label(text='Take photos from a 180-degree angle relative to the object.\n'
                                       '    Example: Photograph a bloodstain on the ground directly from above. \n'
                                       'Photograph important details such as: Wounds, bloodstains, shoeprints, evidence, weapons, strange objects',
                                  font_size=16, color=(1, 1, 1, 1))
        upload_button = Button(text='Upload Photo', on_release=self.upload_photo)
        back_button = Button(text='Back', on_release=self.photography)
        finish_button = Button(text='Finish', on_release=self.options_screen)

        layout.add_widget(stappenplan_label)
        layout.add_widget(upload_button)
        layout.add_widget(back_button)
        layout.add_widget(finish_button)

        with layout.canvas.before:
            Color(0.298, 0.686, 0.855, 1)
            self.rect = Rectangle(size=layout.size, pos=layout.pos)

        layout.bind(size=self._update_rect, pos=self._update_rect)
        self.add_widget(layout)

    def _update_rect(self, instance, value):
        self.rect.pos = instance.pos
        self.rect.size = instance.size

    def upload_photo(self, button):
        # Here, you can implement the logic to open a file browser and select a photo to upload
        # You can use libraries like kivy.garden.filebrowser or plyer for this purpose
        # Once the photo is selected, you can handle it accordingly (e.g., display it, save it, etc.)
        pass

    def photography(self, button):
        self.parent.current = 'photography'

    def options_screen(self, button):
        self.parent.current = 'options_screen'


class NotesScreen(Screen):
    def __init__(self, **kwargs):
        super(NotesScreen, self).__init__(**kwargs)
        layout = BoxLayout(orientation='vertical', padding=20, spacing=20)
        title_label = Label(text='NOTES', font_size=16, color=(1, 1, 1, 1))
        next_button = Button(text='Next', size_hint=(1, 0.5), on_release=self.go_to_next_screen)
        back_button = Button(text='Back', size_hint=(1, 0.5), on_release=self.back_to_options_screen)

        layout.add_widget(title_label)
        layout.add_widget(next_button)
        layout.add_widget(back_button)

        with layout.canvas.before:
            Color(0.298, 0.686, 0.855, 1)
            self.rect = Rectangle(size=layout.size, pos=layout.pos)

        layout.bind(size=self._update_rect, pos=self._update_rect)
        self.add_widget(layout)

    def back_to_options_screen(self, button):
        self.parent.current = 'options_screen'

    def _update_rect(self, instance, value):
        self.rect.pos = instance.pos
        self.rect.size = instance.size

    def go_to_next_screen(self, button):
        self.parent.current = 'step1_notes'


class Step1NotesScreen(Screen):
    def __init__(self, **kwargs):
        super(Step1NotesScreen, self).__init__(**kwargs)
        layout = BoxLayout(orientation='vertical', padding=20, spacing=20)
        title_label = Label(text='Is the victim dead or alive?', font_size=16, color=(1, 1, 1, 1))
        dead_button = Button(text='Dead', on_release=self.dead_button_pressed)
        alive_button = Button(text='Alive', on_release=self.alive_button_pressed)
        back_button = Button(text='Back', on_release=self.notes_screen)

        layout.add_widget(title_label)
        layout.add_widget(dead_button)
        layout.add_widget(alive_button)
        layout.add_widget(back_button)

        with layout.canvas.before:
            Color(0.298, 0.686, 0.855, 1)
            self.rect = Rectangle(size=layout.size, pos=layout.pos)

        layout.bind(size=self._update_rect, pos=self._update_rect)
        self.add_widget(layout)

    def _update_rect(self, instance, value):
        self.rect.pos = instance.pos
        self.rect.size = instance.size

    def dead_button_pressed(self, button):
        self.manager.transition = SlideTransition(direction='left')
        self.manager.current = 'describe_victim_dead'

    def alive_button_pressed(self, button):
        self.manager.transition = SlideTransition(direction='left')
        self.manager.current = 'describe_victim_alive'

    def notes_screen(self, button):
        self.manager.transition = SlideTransition(direction='left')
        self.manager.current = 'notes'


class DescribeVictimDeadScreen(Screen):
    def __init__(self, **kwargs):
        super(DescribeVictimDeadScreen, self).__init__(**kwargs)
        layout = BoxLayout(orientation='vertical', padding=20, spacing=20)
        label = Label(text='Describe the victim', font_size=20)
        text_input = TextInput(multiline=True)
        next_button = Button(text='Next', on_release=self.go_to_victim_wounded_screen)
        back_button = Button(text='Back', on_release=self.step1_notes)

        layout.add_widget(label)
        layout.add_widget(text_input)
        layout.add_widget(next_button)
        layout.add_widget(back_button)

        self.add_widget(layout)

        with layout.canvas.before:
            Color(0, 0, 0, 0)

    def go_to_victim_wounded_screen(self, button):
        self.manager.transition = SlideTransition(direction='left')
        self.manager.current = 'victim_wounded_screen'

    def step1_notes(self, button):
        self.manager.transition = SlideTransition(direction='left')
        self.manager.current = 'step1_notes'


class DescribeVictimAliveScreen(Screen):
    def __init__(self, **kwargs):
        super(DescribeVictimAliveScreen, self).__init__(**kwargs)
        layout = BoxLayout(orientation='vertical', padding=20, spacing=20)
        label = Label(text='Describe the victim', font_size=20)
        text_input = TextInput(multiline=True)
        next_button = Button(text='Next', on_release=self.go_to_victim_wounded_screen)

        layout.add_widget(label)
        layout.add_widget(text_input)
        layout.add_widget(next_button)

        self.add_widget(layout)

        with layout.canvas.before:
            Color(0, 0, 0, 0)

    def go_to_victim_wounded_screen(self, button):
        self.manager.transition = SlideTransition(direction='left')
        self.manager.current = 'victim_wounded_screen'


class VictimWoundedScreen(Screen):
    def __init__(self, **kwargs):
        super(VictimWoundedScreen, self).__init__(**kwargs)
        layout = BoxLayout(orientation='vertical', padding=20, spacing=20)
        label = Label(text='Is the victim visibly wounded?', font_size=20)
        yes_button = Button(text='Yes', on_release=self.on_yes_button)
        no_button = Button(text='No', on_release=self.on_no_button)
        self.text_input = TextInput(multiline=True, hint_text='Describe the wounds...', size_hint=(1, None), height=100)
        next_button = Button(text='Next', on_release=self.go_to_evidence_screen)
        back_button = Button(text='Back', on_release=self.back_to_describe_victim)

        layout.add_widget(label)
        layout.add_widget(yes_button)
        layout.add_widget(no_button)
        layout.add_widget(self.text_input)
        layout.add_widget(next_button)
        layout.add_widget(back_button)

        self.add_widget(layout)

        with layout.canvas.before:
            Color(0, 0, 0, 0)

    def on_yes_button(self, button):
        self.text_input.disabled = False

    def on_no_button(self, button):
        self.text_input.disabled = True
        self.text_input.text = ''

    def go_to_evidence_screen(self, button):
        self.manager.transition = SlideTransition(direction='left')
        # Replace 'NextScreen' with the actual name of the next screen
        self.manager.current = 'evidence_screen'

    def back_to_describe_victim(self, button):
        self.manager.transition = SlideTransition(direction='right')
        if self.manager.get_screen('describe_victim_dead'):
            self.manager.current = 'describe_victim_dead'
        elif self.manager.get_screen('describe_victim_alive'):
            self.manager.current = 'describe_victim_alive'


class EvidenceScreen(Screen):
    def __init__(self, **kwargs):
        super(EvidenceScreen, self).__init__(**kwargs)
        layout = BoxLayout(orientation='vertical', padding=20, spacing=20)
        label = Label(text='Is there possibly evidence and/or traces available?', font_size=20)
        yes_button = Button(text='Yes', on_release=self.on_yes_button)
        no_button = Button(text='No', on_release=self.on_no_button)
        self.text_input = TextInput(multiline=True, hint_text='Describe the evidence...', size_hint=(1, None), height=100)
        upload_button = Button(text='Upload Photo', on_release=self.on_upload_button)
        next_button = Button(text='Next', on_release=self.go_to_next_screen)
        back_button = Button(text='Back', on_release=self.back_to_victim_wounded)

        layout.add_widget(label)
        layout.add_widget(yes_button)
        layout.add_widget(no_button)
        layout.add_widget(self.text_input)
        layout.add_widget(upload_button)
        layout.add_widget(next_button)
        layout.add_widget(back_button)

        self.add_widget(layout)

        with layout.canvas.before:
            Color(0, 0, 0, 0)

    def on_yes_button(self, button):
        self.text_input.disabled = False

    def on_no_button(self, button):
        self.text_input.disabled = True
        self.text_input.text = ''

    def on_upload_button(self, button):
        # Implement the logic for uploading a photo here
        pass

    def go_to_next_screen(self, button):
        self.manager.transition = SlideTransition(direction='left')
        self.manager.current = 'witnesses_screen'

    def back_to_victim_wounded(self, button):
        self.manager.transition = SlideTransition(direction='right')
        self.manager.current = 'victim_wounded_screen'


class WitnessesScreen(Screen):
    def __init__(self, **kwargs):
        super(WitnessesScreen, self).__init__(**kwargs)
        layout = BoxLayout(orientation='vertical', padding=20, spacing=20)
        label = Label(text='Are there possible witnesses?', font_size=20)
        yes_button = Button(text='Yes', on_release=self.select_yes)
        no_button = Button(text='No', on_release=self.select_no)
        self.text_input = TextInput(multiline=True, hint_text="information potential witnesses", size_hint=(1, None), height=100)
        next_button = Button(text='Next', on_release=self.go_to_surroundings_screen)
        back_button = Button(text='Back', on_release=self.go_to_evidence_screen)

        layout.add_widget(label)
        layout.add_widget(yes_button)
        layout.add_widget(self.text_input)
        layout.add_widget(no_button)
        layout.add_widget(next_button)
        layout.add_widget(back_button)

        with layout.canvas.before:
            Color(0.0, 0.0, 0.0, 0)
            self.rect = Rectangle(size=layout.size, pos=layout.pos)

        layout.bind(size=self._update_rect, pos=self._update_rect)
        self.add_widget(layout)

    def on_yes_button(self, button):
        self.text_input.disabled = False

    def on_no_button(self, button):
        self.text_input.disabled = True
        self.text_input.text = ''

    def _update_rect(self, instance, value):
        self.rect.pos = instance.pos
        self.rect.size = instance.size

    def select_yes(self, button):
        self.text_input.disabled = False
        pass

    def select_no(self, button):
        self.text_input.disabled = True
        pass

    def go_to_surroundings_screen(self, button):
        self.parent.current = 'surroundings_screen'

    def go_to_option1_screen(self, button):
        self.parent.current = 'option1'

    def go_to_evidence_screen(self, button):
        self.parent.current = 'evidence_screen'


class SurroundingsScreen(Screen):
    def __init__(self, **kwargs):
        super(SurroundingsScreen, self).__init__(**kwargs)
        layout = BoxLayout(orientation='vertical', padding=20, spacing=20)
        label = Label(text='Is the crime scene inside or outside?', font_size=20)
        inside_button = Button(text='Inside', on_release=self.go_to_inside_screen)
        outside_button = Button(text='Outside', on_release=self.go_to_outside_screen)
        back_button = Button(text='Back', on_release=self.go_to_witnesses_screen)

        layout.add_widget(label)
        layout.add_widget(inside_button)
        layout.add_widget(outside_button)
        layout.add_widget(back_button)

        self.add_widget(layout)

    def go_to_inside_screen(self, button):
        self.parent.current = 'inside_screen'

    def go_to_outside_screen(self, button):
        self.parent.current = 'outside_screen'

    def go_to_witnesses_screen(self, button):
        self.parent.current = 'witnesses_screen'


class InsideScreen(Screen):
    def __init__(self, **kwargs):
        super(InsideScreen, self).__init__(**kwargs)
        layout = BoxLayout(orientation='vertical', padding=20, spacing=20)
        label = Label(text='Describe the surroundings', font_size=20)
        self.text_input = TextInput(multiline=True, hint_text="Type of building; residential, office etc.", size_hint=(1, None), height=100)
        self.text_input_2 = TextInput(multiline=True, hint_text="Description of the room; furniture, other rooms/doors, etc. ", size_hint=(1, None), height=100)
        back_button = Button(text='Back', on_release=self.go_back)
        finish_button = Button(text='Finish', on_release=self.options_screen)

        layout.add_widget(label)
        layout.add_widget(self.text_input)
        layout.add_widget(self.text_input_2)
        layout.add_widget(back_button)
        layout.add_widget(finish_button)

        with layout.canvas.before:
            Color(0.0, 0.0, 0.0, 0)
            self.rect = Rectangle(size=layout.size, pos=layout.pos)

        self.add_widget(layout)

    def go_back(self, button):
        self.parent.current = 'surroundings_screen'

    def options_screen(self, button):
        self.parent.current = 'options_screen'


class OutsideScreen(Screen):
    def __init__(self, **kwargs):
        super(OutsideScreen, self).__init__(**kwargs)
        layout = BoxLayout(orientation='vertical', padding=20, spacing=20)
        label = Label(text="describe the surroundings", font_size=20)
        self.text_input = TextInput(multiline=True, hint_text="sheltered/unsheltered? If sheltered: describe how/with what", size_hint=(1, None), height=100)
        self.text_input_2 = TextInput(multiline=True, hint_text="Describe the roads, bicycle/walking paths visible", size_hint=(1, None), height=100)
        self.text_input_3 = TextInput(multiline=True, hint_text="Describe buildings distinctive objects visible", size_hint=(1, None), height=100)
        self.text_input_4 = TextInput(multiline=True, hint_text="Coordinates", size_hint=(1, None), height=100)
        back_button = Button(text='Back', on_release=self.go_back)
        finish_button = Button(text='Finish', on_release=self.options_screen)

        layout.add_widget(label)
        layout.add_widget(self.text_input)
        layout.add_widget(self.text_input_2)
        layout.add_widget(self.text_input_3)
        layout.add_widget(self.text_input_4)
        layout.add_widget(back_button)
        layout.add_widget(finish_button)

        self.add_widget(layout)

    def go_back(self, button):
        self.parent.current = 'surroundings_screen'

    def options_screen(self, button):
        self.parent.current = 'options_screen'


Builder.load_string('''
<PhotographyScreen>:
    canvas.before:
        Color:
            rgba: 0, 0, 0, 0
        Line:
            rectangle: self.x, self.y, self.width, self.height
            width: 1

<WitnessScreen>:
    # Add any necessary widget definitions and layout for the WitnessScreen here
    # ...
''')


class MyApp(App):
    def build(self):
        sm = ScreenManager(transition=SlideTransition())
        sm.add_widget(LoginScreen(name='login'))
        sm.add_widget(MenuScreen(name='menu'))
        sm.add_widget(Option1Screen(name='option1'))
        sm.add_widget(NotAvailableScreen(name='not_available'))
        sm.add_widget(IdentifyScreen(name='identify'))
        sm.add_widget(PhotographyScreen(name='photography'))
        sm.add_widget(CloseupPhotosScreen(name='closeup_photos'))
        sm.add_widget(Step1NotesScreen(name='step1_notes'))
        sm.add_widget(NotesScreen(name='notes'))
        sm.add_widget(DescribeVictimDeadScreen(name="describe_victim_dead"))
        sm.add_widget(DescribeVictimAliveScreen(name="describe_victim_alive"))
        sm.add_widget(VictimWoundedScreen(name="victim_wounded_screen"))
        sm.add_widget(EvidenceScreen(name="evidence_screen"))
        sm.add_widget(WitnessesScreen(name="witnesses_screen"))
        sm.add_widget(SurroundingsScreen(name="surroundings_screen"))
        sm.add_widget(InsideScreen(name="inside_screen"))
        sm.add_widget(OutsideScreen(name="outside_screen"))
        sm.add_widget(OptionsScreen(name="options_screen"))
        sm.add_widget(AnimalCoveringQuestionScreen(name="animal_covering_screen"))
        sm.add_widget(AnimalColorQuestionScreen(name="animal_color_screen"))
        sm.add_widget(AnimalSizeQuestionScreen(name="animal_size_screen"))
        sm.add_widget(SpecialFeaturesQuestionScreen(name="animal_features_screen"))
        sm.add_widget(AnimalListScreen(name="animal_list"))
        return sm


if __name__ == '__main__':
    Config.set('kivy', 'exit_on_escape', '0')
    MyApp().run()
