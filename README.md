# Description of our project

# «The Virus Cult» — Visual Novel & Official Website

## Visual Novel — Horror Genre

**Age rating:** 18+ (strictly prohibited for children)

**Disclaimer:** All characters are fictitious. Any resemblance to real persons or events is purely coincidental.

---

### Plot

The story takes place in Berkeley. The protagonist, Helen, witnesses strange and unsettling events unfolding at the Institute of Solar-Terrestrial Physics. There, she meets Liliana — a member of an underground resistance fighting against a mysterious virus cult. Helen decides to join her. What happens next is for the player to discover.

---

### Development Tools

#### Coding
- Python 3.13
- Ren'Py 8.5.2

#### Design
- Krita
- Figma

#### External Python Libraries
- python-chess

---

## Official Website

The website serves as a promotional hub for the visual novel.

### Sections

- **Main page** — general information and highlights
- **About us** — the team and the project's vision
- **Download** — links to the latest version of the visual novel
- **Feedback** — contact form and messages
- **Plans** — development roadmap
- **Support us** — ways to help the project (donations, shares, etc.)

### Technology Stack

#### Frontend
- HTML5
- CSS3
- JavaScript (ECMAScript 2025 / ES16)
- Blade (Laravel templating engine)

#### Backend
- Laravel 13

> For more information about the website, use this link.
    [Github](https://github.com/gorohovIlya/the-virus-cult-website.git)

# End of the description
---

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
