import random
print("добро пожаловать в игру выберите класс персонажа")
bacpack=[]

class_pers=["лучник","самурай","воин"]
pers=input("введите класс персонажа(лучник,воин самурай):")

player_stats={"лучник":{"жизненная сила":12,
                   "интеллект":11,
                   "стойкость":13,
                   "сила":12,
                   "ловкость":15,
                   "мудрость":9,
                   "вера":8 ,
                   "колдовство":8
                   },
"самурай":{"жизненная сила":10,
                  "интеллект":9,
                  "стойкость":11,
                  "сила":12,
                  "ловкость":16,
                  "мудрость":8,
                  "вера":9,
                  "колдовство":14
                  },
"воин":{"жизненная сила":8,
                  "интеллект":12,
                  "стойкость":11,
                  "сила":10,
                  "ловкость":16,
                  "мудрость":10,
                  "вера":8,
                  "колдовство":9
                  }}
enemy_stats={
    "большой орк":{"жизненная сила":15,
                  "интеллект":5,
                  "стойкость":15,
                  "сила":20,
                  "ловкость":10,
                  "мудрость":5,
                  "вера":3,
                  "колдовство":3    },
    "проклятый мечник":{"жизненная сила":10,
                "интеллект":7,
                "стойкость":20,
                "сила":20,
                "ловкость":15,
                "мудрость":3,
                "вера":3,
                "колдовство":3  
    },
    "лич":{"жизненная сила":8,
                "интеллект":20,
                "стойкость":10,
                "сила":5,
                "ловкость":5,
                "мудрость":15,
                "вера":20,
                "колдовство":20  
    }
}
hp_lich=enemy_stats["лич"]["жизненная сила"]*40
stamina_lich=enemy_stats["лич"]["стойкость"]*8
damage_lich=enemy_stats["лич"]["интеллект"]+enemy_stats["лич"]["вера"]
hp_ork=enemy_stats["большой орк"]["жизненная сила"]*40
stamina_ork=enemy_stats["большой орк"]["стойкость"]*8
damage_ork=enemy_stats["большой орк"]["сила"]+enemy_stats["большой орк"]["стойкость"]
dark_hp=enemy_stats["проклятый мечник"]["жизненная сила"]*40
dark_stamina=enemy_stats["проклятый мечник"]["стойкость"]*8
dark_damage=enemy_stats["проклятый мечник"]["сила"]+enemy_stats["проклятый мечник"]["ловкость"]
weapon_stats={
    "weapon_warrior_slot1":{
    "тяжелый лук":30,
    "легкий лук":16,
    "композитный лук":20,
    "утигатана":24,
    "сушильный шест":22,
    "кровавая катана":18,
    "тяжелый меч":38,
    "меч рыцаря":26,
    "копье":22},
    "weapon_warrior_slot2":{
        "маленький кинжал":12,
        "зелье здоровья":0,
        "щит":6,
        "вакидзаси":15,
        "кунай":10,
        "маленький арбалет":18
    }

}




if pers==class_pers[0]:
    weapon_archer=["тяжелый лук","легкий лук","композитный лук"]
    weapon_game=input("выберите для себя лук(тяжелый лук,легкий лук,композитный лук):")
    archer_hp=player_stats["лучник"]["жизненная сила"]*40
    archer_stamina=player_stats["лучник"]["стойкость"]*8
    if weapon_game==weapon_archer[0]:
        bacpack.append("основное оружие:"+weapon_archer[0])
        archer_damage=player_stats["лучник"]["ловкость"]+weapon_stats["weapon_warrior_slot1"]["тяжелый лук"]
    if weapon_game==weapon_archer[1]:
        bacpack.append("основное оружие:"+weapon_archer[1])
        archer_damage=player_stats["лучник"]["ловкость"]+weapon_stats["weapon_warrior_slot1"]["легкий лук"]
    if weapon_game==(weapon_archer[2]):
        bacpack.append("основное оружие:"+weapon_archer[2])
        archer_damage=player_stats["лучник"]["ловкость"]+weapon_stats["weapon_warrior_slot1"]["композитный лук"]
    weapon=input("выберите запасной предмет(маленький кинжал,зелье здоровья,щит):")
    weapon_second=["маленький кинжал","зелье здоровья","щит"]
    if weapon==(weapon_second[0]):
        bacpack.append( "второе оружие:"+weapon_second[0])
    if weapon==(weapon_second[1]):
        bacpack.append( "второе оружие"+weapon_second[1])
    if weapon==(weapon_second[2]):
        bacpack.append("второе оружие:"+weapon_second[2])
if pers==class_pers[1]:
    samurai_hp=player_stats["самурай"]["жизненная сила"]*40
    samurai_stamina=player_stats["самурай"]["стойкость"]*8
    weapon_samurai=["утигатана","сушильный шест","кровавая катана"]
    weapon_game=input("выберите для себя катану(утигатана ,сушильный шест ,кровавая катана):")
    if weapon_game==weapon_samurai[0]:
        bacpack.append("основное оружие:"+weapon_samurai[0])
        samurai_damage=player_stats["самурай"]["ловкость"]+weapon_stats["weapon_warrior_slot1"]["утигатана"]
    if weapon_game==weapon_samurai[1]:
        bacpack.append("основное оружие:"+weapon_samurai[1])
        samurai_damage=player_stats["самурай"]["ловкость"]+weapon_stats["weapon_warrior_slot1"]["сушильный шест"]
    if weapon_game==weapon_samurai[2]:
        bacpack.append("основное оружие:"+weapon_samurai[2])
        samurai_damage=player_stats["самурай"]["ловкость"]+weapon_stats["weapon_warrior_slot1"]["кровавая катана"]
    weapon_second_samurai=["вакидзаси","кунай","зелье здоровья"]
    weapon_samurai_slot2=input("выберите второе оружие(вакидзаси,кунай,зелье здоровья):")
    if weapon_samurai_slot2==weapon_second_samurai[0]:
        bacpack.append("второе оружие :"+weapon_second_samurai[0]) 
    if weapon_samurai_slot2==weapon_second_samurai[1]:
        bacpack.append("второе оружие :"+weapon_second_samurai[1])
    if weapon_samurai_slot2==weapon_second_samurai[2]:
        bacpack.append("второе оружие:"+weapon_second_samurai[2])
if pers==class_pers[2]:
    warior_hp=player_stats["воин"]["жизненная сила"]*40
    warior_stamina=player_stats["воин"]["стойкость"]*8
    weapon_warrior=["тяжелый меч","меч рыцаря","копье"]
    weapon_warrior_slot1=input("выберите оружие для своего воина(тяжелый меч,меч рыцаря,копье):")
    if weapon_warrior_slot1==weapon_warrior[0]:
        bacpack.append("основное оружие:"+weapon_warrior[0] )
        weapon_damage=player_stats["воин"]["сила"]+weapon_stats["weapon_warrior_slot1"]["тяжелый меч"]
    if weapon_warrior_slot1==weapon_warrior[1]:
        bacpack.append("основное оружие:"+weapon_warrior[1])
        weapon_damage=player_stats["воин"]["сила"]+weapon_stats["weapon_warrior_slot1"]["меч рыцаря"]
    if weapon_warrior_slot1==weapon_warrior[2]:
        bacpack.append("основное оружие:"+weapon_warrior[2])
        weapon_damage=player_stats["воин"]["сила"]+weapon_stats["weapon_warrior_slot1"]["копье"]
    weapon_warrior_slot2=input("выберите второе оружие(щит,маленький арбалет,зелье здоровья):")
    weapon_warrior_spare=["щит","маленький арбалет","зелье здоровья"]
    if weapon_warrior_slot2==weapon_warrior_spare[0]:
        bacpack.append("второе оружие:"+weapon_warrior_spare[0])
    if weapon_warrior_slot2==weapon_warrior_spare[1]:
        bacpack.append("второе оружие"+weapon_warrior_spare[1])
    if weapon_warrior_slot2==weapon_warrior_spare[2]:
        bacpack.append("второе оружие:"+weapon_warrior_spare[2])
print(bacpack)

# Привязываем уникальные переменные к универсальным для боя
if pers == "лучник":
    player_hp = archer_hp
    player_stamina = archer_stamina # тут проверь опечатку arher_stamina, если не исправил
    player_damage = archer_damage
elif pers == "самурай":
    player_hp = samurai_hp
    player_stamina = samurai_stamina
    player_damage = samurai_damage
elif pers == "воин":
    player_hp = warior_hp
    player_stamina = warior_stamina
    player_damage = weapon_damage # или как ты её назвал в итоге у воина
player_stats2=[]
player_stats2.append(player_hp)
player_stats2.append(player_stamina)
player_stats2.append(player_damage)
print("ваш герой просыпается на арене он ничего не помнит")
print("вашим первым врагом стал проклятый мечник")
print("открывается арена и перед тобой огромной черный мечник с большим мечом и в рыцарских")
print("доспех достаточно сильно потрепан сражениями и проклятый мечник стоит ничего не говоря и сразу нападает словно его контролирует кто то")
print("он летит на вас на полной скорости чтобы разрубить вас ")

enemy_hp = dark_hp
enemy_stamina = dark_stamina
enemy_damage = dark_damage

player_hp2=player_hp

while True:
        
        def roll_d20():
            result=random.randint(1,20)
            return result
        action = input("выберите действие (атака или уклонение ):").strip().lower()
        action_hp = player_hp  # Запоминаем текущее здоровье на старте хода
        enemy_hp_player=enemy_hp

        match action:
            case "атака":
                random_number = roll_d20()
                print("⚔️ Вы готовитесь нанести удар...")
                
                if random_number < 10:
                    print("❌ Вы промахнулись! Враг мгновенно контраатакует!")
                    
                    # Второй кубик: проверка, попал ли враг по тебе
                    enemy_roll = roll_d20()
                    if enemy_roll < 15:
                        print("💥 Вам не удалось уклониться! Враг наносит урон!")
                        if enemy_damage >= player_hp:  # Проверяем фатальный урон
                            print("💀 Вас убили!")
                            player_hp = 0  # Сбрасываем в ноль для красоты
                            break
                        else:
                            player_hp -= enemy_damage
                    else:
                        # Ветка ELSE: если кубик врага >= 15, он промазал!
                        print("✨ Но вы вовремя отпрыгнули! Проклятый мечник рассёк воздух мимо вас!")
                
                else:
                    print("🎯 Ваш удар достиг цели!")
                    if 18<=random_number<=20:
                        enemy_hp-=player_damage*2

                    if enemy_hp <= 0:  # Значок <= ловит и ровно ноль, и любые минусы!
                        print("🏆 Вы убили своего врага!")
                        enemy_hp = 0
                        break

                    else:
                        enemy_hp -= player_damage
                        if enemy_hp <= 0:
                            print("🏆 Ваш враг убит!")
                            break


            case "уклонение":
                print("вы готовитесь для уклонения")
                random_number=roll_d20()
                if random_number<10:
                    print("по вам попали")
                    if enemy_damage>player_hp:
                        print("вас убили конец игры")
                        break
                    else:
                        player_hp-=enemy_damage
                        if player_hp<=0:
                            print("вас убили")
                            break
                else:
                    print("вы сумели уклонится")
            case _:
                print("❌ Неизвестная команда! Проклятый мечник бьет по застывшей цели!")
                player_hp -= enemy_damage
                if player_hp <= 0:
                    print("💀 Вас убили. Конец игры.")
                    break
               # Обновляем и выводим актуальные статы в конце хода
        player_character = [player_damage, action_hp, player_stamina]
        enemy_character=[enemy_damage,enemy_hp_player,enemy_stamina]
        print(f"📊 Текущее состояние героя [Урон, ХП, Стамина]: {player_character}\n")
        print(f"текущее состояние врага [Урон,ХП,Стамина]:{enemy_character}\n")
print("вы убили проклятого мечника снимаете его шлем и узнаете в нем своего друга детства и вспоминаете как вы с ним играли в войнов")
print("перед смертью он говорит я рад тебя видеть меня контролировал король он тебя ненавидит и хочет убить будь осторожнее.")
print("Мария у него постарайся поискать Марию")
print("И на моменте как главный герой спрашивает кто это лучший друг умирает.")
print("он пытался вспомнить имя лучшего друга не смог все было как в тумане он падает в обморок и просыпается в клетке с другим гладиатором")
print("это оказался дряхлый старик которого сослал король из за того что тот не мог выплатить налоги и в нарекание отправил сюда")          
print("к тебе заходят стража тебя вырубают")
print("ты просыпаешься на арене")
print("перед тобой появляется огромный орк он начинает рычать и стоит с огромным топором наш герой начинает готовится для контраатаки")
ork_damage_action=damage_ork
ork_hp_action=hp_ork
while True:
    atack=input("выберите действие(атака,уклонение)").strip().lower()
    
    ork_character=[damage_ork,hp_ork,stamina_ork]
    new_player_character=[player_damage,player_hp,player_stamina]
    match atack:
       
            case "атака":
                random_number = roll_d20()
                print("⚔️ Вы готовитесь нанести удар...")
                
                if random_number < 10:
                    print("❌ Вы промахнулись! Враг мгновенно контраатакует!")
                    
                    # Второй кубик: проверка, попал ли враг по тебе
                    enemy_roll = roll_d20()
                    if enemy_roll < 15:
                        print("💥 Вам не удалось уклониться! Враг наносит урон!")
                        if ork_damage_action >= player_hp:  # Проверяем фатальный урон
                            print("💀 Вас убили!")
                            player_hp = 0  # Сбрасываем в ноль для красоты
                            break
                        else:
                            player_hp-=ork_damage_action
                    else:
                        # Ветка ELSE: если кубик врага >= 15, он промазал!
                        print("✨ Но вы вовремя отпрыгнули! Орк рассёк воздух мимо вас!")
                
                else:
                    print("🎯 Ваш удар достиг цели!")
                    if 18 <= random_number <= 20:
                        current_damage = player_damage * 2
                        print(f"🔥 КРИТИЧЕСКИЙ УДАР! Вы наносите двойной урон: {current_damage}!")
                    else:
                        current_damage = player_damage
                    
                    if ork_hp_action < current_damage:
                        print("🏆 Вы убили своего врага!")
                        ork_hp_action = 0
                        break # Вот теперь брейк нужен, ведь Орк мёртв!
                    else:
                        ork_hp_action -= current_damage
                        if ork_hp_action <= 0:
                            print("🏆 Ваш враг убит!")
                            break

                    


            case "уклонение":
                print("вы готовитесь для уклонения")
                random_number=roll_d20()
                if random_number<10:
                    print("по вам попали")
                    if ork_damage_action>player_hp:
                        print("вас убили конец игры")
                        break
                    else:
                        player_hp-=ork_damage_action
                        if player_hp<=0:
                            print("вас убили")
                            break
                else:
                    print("вы сумели уклонится")
            case _:
                print("❌ Неизвестная команда! Проклятый мечник бьет по застывшей цели!")
                player_hp -=ork_damage_action
                if player_hp <= 0:
                    print("💀 Вас убили. Конец игры.")
                    break   
    ork_character = [ork_damage_action, ork_hp_action, stamina_ork]
    new_player_character = [player_damage, player_hp, player_stamina]
    print(f"ваши характеристики {new_player_character}")
    print(f"характеристики соперника {ork_character}")
    print("вы убиваете орка но сзади появляется лич и вырубает вас вы снова предстаете перед стариком ")
while True:
    if pers=="воин":
        print("старик напал на вас но вы защитились и он сказал что ненавидит вас именно из за того что вы подчинялись королю убили его сына и внука со всей его семьей")
        print("вы говорите что ничего не помните и не понимаете о чем он говорит")
        print("Вы спрашиваете кто такая Мария старик говорит что возможно имеете ввиду дочку короля .")
        print("он рассказал что вы в нее были влюблены но король видимо решил что вы плохой выбор ее дочери")
        print("вас уводят в другую сторону арены вы выходите и перед вами престоет дряхлый старик который уже сбит из сил")
        death_ded=(input("выберите 1.убить старика или 2.Пощадить "))
        if death_ded=="1":
            print("вы убиваете старика .Старик говорит:Хотя бы увижусь со своим сыном и внуком спасибо что дал такую возможность")
            break
        if death_ded=="2":
            print("Вы пощадили старика но что то тянет вашу руку и протыкает старика ")
            print("вы ненамеренно убиваете старика но толпа ликует вы этого не хотели.И главный герой обозлился и понял что это действия лича и короля")
            break
        if death_ded!="1" and  death_ded!="2":
            print("неккоректный выбор!!!!!")
            continue
    if pers=="самурай":
        print("вы просыпаетесь видите старика он говорит ты проснулся а ты очень силен и очень сильно похож на моего мертвого сына.")
        print("вы говорите что ничего не помните и старик говорит что король вас выкупил в другой стране оказалось старик был одним из советников короля и не захотев терпеть деяния короля решил уйти в отставку")
        print("в назедании этому король убил всю его семью и отправил сюда на гладиаторские бои")
        break
    if pers=="лучник":
        print("вы просыпаетесь старик говорит что не хотел уничтожать твою деревню")
        print("он говорит что он нашел вашу скрытую деревню и рассказал королю чтобы он осваивать ваши земли")
        print("но пожалел из за того какая кровь была на его руках он у вас просит прощения только у вас есть выбор простить или не прощать старика")
        vib_pers_luch=int(input("выбирай 1.не прощать и убить старика 2.простить и идти дальше"))
        if vib_pers_luch==1:
            print("спасибо я хочу увидется со своей семьей на том свете")
            break
        if vib_pers_luch==2:
            print("Это будет тебе наказанием за все грехи старик но старик просит чтобы вы его убили и закончили его мучения на что вы не соглашаетесь и  сохраняйте ему жизнь")
            break
    print("ты выходишь на арену перед  тобой предстоет лич он говорит подчинись мне смертный")
    print("впредь на меня не действует твоя магия и начинается бой:")
    print("ты выходишь на арену перед тобой предстоет лич он говорит подчинись мне смертный")
print("Рядом с ним материализуется твой зеркальный Двойник в тяжелых доспехах!")
print("Лич произносит: 'Впредь на меня не действует твоя магия!' И начинается бой:")

# Булев флаг: пока Лич жив, он хилит рыцаря в конце хода!
lich_alive = True 
hp_knight = 100
damage_knight = 15
while player_hp > 0 and (hp_lich > 0 or hp_knight > 0):
    print(f"\n❤️ Твое HP: {player_hp} | 💜 HP Рыцаря: {hp_knight if hp_knight > 0 else 'Мертв'} | 💀 HP Лича: {hp_lich if lich_alive else 'Мертв'}")
    
    atack_pers = input("выберите действие (атака рыцаря / атака лича / уклонение): ").strip().lower()
    
    # --- ХОД ИГРОКА ---
    if atack_pers in ["атака рыцаря", "атака лича"]:
        random_number = roll_d20()
        print("⚔️ Вы готовитесь нанести удар...")
        
        if random_number < 10:
            print("❌ Вы промахнулись! Боссы готовы к контратаке!")
            # Контратака Рыцаря, если он жив
            if hp_knight > 0:
                print(f"💥 Рыцарь-двойник наносит урон: {damage_knight}!")
                player_hp -= damage_knight
        else:
            print("🎯 Ваш удар достиг цели!")
            current_damage = player_damage * 2 if 18 <= random_number <= 20 else player_damage
            if 18 <= random_number <= 20:
                print(f"🔥 КРИТИЧЕСКИЙ УДАР! Двойной урон: {current_damage}!")
                
            # Распределение урона
            if atack_pers == "атака лича" and lich_alive:
                hp_lich -= current_damage
                if hp_lich <= 0:
                    print("🏆 Вы сокрушили Лича-колдуна! Его магия развеялась!")
                    hp_lich = 0
                    lich_alive = False
                else:
                    print(f"💀 У Лича осталось {hp_lich} HP")
                    
            elif atack_pers == "атака рыцаря" and hp_knight > 0:
                # Механика "Зеркала" Рыцаря-двойника (30% шанс вернуть урон)
                if roll_d20() > 14: 
                    print(f"🔮 Зеркальный доспех Рыцаря отразил удар! Вы получили {current_damage} урона!")
                    player_hp -= current_damage
                else:
                    hp_knight -= current_damage
                    if hp_knight <= 0:
                        print("🏆 Рыцарь-двойник повержен и рассыпался в прах!")
                        hp_knight = 0
                    else:
                        print(f"💜 У Рыцаря осталось {hp_knight} HP")
                        
    elif atack_pers == "уклонение":
        print("Вы пригнулись, ожидая заклинаний и ударов...")
        if roll_d20() >= 10:
            print("✨ Вы идеально уклонились от всех атак в этом раунде!")
            continue
        else:
            print("❌ Уклонение провалено!")
            if hp_knight > 0: player_hp -=damage_knight
            
    else:
        print("❌ Неизвестная команда! Ты застыл, и боссы бьют без промаха!")
        if hp_knight > 0: player_hp -= damage_knight
        if lich_alive: player_hp -= damage_lich

    # --- ХОД БОССОВ (Конец раунда) ---
    if player_hp <= 0:
        print("💀 Вас убили в финальном бою! Конец игры.")
        break
        
    # Магия Лича: если Лич жив, он хилит Рыцаря!
    if lich_alive and hp_knight > 0:
        hp_knight = min(120, hp_knight + 20) # Хилит на 20, но не выше макса
        print(f"🔮 Лич кастует темную регенерацию! Рыцарь-двойник восстановил 20 HP!")

print("\n🏆 БИТВА ЗАВЕРШЕНА!")
print("вы убиваете лича  и прорываетесь через стражу короля убивая всех подряд")
print("король убегает но вы его догоняете в его покоях и появляется Мария говорит стой не убивай его .")
death_king=input("что ты выберешь 1.уйти с Марией и пощадить короля 2.Убить короля за своего друга и за тех кого он убивал")
if death_king==1:
    print("вы уходите с Марией уезжаете подальше от королевства и живете тихой мирной жизнью и у героя появляются два сына которые вместе играют в солдатиков и герой вспоминает спустя 15 лет о своих испытаниях")
if death_king==2:
    print("вы убили короля и хотите подойти к Марии но она в вас видит монстра")
    print("вы убегаете от нее и спустя два дня решаете совершить самоубийство и обреченным горем Мария не выдерживает и решает выпить яд и умереть")

