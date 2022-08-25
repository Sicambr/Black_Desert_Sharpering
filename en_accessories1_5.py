import random

class sharpering:
    def __init__(self,tochka, report_switch, valkas_sv, use_cron_stone, colour_w, valkas,item_price, black_cr_weapon,
                 black_cr_weapon_16, cron_stone_price, base_persent, one_fail, potolok, Cron_amount,
                 fragments_memory_price, black_gem, black_gem_price, con_blgem_price):

        self.amount = 10000

        self.base_persent = base_persent
        self.one_fail = one_fail
        self.potolok = potolok
        self.Cron_amount = Cron_amount

        self.valkas_sv = valkas_sv
        self.colour_w = colour_w
        self.valkas = valkas
        self.item_price = item_price
        self.black_cr_weapon = black_cr_weapon
        self.black_cr_weapon_16 = black_cr_weapon_16
        self.use_cron_stone = use_cron_stone
        self.cron_stone_price = cron_stone_price
        self.fragments_memory_price = fragments_memory_price

        self.full_report = {'black_st_price':0,'Black_st':0,'Con_black_st':0,'Durability':0,'Cron_st':0,'save_chanse':0,
                            'valks_amount':0,'full_price':0,'fragm_memory':0}
        self.tochka = tochka
        self.report_switch = report_switch
        self.black_gem = black_gem
        self.black_gem_price = black_gem_price
        self.con_blgem_price = con_blgem_price

    def diap_tochki(self):
        j = self.tochka[0]
        save_chanse = 0

        valkas_on = 0
        fail_increase = 1
        report_enchantment = {}
        if self.valkas == 'valkas_on':
            valkas_on = 1
        fail_increase = 1

        valkas = self.valkas_sv[j + 1] * valkas_on

        otchet = {'level_0': 0, 'level_1': 0, 'level_2': 0, 'level_3': 0, 'level_4': 0, 'save_chanse': 0,
                  'valks_amount': 0, 'full_price': 0, 'save_level': 0, 'Cron_st': 0}

        otchet['save_chanse'] = save_chanse
        stone_amount = {0: 0, 5: 5, 10: 12, 15: 21, 20: 33, 25: 53, 30: 84}
        persent = 0
        stroka = ''

        stroka = stroka + 'Advice of VALKS: ' + str(valkas) + '\n'
        if self.base_persent[j] + valkas * self.one_fail[j] > self.potolok[j]:
            persent = self.potolok[j]
        else:
            persent = self.base_persent[j] + valkas * self.one_fail[j]
            otchet['save_chanse'] = valkas
        if valkas in stone_amount:
            otchet['valks_amount'] += stone_amount[valkas]
            if (stone_amount[valkas] * self.black_cr_weapon) / 1000000 >= 1:
                stroka = stroka + 'Black stones for VALKS: ' + str(stone_amount[valkas]) + ' = ' \
                         + str(stone_amount[valkas] * self.black_cr_weapon) + ' silver (' \
                         + str(
                    round((stone_amount[valkas] * self.black_cr_weapon) / 1000000, 2)) + ' millions)\n'
            else:
                stroka = stroka + 'Black stones for VALKS: ' + str(stone_amount[valkas]) + ' = ' \
                         + str(stone_amount[valkas] * self.black_cr_weapon) + ' silver\n'

        i = 0
        while 1:
            i += 1
            lucky = random.randint(1, self.amount)
            if lucky in range(int(persent * 100)):
                if (otchet['save_level']+1) == self.tochka[1]:
                    otchet['save_level'] += 1
                    otchet['full_price'] += self.item_price
                    stroka = stroka + '\nSuccess! We got jewelry number' + str(otchet['save_level']) + ',chanse = ' + str(persent) + '%\n'
                    stroka = stroka + '\nWE WON!!!\n'
                    stroka = stroka + 'We had ' + str(i) + ' attempts\n'
                    stroka = stroka + 'FULL PRICE =' + str(otchet['full_price']) + ' (' + str(int(otchet['full_price']/1000000)) + ' millions)\n'
                    break
                else:
                    otchet['save_level'] += 1
                    stroka = stroka + '\nSuccess! We got jewelry number' + str(otchet['save_level']) + ',chanse = ' + str(persent) + '%\n'
                    otchet['full_price'] += self.item_price
                    otchet[('level_' + str(otchet['save_level']))] += 1
                    otchet['level_0'] += 1
                    valkas = self.valkas_sv[otchet['save_level'] + 1] * valkas_on
                    persent = self.base_persent[otchet['save_level']+1] \
                              + valkas * self.one_fail[otchet['save_level']+1]
                    if persent > self.potolok[otchet['save_level']+1]:
                        persent = self.potolok[otchet['save_level']+1]

            else:
                otchet['level_0'] += 1
                otchet['full_price'] += self.item_price
                if self.use_cron_stone == 'no':
                    otchet['save_level'] = 0
                    valkas = self.valkas_sv[otchet['save_level'] + 1] * valkas_on
                    persent = self.base_persent[otchet['save_level'] + 1] \
                              + valkas * self.one_fail[otchet['save_level'] + 1]
                    if persent > self.potolok[otchet['save_level'] + 1]:
                        persent = self.potolok[otchet['save_level'] + 1]
                    stroka = stroka +"Bad luck! Jewelry destroyed! We have to start again. Enchantment chance = " \
                             + str(round(persent, 2)) + '%\n'
                    stroka = stroka + 'WE SPENT: ' + str(otchet['level_0']) + ' base stuff, ' + str(
                        otchet['level_1']) + ' number I, ' \
                             + str(otchet['level_2']) + ' number II, ' + str(otchet['level_3']) + ' number III, ' \
                             + str(otchet['level_4']) + ' number IV\n'
                else:
                    otchet['Cron_st'] += self.Cron_amount[otchet['save_level'] + 1]
        self.full_report['full_price'] = otchet['full_price']


        if self.report_switch == 'report_on':
            print(stroka)

        return self.full_report


    def loggia_tochki(self):
        j = self.tochka[0]
        valkas_on = 0
        otchet = {'level_0': 0, 'level_1': 0, 'level_2': 0, 'level_3': 0, 'level_4': 0, 'save_chanse': 0,
                  'valks_amount': 0, 'full_price': 0, 'save_level': 0, 'Cron_st': 0, 'base_items':0}
        otchet['save_level'] = j - 1
        all_levels = {0:0,1:0,2:0,3:0,4:0,5:0}
        stroka = ''
        persent = self.base_persent[j]
        numbers_log = {0:'0', 1:'I', 2:'II', 3:'III', 4:'IV', 5:'V'}
        i = 0
        while 1:
            i += 1
            lucky = random.randint(1, self.amount)
            if lucky in range(int(persent * 100)):
                if (otchet['save_level']+1) == self.tochka[1]:
                    otchet['save_level'] += 1
                    otchet['level_0'] += self.black_gem[otchet['save_level']]
                    all_levels[otchet['save_level']] += 1
                    otchet['full_price'] += self.black_gem[otchet['save_level']]*self.black_gem_price
                    if self.tochka[1] == self.tochka[0]:
                        otchet['full_price'] += self.item_price
                    if self.report_switch == 'report_on':
                        stroka = stroka + '\nSUCCESS! We got jewelry number ' + numbers_log[otchet['save_level']] \
                                 + ', chance = ' + str(persent) + '%\n'
                        stroka = stroka + '\nWE REACH!!!\n'
                        stroka = stroka + 'We had ' + str(i) + ' attempts\n'
                        stroka = stroka + 'TOTAL SPENT: ' + str(otchet['level_0']) + ' black gems = ' \
                                 + str(otchet['level_0'] * self.black_gem_price) + ' silver  (' \
                                 + str(round(((otchet['level_0'] * self.black_gem_price) / 1000000), 1)) + ' millions)\n'
                        stroka = stroka + 'TOTAL USED: ' + str(otchet['base_items']) + ' base items = ' \
                                 + str(otchet['base_items'] * self.item_price) + ' silver  (' \
                                 + str(round(((otchet['base_items'] * self.item_price) / 1000000), 1)) + ' millions)\n'
                        stroka = stroka + 'TOTAL LOST: ' + str(otchet['level_1']) + ' number I, ' \
                                 + str(otchet['level_2']) + ' number II, ' + str(otchet['level_3']) + ' number III, ' \
                                 + str(otchet['level_4']) + ' number IV\n'
                        for k in all_levels.keys():
                            if k > 0 and k < 5:
                                stroka = stroka + 'WE COULD GET ' + str(all_levels[k]) +' number ' + numbers_log[k] + '\n'
                        stroka = stroka + 'FULL PRICE = ' + str(otchet['full_price']) + ' silver (' \
                                 + str(int(otchet['full_price']/1000000)) + ' millions)\n'
                    break
                else:
                    otchet['full_price'] += self.black_gem[otchet['save_level']+1]*self.black_gem_price
                    otchet['level_0'] += self.black_gem[otchet['save_level']+1]
                    otchet['save_level'] += 1
                    all_levels[otchet['save_level']] += 1
                    if self.report_switch == 'report_on':
                        stroka = stroka + '\nSUCCESS! We got jewelry number ' + numbers_log[otchet['save_level']] + ', chance = ' + str(persent) + '%\n'
                    otchet[('level_' + str(otchet['save_level']))] += 1
                    if otchet['save_level'] > 1:
                        otchet[('level_' + str(otchet['save_level']-1))] -= 1
                    if self.report_switch == 'report_on':
                        stroka = stroka + 'SPENT: ' + str(otchet['level_0']) + ' black gems = ' \
                                 + str(otchet['level_0'] * self.black_gem_price) + ' silver  (' \
                                 + str(round(((otchet['level_0'] * self.black_gem_price) / 1000000), 1)) + ' millions)\n'
                    if otchet['save_level'] == 1:
                        otchet['base_items'] += 1
                        otchet['full_price'] += self.item_price
                        if self.report_switch == 'report_on':
                            stroka = stroka + 'SPENT: ' + str(otchet['base_items']) + ' base items = ' \
                                     + str(otchet['base_items'] * self.item_price) + ' silver  (' \
                                     + str(round(((otchet['base_items'] * self.item_price) / 1000000), 1)) + ' millions)\n'
                    if self.report_switch == 'report_on':
                        stroka = stroka + 'LOST: ' + str(otchet['level_1']) + ' number I, ' \
                                 + str(otchet['level_2']) + ' number II, ' + str(otchet['level_3']) + ' number III, ' \
                                 + str(otchet['level_4']) + ' number IV\n'
                    persent = self.base_persent[otchet['save_level']+1]

            else:
                otchet['full_price'] += self.black_gem[otchet['save_level']+1]*self.black_gem_price
                otchet['level_0'] += self.black_gem[otchet['save_level']+1]
                if self.report_switch == 'report_on':
                    stroka = stroka +"\nBad luck! Jewelry number " + numbers_log[otchet['save_level']] + " destroyed! START AGAIN.\n"
                    stroka = stroka + 'SPENT: ' + str(otchet['level_0']) + ' black gems = ' \
                             + str(otchet['level_0'] * self.black_gem_price) + ' silver  (' \
                             + str(round(((otchet['level_0'] * self.black_gem_price) / 1000000),1)) + ' millions)\n'
                if otchet['save_level'] == j - 1:
                    otchet['base_items'] += 1
                    otchet['full_price'] += self.item_price
                    if self.report_switch == 'report_on':
                        stroka = stroka + 'SPENT: ' + str(otchet['base_items']) + ' base items = ' \
                                 + str(otchet['base_items'] * self.item_price) + ' silver  (' \
                                 + str(round(((otchet['base_items'] * self.item_price) / 1000000), 1)) + ' millions)\n'
                if self.report_switch == 'report_on':
                    stroka = stroka + 'LOST: ' + str(otchet['level_1']) + ' number I, ' \
                             + str(otchet['level_2']) + ' number II, ' + str(otchet['level_3']) + ' number III, ' \
                             + str(otchet['level_4']) + ' number IV\n'
                otchet['save_level'] = j - 1
                all_levels[otchet['save_level']] += 1
                persent = self.base_persent[otchet['save_level'] + 1]
        self.full_report['full_price'] = otchet['full_price']
        if self.report_switch == 'report_on':
            print(stroka)
        return self.full_report


    def Geranoa_tochki(self):
        j = self.tochka[0]
        valkas_on = 0
        otchet = {'level_0': 0, 'level_1': 0, 'level_2': 0, 'level_3': 0, 'level_4': 0, 'save_chanse': 0,
                  'valks_amount': 0, 'full_price': 0, 'save_level': 0, 'Cron_st': 0, 'base_items':0}
        otchet['save_level'] = j - 1
        all_levels = {0:0,1:0,2:0,3:0,4:0,5:0}
        stroka = ''
        persent = self.base_persent[j]
        numbers_log = {0:'0', 1:'I', 2:'II', 3:'III', 4:'IV', 5:'V'}
        i = 0
        while 1:
            i += 1
            lucky = random.randint(1, self.amount)
            if lucky in range(int(persent * 100)):
                if (otchet['save_level']+1) == self.tochka[1]:
                    otchet['save_level'] += 1
                    otchet['level_0'] += self.black_gem[otchet['save_level']]
                    all_levels[otchet['save_level']] += 1
                    otchet['full_price'] += self.black_gem[otchet['save_level']]*self.con_blgem_price
                    if self.tochka[1] == self.tochka[0]:
                        otchet['full_price'] += self.item_price
                    if self.report_switch == 'report_on':
                        stroka = stroka + '\nSUCCESS! We got jewelry number ' + numbers_log[otchet['save_level']] \
                                 + ', chance = ' + str(persent) + '%\n'
                        stroka = stroka + '\nWE REACH!!!\n'
                        stroka = stroka + 'We had ' + str(i) + ' attempts\n'
                        stroka = stroka + 'TOTAL SPENT: ' + str(otchet['level_0']) + ' concentrated black gems = ' \
                                 + str(otchet['level_0'] * self.con_blgem_price) + ' silver  (' \
                                 + str(round(((otchet['level_0'] * self.con_blgem_price) / 1000000), 1)) + ' millions)\n'
                        stroka = stroka + 'TOTAL USED: ' + str(otchet['base_items']) + ' base items = ' \
                                 + str(otchet['base_items'] * self.item_price) + ' silver  (' \
                                 + str(round(((otchet['base_items'] * self.item_price) / 1000000), 1)) + ' millions)\n'
                        stroka = stroka + 'TOTAL LOST: ' + str(otchet['level_1']) + ' number I, ' \
                                 + str(otchet['level_2']) + ' number II, ' + str(otchet['level_3']) + ' number III, ' \
                                 + str(otchet['level_4']) + ' number IV\n'
                        for k in all_levels.keys():
                            if k > 0 and k < 5:
                                stroka = stroka + 'WE COULD GET ' + str(all_levels[k]) +' number ' + numbers_log[k] + '\n'
                        stroka = stroka + 'FULL PRICE = ' + str(otchet['full_price']) + ' silver (' \
                                 + str(int(otchet['full_price']/1000000)) + ' millions)\n'
                    break
                else:
                    otchet['full_price'] += self.black_gem[otchet['save_level']+1]*self.con_blgem_price
                    otchet['level_0'] += self.black_gem[otchet['save_level']+1]
                    otchet['save_level'] += 1
                    all_levels[otchet['save_level']] += 1
                    if self.report_switch == 'report_on':
                        stroka = stroka + '\nSUCCESS! We got jewelry number ' + numbers_log[otchet['save_level']] + ', chance = ' + str(persent) + '%\n'
                    otchet[('level_' + str(otchet['save_level']))] += 1
                    if otchet['save_level'] > 1:
                        otchet[('level_' + str(otchet['save_level']-1))] -= 1
                    if self.report_switch == 'report_on':
                        stroka = stroka + 'SPENT: ' + str(otchet['level_0']) + ' concentrated black gems = ' \
                                 + str(otchet['level_0'] * self.con_blgem_price) + ' silver  (' \
                                 + str(round(((otchet['level_0'] * self.con_blgem_price) / 1000000), 1)) + ' millions)\n'
                    if otchet['save_level'] == 1:
                        otchet['base_items'] += 1
                        otchet['full_price'] += self.item_price
                        if self.report_switch == 'report_on':
                            stroka = stroka + 'SPENT: ' + str(otchet['base_items']) + ' base items = ' \
                                     + str(otchet['base_items'] * self.item_price) + ' silver  (' \
                                     + str(round(((otchet['base_items'] * self.item_price) / 1000000), 1)) + ' millions)\n'
                    if self.report_switch == 'report_on':
                        stroka = stroka + 'LOST: ' + str(otchet['level_1']) + ' number I, ' \
                                 + str(otchet['level_2']) + ' number II, ' + str(otchet['level_3']) + ' number III, ' \
                                 + str(otchet['level_4']) + ' number IV\n'
                    persent = self.base_persent[otchet['save_level']+1]

            else:
                otchet['full_price'] += self.black_gem[otchet['save_level']+1]*self.con_blgem_price
                otchet['level_0'] += self.black_gem[otchet['save_level']+1]
                if self.report_switch == 'report_on':
                    stroka = stroka +"\nBad luck! Jewelry number " + numbers_log[otchet['save_level']] + " destroyed! START AGAIN.\n"
                    stroka = stroka + 'SPENT: ' + str(otchet['level_0']) + ' concentrated black gems = ' \
                             + str(otchet['level_0'] * self.con_blgem_price) + ' silver  (' \
                             + str(round(((otchet['level_0'] * self.con_blgem_price) / 1000000),1)) + ' millions)\n'
                if otchet['save_level'] == j - 1:
                    otchet['base_items'] += 1
                    otchet['full_price'] += self.item_price
                    if self.report_switch == 'report_on':
                        stroka = stroka + 'SPENT: ' + str(otchet['base_items']) + ' base items = ' \
                                 + str(otchet['base_items'] * self.item_price) + ' silver  (' \
                                 + str(round(((otchet['base_items'] * self.item_price) / 1000000), 1)) + ' millions)\n'
                if self.report_switch == 'report_on':
                    stroka = stroka + 'LOST: ' + str(otchet['level_1']) + ' number I, ' \
                             + str(otchet['level_2']) + ' number II, ' + str(otchet['level_3']) + ' number III, ' \
                             + str(otchet['level_4']) + ' number IV\n'
                otchet['save_level'] = j - 1
                all_levels[otchet['save_level']] += 1
                persent = self.base_persent[otchet['save_level'] + 1]
        self.full_report['full_price'] = otchet['full_price']
        if self.report_switch == 'report_on':
            print(stroka)
        return self.full_report



def main_test_10000(check_test,test_cases,tochka,valkas_sv,use_cron_stone,Colour,valkas_m,item_price,
                    black_cr_weapon,black_cr_weapon_16,cron_stone_price,type_stuff,valkas_test,test_valkas,
                    base_persent, one_fail, potolok, Cron_amount,fragments_memory_price,name_stuff,
                    black_gem, black_gem_price, con_blgem_price,report_test, auction_prices):
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
        report_switch = 'report_off'
        stone_amount = {0: 0, 5: 5, 10: 12, 15: 21, 20: 33, 25: 53, 30: 84}
        my_caces = {}
        sort_caces = {}
        know_price = {'good_price':0,'double_auc_price':0,'bad_price':0}
        mas = []
        if name_stuff == 'LoggiaAccessories' or name_stuff == 'GeranoaAccessories':
            valkas_m = 'valkas_off'
        while j < test_cases:
            toch_b = sharpering(tochka, report_switch,valkas_sv, use_cron_stone, Colour, valkas_m, item_price,
                                    black_cr_weapon, black_cr_weapon_16, cron_stone_price, base_persent, one_fail, potolok,
                                            Cron_amount,fragments_memory_price,black_gem, black_gem_price, con_blgem_price)
            if name_stuff == 'LoggiaAccessories':
                mas.append(toch_b.loggia_tochki())
            elif name_stuff == 'GeranoaAccessories':
                mas.append(toch_b.Geranoa_tochki())
            elif name_stuff == 'ManosAccessories':
                mas.append(toch_b.Geranoa_tochki())
            else:
                mas.append(toch_b.diap_tochki())
            total_price += mas[j]['full_price']
            if report_test == 'on':
                if int((mas[j]['full_price'])/1000000) <= auction_prices[tochka[1]]:
                    know_price['good_price'] += 1
                elif int((mas[j]['full_price'])/1000000) > auction_prices[tochka[1]] \
                        and int((mas[j]['full_price'])/1000000) < auction_prices[tochka[1]]*2:
                    know_price['double_auc_price'] += 1
                else:
                    know_price['bad_price'] += 1
                stroka = str(round(((mas[j]['full_price'])/1000000),2))  + ' millions'
                if int((mas[j]['full_price'])/1000000) not in my_caces.keys():
                    my_caces[int((mas[j]['full_price'])/1000000)] = 1
                else:
                    my_caces[int((mas[j]['full_price']) / 1000000)] += 1
                #print(stroka)
            j += 1
        if report_test == 'on':
            print('WE ARE SEARSH:',auction_prices[tochka[1]])
            print(know_price)
            for k in sorted(my_caces.keys()):
                sort_caces[k] = my_caces[k]
            print(sort_caces)
        average_price = total_price / len(mas)
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
        print('AVERAGE COSTS = ', average_price,'silver (', int(average_price/1000000),' millions )')

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
            toch_b = sharpering(tochka, report_switch,valkas_sv, use_cron_stone, Colour, valkas_m, item_price,
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
                toch_b = sharpering(tochka, report_switch,valkas_sv, use_cron_stone, Colour, valkas_m, item_price,
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
