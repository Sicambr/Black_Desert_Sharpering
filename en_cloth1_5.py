import random

class sharpering:
    def __init__(self,tochka, report_switch, valkas_sv, use_cron_stone, colour_w, valkas,item_price, black_cr_weapon,
                 black_cr_weapon_16, cron_stone_price, base_persent, one_fail, potolok, Cron_amount,
                 fragments_memory_price, black_gem_price, con_blgem_price,black_gem):

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
        self.black_gem = black_gem

        self.full_report = {'full_price':0, 'Black_st': 0, 'base_items':0, 'Durability':0}
        self.tochka = tochka
        self.report_switch = report_switch
        self.black_gem_price = black_gem_price
        self.con_blgem_price = con_blgem_price

    def silver_tochki(self):
        stone_amount = {0: 0, 5: 5, 10: 12, 15: 21, 20: 33, 25: 53, 30: 84}
        j = self.tochka[0]
        otchet = {'level_1': 0, 'level_2': 0, 'level_3': 0, 'level_4': 0, 'valkas_chanse': 0,
                  'valks_amount': 0, 'full_price': 0, 'save_level': 0, 'Black_st': 0, 'base_items':0}
        otchet['save_level'] = j - 1
        otchet['valkas_chanse'] = self.valkas_sv[self.tochka[0]]
        all_levels = {0:0,1:0,2:0,3:0,4:0,5:0}
        stroka = ''
        softcap = {0:0,1:14,2:40,3:44,4:120,5:120}
        new_onefail = {0:0,1:0.6,2:0.2,3:0.15,4:0.25,5:0.03}
        persent = 0
        if self.valkas_sv[j] <= softcap[j]:
            persent = self.base_persent[j] + self.valkas_sv[j]*self.one_fail[j]
        else:
            persent = self.base_persent[j] + (self.valkas_sv[j]-softcap[j])*new_onefail[j] \
                      + softcap[j] *self.one_fail[j]
        if persent > self.potolok[j]:
            persent = self.potolok[j]
        numbers_log = {0:'0', 1:'+1', 2:'+2', 3:'+3', 4:'+4', 5:'+5'}
        i = 0
        while 1:
            i += 1
            lucky = random.randint(1, self.amount)
            if lucky in range(int(persent * 100)):
                if (otchet['save_level']+1) == self.tochka[1]:
                    otchet['save_level'] += 1
                    otchet['base_items'] += 1
                    all_levels[otchet['save_level']] += 1
                    otchet['full_price'] += self.item_price
                    if self.valkas_sv[otchet['save_level']] in stone_amount.keys():
                        stroka = stroka + '\nADVICE VALKS: ' + str(self.valkas_sv[otchet['save_level']]) + ' = ' \
                                 + str(round((stone_amount[self.valkas_sv[otchet['save_level']]]*self.black_cr_weapon)/1000000,2)) + ' millions\n'
                        otchet['full_price'] += stone_amount[self.valkas_sv[otchet['save_level']]]*self.black_cr_weapon
                        otchet['Black_st'] += stone_amount[self.valkas_sv[otchet['save_level']]]
                    elif self.valkas_sv[otchet['save_level']] > 30:
                        stroka = stroka + '\nADVICE VALKS: ' + str(self.valkas_sv[otchet['save_level']]) + ' = ' \
                                 + str(round((84*self.black_cr_weapon)/1000000,2)) + ' millions\n'
                        otchet['full_price'] += 84*self.black_cr_weapon
                        otchet['Black_st'] += 84
                    if self.report_switch == 'report_on':
                        stroka = stroka + 'Total used ' + str(otchet['Black_st']) + ' Black stones = ' \
                                 + str(round(((otchet['Black_st'] * self.black_cr_weapon) / 1000000), 2)) + ' millions\n'
                        stroka = stroka + 'SUCCESS! We got silver embroidered life cloth ' + numbers_log[otchet['save_level']] \
                                 + ', chance = ' + str(persent) + '%\n'
                        stroka = stroka + 'WE REACH!!!\n'
                        stroka = stroka + 'We had ' + str(i) + ' attempts\n'
                        stroka = stroka + 'TOTAL SPENT: ' + str(otchet['base_items']) + ' base items = ' \
                                 + str(otchet['base_items'] * self.item_price) + ' silver  (' \
                                 + str(round(((otchet['base_items'] * self.item_price) / 1000000), 1)) + ' millions)\n'
                        stroka = stroka + 'TOTAL LOST: ' + str(otchet['level_1']) + ' cloth +1, ' \
                                 + str(otchet['level_2']) + ' cloth +2, ' + str(otchet['level_3']) + ' cloth +3, ' \
                                 + str(otchet['level_4']) + ' cloth +4\n'
                        for k in all_levels.keys():
                            if k > 0 and k < 5:
                                stroka = stroka + 'WE COULD GET ' + str(all_levels[k]) +' cloth ' + numbers_log[k] + '\n'
                        stroka = stroka + 'FULL PRICE = ' + str(otchet['full_price']) + ' silver (' \
                                 + str(int(otchet['full_price']/1000000)) + ' millions)\n'
                    break
                else:
                    otchet['full_price'] += self.item_price
                    otchet['base_items'] += 1
                    otchet['save_level'] += 1
                    all_levels[otchet['save_level']] += 1
                    if self.valkas_sv[otchet['save_level']] in stone_amount.keys():
                        stroka = stroka + '\nADVICE VALKS: ' + str(self.valkas_sv[otchet['save_level']]) + ' = ' \
                                 + str(round((stone_amount[self.valkas_sv[otchet['save_level']]]*self.black_cr_weapon)/1000000,2)) + ' millions\n'
                        otchet['full_price'] += stone_amount[self.valkas_sv[otchet['save_level']]]*self.black_cr_weapon
                        otchet['Black_st'] += stone_amount[self.valkas_sv[otchet['save_level']]]
                    elif self.valkas_sv[otchet['save_level']] > 30:
                        stroka = stroka + '\nADVICE VALKS: ' + str(self.valkas_sv[otchet['save_level']]) + ' = ' \
                                 + str(round((84 * self.black_cr_weapon) / 1000000, 2)) + ' millions\n'
                        otchet['full_price'] += 84*self.black_cr_weapon
                        otchet['Black_st'] += 84

                    if self.report_switch == 'report_on':
                        stroka = stroka + 'Total used ' + str(otchet['Black_st']) + ' Black stones = ' \
                                 + str(round(((otchet['Black_st'] * self.black_cr_weapon) / 1000000), 2)) + ' millions\n'
                        stroka = stroka + 'SUCCESS! We got silver embroidered  life cloth ' + numbers_log[otchet['save_level']] + ', chance = ' + str(persent) + '%\n'
                    otchet[('level_' + str(otchet['save_level']))] += 1
                    if otchet['save_level'] > 1:
                        otchet[('level_' + str(otchet['save_level']-1))] -= 1
                    if self.report_switch == 'report_on':
                        stroka = stroka + 'SPENT: ' + str(otchet['base_items']) + ' base items = ' \
                                 + str(otchet['base_items'] * self.item_price) + ' silver  (' \
                                 + str(round(((otchet['base_items'] * self.item_price) / 1000000), 1)) + ' millions)\n'
                        stroka = stroka + 'LOST: ' + str(otchet['level_1']) + ' cloth +1, ' \
                                 + str(otchet['level_2']) + ' cloth +2, ' + str(otchet['level_3']) + ' cloth +3, ' \
                                 + str(otchet['level_4']) + ' cloth +4\n'
                    if self.valkas_sv[otchet['save_level']+1] <= softcap[otchet['save_level']+1]:
                        persent = self.base_persent[otchet['save_level']+1] \
                                  + self.valkas_sv[otchet['save_level']+1]*self.one_fail[otchet['save_level']+1]
                    else:
                        persent = self.base_persent[otchet['save_level']+1] \
                                  + (self.valkas_sv[otchet['save_level']+1]-softcap[otchet['save_level']+1])*new_onefail[otchet['save_level']+1] \
                                  + softcap[otchet['save_level']+1] *self.one_fail[otchet['save_level']+1]
                    if persent > self.potolok[otchet['save_level']+1]:
                        persent = self.potolok[otchet['save_level']+1]

            else:
                if self.valkas_sv[otchet['save_level']+1] in stone_amount.keys():
                    stroka = stroka + '\nADVICE VALKS: ' + str(self.valkas_sv[otchet['save_level']+1]) + ' = ' \
                             + str(round((stone_amount[self.valkas_sv[otchet['save_level']+1]] * self.black_cr_weapon) / 1000000,2)) + ' millions\n'
                    otchet['full_price'] += stone_amount[self.valkas_sv[otchet['save_level']+1]]*self.black_cr_weapon
                    otchet['Black_st'] += stone_amount[self.valkas_sv[otchet['save_level']+1]]
                elif self.valkas_sv[otchet['save_level']+1] > 30:
                    stroka = stroka + '\nADVICE VALKS: ' + str(self.valkas_sv[otchet['save_level']+1]) + ' = ' \
                             + str(round((84 * self.black_cr_weapon) / 1000000, 2)) + ' millions\n'
                    otchet['full_price'] += 84*self.black_cr_weapon
                    otchet['Black_st'] += 84
                otchet['full_price'] += self.item_price
                otchet['base_items'] += 1
                if self.report_switch == 'report_on':
                    stroka = stroka + 'Total used ' + str(otchet['Black_st']) + ' Black stones = ' \
                             + str(round(((otchet['Black_st'] * self.black_cr_weapon) / 1000000),2)) + ' millions\n'
                    stroka = stroka +"Bad luck! Silver embroidered life cloth " + numbers_log[otchet['save_level']] + " destroyed! START AGAIN.\n"
                    stroka = stroka + 'SPENT: ' + str(otchet['base_items']) + ' base items = ' \
                             + str(otchet['base_items'] * self.item_price) + ' silver  (' \
                             + str(round(((otchet['base_items'] * self.item_price) / 1000000), 1)) + ' millions)\n'
                    stroka = stroka + 'LOST: ' + str(otchet['level_1']) + ' cloth +1, ' \
                             + str(otchet['level_2']) + ' cloth +2, ' + str(otchet['level_3']) + ' cloth +3, ' \
                             + str(otchet['level_4']) + ' cloth +4\n'
                otchet['save_level'] = j - 1
                all_levels[otchet['save_level']] += 1
                if self.valkas_sv[otchet['save_level']+1] <= softcap[otchet['save_level']+1]:
                    persent = self.base_persent[otchet['save_level']+1] \
                              + self.valkas_sv[otchet['save_level']+1]*self.one_fail[otchet['save_level']+1]
                else:
                    persent = self.base_persent[otchet['save_level']+1] \
                              + (self.valkas_sv[otchet['save_level']+1]-softcap[otchet['save_level']+1])*new_onefail[otchet['save_level']+1] \
                              + softcap[otchet['save_level']+1] *self.one_fail[otchet['save_level']+1]
                if persent > self.potolok[otchet['save_level']+1]:
                    persent = self.potolok[otchet['save_level']+1]
        self.full_report['full_price'] = otchet['full_price']
        self.full_report['Black_st'] = otchet['Black_st']
        self.full_report['base_items'] = otchet['base_items']
        if self.report_switch == 'report_on':
            print(stroka)
        return self.full_report


    def logia_cloth(self):
        j = self.tochka[0]
        otchet = {'full_price': 0, 'Black_gem': 0, 'Con_black_gem':0, 'Durability':0}
        stroka = ''
        persent = self.base_persent[j+1]
        i = 0
        attempt_case = 0
        while 1:
            i += 1
            attempt_case += 1
            lucky = random.randint(1, self.amount)
            if lucky in range(int(persent * 100)):
                if j == self.tochka[1]:
                    if j < 16:
                        otchet['Black_gem'] += self.black_gem[j]
                        otchet['full_price'] += self.black_gem[j]*self.black_gem_price
                    else:
                        otchet['Con_black_gem'] += self.black_gem[j]
                        otchet['full_price'] += self.black_gem[j] * self.con_blgem_price
                    otchet['full_price'] += (otchet['Durability']/10)* self.item_price
                    stroka = stroka + '\nSUCCESS! +' + str(j) + ' after ' + str(attempt_case) + ' attempts' + ', chance = ' \
                             + str(self.base_persent[j]) + '\n'
                    stroka = stroka + 'TOTAL attempts: ' + str(i)
                    stroka = stroka + '\nWe started +' + str(self.tochka[0]-1) + ' and finished +' + str(self.tochka[1]) + '\n'
                    stroka = stroka + 'TOTAL SPENT: ' + str(otchet['Black_gem']) + ' black gems = ' \
                             + str(otchet['Black_gem'] * self.black_gem_price) + ' silver  (' \
                             + str(round(((otchet['Black_gem'] * self.black_gem_price) / 1000000), 1)) + ' millions)\n'
                    stroka = stroka + 'TOTAL SPENT: ' + str(otchet['Con_black_gem']) + ' concentrated black gems = ' \
                             + str(otchet['Con_black_gem'] * self.con_blgem_price) + ' silver  (' \
                             + str(round(((otchet['Con_black_gem'] * self.con_blgem_price) / 1000000), 1)) + ' millions)\n'
                    stroka = stroka + 'LOST DURABILITY: ' + str(otchet['Durability']) + ' points = ' \
                             + str((otchet['Durability']/10)* self.item_price) + ' silver  (' \
                             + str(round(((otchet['Durability']/10) * self.item_price) / 1000000, 1)) + ' millions)\n'
                    stroka = stroka + 'FULL PRICE = ' + str(otchet['full_price']) + ' silver (' \
                             + str(round((otchet['full_price']/1000000),2)) + ' millions)\n'
                    break
                else:
                    if j < 16:
                        otchet['Black_gem'] += self.black_gem[j]
                        otchet['full_price'] += self.black_gem[j]*self.black_gem_price
                    else:
                        otchet['Con_black_gem'] += self.black_gem[j]
                        otchet['full_price'] += self.black_gem[j] * self.con_blgem_price
                    stroka = stroka + '\nSUCCESS! +' + str(j) + ' after ' + str(attempt_case) + ' attempts' + ', chance = ' \
                             + str(self.base_persent[j]) + '\n'
                    if otchet['Con_black_gem'] == 0:
                        stroka = stroka + 'SPENT: ' + str(attempt_case) + ' black gems = ' \
                                 + str(attempt_case * self.black_gem_price) + ' silver  (' \
                                 + str(round(((attempt_case * self.black_gem_price) / 1000000), 1)) + ' millions)\n'
                    else:
                        stroka = stroka + 'SPENT: ' + str(attempt_case) + ' concentrated black gems = ' \
                                 + str(attempt_case * self.con_blgem_price) + ' silver  (' \
                                 + str(round(((attempt_case * self.con_blgem_price) / 1000000), 1)) + ' millions)\n'
                    stroka = stroka + 'FULL PRICE = ' + str(otchet['full_price']) + ' silver (' \
                             + str(round((otchet['full_price']/1000000),2)) + ' millions)\n'
                    j += 1
                    persent = self.base_persent[j]
                    attempt_case = 0
            else:
                if j <= 17:
                    otchet['Durability'] += 5
                    persent = self.base_persent[j]
                    if j < 16:
                        otchet['Black_gem'] += self.black_gem[j]
                        otchet['full_price'] += self.black_gem[j] * self.black_gem_price
                    else:
                        otchet['Con_black_gem'] += self.black_gem[j]
                        otchet['full_price'] += self.black_gem[j] * self.con_blgem_price
                else:
                    otchet['Durability'] += 10
                    otchet['Con_black_gem'] += self.black_gem[j]
                    otchet['full_price'] += self.black_gem[j] * self.con_blgem_price
                    stroka = stroka + '\nBAD LUCK! We lost level of enchanting. Now we have +' + str(j-2) + ' again\n'
                    stroka = stroka + 'SPENT: ' + str(attempt_case) + ' concentrated black gems = ' \
                             + str(attempt_case * self.con_blgem_price) + ' silver  (' \
                             + str(round(((attempt_case * self.con_blgem_price) / 1000000), 1)) + ' millions)\n'
                    stroka = stroka + 'FULL PRICE = ' + str(otchet['full_price']) + ' silver (' \
                             + str(round((otchet['full_price']/1000000),2)) + ' millions)\n'
                    j -= 1
                    persent = self.base_persent[j]
                    attempt_case = 0
        self.full_report['full_price'] = otchet['full_price']
        self.full_report['Black_gem'] = otchet['Black_gem']
        self.full_report['Con_black_gem'] = otchet['Con_black_gem']
        self.full_report['Durability'] = otchet['Durability']
        if self.report_switch == 'report_on':
            print(stroka)
        return self.full_report


def main_test_10000(check_test,test_cases,tochka,valkas_sv,use_cron_stone,Colour,valkas_m,item_price,
                    black_cr_weapon,black_cr_weapon_16,cron_stone_price,type_stuff,valkas_test,test_valkas,
                    base_persent, one_fail, potolok, Cron_amount,fragments_memory_price,name_stuff,
                    black_gem_price, con_blgem_price,report_test, auction_prices,black_gem):
    if check_test == 1 and valkas_test != 1:
        j = 0
        total_price = 0
        total_Black_st = 0
        total_base_items = 0
        total_black_gem = 0
        total_Conblack_gem = 0
        total_Dur = 0
        report_switch = 'report_off'
        stone_amount = {0: 0, 5: 5, 10: 12, 15: 21, 20: 33, 25: 53, 30: 84}
        my_caces = {}
        sort_caces = {}
        know_price = {'good_price':0,'double_auc_price':0,'bad_price':0}
        mas = []

        while j < test_cases:
            toch_b = sharpering(tochka, report_switch,valkas_sv, use_cron_stone, Colour, valkas_m, item_price,
                                    black_cr_weapon, black_cr_weapon_16, cron_stone_price, base_persent, one_fail, potolok,
                                            Cron_amount,fragments_memory_price, black_gem_price, con_blgem_price,black_gem)
            if name_stuff == 'Silverembroidered':
                mas.append(toch_b.silver_tochki())
                total_Black_st += mas[j]['Black_st']
                total_base_items += mas[j]['base_items']
                total_price += mas[j]['full_price']
            elif name_stuff == 'LoggiaCloth' or name_stuff == 'GeranoaCloth':
                mas.append(toch_b.logia_cloth())
                total_black_gem += mas[j]['Black_gem']
                total_Conblack_gem += mas[j]['Con_black_gem']
                total_Dur += mas[j]['Durability']
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
        if name_stuff == 'Silverembroidered':
            average_Black_st = int(total_Black_st / len(mas))
            average_base_items = int(total_base_items / len(mas))
        elif name_stuff == 'LoggiaCloth' or name_stuff == 'GeranoaCloth':
            average_black_gem = int(total_black_gem / len(mas))
            average_Conblack_gem = int(total_Conblack_gem / len(mas))
            average_Dur = int(total_Dur / len(mas))
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
        if name_stuff == 'Silverembroidered':
            print('AVERAGE SPENT ',average_Black_st, ' Black stones')
            print('AVERAGE SPENT ', average_base_items, ' base items')
        elif name_stuff == 'GeranoaCloth' or name_stuff == 'GeranoaCloth':
            print('AVERAGE SPENT ',average_black_gem, ' black gems')
            print('AVERAGE SPENT ', average_Conblack_gem, ' concentreted black gems')
            print('LOST ', average_Dur, ' durability points')
        print('AVERAGE COSTS = ', average_price,'silver (', int(average_price/1000000),' millions )')


    # BIG VALKS TEST
    if valkas_test == 1:
        PRICE_s = 0
        j = 0
        total_price = 0
        report_switch = 'report_off'
        valkas_m = 'valkas_off'
        stone_amount = {0: 0, 5: 5, 10: 12, 15: 21, 20: 33, 25: 53, 30: 84}
        mas = []
        while j < test_cases:
            toch_b = sharpering(tochka, report_switch,valkas_sv, use_cron_stone, Colour, valkas_m, item_price,
                                    black_cr_weapon, black_cr_weapon_16, cron_stone_price, base_persent, one_fail, potolok,
                                            Cron_amount,fragments_memory_price, black_gem_price, con_blgem_price)
            if name_stuff == 'Silverembroidered':
                mas.append(toch_b.silver_tochki())
            total_price += mas[j]['full_price']
            j += 1

        average_price = total_price / len(mas)
        PRICE_s = average_price
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

        print('\nCALCULATING THE BEST OPTION...')

        mas = []
        valkas_m = 'valkas_on'
        valkas_sv = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0}
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
            while t < test_valkas:
                toch_b = sharpering(tochka, report_switch, valkas_sv, use_cron_stone, Colour, valkas_m, item_price,
                                    black_cr_weapon, black_cr_weapon_16, cron_stone_price, base_persent, one_fail,
                                    potolok,
                                    Cron_amount, fragments_memory_price, black_gem_price, con_blgem_price)
                if name_stuff == 'Silverembroidered':
                    mas.append(toch_b.silver_tochki())
                total_price += mas[t]['full_price']
                total_black_st += mas[t]['Black_st']
                t += 1
            average_price = total_price / len(mas)
            average_black_st = total_black_st / len(mas)
            average_price_dur = 0
            if average_price < PRICE_s:
                PRICE_s = average_price
                the_best_valkas.clear()
                the_best_valkas = valkas_sv.copy()
        print('\n\nGRADE: ', Colour, '  TYPE: ', type_stuff)
        print('The best TOTAL PRICE is ', PRICE_s, '  (',int(PRICE_s/1000000), 'millions )')
        print('The best valks is ',the_best_valkas)
