import os

def Customise_DATA(Colour, type_stuff, name_stuff):
    name_of_file = 'data.txt'
    my_data_file = []
    for line in open(name_of_file):my_data_file.append(line)
    full_data = {}
    base_persent = {}
    one_fail = {}
    potolok = {}
    Cron_amount = {}
    valkas_sv = {}
    auction_prices = {}
    i = 0
    while i < len(my_data_file):
        my_data_file[i] = my_data_file[i].rstrip('\n')
        if my_data_file[i][0] == '#':
            category = my_data_file[i].split('_')
            category[0] = category[0].lstrip('#')
            if Colour == category[0] and type_stuff == category[1] and name_stuff == (category[2]+category[3]):
                b_p = my_data_file[i+1].partition('{')[2].rstrip('}\n').replace(' ','')
                b_p_list = b_p.split(',')
                for j in b_p_list:
                    base_persent[int(j.partition(':')[0])] = round(float(j.partition(':')[2]),5)
                    full_data['base_persent'] = base_persent
                o_f = my_data_file[i + 2].partition('{')[2].rstrip('}\n').replace(' ', '')
                o_f_list = o_f.split(',')
                for j in o_f_list:
                    one_fail[int(j.partition(':')[0])] = round(float(j.partition(':')[2]), 5)
                    full_data['one_fail'] = one_fail
                p = my_data_file[i + 3].partition('{')[2].rstrip('}\n').replace(' ', '')
                p_list = p.split(',')
                for j in p_list:
                    potolok[int(j.partition(':')[0])] = round(float(j.partition(':')[2]), 5)
                    full_data['potolok'] = potolok
                c_a = my_data_file[i + 4].partition('{')[2].rstrip('}\n').replace(' ', '')
                c_a_list = c_a.split(',')
                for j in c_a_list:
                    Cron_amount[int(j.partition(':')[0])] = round(float(j.partition(':')[2]), 5)
                    full_data['Cron_amount'] = Cron_amount
                v_s = my_data_file[i + 5].partition('{')[2].rstrip('}\n').replace(' ', '')
                v_s_list = v_s.split(',')
                for j in v_s_list:
                    valkas_sv[int(j.partition(':')[0])] = int(j.partition(':')[2])
                    full_data['valkas_sv'] = valkas_sv
                a_p = my_data_file[i + 6].partition('{')[2].rstrip('}\n').replace(' ', '')
                a_p_list = a_p.split(',')
                for j in a_p_list:
                    auction_prices[int(j.partition(':')[0])] = round(float(j.partition(':')[2]), 2)
                    full_data['auction_prices'] = auction_prices
                break
        i += 1
    return full_data

