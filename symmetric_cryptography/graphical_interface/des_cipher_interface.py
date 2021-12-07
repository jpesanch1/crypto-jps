import PySimpleGUI as sg
from symmetric_cryptography import des_cipher


def main():

    # print(sg.theme_list())
    # sg.theme("DarkAmber")

    # Define the window layout
    layout = [
        # [sg.Text("DES Cipher Calculator", expand_x=True, justification="center")],
        [
            sg.Text("Message (hex)", size=(20, 1), justification="left"),
            sg.InputText(size=60, key='message')
        ],
        [
            sg.Text("Key (hex)", size=(20, 1), justification="left"),
            sg.InputText(size=60, key='key')
        ],
        [
            sg.Text("IV (hex)", size=(20, 1), justification="left"),
            sg.InputText(size=60, key='iv')
        ],
        [
            sg.Button("Encrypt", size=(20, 1), expand_x=True, key='encrypt'),
            sg.Button("Decrypt", size=(20, 1), expand_x=True, key='decrypt')
        ],
        {
            sg.Text("", size=(20, 1), justification="left", visible=False, key='result'),
            sg.InputText("", size=(20, 1), justification="left", visible=False, disabled=True, background_color="black",
                         key='result2'),
        }
    ]
    window = sg.Window(title="DES Cipher Calculator", layout=layout)

    while True:
        event, values = window.read()
        # End program if user closes window or
        # presses the OK button
        message = values['message']
        key = values['key']
        iv = values['iv']
        result = ""
        if event == "encrypt":
            result = des_cipher.encrypt(message, key, iv)
        elif event == "decrypt":
            result = des_cipher.decrypt(message, key, iv)
        elif event == sg.WIN_CLOSED:
            break

        print(result)
        window["result"].update(result, visible=True)
        window["result2"].update(result, visible=True)


main()
