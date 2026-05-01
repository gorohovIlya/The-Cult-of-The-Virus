# Вы можете расположить сценарий своей игры в этом файле.
# Определение персонажей игры.
# Вместо использования оператора image можете просто
# складывать все ваши файлы изображений в папку images.
# Например, сцену bg room можно вызвать файлом "bg room.png",
# а eileen happy — "eileen happy.webp", и тогда они появятся в игре.
# Игра начинается здесь:
label start:
    'Начинаем'
    jump a1

label a1:
    'Сцена а1'
    jump a2

label a2:
    'Сцена а2'
    menu:
        'Согласиться':
            jump a4
        'Отказаться':
            jump a51

label a4:
    'Сцена а4'
    jump a5

label a5:
    'Сцена а5'
    jump a6

label a6:
    'Сцена а6'
    jump a7

label a7:
    'Сцена а7'
    jump a8

label a8:
    'Сцена а8'
    menu:
        'Согласиться':
            jump a10
        'Отказаться':
            jump a9

label a9:
    'Сцена a9'
    jump a12
    
label a10:
    'Сцена а10'
    jump a12

label a12:
    'Сцена а12'
    menu:
        'Прогуляться по коридору':
            jump a13
        'Остаться и осмотреть аудиторию':
            jump a64
        'Уйти':
            jump a50

label a13:
    menu:
        'Налево':
            jump a14
        'Направо':
            jump a21

label a14:
    'Сцена а14'
    jump a15

label a15:
    'Сцена а15'
    menu:
        'Пройти мимо':
            jump a16
        'Зайти в аудиторию':
            jump a17

label a16:
    'Сцена а16'
    jump a18

label a17:
    'Сцена а17'
    jump a18

label a18:
    'Сцена а18'
    jump a19

label a19:
    'Сцена а19'
    jump a20

label a20:
    'Сцена а20'
    jump a24

label a24:
    'Сцена а24'
    jump a25

label a26:
    'Сцена а26'
    menu:
        'Осмотреть':
            jump a27
        'Не осматривать':
            jump a28

label a29:
    'Сцена а29'
    jump a30

label a30:
    'Сцена а30'

label a31:
    'Сцена а31'
    jump a32

label a32:
    'Сцена а32'
    jump a33

label a33:
    'Сцена а33'
    jump a34

label a34:
    'Сцена а34'
    menu:
        'Остаться':
            jump a35
        'Уйти домой':
            jump a42

label a36:
    'Сцена а36'
    jump a37

label a37:
    'Сцена а37'
    jump a38

label a38:
    'Сцена а38'
    jump a39

label a39:
    'Сцена а39'
    menu:
        'Отказаться':
            jump a40
        'Согласиться':
            jump a41

label a42:
    'Сцена а42'
    jump a43

label a43:
    'Сцена а43'
    jump a44

label a44:
    'Сцена а44'
    jump a45

label a45:
    'Сцена а45'
    jump a46

label a46:
    'Сцена а46'
    jump a46

label a47:
    'Сцена а47'
    jump a48

label a48:
    'Сцена а48'
    jump a49

label a49:
    'Сцена а49'
    jump a53

label a53:
    'Сцена а53'
    jump a54

label a54:
    'Сцена а54'
    jump a55

label a55:
    'Сцена а55'
    jump a56

label a56:
    'Сцена а56'
    jump a57

label a57:
    'Сцена а57'
    return

label a58:
    'Сцена а58'
    jump a59

label a59:
    'Сцена а59'
    jump a60

label a60:
    'Сцена а60'
    return

label a61:
    'Сцена а61'
    jump a62

label a62:
    'Сцена а62'
    jump a63

label a63:
    'Сцена а63'
    return

label a64:
    'Сцена а64'
    jump a65

label a65:
    'Сцена а65'
    jump a66

label a66:
    'Сцена а66'
    menu:
        'Забрать документы':
            jump a67
        'Оставить документы':
            jump a68

label a67:
    'Сцена а67'
    jump a68

label a68:
    'Сцена а68'
    jump a29

label a50:
    'Сцена а50'
    jump a53