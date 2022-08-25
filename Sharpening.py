import enchant_weapon1_20
import en_accessories1_5
import test_accessories
import test_sharp
import test_gun
import load_data
import en_cloth1_5
import en_ship_parts1_10

# Create enchantment
# valkas means = valkas_off, valkas_on
# tier means = GREEN, BLUE, GRAY, GOLD, RED
# report_switch = report_on, report_off
# use_cron_stone = yes, no
# worth of black cristal for weapon
# type stuff = JEWELRY, WEAPON

# worth of black stone
black_cr_weapon = 196000
# worth of concentrated black cristal for weapon
black_cr_weapon_16 = 2240000
# worth of black gem
black_gem_price = 935000
# worth of concentated black gem
con_blgem_price = 9350000
# worth of cron stone
cron_stone_price = 2000000
# worth of fragments of a memory
fragments_memory_price = 2900000

tochka = [1,18]


Colour = 'BLUE'
type_stuff = 'CLOTH'
name_stuff = 'GeranoaCloth'
valkas_sv = {}


my_date = load_data.Customise_DATA(Colour,type_stuff,name_stuff)
base_persent = my_date['base_persent']
one_fail = my_date['one_fail']
potolok = my_date['potolok']
Cron_amount = my_date['Cron_amount']
valkas_sv = my_date['valkas_sv']
auction_prices = my_date['auction_prices']



# worth of item from auction house
item_price = 10000000
valkas_m = 'valkas_on'
report_switch = 'report_off'
report_test = 'on'
use_cron_stone = 'no'

test_cases = 10000
check_test = 1
test_valkas = 100
valkas_test = 0

test_for_range = 0

if test_for_range == 1:
    Colour = 'GRAY'
    type_stuff = 'WEAPON'
    name_stuff = 'MainWeapon'
    valkas_m = 'valkas_off'
    report_switch = 'report_off'
    test_cases = 10000
    test_sharp.range_test(test_cases,tochka,valkas_sv,use_cron_stone,Colour,valkas_m,item_price,
                        black_cr_weapon,black_cr_weapon_16,cron_stone_price,type_stuff,
                               base_persent, one_fail, potolok, Cron_amount,fragments_memory_price)
else:

    if type_stuff == 'WEAPON' or type_stuff == 'ARMOR':
        toch_a = enchant_weapon1_20.sharpering(tochka, report_switch, valkas_sv, use_cron_stone, Colour, valkas_m, item_price,
                                        black_cr_weapon, black_cr_weapon_16, cron_stone_price,base_persent,one_fail,
                                        potolok,Cron_amount,fragments_memory_price)
        toch_a.diap_tochki()
        test_sharp.main_test_10000(check_test,test_cases,tochka,valkas_sv,use_cron_stone,Colour,valkas_m,item_price,
                            black_cr_weapon,black_cr_weapon_16,cron_stone_price,type_stuff,valkas_test,test_valkas,
                                   base_persent, one_fail, potolok, Cron_amount,fragments_memory_price)
    elif type_stuff == 'JEWELRY':
        black_gem = {0: 1, 1: 1, 2: 2, 3: 3, 4: 4, 5: 5}
        # FOR ONE CASE
        toch_a = en_accessories1_5.sharpering(tochka, report_switch, valkas_sv, use_cron_stone, Colour, valkas_m, item_price,
                                        black_cr_weapon, black_cr_weapon_16, cron_stone_price,base_persent,one_fail,
                                        potolok,Cron_amount,fragments_memory_price,black_gem,black_gem_price,con_blgem_price)
        if name_stuff == 'LoggiaAccessories':
            toch_a.loggia_tochki()
        elif name_stuff == 'GeranoaAccessories':
            toch_a.Geranoa_tochki()
        elif name_stuff == 'ManosAccessories':
            black_gem = {0: 10, 1: 10, 2: 11, 3: 13, 4: 16, 5: 20}
            toch_a.Geranoa_tochki()
        else:
            toch_a.diap_tochki()
        # FOR MASS TEST
        en_accessories1_5.main_test_10000(check_test,test_cases,tochka,valkas_sv,use_cron_stone,Colour,valkas_m,item_price,
                            black_cr_weapon,black_cr_weapon_16,cron_stone_price,type_stuff,valkas_test,test_valkas,
                                   base_persent, one_fail, potolok, Cron_amount,fragments_memory_price,name_stuff,
                                          black_gem,black_gem_price,con_blgem_price,report_test, auction_prices)
    elif type_stuff == 'CLOTH':
        black_gem = {1: 1, 2: 1, 3: 1, 4: 1, 5: 1, 6: 1, 7: 1, 8: 1, 9: 1, 10: 1, 11: 1, 12: 1, 13: 1, 14: 1, 15: 1, 16: 1, 17: 1, 18: 1, 19: 1, 20: 1}
        # FOR ONE CASE
        toch_a = en_cloth1_5.sharpering(tochka, report_switch, valkas_sv, use_cron_stone, Colour, valkas_m, item_price,
                                        black_cr_weapon, black_cr_weapon_16, cron_stone_price,base_persent,one_fail,
                                        potolok,Cron_amount,fragments_memory_price,black_gem_price,con_blgem_price,black_gem)
        if name_stuff == 'Silverembroidered':
            toch_a.silver_tochki()
        elif name_stuff == 'LoggiaCloth':
            toch_a.logia_cloth()
        elif name_stuff == 'GeranoaCloth':
            toch_a.logia_cloth()
        # FOR MASS TEST
        en_cloth1_5.main_test_10000(check_test,test_cases,tochka,valkas_sv,use_cron_stone,Colour,valkas_m,item_price,
                            black_cr_weapon,black_cr_weapon_16,cron_stone_price,type_stuff,valkas_test,test_valkas,
                                   base_persent, one_fail, potolok, Cron_amount,fragments_memory_price,name_stuff,
                                          black_gem_price,con_blgem_price,report_test, auction_prices,black_gem)
    elif type_stuff == 'GUN':
        toch_a = en_ship_parts1_10.sharpering(tochka, report_switch, valkas_sv, use_cron_stone, Colour, valkas_m, item_price,
                                        black_cr_weapon, black_cr_weapon_16, cron_stone_price,base_persent,one_fail,
                                        potolok,Cron_amount,fragments_memory_price)
        toch_a.diap_tochki()
        test_gun.main_test_10000(check_test,test_cases,tochka,valkas_sv,use_cron_stone,Colour,valkas_m,item_price,
                            black_cr_weapon,black_cr_weapon_16,cron_stone_price,type_stuff,valkas_test,test_valkas,
                                   base_persent, one_fail, potolok, Cron_amount,fragments_memory_price)







