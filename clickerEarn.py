from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.popup import Popup
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.image import Image
from kivy.uix.filechooser import FileChooserIconView

class BaseScreen(Screen):
    def __init__(self, **kwargs):
        super(BaseScreen, self).__init__(**kwargs)
        self.layout = BoxLayout(orientation='vertical')
        self.add_widgets()
        self.add_widget(self.layout)

    def add_widgets(self):
        pass

    def go_back(self, instance):
        app = App.get_running_app()
        app.root.current = 'login'

    def show_error_message(self, message):
        popup = Popup(title='Error', content=Label(text=message), size_hint=(None, None), size=(400, 200))
        ok_button = Button(text='OK', size_hint=(None, None), size=(100, 50))
        ok_button.bind(on_press=popup.dismiss)
        popup.content.add_widget(ok_button)
        popup.open()

class LoginScreen(BaseScreen):
    def add_widgets(self):
        title_label = Label(text='Login', size_hint_y=0.1)
        self.layout.add_widget(title_label)
        username_label = Label(text='Username:')
        self.layout.add_widget(username_label)
        self.username_input = TextInput()
        self.layout.add_widget(self.username_input)
        password_label = Label(text='Password:')
        self.layout.add_widget(password_label)
        self.password_input = TextInput(password=True)
        self.layout.add_widget(self.password_input)
        login_button = Button(text='Login')
        login_button.bind(on_press=self.login)
        self.layout.add_widget(login_button)
        register_button = Button(text='Register')
        register_button.bind(on_press=self.go_to_register)
        self.layout.add_widget(register_button)

    def login(self, instance):
        username = self.username_input.text
        password = self.password_input.text
        if not username or not password:
            self.show_error_message("Username and password are required.")
            return
        # Logika logowania
        print(f'Logged in with username: {username} and password: {password}')
        app = App.get_running_app()
        app.root.current = 'panel'

    def go_to_register(self, instance):
        app = App.get_running_app()
        app.root.current = 'register'

class RegisterScreen(BaseScreen):
    def add_widgets(self):
        self.firstname_input = TextInput(hint_text='First name')
        self.layout.add_widget(self.firstname_input)
        self.lastname_input = TextInput(hint_text='Last name')
        self.layout.add_widget(self.lastname_input)
        self.email_input = TextInput(hint_text='Email')
        self.layout.add_widget(self.email_input)
        self.address_input = TextInput(hint_text='Address')
        self.layout.add_widget(self.address_input)
        self.password_input = TextInput(hint_text='Password', password=True)
        self.layout.add_widget(self.password_input)
        register_button = Button(text='Register')
        register_button.bind(on_press=self.register)
        self.layout.add_widget(register_button)
        back_button = Button(text='Back')
        back_button.bind(on_press=self.go_back)
        self.layout.add_widget(back_button)

    def register(self, instance):
        firstname = self.firstname_input.text
        lastname = self.lastname_input.text
        email = self.email_input.text
        address = self.address_input.text
        password = self.password_input.text
        if not firstname or not lastname or not email or not address or not password:
            self.show_error_message("All fields are required.")
            return
        # Logika rejestracji
        print(f'Registered user: {firstname} {lastname}, email: {email}, address: {address}, password: {password}')
        app = App.get_running_app()
        app.root.current = 'login'

class EarningsScreen(BaseScreen):
    def __init__(self, **kwargs):
        super(EarningsScreen, self).__init__(**kwargs)
        self.earn_count = 0

    def add_widgets(self):
        self.earnings_label = Label(text='Earned: 0,00€')
        self.layout.add_widget(self.earnings_label)
        earn_button = Button(text='Earn Money')
        earn_button.bind(on_press=self.earn_money)
        self.layout.add_widget(earn_button)
        back_button = Button(text='Back')
        back_button.bind(on_press=self.go_back_to_panel)
        self.layout.add_widget(back_button)

    def earn_money(self, instance):
        self.earn_count += 1
        earnings_formatted = "{:.2f}".format(self.earn_count * 10)
        self.earnings_label.text = f'Earned: {earnings_formatted}€'

    def go_back_to_panel(self, instance):
        app = App.get_running_app()
        app.root.current = 'panel'

class UserPanelScreen(BaseScreen):
    def add_widgets(self):
        view_profile_button = Button(text='View Profile')
        view_profile_button.bind(on_press=self.view_profile)
        self.layout.add_widget(view_profile_button)
        edit_profile_button = Button(text='Edit Profile')
        edit_profile_button.bind(on_press=self.edit_profile)
        self.layout.add_widget(edit_profile_button)
        earnings_button = Button(text='View Earnings')
        earnings_button.bind(on_press=self.view_earnings)
        self.layout.add_widget(earnings_button)
        logout_button = Button(text='Logout')
        logout_button.bind(on_press=self.logout)
        self.layout.add_widget(logout_button)

    def view_profile(self, instance):
        app = App.get_running_app()
        app.root.current = 'profile'

    def edit_profile(self, instance):
        app = App.get_running_app()
        app.root.current = 'edit_profile'

    def view_earnings(self, instance):
        app = App.get_running_app()
        app.root.current = 'earnings'

    def logout(self, instance):
        app = App.get_running_app()
        app.root.current = 'login'

class ProfileScreen(BaseScreen):
    def __init__(self, **kwargs):
        super(ProfileScreen, self).__init__(**kwargs)

    def add_widgets(self):
        profile_image = Image(source='profile_image.png', size_hint=(None, None), size=(100, 100), allow_stretch=True, keep_ratio=True)
        profile_image.bind(on_press=self.change_profile_image)
        self.layout.add_widget(profile_image)
        back_button = Button(text='Back to Menu')
        back_button.bind(on_press=self.go_back_to_menu)
        # Dodajemy przycisk powrotu na samym końcu
        self.layout.add_widget(back_button)

    def on_pre_enter(self):
        app = App.get_running_app()
        user_info = app.get_user_info()
        self.layout.clear_widgets()  # Clear existing widgets
        self.add_widgets()
        for key, value in user_info.items():
            if key != 'password':
                self.layout.add_widget(Label(text=f'{key.capitalize()}: {value}'))

    def change_profile_image(self, instance):
        file_chooser = FileChooserIconView()
        file_chooser.bind(on_submit=self.on_file_selected)
        popup = Popup(title="Select Image", content=file_chooser, size_hint=(0.9, 0.9))
        popup.open()

    def on_file_selected(self, instance):
        selected_file = instance.selection and instance.selection[0]
        if selected_file:
            # Here you would implement logic to save the selected image as the profile picture
            print(f"Selected file: {selected_file}")
        else:
            print("No file selected")

    def go_back_to_menu(self, instance):
        app = App.get_running_app()
        app.root.current = 'panel'


class EditProfileScreen(BaseScreen):
    def add_widgets(self):
        self.firstname_input = TextInput(hint_text='First name')
        self.layout.add_widget(self.firstname_input)
        self.lastname_input = TextInput(hint_text='Last name')
        self.layout.add_widget(self.lastname_input)
        self.email_input = TextInput(hint_text='Email')
        self.layout.add_widget(self.email_input)
        self.address_input = TextInput(hint_text='Address')
        self.layout.add_widget(self.address_input)
        self.password_input = TextInput(hint_text='Password', password=True)
        self.layout.add_widget(self.password_input)
        save_button = Button(text='Save')
        save_button.bind(on_press=self.save_profile)
        self.layout.add_widget(save_button)
        back_button = Button(text='Back')
        back_button.bind(on_press=self.go_back_to_panel)
        self.layout.add_widget(back_button)

    def save_profile(self, instance):
        firstname = self.firstname_input.text
        lastname = self.lastname_input.text
        email = self.email_input.text
        address = self.address_input.text
        password = self.password_input.text
        if not firstname or not lastname or not email or not address or not password:
            self.show_error_message("All fields are required.")
            return
        # Logika zapisywania profilu
        print(f'Profile updated: {firstname} {lastname}, email: {email}, address: {address}, password: {password}')
        app = App.get_running_app()
        app.root.current = 'panel'

    def go_back_to_panel(self, instance):
        app = App.get_running_app()
        app.root.current = 'panel'

    def save_profile(self, instance):
        firstname = self.firstname_input.text
        lastname = self.lastname_input.text
        email = self.email_input.text
        address = self.address_input.text
        password = self.password_input.text
        if not firstname or not lastname or not email or not address or not password:
            self.show_error_message("All fields are required.")
            return
        # Logika zapisywania profilu
        print(f'Profile updated: {firstname} {lastname}, email: {email}, address: {address}, password: {password}')
        app = App.get_running_app()
        app.root.current = 'panel'

class EarningApp(App):
    def build(self):
        self.sm = ScreenManager()
        self.login_screen = LoginScreen(name='login')
        self.register_screen = RegisterScreen(name='register')
        self.earnings_screen = EarningsScreen(name='earnings')
        self.user_panel_screen = UserPanelScreen(name='panel')
        self.profile_screen = ProfileScreen(name='profile')
        self.edit_profile_screen = EditProfileScreen(name='edit_profile')  # Dodaj nowy ekran edycji profilu
        self.sm.add_widget(self.login_screen)
        self.sm.add_widget(self.register_screen)
        self.sm.add_widget(self.earnings_screen)
        self.sm.add_widget(self.user_panel_screen)
        self.sm.add_widget(self.profile_screen)
        self.sm.add_widget(self.edit_profile_screen)  # Dodaj nowy ekran edycji profilu do menedżera ekranów
        return self.sm

    def get_user_info(self):
        # Tu można umieścić logikę pobierania informacji o zalogowanym użytkowniku
        return {'first_name': 'John', 'last_name': 'Doe', 'email': 'john@example.com', 'address': '123 Main St'}

if __name__ == '__main__':
    EarningApp().run()
