## Структура проекта

```
└── game
    ├── audio
    ├── cache
    ├── chess   # Python-библиотека
    ├── gui
    │   ├── bar
    │   ├── button
    │   ├── overlay
    │   ├── phone
    │   │   ├── bar
    │   │   ├── button
    │   │   ├── overlay
    │   │   ├── scrollbar
    │   │   └── slider
    │   ├── scrollbar
    │   └── slider
    ├── images  # Изображения (фоны и спрайты)
    │   ├── backgrounds
    │   ├── characters
    │   │   ├── bismarck
    │   │   ├── janet
    │   │   ├── john
    │   │   ├── unknown
    │   │   └── virus
    │   └── chess_puzzle
    ├── libs
    ├── saves
    ├── scripts # Скрипты 
    │   └── characters
    └── tl
        └── None
```
## Makefile (в папке characters)

создаёт файлы со спрайтами персонажей вида

```
define cultist = Character(_("Персонаж"))

layeredimage cultist:
    group body:
        attribute body_aa default:
            "characters/character/character_body_aa.png"
        ...

    group head:
        attribute head_a default: 
            "characters/cultist/character_head_a.png"
        ...

```
### Запуск

```
Make
```

## Rename.sh (в images/characters)

Переименовывает файлы персонажей






