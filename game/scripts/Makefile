CHARS := bismarck.rpy helen.rpy janet.rpy john.rpy lilian.rpy narrator.rpy swan.rpy
DIR := characters2
PRE := char_

FILES := $(addprefix $(DIR)/$(PRE), $(CHARS))

# Отображаемые имена
ru_bismarck.rpy := Стэнли Фон Бисмарк
ru_helen.rpy := Хэлен
ru_janet.rpy := Джанет
ru_john.rpy := Джон
ru_lilian.rpy := Лилиана
ru_narrator.rpy := None
ru_swan.rpy := Профессор Свэн

# Шаблон текста файла
define BODY_TEXT
_define $(basename $(1)) = Character($(if $(filter None,$(2)),None,_("$(2)")))

layeredimage $(basename $(1)):
    group body:
        attribute body_aa default:
            "characters/$(basename $(1))/$(basename $(1))_body_aa.png"
        attribute body_ab: 
            "characters/$(basename $(1))/$(basename $(1))_body_ab.png"
        attribute body_ac:
            "characters/$(basename $(1))/$(basename $(1))_body_ac.png"
        attribute body_ad:
            "characters/$(basename $(1))/$(basename $(1))_body_ad.png"
        attribute body_ae:
            "characters/$(basename $(1))/$(basename $(1))_body_ae.png"
        attribute body_af:
            "characters/$(basename $(1))/$(basename $(1))_body_af.png"

    group head:
        attribute head_a default: 
            "characters/$(basename $(1))/$(basename $(1))_head_a.png"
        attribute head_b: 
            "characters/$(basename $(1))/$(basename $(1))_head_b.png"
        attribute head_c: 
            "characters/$(basename $(1))/$(basename $(1))_head_c.png"
        attribute head_d: 
            "characters/$(basename $(1))/$(basename $(1))_head_d.png"
        attribute head_e: 
            "characters/$(basename $(1))/$(basename $(1))_head_e.png"
        attribute head_f: 
            "characters/$(basename $(1))/$(basename $(1))_head_f.png"
endef

.PHONY: all clean

all: $(FILES)

$(DIR):
	mkdir -p $(DIR)

# Правило генерации каждого файла
$(DIR)/$(PRE)%.rpy: | $(DIR)
	@echo "Создаю: $@"
	$(eval CUR_CHAR := $*.rpy)
	$(file > $@,$(call BODY_TEXT,$(CUR_CHAR),$(ru_$(CUR_CHAR))))

clean:
	rm -rf $(DIR)