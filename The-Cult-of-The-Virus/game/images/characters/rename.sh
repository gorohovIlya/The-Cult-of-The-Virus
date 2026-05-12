#!/bin/bash

TARGET_DIR="."
char_name="janet_"

# Настраиваем разделитель полей, чтобы цикл корректно читал имена с пробелами
IFS=$'\n'

for file in "$TARGET_DIR"/*; do
    # Пропускаем, если это не файл или если файл сам скрипт
    [ -f "$file" ] || continue
    [[ "$file" == *"$0"* ]] && continue

    dir=$(dirname "$file")
    base=$(basename "$file")

    # 1. Перевод в нижний регистр
    new_base="${base,,}"

    # 2. Замена ПРОБЕЛА на нижнее ПОДЧЕРКИВАНИЕ
    new_base="${new_base// /_}"

    # 3. Твои дополнительные замены
    new_base="${new_base//тело/body}"
    new_base="${new_base//голова/head}"
    new_base="$char_name$new_base"
    new_name="$dir/$new_base"

    # Переименовываем только если имя реально изменилось
    if [ "$file" != "$new_name" ]; then
        if [ -e "$new_name" ]; then
            echo "Предупреждение: Файл '$new_name' уже существует, пропускаю '$file'"
        else
            mv "$file" "$new_name"
            echo "Выполнено: '$file' -> '$new_name'"
        fi
    fi
done
