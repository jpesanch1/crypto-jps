import PySimpleGUI as sg


def main():
    # print(sg.theme_list())
    # sg.theme("DarkAmber")

    # Define the window layout
    layout = [
        # [
        #     sg.Text("Action", size=(20, 1), justification="left"),
        #     sg.Combo(['DES cipher', 'AES cipher', 'Hash'], key='operation')
        # ],
        [
            sg.Button("DES cipher", size=(20, 1), expand_x=True, key='des'),
            sg.Button("Hash", size=(20, 1), expand_x=True, key='hash')
        ]
    ]

    des_cipher_layout = [
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
        [
            sg.InputText("", size=(20, 1), justification="left", visible=False, disabled=True, background_color="black",
                         key='result2'),
        ]
    ]

    hash_layout = [
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
        [
            sg.InputText("", size=(20, 1), justification="left", visible=False, disabled=True, background_color="black",
                         key='result2'),
        ]
    ]
    window = sg.Window(title="Cryptography", layout=layout)

    while True:
        event, values = window.read()
        # End program if user closes window or
        # presses the OK button
        if event == "des":
            print("DES")
            sg.Window(title="DES cipher calculator", layout=des_cipher_layout).read()
        elif event == "hash":
            print("hash")
            sg.Window(title="Hash calculator", layout=hash_layout).read()
        elif event == sg.WIN_CLOSED:
            break


main()
