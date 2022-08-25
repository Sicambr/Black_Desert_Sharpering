import random

class sharpering:
    def __init__(self,tochka, report_switch, valkas_sv, use_cron_stone, colour_w, valkas,item_price, black_cr_weapon,
                 black_cr_weapon_16, cron_stone_price, base_persent, one_fail, potolok, Cron_amount,fragments_memory_price):

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


    def trati(self,amount,cost_stone,base_persent,potolok,one_fail,valkas,fail_increase,j,save_chanse):
        otchet = {'black_st_price':0,'Black_st':0,'Con_black_st':0,'Durability':0,'Cron_st':0,'our_pos':0,
                  'save_chanse':0, 'valks_amount':0,'full_price':0,'fragm_memory':0}
        otchet['our_pos'] = j
        otchet['save_chanse'] = save_chanse
        koef_restore = 1
        if self.colour_w == 'GREEN':
            koef_restore = 5
        elif self.colour_w == 'BLUE':
            koef_restore = 2
        elif self.colour_w == 'GRAY':
            koef_restore = 10
        stone_amount = {0: 0, 5: 5, 10: 12, 15: 21, 20: 33, 25: 53, 30: 84}
        persent = 0
        stroka = ''
        if save_chanse == 0:
            stroka = stroka + 'Advice of VALKS: ' + str(valkas) + '\n'
            if base_persent + valkas * one_fail > potolok:
                persent = potolok
                otchet['save_chanse'] = valkas
            else:
                persent = base_persent + valkas * one_fail
                otchet['save_chanse'] = valkas
            if valkas in stone_amount:
                otchet['valks_amount'] += stone_amount[valkas]
                if (stone_amount[valkas]*self.black_cr_weapon) / 1000000 >= 1:
                    stroka = stroka + 'Black stones for VALKS: ' + str(stone_amount[valkas]) + ' = ' \
                             + str(stone_amount[valkas]*self.black_cr_weapon) + ' silver (' \
                             + str(round((stone_amount[valkas]*self.black_cr_weapon)/1000000 , 2)) + ' millions)\n'
                else:
                    stroka = stroka + 'Black stones for VALKS: ' + str(stone_amount[valkas]) + ' = ' \
                             + str(stone_amount[valkas]*self.black_cr_weapon) + ' silver\n'
        else:
            persent = otchet['save_chanse'] * one_fail + base_persent
            stroka = stroka + 'Saved failures: ' + str(otchet['save_chanse']) + '\n'
            if persent > potolok:
                persent = potolok
        base_durability = 5
        if fail_increase != 1:
            base_durability = 10
        i = 0

        while 1:
            i += 1
            lucky = random.randint(1,amount)
            if lucky in range(int(persent*100)):
                if j <= 15:
                    otchet['Black_st'] += 1
                elif j == 16:
                    otchet['Con_black_st'] += 1
                else:
                    if self.use_cron_stone == 'yes':
                        otchet['Cron_st'] += self.Cron_amount[otchet['our_pos'] + 1]
                    otchet['Con_black_st'] += 1
                otchet['our_pos'] = j + 1
                stroka = stroka + '+' + str(otchet['our_pos']) + ' enchantment with a chance = ' \
                         + str(round(persent, 2)) + '%\n'
                stroka = stroka + 'Additional enchantment chance when we finished: ' + str(otchet['save_chanse']) + '\n'
                otchet['save_chanse'] = 0
                break
            else:
                if fail_increase == 1:
                    otchet['Black_st'] += 1
                else:
                    otchet['Con_black_st'] += 1
                if j > 16 and self.use_cron_stone == 'no':
                    otchet['our_pos'] = j - 1
                    otchet['Durability'] += base_durability
                    stroka = stroka +  "Bad luck! We're back +" + str(otchet['our_pos']) \
                             + ' enchantment with a chance = ' \
                             + str(round(persent, 2)) + '%\n'
                    otchet['save_chanse'] += fail_increase
                    stroka = stroka + 'Additional enchantment chance when we finished: ' + str(otchet['save_chanse']) + '\n'
                    break
                if j > 16 and self.use_cron_stone == 'yes':
                    otchet['Cron_st'] += self.Cron_amount[otchet['our_pos']+1]
                otchet['save_chanse'] += fail_increase
                persent = otchet['save_chanse'] * one_fail + base_persent
                if persent > potolok:
                    persent = potolok
                otchet['Durability'] += base_durability
        otchet['black_st_price'] = cost_stone*i
        if self.item_price / 100 > self.fragments_memory_price / koef_restore:
            otchet['fragm_memory'] = otchet['Durability'] / koef_restore
        all_price_enchanting = otchet['valks_amount'] * self.black_cr_weapon + otchet['black_st_price'] \
                               + otchet['Cron_st']*self.cron_stone_price
        if self.item_price / 100 > self.fragments_memory_price / koef_restore:
            all_price_enchanting += otchet['fragm_memory']*self.fragments_memory_price
        else:
            all_price_enchanting += ((otchet['Durability'] / 10) * self.item_price)
        otchet['full_price'] = all_price_enchanting
        if self.report_switch == 'report_on':
            if fail_increase == 1:
                if otchet['black_st_price'] / 1000000 >= 1:
                    stroka = stroka + str(i) + ' Black stones : ' + str(otchet['black_st_price']) + ' silver (' \
                             + str(round((otchet['black_st_price']/1000000),2)) + ' millions)\n'
                else:
                    stroka = stroka + str(i) + ' Black stones : ' + str(otchet['black_st_price']) + ' silver\n'
                if otchet['Durability'] != 0:
                    if self.item_price / 100 > self.fragments_memory_price / koef_restore:
                        stroka = stroka + 'Lost ' + str(otchet['Durability']) + ' durability\n'
                        stroka = stroka + 'Used ' + str(int(otchet['fragm_memory'])) + ' fragments of memory = ' \
                                 + str(int(otchet['fragm_memory']*self.fragments_memory_price)) + ' silver (' \
                                 + str(int((otchet['fragm_memory']*self.fragments_memory_price)/1000000)) + ' millions)\n'
                    else:
                        stroka = stroka + 'Lost ' + str(otchet['Durability']) + ' durability = ' \
                                 + str(int((otchet['Durability'] / 10) * self.item_price)) + ' silver (' \
                                 + str(round(((otchet['Durability'] / 10) * self.item_price)/1000000,2)) + ' millions)\n'
            else:
                if otchet['black_st_price'] / 1000000 >= 1:
                    stroka = stroka + str(i) + ' Concentrated black stones : ' + str(otchet['black_st_price']) + ' silver (' \
                             + str(round((otchet['black_st_price']/1000000),2)) + ' millions)\n'
                else:
                    stroka = stroka + str(i) + ' Concentrated black stones : ' + str(otchet['black_st_price']) + ' silver\n'
                # if to use fragments memore is cheaper
                if otchet['Durability'] != 0:
                    if self.item_price / 100 > self.fragments_memory_price / koef_restore:
                        stroka = stroka + 'Lost ' + str(otchet['Durability']) + ' durability\n'
                        stroka = stroka + 'Used ' + str(int(otchet['fragm_memory'])) + ' fragments of memory = ' \
                                 + str(int(otchet['fragm_memory']*self.fragments_memory_price)) + ' silver (' \
                                 + str(int((otchet['fragm_memory']*self.fragments_memory_price)/1000000)) + ' millions)\n'
                    else:
                        stroka = stroka + 'Lost ' + str(otchet['Durability']) + ' durability = ' \
                                 + str(int((otchet['Durability'] / 10) * self.item_price)) + ' silver (' \
                                 + str(round(((otchet['Durability'] / 10) * self.item_price)/1000000,2)) + ' millions)\n'
                if self.use_cron_stone == 'yes' and j > 16:
                    if (otchet['Cron_st']*self.cron_stone_price) / 1000000 >= 1:
                        stroka = stroka + 'Lost ' + str(otchet['Cron_st']) + ' Cron stones: ' \
                                 + str(otchet['Cron_st'] * self.cron_stone_price) + ' silver (' \
                                 + str(int((otchet['Cron_st']*self.cron_stone_price)/1000000)) + ' millions)\n'
                    else:
                        stroka = stroka + 'Lost ' + str(otchet['Cron_st']) + ' Cron stones: ' \
                                 + str(otchet['Cron_st']*self.cron_stone_price) + ' silver\n'
            if otchet['valks_amount'] != 0:
                if (otchet['black_st_price'] + otchet['valks_amount'] * self.black_cr_weapon) / 1000000 >= 1:
                    stroka = stroka + 'All Black stones cost = '\
                             + str(otchet['black_st_price'] + otchet['valks_amount'] * self.black_cr_weapon) \
                             + ' silver (' + str(round((otchet['black_st_price'] + otchet['valks_amount'] * self.black_cr_weapon)/1000000, 2)) \
                             + ' millions)\n'
                else:
                    stroka = stroka + 'All Black stones cost = '\
                             + str(otchet['black_st_price'] + otchet['valks_amount'] * self.black_cr_weapon) + ' silver\n'
            if (all_price_enchanting / 1000000) >= 1:
                stroka = stroka + 'FULL PRICE = ' + str(all_price_enchanting) + ' silver (' \
                         + str(all_price_enchanting/1000000) +' millions)\n'
            else:
                stroka = stroka + 'FULL PRICE = ' + str(all_price_enchanting) + ' silver\n'
            print(stroka)
        return otchet

    def diap_tochki(self):
        i = (self.tochka[0]-1)
        save_chanse = 0
        koef_restore = 1
        if self.colour_w == 'GREEN':
            koef_restore = 5
        elif self.colour_w == 'BLUE':
            koef_restore = 2
        elif self.colour_w == 'GRAY':
            koef_restore = 10
        while i < self.tochka[1]:
            valkas_on = 0
            fail_increase = 1
            report_enchantment = {}
            if self.valkas == 'valkas_on':
                valkas_on = 1
            if (i+1) <= 15:
                report_enchantment = self.trati(self.amount, self.black_cr_weapon, self.base_persent[i+1],
                                                 self.potolok[i+1], self.one_fail[i+1],
                                                 self.valkas_sv[i+1]*valkas_on, fail_increase, i,save_chanse)
                self.full_report['save_chanse'] = report_enchantment['save_chanse']
                self.full_report['valks_amount'] += report_enchantment['valks_amount']
                self.full_report['black_st_price'] += report_enchantment['black_st_price']
                self.full_report['Durability'] += report_enchantment['Durability']
                self.full_report['Black_st'] += report_enchantment['Black_st']
                self.full_report['Con_black_st'] += report_enchantment['Con_black_st']
                self.full_report['Cron_st'] += report_enchantment['Cron_st']
                self.full_report['fragm_memory'] += report_enchantment['fragm_memory']
            else:
                if (i+1) == 16:
                    fail_increase = 2
                elif (i+1) == 17:
                    fail_increase = 3
                elif (i+1) == 18:
                    fail_increase = 4
                elif (i+1) == 19:
                    fail_increase = 5
                elif (i+1) == 20:
                    fail_increase = 6
                report_enchantment = self.trati(self.amount, self.black_cr_weapon_16, self.base_persent[i + 1],
                                                 self.potolok[i + 1], self.one_fail[i + 1],
                                                 self.valkas_sv[i + 1] * valkas_on, fail_increase, i,save_chanse)
                self.full_report['save_chanse'] = report_enchantment['save_chanse']
                self.full_report['valks_amount'] += report_enchantment['valks_amount']
                self.full_report['black_st_price'] += report_enchantment['black_st_price']
                self.full_report['Durability'] += report_enchantment['Durability']
                self.full_report['Black_st'] += report_enchantment['Black_st']
                self.full_report['Con_black_st'] += report_enchantment['Con_black_st']
                self.full_report['Cron_st'] += report_enchantment['Cron_st']
                self.full_report['fragm_memory'] += report_enchantment['fragm_memory']
            save_chanse = self.full_report['save_chanse']
            i = report_enchantment['our_pos']
        self.full_report['black_st_price'] += self.full_report['valks_amount'] * self.black_cr_weapon
        self.full_report['Black_st'] += self.full_report['valks_amount']
        full_price = 0
        if self.full_report['fragm_memory'] == 0:
            full_price = self.full_report['black_st_price'] + self.full_report['Cron_st'] * self.cron_stone_price \
                         + int(self.full_report['Durability'] / 10) * self.item_price
        else:
            full_price = self.full_report['black_st_price'] + self.full_report['Cron_st'] * self.cron_stone_price \
                         + int((self.full_report['Durability'] / koef_restore) * self.fragments_memory_price)
        self.full_report['full_price'] = full_price

        if self.report_switch == 'report_on':
            print('\nTOTAL USED ', self.full_report['Black_st'], ' Black stones')
            print('TOTAL USED ', self.full_report['Con_black_st'], ' Concentrated black stones')
            if int(self.full_report['black_st_price']/1000000) >= 1:
                print('All STONES COSTS = ', self.full_report['black_st_price'], 'silver  (',
                      int(self.full_report['black_st_price']/1000000),'millions )')
            else:
                print('All STONES COSTS = ', self.full_report['black_st_price'], ' silver')
            if self.full_report['fragm_memory'] == 0:
                if int(int(self.full_report['Durability']/10)*self.item_price / 1000000) >= 1:
                    print('TOTAL LOST', self.full_report['Durability'], 'POINTS OF DURABILITY = ',
                          int(self.full_report['Durability']/10)*self.item_price, 'silver  (',
                          int(int(self.full_report['Durability']/10)*self.item_price / 1000000), 'millions )')
                else:
                    print('TOTAL LOST', self.full_report['Durability'], 'POINTS OF DURABILITY = ',
                          int(self.full_report['Durability']/10)*self.item_price, 'silver')
            else:
                print('TOTAL LOST', self.full_report['Durability'], 'POINTS OF DURABILITY')
                print('TOTAL LOST', int(self.full_report['Durability']/koef_restore), 'fragments of memory = ',
                      int((self.full_report['Durability']/koef_restore)*self.fragments_memory_price), 'silver (',
                      int(((self.full_report['Durability']/koef_restore)*self.fragments_memory_price)/1000000), 'millions )')
            if self.use_cron_stone == 'yes':
                if self.full_report['Cron_st']*self.cron_stone_price / 1000000 >= 1:
                    print('TOTAL USED ', self.full_report['Cron_st'], ' CRONE STONES = ',
                          str(self.full_report['Cron_st']*self.cron_stone_price), 'silver  (',
                          int(int(self.full_report['Cron_st']*self.cron_stone_price/ 1000000)), 'millions )')
                else:
                    print('TOTAL USED ', self.full_report['Cron_st'], ' CRONE STONES = ',
                          str(self.full_report['Cron_st']*self.cron_stone_price),'silver')
            if int(full_price/1000000)>=1:
                print('ALL PRICE = ', full_price, 'silver  (', int(full_price / 1000000), 'millions )')
            else:
                print('ALL PRICE = ', full_price, 'silver')
        return self.full_report


