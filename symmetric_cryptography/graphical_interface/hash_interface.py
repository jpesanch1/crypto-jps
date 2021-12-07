import PySimpleGUI as sg
from symmetric_cryptography import des_cipher


def main():

    # print(sg.theme_list())
    # sg.theme("DarkAmber")

    # Define the window layout
    layout = [
        [
            sg.Text("Message (hex)", size=(20, 1), justification="left"),
            sg.InputText(size=60, key='message')
        ],
        [
            sg.Text("Algorithm", size=(20, 1), justification="left"),
            sg.Combo(['MD5', 'SHA-1', 'SHA-256', 'SHA-256'], key='algorithm')
        ],
        [
            sg.Button("Calculate", size=(20, 1), expand_x=True, key='calculate')
        ],
        {
            sg.Text("", size=(20, 1), justification="left", visible=False, key='result'),
            sg.InputText("", size=(20, 1), justification="left", visible=False, disabled=True, background_color="black",
                         key='result2'),
        }
    ]
    window = sg.Window(title="Hash calculator", layout=layout)

    while True:
        event, values = window.read()
        # End program if user closes window or
        # presses the OK button
        message = values['message']
        algorithm = values['algorithm']
        result = ""
        if event == "calculate":
            result = "jajaja " + algorithm
        elif event == sg.WIN_CLOSED:
            break

        print(result)
        window["result"].update(result, visible=True)
        window["result2"].update(result, visible=True)


main()
