from kivy.app import App
from kivy.uix.widget import Widget
from kivy.core.window import Window
from kivy.properties import StringProperty
from kivy.clock import Clock
import datesFinders

class CalendarPage(Widget):
    englishEthDate = StringProperty()
    amharicEthDate = StringProperty()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.update_dates()
        Clock.schedule_interval(lambda dt: self.update_dates(), 60)  # Update every 60 seconds

    def update_dates(self):
        self.englishEthDate = datesFinders.findEthiopianDateWordsEnglish()
        self.amharicEthDate = datesFinders.findEthiopianDateWordsAmharic()

class CalendarApp(App):
    def build(self):
        Window.clearcolor = (1,1,1,1)
        return CalendarPage()

if __name__ == '__main__':
    CalendarApp().run()
