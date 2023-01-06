import trello
import os
from dotenv import load_dotenv
load_dotenv()

# Erstelle eine Trello-API-Instanz
trello_api = trello.TrelloApi(os.environ['API_KEY'])

# Setze deinen persönlichen Token
trello_api.set_token(os.environ['TOKEN'])

def Programm(kartenname, board):
    # Karte mit dem Namen Beamer lesen
    beamercard = trello_api.boards.get_card(board)
    for card in beamercard:
        if card['name'] == kartenname:
            oldcard_ID = card['id']
            oldcard_name = card['name']
            oldcard_desc = card['desc']
            oldcard_idlist = card['idList']

    #cardIDX = trello_api.cards.get(oldcardID)
    # print(oldcardID)
    # print(oldcardID_index)
    #print(cardIDX)

    # Karte duplizieren
    duplicate_card = trello_api.cards.new(
        name=oldcard_name,
        desc=oldcard_desc,
        idList=oldcard_idlist
    )

    # Neue KartenID merken
    new_cardID = duplicate_card['id']

    # Lese die Eigenschaften der Checkliste, die du duplizieren möchtest
    original_checklist = trello_api.cards.get_checklist(oldcard_ID)
    original_checklist_id = original_checklist[0]['id']

    # Erstelle eine neue Checkliste mit den Eigenschaften der originalen Checkliste
    duplicate_checklist = trello_api.checklists.new(
        name=original_checklist[0]['name'],
        idCard=new_cardID
    )

    new_checklistID = duplicate_checklist['id']

    # Lese alle Items der originalen Checkliste ein
    original_items = trello_api.checklists.get_checkItem(original_checklist_id)

    # Iteriere über die originalen Items und erstelle für jedes ein neues Item in der neuen Checkliste
    for item in original_items:
        trello_api.checklists.new_checkItem(
            name=item['name'],
            idChecklist=new_checklistID
        )

    # Alte Karte löschen
    #trello_api.cards.delete(oldcard_ID)

    # Alte Karte archivieren
    trello_api.cards.update_closed(oldcard_ID, 'true')

# Ausführung
# Varianten (Beamer, Stream, Regie, Kamera)
# Board "Testboard:" 'GKbrBHkk'

Programm('Beamer', "GKbrBHkk")
Programm('Stream', 'GKbrBHkk')
Programm('Regie', 'GKbrBHkk')
Programm('Kamera', 'GKbrBHkk')
