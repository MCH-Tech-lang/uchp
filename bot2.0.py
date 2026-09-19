import time, random, uiautomator2 as u2, winsound

PORT = "127.0.0.1:5555"
# Наша главная цель на экране среди всех галочек
TARGET_SHIFT = "Производство непрофиль" 

try:
    d = u2.connect(PORT)
    print("🤖 CONNECTED TO OZON HIRE!")
except Exception as e:
    print(f"CONNECTION ERROR: {e}"); exit()

def click_element_center(element):
    """Находит центр элемента на экране и кликает по нему"""
    b = element.info['bounds']
    cx = (b['left'] + b['right']) // 2
    cy = (b['top'] + b['bottom']) // 2
    d.click(cx, cy)

def main():
    print(f"🤖 Бот запущен. Ищу ГОРЯЩЕЕ '{TARGET_SHIFT}' среди списка смен...")
    
    while True:
        try:
            # 1. Мы находимся на экране, где вывалились все смены с галочками.
            # Ищем глазами строку "Производство непрофиль"
            production_row = d(textContains=TARGET_SHIFT)
            
            if production_row.exists:
                # 2. Ищем значок огонька (проверяем, горящая ли смена)
                hot_icon = d(resourceIdMatches=".*(hot|fire|flame|priority|burning|status).*")
                if not hot_icon.exists:
                    hot_icon = d(descriptionMatches=".*(Горящая|горящая|огонь|Огонь|hot|fire).*")
                
                # ТЕСТ КЛИКОВ: Чтобы проверить, что бот выберет именно Производство (а не Размещение),
                # временно замените строчку ниже на: if True:
                if hot_icon.exists:
                    print(f"🔥 НАЙДЕНА ГОРЯЩАЯ СМЕНА: {TARGET_SHIFT}!")
                    
                    # КЛИК 1: Кликаем точно по центру строки "Производство непрофиль"
                    # Это активирует именно ту круглую галочку, которая привязана к производству
                    print("-> Выбираю галочку Производства...")
                    click_element_center(production_row)
                    time.sleep(0.4)
                    
                    # КЛИК 2: Нажимаем большую кнопку "Записаться" в самом низу экрана
                    # Координаты: центр по ширине (0.5), самый низ экрана (0.92)
                    print("-> Нажимаю общую кнопку ЗАПИСАТЬСЯ...")
                    d.click(0.5, 0.92)
                    time.sleep(0.8)
                    
                    # КЛИК 3: Клик на случай всплывающего окна подтверждения ("Вы уверены?")
                    d.click(0.7, 0.6) 
                    
                    print("🎉 Попытка записи выполнена! Проверьте приложение.")
                    winsound.Beep(2500, 2000) # Победный писк
                    break # Выключаем бота после успешного выполнения
                else:
                    print("Производство непрофиль есть на экране, но оно без огонька (очередь). Пропускаю...")
            
            # 3. ОБНОВЛЕНИЕ СТРАНИЦЫ
            # Чтобы обновить список с галочками, боту нужно выйти из этого окна назад на календарь и зайти снова
            back_arrow = d(descriptionMatches=".*(Назад|back|Arrow|Navigate).*")
            if back_arrow.exists:
                back_arrow.click()
            else:
                d.press("back") # Системная кнопка "Назад" эмулятора
                
            time.sleep(random.uniform(1.0, 1.4))
            
            # Нажимаем на нужную дату или кнопку склада на Главной, чтобы заново открыть это окно с галочками
            # На вашем экране это карточка склада Краснодар 2 РФЦ
            target_card = d(textContains="Краснодар 2")
            if target_card.exists:
                click_element_center(target_card)
                time.sleep(random.uniform(1.2, 1.8)) # Ждем подгрузки окна с галочками
                
        except Exception as e:
            print("ОШИБКА ЦИКЛА:", e)
            
        time.sleep(random.uniform(1.5, 3.0))

if __name__ == "__main__":
    main()
