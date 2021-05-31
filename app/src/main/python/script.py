import requests
from bs4 import BeautifulSoup

def request():
    session = requests.Session()
    r = session.get('https://ruokalistat.ravitsemispalvelut.fi/AromieMenus/FI/Default/HYVINKAA/HysaKoulut/Restaurant.aspx')

    soup = BeautifulSoup(r.text,features="html.parser")

    div = soup.find('div', {'id':'MainContent_WeekdayListView_DataPanel_0'})
    children = div.findChildren('span')

    dishesh = [
        'MainContent_WeekdayListView_Meals_0_Meals_0_SecureLabelDish_0',
        'MainContent_WeekdayListView_Meals_0_Meals_0_SecureLabelDish_1',
        'MainContent_WeekdayListView_Meals_0_Meals_0_SecureLabelDish_2',
        'MainContent_WeekdayListView_Meals_0_Meals_0_SecureLabelDish_3',
        'MainContent_WeekdayListView_Meals_0_Meals_0_SecureLabelDish_4',
        'MainContent_WeekdayListView_Meals_0_Meals_0_SecureLabelDish_5',
        'MainContent_WeekdayListView_Meals_0_Meals_0_SecureLabelDish_6'
    ]
    date_id = 'MainContent_WeekdayListView_SecureLabel3_0'

    date = ''
    lunch = ''

    for child in children:
        id = child.get('id')
        if id in dishesh:
            dish = child.text.replace(' ', '')
            lunch += dish + ', '
        if id == date_id:
            date = child.text

    size = len(lunch)
    lunch = lunch[:size -2 ]

    return date, lunch