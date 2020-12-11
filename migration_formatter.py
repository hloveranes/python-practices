import re

barangays = [
    # Bangued
    [
        'Agtangao', 'Angad', 'Bañacao', 'Bangbangar', 'Cabuloan', 'Calaba',
        'Tablac(Calot)', 'Cosili West(Buaya)', 'Cosili East(Proper)',
        'Dangdangla', 'Lingtan', 'Lipcan', 'Lubong', 'Macarcarmay', 'Maoay',
        'Macray', 'Malita', 'Palao', 'Patucannay', 'Sagap', 'San Antonio',
        'Santa Rosa', 'Sao-atan', 'Sappaac', 'Zone 2 Pob. (Consiliman)',
        'Zone 3 Pob. (Lalaud)', 'Zone 4 Pob. (Town Proper)',
        'Zone 5 Pob. (Bo. Barikir)', 'Zone 6 Pob. (Sinapangan)',
        'Zone 7 Pob. (Baliling)', 'Zone 1 Pob. (Nalasin)'
    ],
    # Boliney
    [
        'Amti', 'Bao-yan', 'Danac East', 'Dao-angan', 'Dumagas', 'Kilong-Olao',
        'Poblacion(Boliney)', 'Danac West'
    ],
    # Bucay
    [
        'Abang', 'Bangbangcag', 'Bangcagan', 'Banglolao', 'Bugbog', 'Calao',
        'Dugong', 'Labon', 'Layugan', 'Madalipay', 'Pagala', 'Palaquio',
        'Pakiling', 'Patoc', 'North Poblacion', 'South Poblacion', 'Quimloong',
        'Salnec', 'San Miguel', 'Siblong', 'Tabiog'
    ],
    # Bucloc
    ['Ducligan', 'Labaan', 'Lingay', 'Lamao(Pob.)'],
    # Daguioman
    ['Ableg', 'Cabaruyan', 'Pikek', 'Tui(Pob.)'],
    # Danglas
    [
        'Abaquid', 'Cabaruan', 'Caupasan(Pob.)', 'Danglas', 'Nagaparan',
        'Padangitan', 'Pangal'
    ],
    # Dolores
    [
        'Bayaan', 'Cabaroan', 'Calumbaya', 'Cardona', 'Isit', 'Kimmalaba',
        'Libtec', 'Lub-lubba', 'Mudiit', 'Namit-ingan', 'Pacac', 'Poblacion',
        'Salucag', 'Talogtog', 'Taping'
    ],
    # La Paz
    [
        'Benben(Bonbon)', 'Bulbulala', 'Buli', 'Canan(Gapan)', 'Liguis',
        'Malabbaga', 'Mudeng', 'Pidipid', 'Poblacion', 'San Gregorio', 'Toon',
        'Udangan'
    ],
    # Lacub
    [
        'Bacag', 'Buneg', 'Guinguinabang', 'Lan-ag', 'Pacoc',
        'Poblacion(Talampac)'
    ],
    # Lagangilang
    [
        'Aguet', 'Bacooc', 'Balais', 'Cayapa', 'Dalaguisen', 'Laang', 'Lagben',
        'Laguiben', 'Nagtipulan', 'Nagtupacan', 'Paganao', 'Pawa', 'Poblacion',
        'Presentar', 'San Isidro', 'Tagodtod', 'Taping'
    ],
    # Lagayan
    ['Ba-i', 'Collago', 'Pang-ot', 'Poblacion', 'Pulot'],
    # Langiden
    [
        'Baac', 'Dalayap (Nalaas)', 'Mabungtot', 'Malapaao', 'Poblacion',
        'Quillat'
    ],
    # Licuan-Baay(Licuan)
    [
        'Bonglo (Patagui)', 'Bulbulala', 'Cawayan', 'Domenglay', 'Lenneng',
        'Mapisla', 'Mogao', 'Nalbuan', 'Poblacion', 'Subagan', 'Tumalip'
    ],
    # Luba
    [
        'Ampalioc', 'Barit', 'Gayaman', 'Lul-luno', 'Luzong',
        'Nagbukel-Tuquipa', 'Poblacion', 'Sabnangan'
    ],
    # Malibcong
    [
        'Bayabas', 'Binasaran', 'Buanao', 'Dulao', 'Duldulao', 'Gacab',
        'Lat-ey', 'Malibcong (Pob.)', 'Mataragan', 'Pacgued', 'Taripan',
        'Umnap'
    ],
    # Manabo
    [
        'Catacdegan Viejo', 'Luzong', 'Ayyeng(Pob.)', 'San Jose Norte',
        'San Jose Sur', 'San Juan Norte', 'San Juan Sur', 'San Ramon East',
        'San Ramon West', 'Santo Tomas', 'Catacdegan Nuevo'
    ],
    # Peñarrubia
    [
        'Dumayco', 'Lusuac', 'Namarabar', 'Patiao', 'Malamsit (Pau-Malamsit)',
        'Poblacion', 'Riang (Tiang)', 'Santa Rosa', 'Tattawa'
    ],
    # Pidigan
    [
        'Alinaya', 'Arab', 'Garreta', 'Immuli', 'Laskig', 'Naguirayan',
        'Monggoc', 'Pamutic', 'Pangtud', 'Poblacion East', 'Poblacion West',
        'San Diego', 'Sulbec', 'Suyo (Malidong)', 'Yuyeng'
    ],
    # Pilar
    [
        'Bolbolo', 'Brookside', 'Ocup', 'Dalit', 'Dintan', 'Gapang',
        'Kinabiti', 'Maliplipit', 'Nagcanasan', 'Nanangduan', 'Narnara',
        'Pang-ot', 'Patad', 'Poblacion', 'San Juan East', 'San Juan West',
        'South Balioag', 'Tikitik', 'Villavieja'
    ],
    # Sallapadan
    [
        'Bazar', 'Bilabila', 'Gangal (Pob.)', 'Maguyepyep', 'Naguilian',
        'Saccaang', 'Sallapadan', 'Subusob', 'Ud-udiao'
    ],
    # San Isidro
    [
        'Cabayogan', 'Dalimag', 'Langbaban', 'Manayday', 'Pantoc', 'Poblacion',
        'Sabtan-olo', 'San Marcial', 'Tangbao'
    ],
    # San Juan
    [
        'Abualan', 'Ba-ug', 'Badas', 'Cabcaborao', 'Colabaoan', 'Culiong',
        'Daoidao', 'Guimba', 'Lam-ag', 'Lumobang', 'Nangobongan', 'Pattaoig',
        'Poblacion North', 'Poblacion South', 'Quidaoen', 'Sabangan', 'Silet',
        'Supi-il', 'Tagaytay'
    ],
    # San Quintin
    ['Labaan', 'Palang', 'Pantoc', 'Poblacion', 'Tangadan', 'Villa Mercedes'],
    # Tayum
    [
        'Bagalay', 'Basbasa', 'Budac', 'Bumagcat', 'Cabaroan', 'Deet',
        'Gaddani', 'Patucannay', 'Pias', 'Poblacion', 'Velasco'
    ],
    # Tineg
    [
        'Poblacion (Agsimao)', 'Alaoa', 'Anayan', 'Apao', 'Belaat',
        'Caganayan', 'Cogon', 'Lanec', 'Lapat-Balantay', 'Naglibacan'
    ],
    # Tubo
    [
        'Alangtin', 'Amtuagan', 'Dilong', 'Kili', 'Poblacion (Mayabo)', 'Supo',
        'Tiempo', 'Tubtuba', 'Wayangan', 'Tabacda'
    ],
    # Villaviciosa
    [
        'Ap-apaya', 'Bol-lilising', 'Cal-lao', 'Lap-lapog', 'Lumaba',
        'Poblacion', 'Tamac', 'Tuquib'
    ]
]
""" re-structuring a file and formatting the string

txt_file.write('\n   ')
# add 3 spaces as a replacement for tab

txt_file.write('\n      ')
# add 6 spaces as a replacement for double tab

"""

# get the list data to process
obj = barangays

belongs_to_model = 'municipality'

# create/open a file if not exist, if exist overwrite
txt_file = open('formatted.txt', 'w+')

# write the symbol for opening tag
txt_file.write('[')

for parent_obj in obj:

    # write the symbol for opening tag
    txt_file.write('\n')
    txt_file.write('   ')
    txt_file.write('{')
    txt_file.write('\n')

    txt_file.write('      ')
    txt_file.write('\'code\'')
    txt_file.write(': ')

    txt_file.write('\'' + belongs_to_model + '\'')
    txt_file.write(',')
    txt_file.write('\n')

    txt_file.write('      ')
    txt_file.write('\'' + belongs_to_model + '\'')

    # add the separator for json structure
    txt_file.write(': ')

    # write the symbol for opening tag
    txt_file.write('[')
    txt_file.write('\n')

    # format each string in a file
    for each_obj in parent_obj:
        # re format the object characters
        # convert the object string to lower case
        result = each_obj.lower()
        # replace each whitespace by underscore "_"
        result = result.replace(' ', '_')
        # remove any non alpha numeric character
        result = result.replace('-', '_')

        txt_file.write('\n\t')
        # write the symbol for opening tag
        txt_file.write('{')

        txt_file.write('\n\t   ')
        # format the file to have quotation for json key
        txt_file.write('\'' + 'name' + '\'')

        # add the separator for json structure
        txt_file.write(': ')

        # format the file to have quotation for json value
        txt_file.write('\'' + each_obj + '\'')

        # add comma character for each string
        txt_file.write(',')

        txt_file.write('\n\t   ')
        # format the file to have quotation for json key
        txt_file.write('\'' + 'code' + '\'')

        # add the separator for json structure
        txt_file.write(': ')

        # format the file to have quotation for json value
        txt_file.write('\'' + result + '\'')

        txt_file.write('\n\t')
        # write the symbol for closing tag
        txt_file.write('}')

        # add comma character for each string
        txt_file.write(',')

    # write the symbol for closing tag
    txt_file.write('\n      ')
    txt_file.write(']')

    # write the symbol for closing tag
    txt_file.write('\n   ')
    txt_file.write('}')
    txt_file.write(',')

# write the symbol for closing tag
txt_file.write('\n')
txt_file.write(']')

# close the file
txt_file.close()

# [
#     {
#         'code': '',
#         'provinces': [
#             {
#                 'code': '',
#                 'name':
#             }
#         ]
#     },
#     {
#         'code': '',
#         'provinces': [
#             {
#                 'code': '',
#                 'name':
#             }
#         ]
#     }
# ]