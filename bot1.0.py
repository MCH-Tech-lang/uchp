import time
import random
import uiautomator2 as u2

# Укажите ваш порт из расширенных настроек BlueStacks
PORT = "127.0.0.1:5555" 

try:
    d = u2.connect(PORT)
    print(f"Успешно подключено к BlueStacks на порту {PORT}!")
except Exception as e:
    print(f"Ошибка подключения к эмулятору: {e}")
    exit()

def safe_click(element):
    """Клик в случайную точку внутри кнопки для защиты от антифрода Ozon"""
    bounds = element.info['bounds']
    left, top, right, bottom = bounds['left'], bounds['top'], bounds['right'], bounds['bottom']
    random_x = random.randint(left + 10, right - 10)
    random_y = random.randint(top + 10, bottom - 10)
    d.click(random_x, random_y)

def find_hot_shift():
    # 1. Проверяем, есть ли на экране значок огонька по его ID или описанию.
    # В Ozon Job это чаще всего графический элемент (ImageView).
    # Мы ищем элемент, у которого в ID или описании есть слово "hot" или "fire".
    
    # Способ А: Поиск по id элемента (проверяем самые частые варианты)
    hot_icon = d(resourceIdMatches=".*(hot|fire|flame|priority).*")
    
    # Способ Б: Если А не сработал, ищем по описанию (Content Description)
    if not hot_icon.exists:
        hot_icon = d(descriptionMatches=".*(Горящая|горящая|огонь|Огонь|hot|fire).*")
        
    if hot_icon.exists:
        print("🔥 ОБНАРУЖЕНА ГОРЯЩАЯ СМЕНА С ОГОНЬКОМ!")
        
        # Нам нужно нажать кнопку выбора именно в этой карточке.
        # uiautomator2 позволяет найти кнопку "Выбрать" или "Взять", которая находится 
        # на той же карточке, что и огонек (используем относительный поиск).
        
        # Ищем кнопку "Выбрать" рядом с огоньком (в пределах одного блока)
        # Если кнопка называется по-другому, замените текст "Выбрать смену"
        take_button = hot_icon.sibling(text="Выбрать смену")
        
        if not take_button.exists:
            # Если рядом сиблинга нет, ищем просто ближайшую кнопку ниже огонька
            take_button = d(text="Выбрать смену")
            
        if take_button.exists:
            print("Нажимаю кнопку взять...")
            safe_click(take_button)
            
            # Ждем секунду перед подтверждением
            time.sleep(random.uniform(0.6, 1.1))
            
            # Если Ozon просит подтвердить выбор во всплывающем окне:
            if d(text="Подтвердить").exists:
                safe_click(d(text="Подтвердить"))
            
            print("🎉 Ура! Горящая смена успешно поймана напрямую без очереди.")
            import winsound
            winsound.Beep(2500, 3000) # Длинный гудок на ноутбуке
            return True
    return False

def main():
    print("\nБот запущен. Ищу ТОЛЬКО горящие смены (с огоньком)...")
    
    while True:
        try:
            # Имитируем человеческий плавный свайп вниз для обновления списка
            d.swipe(random.uniform(0.45, 0.55), random.uniform(0.25, 0.35), 
                    random.uniform(0.45, 0.55), random.uniform(0.75, 0.85), 
                    duration=random.uniform(0.4, 0.6))
            
            # Задержка, пока подгружаются данные (от 1.8 до 3.0 сек)
            time.sleep(random.uniform(1.8, 3.0)) 
            
            # Вызываем функцию поиска горящей смены
            if find_hot_shift():
                break # Если поймали, выключаем бота
                
        except Exception as e:
            print(f"Пропуск цикла (возможно, приложение обновляется): {e}")
            
        # Случайная пауза между обновлениями экрана
        time.sleep(random.uniform(1.5, 3.5)) 

if __name__ == "__main__":
    main()
