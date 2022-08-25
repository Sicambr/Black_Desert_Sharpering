import enchant_weapon1_20

def main_test_10000(check_test,test_cases,tochka,valkas_sv,use_cron_stone,Colour,valkas_m,item_price,
                    black_cr_weapon,black_cr_weapon_16,cron_stone_price,type_stuff,valkas_test,test_valkas,
                    base_persent, one_fail, potolok, Cron_amount,fragments_memory_price):
    koef_restore = 1
    if Colour == 'GREEN':
        koef_restore = 5
    elif Colour == 'BLUE':
        koef_restore = 2
    elif Colour == 'GRAY':
        koef_restore = 10
    if check_test == 1 and valkas_test != 1:
        j = 0
        total_price = 0
        total_black_st = 0
        total_con_black_st = 0
        total_lost_dur = 0
        total_lost_cron = 0
        total_valkas_st = 0
        report_switch = 'report_off'
        stone_amount = {0: 0, 5: 5, 10: 12, 15: 21, 20: 33, 25: 53, 30: 84}
        mas = []
        amount_p = 75000000000
        st = 0
        while j < test_cases:
            toch_b = enchant_weapon1_20.sharpering(tochka, report_switch,valkas_sv, use_cron_stone, Colour, valkas_m, item_price,
                                    black_cr_weapon, black_cr_weapon_16, cron_stone_price, base_persent, one_fail, potolok,
                                            Cron_amount,fragments_memory_price)
            mas.append(toch_b.diap_tochki())
            total_price += mas[j]['black_st_price']
            total_black_st += mas[j]['Black_st']
            total_con_black_st += mas[j]['Con_black_st']
            total_lost_dur += mas[j]['Durability']
            total_lost_cron += mas[j]['Cron_st']
            total_valkas_st += mas[j]['valks_amount']
            st += 1
            if mas[j]['full_price'] >= amount_p:
                print('We got ',int(mas[j]['full_price']/1000000), 'millions  on ', st, ' attempt CASE!!!')
            else:
                print('We got ', int(mas[j]['full_price'] / 1000000), 'millions  on ', st, ' attempt')
            j += 1
        average_price = total_price / len(mas)
        average_black_st = total_black_st / len(mas)
        average_con_black_st = total_con_black_st / len(mas)
        average_lost_dur = total_lost_dur / len(mas)
        average_lost_cron = total_lost_cron / len(mas)
        average_lost_memory = int(average_lost_dur/koef_restore)
        average_valkas_st = int(total_valkas_st / len(mas))
        average_price_dur = 0
        if item_price / 100 > fragments_memory_price / koef_restore:
            average_price_dur = int((average_lost_dur / koef_restore)*fragments_memory_price)
        else:
            average_price_dur = int((average_lost_dur / 10) * item_price)
        full_price_w = int(average_price_dur) + int(average_price) + int(average_lost_cron * cron_stone_price)
        print('\nRESULTS OF ',j,'ENCHANTMENT TESTS')
        print('Type :',Colour, type_stuff, ',we have +',(tochka[0]-1),', we will reach +',tochka[1])
        if int(item_price / 1000000) >= 1:
            print('One item price on the auction house = ',item_price,'silver  (', round((item_price / 1000000),1), 'millions )')
        else:
            print('One item price on the auction house = ', item_price, 'silver')
        if valkas_m == 'valkas_off':
            print('Used advices of Valks - NO')
        else:
            print('Used advices of Valks - YES')
            print(valkas_sv)
            if int(average_valkas_st * black_cr_weapon / 1000000) >= 1:
                print('We bought ', average_valkas_st, ' black stones for advices of Valks = ', average_valkas_st * black_cr_weapon,
                      'silver  (', round(((average_valkas_st * black_cr_weapon) / 1000000),1), 'millions )')
            else:
                print('We bought ', average_valkas_st, ' black stones = ', average_valkas_st * black_cr_weapon,
                      ' silver for VALKS')
        if int(average_price / 1000000) >= 1:
            print('Average price of black stones and Concentrated black stones for Enchanting = ',int(average_price),
                  'silver  (', round((average_price / 1000000),1), 'millions )')
        else:
            print('Average price of black stones and Concentrated black stones for Enchanting = ', int(average_price),'silver')
        print('Average amount of Black stones for Enchanting process = ',int(average_black_st))
        print('Average amount of Concentrated black stones for Enchanting process = ',int(average_con_black_st))
        if item_price / 100 > fragments_memory_price / koef_restore:
            print('The cost of restoring durability = ', int(average_price_dur),
                  'silver  (', round(((average_price_dur) / 1000000),1), 'millions )')
            print('Averge amount of FRAGMENTS MEMORY =',int(average_lost_memory))
        else:
            if int((average_price_dur) / 1000000) >= 1:
                print('The cost of restoring durability = ', int(average_price_dur),
                      'silver  (', round((average_price_dur / 1000000),1), 'millions )')
            else:
                print('The cost of restoring durability = ',int(average_price_dur),'silver')
        print('Average value of lost durability = ',int(average_lost_dur))
        print('Average amount of Crone stones = ', int(average_lost_cron))
        if int(average_lost_cron * cron_stone_price / 1000000) >= 1:
            print('The cost of all Crone stones = ', int(average_lost_cron * cron_stone_price),
                  'silver  (', round(((average_lost_cron * cron_stone_price) / 1000000),1), 'millions )')
        else:
            print('The cost of all Crone stones = ', int(average_lost_cron * cron_stone_price), 'silver')
        if int(full_price_w / 1000000000) >= 1:
            print('FULL COSTS = ', full_price_w, 'silver  (', str(round((full_price_w / 1000000000),2)), 'billions )')
        elif int(full_price_w/1000000) >= 1:
            print('FULL COSTS = ', full_price_w,'silver  (',int(full_price_w/1000000),'millions )')
        else:
            print('FULL COSTS = ', full_price_w,'silver')

    # BIG VALKS TEST
    if valkas_test == 1:
        PRICE_s = 0
        DURABILITY_s = 0
        j = 0
        total_price = 0
        total_black_st = 0
        total_con_black_st = 0
        total_lost_dur = 0
        additional_buy_stones = 0
        total_lost_cron = 0
        total_valkas_st = 0
        report_switch = 'report_off'
        valkas_m = 'valkas_off'
        stone_amount = {0: 0, 5: 5, 10: 12, 15: 21, 20: 33, 25: 53, 30: 84}
        mas = []
        while j < test_cases:
            toch_b = enchant_weapon1_20.sharpering(tochka, report_switch,valkas_sv, use_cron_stone, Colour, valkas_m, item_price,
                                    black_cr_weapon, black_cr_weapon_16, cron_stone_price, base_persent, one_fail, potolok,
                                            Cron_amount,fragments_memory_price)
            mas.append(toch_b.diap_tochki())
            total_price += mas[j]['black_st_price']
            total_black_st += mas[j]['Black_st']
            total_con_black_st += mas[j]['Con_black_st']
            total_lost_dur += mas[j]['Durability']
            total_lost_cron += mas[j]['Cron_st']
            total_valkas_st += mas[j]['valks_amount']
            j += 1
        average_price = total_price / len(mas)
        average_black_st = total_black_st / len(mas)
        average_con_black_st = total_con_black_st / len(mas)
        average_lost_dur = total_lost_dur / len(mas)
        average_lost_cron = total_lost_cron / len(mas)
        average_lost_memory = int(average_lost_dur/koef_restore)
        average_valkas_st = int(total_valkas_st / len(mas))
        average_price_dur = 0
        if item_price / 100 > fragments_memory_price / koef_restore:
            average_price_dur = int((average_lost_dur / koef_restore)*fragments_memory_price)
        else:
            average_price_dur = int((average_lost_dur / 10) * item_price)
        full_price_w = int(average_price_dur) + int(average_price) + int(average_lost_cron * cron_stone_price)

        DURABILITY_s = average_lost_dur
        PRICE_s = full_price_w

        print('\nRESULTS OF ',j,'ENCHANTMENT TESTS')
        print('Type :',Colour, type_stuff, ',we have +',(tochka[0]-1),', we will reach +',tochka[1])
        if int(item_price / 1000000) >= 1:
            print('One item price on the auction house = ',item_price,'silver  (', round((item_price / 1000000),1), 'millions )')
        else:
            print('One item price on the auction house = ', item_price, 'silver')
        if valkas_m == 'valkas_off':
            print('Used advices of Valks - NO')
        else:
            print('Used advices of Valks - YES')
            print(valkas_sv)
            if int(average_valkas_st * black_cr_weapon / 1000000) >= 1:
                print('We bought ', average_valkas_st, ' black stones for advices of Valks = ', average_valkas_st * black_cr_weapon,
                      'silver  (', round(((average_valkas_st * black_cr_weapon) / 1000000),1), 'millions )')
            else:
                print('We bought ', average_valkas_st, ' black stones = ', average_valkas_st * black_cr_weapon,
                      ' silver for VALKS')
        if int(average_price / 1000000) >= 1:
            print('Average price of black stones and Concentrated black stones for Enchanting = ',int(average_price),
                  'silver  (', round((average_price / 1000000),1), 'millions )')
        else:
            print('Average price of black stones and Concentrated black stones for Enchanting = ', int(average_price),'silver')
        print('Average amount of Black stones for Enchanting process = ',int(average_black_st))
        print('Average amount of Concentrated black stones for Enchanting process = ',int(average_con_black_st))
        if item_price / 100 > fragments_memory_price / koef_restore:
            print('The cost of restoring durability = ', int(average_price_dur),
                  'silver  (', round(((average_price_dur) / 1000000),1), 'millions )')
            print('Averge amount of FRAGMENTS MEMORY =',int(average_lost_memory))
        else:
            if int((average_price_dur) / 1000000) >= 1:
                print('The cost of restoring durability = ', int(average_price_dur),
                      'silver  (', round((average_price_dur / 1000000),1), 'millions )')
            else:
                print('The cost of restoring durability = ',int(average_price_dur),'silver')
        print('Average value of lost durability = ',int(average_lost_dur))
        print('Average amount of Crone stones = ', int(average_lost_cron))
        if int(average_lost_cron * cron_stone_price / 1000000) >= 1:
            print('The cost of all Crone stones = ', int(average_lost_cron * cron_stone_price),
                  'silver  (', round(((average_lost_cron * cron_stone_price) / 1000000),1), 'millions )')
        else:
            print('The cost of all Crone stones = ', int(average_lost_cron * cron_stone_price), 'silver')
        if int(full_price_w / 1000000000) >= 1:
            print('FULL COSTS = ', full_price_w, 'silver  (', str(round((full_price_w / 1000000000),2)), 'billions )')
        elif int(full_price_w/1000000) >= 1:
            print('FULL COSTS = ', full_price_w,'silver  (',int(full_price_w/1000000),'millions )')
        else:
            print('FULL COSTS = ', full_price_w,'silver')

        print('\nCALCULATING THE BEST OPTION...')

        mas = []
        valkas_m = 'valkas_on'
        valkas_sv = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0,
                     10: 0, 11: 0, 12: 0, 13: 0, 14: 0, 15: 0,
                     16: 0, 17: 0, 18: 0, 19: 0, 20: 0}
        stone_amount = {0:0, 5:5, 10:12, 15:21, 20:33, 25:53, 30:84}
        additional_buy_stones = 0
        base_plus = 5
        maximum_valkas = 30
        the_best_valkas = valkas_sv.copy()
        sdvig = []

        # FOR TIME COUNT:
        all_test_time = pow(len(stone_amount),(tochka[1]-tochka[0]+1))
        base_test_time = 100/all_test_time
        start_test_time = 0
        time_range = []
        for ti in range(1,100):
            time_range.append(ti)

        for i in range(tochka[0],tochka[1]+1):
            sdvig.append(0)
        marker = 1
        while marker == 1:
            start_test_time += base_test_time
            if (int(start_test_time) in time_range):
                print(int(start_test_time),end=' ')
                if int(start_test_time) == 51:
                    print('')
                time_range.remove(int(start_test_time))
            additional_buy_stones = 0
            sdvig[0] += base_plus
            j = 0
            while j < len(sdvig):
                if sdvig[j] > maximum_valkas:
                    sdvig[j] = 0
                    if j < len(sdvig)-1:
                        sdvig[j+1] += base_plus
                    else:
                        marker = 0
                j += 1

            k = 0
            while k < len(sdvig):
                valkas_sv[tochka[0]+k] = sdvig[k]
                additional_buy_stones += stone_amount[sdvig[k]]
                k += 1
            t = 0
            mas.clear()
            total_price = 0
            total_black_st = 0
            total_con_black_st = 0
            total_lost_dur = 0
            total_lost_cron = 0
            total_valkas_st = 0
            while t < test_valkas:
                toch_b = enchant_weapon1_20.sharpering(tochka, report_switch,valkas_sv, use_cron_stone, Colour, valkas_m, item_price,
                                    black_cr_weapon, black_cr_weapon_16, cron_stone_price, base_persent, one_fail, potolok,
                                                Cron_amount,fragments_memory_price)
                mas.append(toch_b.diap_tochki())
                total_price += mas[t]['black_st_price']
                total_black_st += mas[t]['Black_st']
                total_con_black_st += mas[t]['Con_black_st']
                total_lost_dur += mas[t]['Durability']
                total_lost_cron += mas[t]['Cron_st']
                total_valkas_st += mas[t]['valks_amount']
                t += 1
            average_price = total_price / len(mas)
            average_black_st = total_black_st / len(mas)
            average_con_black_st = total_con_black_st / len(mas)
            average_lost_dur = total_lost_dur / len(mas)
            average_lost_cron = total_lost_cron / len(mas)
            average_lost_memory = int(average_lost_dur / koef_restore)
            average_valkas_st = int(total_valkas_st / len(mas))
            average_price_dur = 0
            if item_price / 100 > fragments_memory_price / koef_restore:
                average_price_dur = int((average_lost_dur / koef_restore) * fragments_memory_price)
            else:
                average_price_dur = int((average_lost_dur / 10) * item_price)
            full_price_w = int(average_price_dur) + int(average_price) + int(average_lost_cron * cron_stone_price)
            if full_price_w < PRICE_s:
                PRICE_s = full_price_w
                DURABILITY_s = average_lost_dur
                the_best_valkas.clear()
                the_best_valkas = valkas_sv.copy()
        print('\n\nGRADE: ', Colour, '  TYPE: ', type_stuff)
        print('The best TOTAL PRICE is ', PRICE_s, '  (',int(PRICE_s/1000000), 'millions )')
        print('DURABILITY is ', DURABILITY_s)
        print('The best valks is ',the_best_valkas)


def range_test(test_cases,tochka,valkas_sv,use_cron_stone,Colour,valkas_m,item_price,
                    black_cr_weapon,black_cr_weapon_16,cron_stone_price,type_stuff,
                    base_persent, one_fail, potolok, Cron_amount,fragments_memory_price):
    koef_restore = 1
    if Colour == 'GREEN':
        koef_restore = 5
    elif Colour == 'BLUE':
        koef_restore = 2
    elif Colour == 'GRAY':
        koef_restore = 10
    j = 0
    total_black_st = 0
    total_lost_dur = 0
    case_i = 0
    kamni = 0
    durab = 0
    cases_blask_st = {}
    report_switch = 'report_off'
    mas = []
    k = 0
    our_case = 20
    while j < test_cases:
        k += 1
        toch_b = enchant_weapon1_20.sharpering(tochka, report_switch,valkas_sv, use_cron_stone, Colour, valkas_m, item_price,
                                black_cr_weapon, black_cr_weapon_16, cron_stone_price, base_persent, one_fail, potolok,
                                        Cron_amount,fragments_memory_price)
        mas.append(toch_b.diap_tochki())
        if mas[j]['Black_st'] > our_case:
            total_black_st += our_case
        else:
            total_black_st += mas[j]['Black_st']
        total_lost_dur += mas[j]['Durability']
        if mas[j]['Black_st'] >= our_case:
            case_i += 1
            kamni += total_black_st
            durab += total_lost_dur
            print('After ',k,' attempts')
            print('Spent ',total_black_st, ' Black stones =', int((total_black_st*black_cr_weapon)/1000000),' millions')
            print('Lost ', total_lost_dur, ' Durability =', int(((total_lost_dur / 10) * item_price) / 1000000), 'millions\n')
            total_black_st = 0
            total_lost_dur = 0
            k = 0
        if mas[j]['Black_st'] not in cases_blask_st.keys():
            cases_blask_st[mas[j]['Black_st']] = 1
        else:
            cases_blask_st[mas[j]['Black_st']] += 1
        j += 1
    keys_blask_st = sorted(cases_blask_st.keys())
    print('\n TO REACH: ',our_case,'\n')
    print('Black st ',int(kamni/case_i), ' = ', int(((kamni/case_i)*black_cr_weapon)/1000000), ' millionas')
    print('Durabil ', int(durab / case_i), ' = ', int((((durab / case_i) / 10) * item_price)/1000000), ' millionas')
    print('Every = ',test_cases/case_i, ' steps')
    #for i in keys_blask_st:
    #    print(i,':',cases_blask_st[i])