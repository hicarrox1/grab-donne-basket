import flet as ft
import requests
from bs4  import BeautifulSoup as bs



def main(page:ft.Page):

    page.theme_mode = "light"

    page.fonts = {
        "kobani": "kobani.ttf"
    }
    
    # CALLBACKS SECTION
    def open_url(e):
        page.launch_url(e.data)

    # CONTROLS SECTION
    c_text = ft.Text("basket resultat 🏀",color=ft.colors.CYAN,style=ft.TextThemeStyle.TITLE_LARGE)

    row = ft.Row([c_text],alignment=ft.MainAxisAlignment.CENTER)

    c3 = ft.Container(content=row,padding=50,)

    #c_test = ft.TextButton(text="lol",on_click= lambda e: print(e.control.text))
    
    #c_date_selector = ft.Row([ft.TextField() for _ in range(3)])

    t = ft.Tabs(
        animation_duration=300,
        tabs=[],
        expand=1
    )

    page.add(c3,t)

    # FONCTIONS SECTION

    def init():
        page.scroll = True

        page_basket = requests.get("https://www.matchendirect.fr/basket/")
        soup = bs(page_basket.text,"lxml")
        leagues = soup.find_all("div", attrs={'class':'tournament basket table-block'})
        
        leagues = sorted(leagues,key=get_pays_name)
        
        name = ''
        current_tab = None

        for league in leagues:
            new_name = get_pays_name(league)
            if new_name != name:
                name = new_name
                current_tab = ft.Tabs(animation_duration=300, tabs=[], expand=1)
                t.tabs.append(ft.Tab(name,content=current_tab))

            tableau = create_tableau_league()
            current_tab.tabs.append(ft.Tab(text=league.thead.find('th',attrs={'class':'time'}).contents[1],content= tableau))

            met_a_jour_tableau(get_info_league(league),tableau)

        compte = 0

        """for tab in t.tabs:
            league_match = leagues[compte].tbody.find_all("tr")
            met_a_jour_tableau(get_info_league(league_match), tab.content)
            compte += 1
        
        print(get_pays_name(leagues[0]))"""

    def get_info_league(league):

        info_league = []

        league_match = league.tbody.find_all("tr")

        for match in league_match:

            info = []
            info.append(match.find('td', attrs={'class':'time'}).contents[0])
            teams = match.find('td', attrs={'class':'teams'})
            score = match.find('td', attrs={'class':'score'})
            #statut = match.find('td', attrs={'class':'status jPlayed'})
            quarter1 = match.find('td', attrs={'class':'quarter p1'})
            quarter2 = match.find('td', attrs={'class':'quarter p2'})
            quarter3 = match.find('td', attrs={'class':'quarter p3'})
            quarter4 = match.find('td', attrs={'class':'quarter p4'})
            liste_donne = [teams.a, score, quarter1, quarter2, quarter3, quarter4]
            info.append([donee.span.string for donee in liste_donne])
            info.append([donee.contents[2].string for donee in liste_donne])
            #print(statut,league)
            info.append(match.find('span',attrs={'class':'statusname'}).string)

            info_league.append(info)

        return info_league



    def met_a_jour_tableau(info_league:list, tableau:ft.Control):

        for match in info_league:

            if None in match[1] or None in match[2] :

                match[1] = change_None_into_str(match[1],"-")
                match[2] = change_None_into_str(match[2],'-')

                gagnant = '?'

            else:
                if match[1][1] == match[2][1]:
                    gagnant = 'nul'
                elif match[1][1] > match[2][1]:
                    gagnant = match[1][0]
                else:
                    gagnant = match[2][0]

            tableau.rows.append(ft.DataRow([
                ft.DataCell(ft.Text(match[0])),
                ft.DataCell(ft.Text(match[1][0]+'\n'+match[2][0])),
                ft.DataCell(ft.Text(match[1][1]+'\n'+match[2][1])),
                ft.DataCell(ft.Text(match[1][2]+'\n'+match[2][2])),
                ft.DataCell(ft.Text(match[1][3]+'\n'+match[2][3])),
                ft.DataCell(ft.Text(match[1][4]+'\n'+match[2][4])),
                ft.DataCell(ft.Text(match[1][5]+'\n'+match[2][5])),
                ft.DataCell(ft.Text(match[3])),
                ft.DataCell(ft.Text(gagnant,color=ft.colors.RED))
                ]))
            
    def change_None_into_str(liste:list,lettre:str):

        result = []

        for el in liste:

            if el == None:

                result.append(lettre)
            else:
                result.append(el)

        return result
    
    def create_tableau_league():

        return ft.DataTable(
            columns=[
                ft.DataColumn(ft.Text("heure")),
                ft.DataColumn(ft.Text("equipe")),
                ft.DataColumn(ft.Text("score")),
                ft.DataColumn(ft.Text("quarter 1")),
                ft.DataColumn(ft.Text("quarter 2")),
                ft.DataColumn(ft.Text("quarter 3")),
                ft.DataColumn(ft.Text("quarter 4")),
                ft.DataColumn(ft.Text("statut")),
                ft.DataColumn(ft.Text("gagnant")),
            ],
            rows=[],
        )
    
    def get_pays_name(league:list):

        league_name = league.thead.find('th',attrs={'class':'time'}).contents[1]

        compte = 0
        for lettre in league_name:
            if lettre == '-':
                break
            compte += 1
        
        return league_name[:compte]

    init()

    page.update()

ft.app(target=main,assets_dir=".")

#kozuv
#pelister