from kivy.app import App
from kivy.uix.widget import Widget
from kivy.core.window import Window
from kivy.properties import StringProperty

import datesFinders
class CalendarPage(Widget):
    englishEthDate = StringProperty(datesFinders.findEthiopianDateWordsEnglish())
    amharicEthDate = datesFinders.findEthiopianDateWordsAmharic()
class CalendarApp(App):
    def build(self):
        Window.clearcolor = (1,1,1,1)
        return CalendarPage()
if __name__ == '__main__':
    CalendarApp().run()