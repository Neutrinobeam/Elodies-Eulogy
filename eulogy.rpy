init 600 python:

    def update_bonuses():
    
        if 'mod_eulogy' not in globals():
            start_mod()

        global royal_demeanor_bonus
        royal_demeanor_bonus = (composure_+elegance_+presence_)*.01
        global conversation_bonus
        conversation_bonus = (public_speaking_+court_manners_+flattery_)*.01
        global expression_bonus
        expression_bonus = (decoration_+instrument_+voice_skill_)*.01
        global social_bonus
        social_bonus = (royal_demeanor_bonus+conversation_bonus+expression_bonus)*.1
        global agility_bonus
        agility_bonus = (dance_+reflexes_+flexibility_)*.01
        global weapons_bonus
        weapons_bonus = (swords_+archery_+polearms_)*.01
        global athletics_bonus
        athletics_bonus = (running_+climbing_+swimming_)*.01
        global animal_handling_bonus
        animal_handling_bonus = (horses_+dogs_+falcons_)*.01
        global physical_bonus
        physical_bonus = (agility_bonus+weapons_bonus+athletics_bonus+animal_handling_bonus)*.1
        global history_bonus
        history_bonus = (novan_history_+foreign_affairs_+world_history_)*.01
        global intrigue_bonus
        intrigue_bonus = (internal_affairs_+foreign_intelligence_+ciphering_)*.01
        global medicine_bonus
        medicine_bonus = (herbs_+battlefield_medicine_+poison_)*.01
        global economics_bonus
        economics_bonus = (accounting_+trade_+production_)*.01
        global military_bonus
        military_bonus = (strategy_+naval_strategy_+logistics_)*.01
        global intellectual_bonus
        intellectual_bonus = (history_bonus+intrigue_bonus+medicine_bonus+economics_bonus+military_bonus)*.1
        global faith_bonus
        faith_bonus = (meditation_+divination_+lore_)*.01
        global lumen_bonus
        lumen_bonus = (sense_magic_+resist_magic_+wield_magic_)*.01
        global mystical_bonus
        mystical_bonus = (faith_bonus+lumen_bonus)*.1
        determine_mood()
        apply_mood_bonuses()
    
    def start_mod():
    
        data = renpy.call_in_new_context('mod_start')

        skillBonus = 15
        moodBonus = 1
        
        global composure_
        global elegance_
        global presence_
        global public_speaking_
        global court_manners_
        global flattery_
        global decoration_
        global instrument_
        global voice_skill_
        
        if data[0] == 0:
            composure_ = elegance_ = presence_ = skillBonus
        elif data[0] == 1:
            public_speaking_ = court_manners_ = flattery_ = skillBonus
        elif data[0] == 2:
            decoration_ = instrument_ = voice_skill_ = skillBonus
        
        global dance_
        global reflexes_
        global flexibility_
        global swords_
        global archery_
        global polearms_
        global running_
        global climbing_
        global swimming_
        global horses_
        global dogs_
        global falcons_

        if data[1] == 0:
            dance_ = reflexes_ = flexibility = skillBonus
        elif data[1] == 1:
            swords_ = archery_ = polearms_ = skillBonus
        elif data[1] == 2:
            running_ = climbing_ = swimming_ = skillBonus
        elif data[1] == 3:
            horses_ = dogs_ = falcons_ = skillBonus

        global novan_history_
        global foreign_affairs_
        global world_history_
        global internal_affairs_
        global foreign_intelligence_
        global ciphering_
        global herbs_
        global battlefield_medicine_
        global poison_
        global accounting_
        global trade_
        global production_
        global strategy_
        global naval_strategy_
        global logistics_

        if data[2] == 0:
            novan_history_ = foreign_affairs_ = world_history_ = skillBonus
        elif data[2] == 1:
            internal_affairs_ = foreign_intelligence_ = ciphering_ = skillBonus
        elif data[2] == 2:
            herbs_ = battlefield_medicine_ = poison_ = skillBonus
        elif data[2] == 3:
            accounting_ = trade_ = production_ = skillBonus
        elif data[2] == 4:
            strategy_ = naval_strategy_ = logistics_ = skillBonus

        global meditation_
        global divination_
        global lore_
        global sense_magic_
        global resist_magic_
        global wield_magic_

        if data[3] == 0:
            meditation_ = divination_ = lore_ = skillBonus
        elif data[3] == 1:
            sense_magic_ = resist_magic_ = wield_magic_ = skillBonus

        global anger
        global cheerfulness
        global willful
        global crowded

        if data[4] == 0:
            anger += moodBonus
        elif data[4] == 1:
            cheerfulness += moodBonus
        elif data[4] == 2:
            willful += moodBonus
        elif data[4] == 3:
            crowded += moodBonus
        elif data[4] == 4:
            anger -= moodBonus
        elif data[4] == 5:
            cheerfulness -= moodBonus
        elif data[4] == 6:
            willful -= moodBonus
        elif data[4] == 7:
            crowded -= moodBonus

        update_adjusted_stats()

label mod_start:

    stop music
    $ switchfade('music/visit tomb (opal).ogg')
    
    $ mod_eulogy = True
    $ mod_data = []
    
    show ballroom
    
    elodie_lonely "I'd like to say something."
    elodie_depressed "My Mother, the Queen, was an incredibly kind, caring, and loving woman."    
    elodie_depressed "To you, she was your Grace. A wise ruler, a strong protector, a fair judge."
    elodie_lonely "To me, she was ... mom. She loved me and raised me. She taught me so much -"
    menu:
        "Self Respect":
            $ mod_data.append(0)
            elodie_neutral "to always carry myself with pride."
        "Care for Others":
            $ mod_data.append(1)
            elodie_neutral "to treat all with kindness, regardless of birth."
        "Beauty Everywhere":
            $ mod_data.append(2)
            elodie_neutral "to see beauty in all things and people."

    elodie_lonely "She always had time for me. I never felt second to her royal duties."
    elodie_neutral "She would even leave court early to take me to"
    menu:
        "Hide-and-Seek":
            $ mod_data.append(0)
            elodie_yielding "the gardens to play tag and hide-and-seek."
        "Play Fight":
            $ mod_data.append(1)
            elodie_afraid "the barracks to spar with wooden swords."
        "Explore":
            $ mod_data.append(2)
            elodie_willful "the grove to run and swim in the shade."
        "Birdwatch":
            $ mod_data.append(3)
            elodie_depressed "the gardens to watch the birds and critters."

    elodie_lonely "She would always say that knowledge was a leader's greatest strength."
    elodie_yielding "She encouraged my studies, particularly those of"
    menu:
        "History":
            $ mod_data.append(0)
            elodie_neutral "societies past, their peoples and customs."
        "Leaders":
            $ mod_data.append(1)
            elodie_neutral "knights and nobles and their great deeds."
        "Healers":
            $ mod_data.append(2)
            elodie_willful "herbalism and alchemy to aide all peoples."
        "Sciences":
            $ mod_data.append(3)
            elodie_neutral "mathematics and the commerce between nations."
        "Battles":
            $ mod_data.append(4)
            elodie_crowded "great dynasties and how they defended their people."

    elodie_lonely "And when the lessons were too difficult, she would hold me tight -"
    elodie_depressed "and whisper in my ear"
    menu:
        "Calming Words":
            $ mod_data.append(0)
            elodie_yielding "that I would have a great place in the gods' story."        
        "Inspiring Words":
            $ mod_data.append(1)
            elodie_crowded "that I had the strength inside to do incredible things."

    elodie_neutral "She was many things to many people."
    elodie_depressed "..."
    elodie_depressed "But most of all, she" 
    menu:
        "was taken too soon.":
            $ mod_data.append(0)
        "was a light in the darkness.":
            $ mod_data.append(1)
        "did things the right way, not the easy.":
            $ mod_data.append(2)
        "was an inspiring leader.":
            $ mod_data.append(3)
        "valued tradition and stability.":
            $ mod_data.append(4)
        "was unique among men.":
            $ mod_data.append(5)
        "did what was right for Nova.":
            $ mod_data.append(6)
        "was my mom.":
            $ mod_data.append(7)

    joslyn "That was lovely sweetheart."

    show black with fade

    joslyn "Thank you all for coming and remembering Fidelia."
    
    return mod_data
