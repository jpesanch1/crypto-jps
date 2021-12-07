import PySimpleGUI as sg


def main():

    # print(sg.theme_list())
    sg.theme("DarkGrey")

    # Define the window layout
    layout = [
        [sg.Text("OpenCV Demo", size=(60, 1), justification="center")],

        [sg.InputText(size=20)],

        [sg.Image(filename="", key="-IMAGE-")],
        [sg.Radio("None", "Radio", True, size=(10, 1))],
        [
            sg.Radio("threshold", "Radio", size=(10, 1), key="-THRESH-"),
            sg.Slider(
                (0, 255),
                128,
                1,
                orientation="h",
                size=(40, 15),
                key="-THRESH SLIDER-",
            ),
        ],
        [
            sg.Radio("canny", "Radio", size=(10, 1), key="-CANNY-"),
            sg.Slider(
                (0, 255),
                128,
                1,
                orientation="h",
                size=(20, 15),
                key="-CANNY SLIDER A-",
            ),
            sg.Slider(
                (0, 255),
                128,
                1,
                orientation="h",
                size=(20, 15),
                key="-CANNY SLIDER B-",
            ),
        ],
        [
            sg.Radio("blur", "Radio", size=(10, 1), key="-BLUR-"),
            sg.Slider(
                (1, 11),
                1,
                1,
                orientation="h",
                size=(40, 15),
                key="-BLUR SLIDER-",
            ),
        ],
        [
            sg.Radio("hue", "Radio", size=(10, 1), key="-HUE-"),
            sg.Slider(
                (0, 225),
                0,
                1,
                orientation="h",
                size=(40, 15),
                key="-HUE SLIDER-",
            ),
        ],
        [
            sg.Radio("enhance", "Radio", size=(10, 1), key="-ENHANCE-"),
            sg.Slider(
                (1, 255),
                128,
                1,
                orientation="h",
                size=(40, 15),
                key="-ENHANCE SLIDER-",
            ),
        ],
        [sg.Button("Exit", size=(10, 1))],
    ]

    layout2 = [
        [sg.Text("Hash Calculator", size=(60, 1), justification="center")],
        [
            sg.Text("Message", size=(10, 1), justification="center"),
            sg.InputText(size=20, key='message')
        ],

        [sg.Text("Algorithm", size=(10, 1))],
        [
            sg.Radio("md5", "Radio", size=(10, 1), key='md5'),
            sg.Radio("sha-1", "Radio", size=(10, 1), key='sha1'),
            sg.Radio("sha-256", "Radio", size=(10, 1), key='sha256'),
            sg.Radio("sha-512", "Radio", size=(10, 1), key='sha512')
        ],

        [sg.Button("Calculate", size=(10, 1), key='calcular')],
    ]
    window = sg.Window(title="Cryptography", layout=layout2)

    while True:
        event, values = window.read()
        # End program if user closes window or
        # presses the OK button
        if event == "calcular":
            print(values['message'])  # get the content of multiline via its unique key
        elif event == sg.WIN_CLOSED:
            break

main()
