from ethiopian_date import EthiopianDateConverter
from datetime import date
def findEthiopianDateNumbers():
    today = date.today()
    return(EthiopianDateConverter.date_to_ethiopian(today))
def findEthiopianDateWordsEnglish():
    months = [
  "Meskerem",
  "Tikimt",
  "Hidar",
  "Tahsas",
  "Tir",
  "Yakatit",
  "Maggabit",
  "Miazia",
  "Ginbot",
  "Sene",
  "Hamle",
  "Nehasa",
  "Pagume"
    ]
    today = date.today()
    dateEth = (EthiopianDateConverter.date_to_ethiopian(today))
    monthName = months[dateEth.month-1]
    day = dateEth.day
    year = dateEth.year
    return (f"{monthName} {day}, {year}")
def findEthiopianDateWordsAmharic():
    months = [
  "መስከረም",
  "ጥቅምት",
  "ህዳር",
  "ታህሳስ",
  "ጥር",
  "የካቲት",
  "መጋቢት",
  "ሚይዚያ",
  "ግንቦት",
  "ሰኔ",
  "ሐምሌ",
  "ነሐሴ",
  "ጳጉሜ"
]
    numbers=[
  "፩", "፪", "፫", "፬", "፭", "፮", "፯", "፰", "፱", "፲",  
  "፲፩", "፲፪", "፲፫", "፲፭","፲፮","፲፯", "፲፰","፲፱", "፳", "፳፩" "፳፪", "፳፫", "፳፬", "፳፭", 
  "፳፮", "፳፯", "፳፰", "፳፱", "፴"
]
    today = date.today()
    dateEth = (EthiopianDateConverter.date_to_ethiopian(today))
    monthName = months[dateEth.month-1]
    day = numbers[dateEth.day-1]
    year = dateEth.year
    return (f"{monthName} {day}")
