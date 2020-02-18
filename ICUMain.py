import logging
from Learning import Learning
from GeneticSpec.GeneticPopulation import GeneticPopulation


#make learning object
variables = ['LOS', 'ICU_Pt_Days', 'Mort', 'n_evts', 'tte', 'death', 'direct', 'MET',
       'Sgy', 'GlasgowComaScaleTotal', 'O2Flow', 'Resp', 'SpO2', 'SBP',
       'Pulse', 'Temp', 'ALBUMIN', 'ALKALINE_PHOSPHATASE', 'ALT_GPT',
       'AST_GOT', 'BLOOD_UREA_NITROGEN', 'CALCIUM', 'CHLORIDE', 'CO2',
       'CREATININE', 'GLUCOSE', 'HEMOGLOBIN', 'LACTIC_ACID', 'MAGNESIUM',
       'OXYGEN_SATURATION', 'PARTIAL_THROMBOPLASTIN_TIME', 'PCO2',
       'PHOSPHORUS', 'PLATELET_COUNT', 'POTASSIUM', 'PROTIME_INR', 'SODIUM',
       'TOTAL_BILIRUBIN', 'TOTAL_PROTEIN', 'TROPONIN_I',
       'WHITE_BLOODCELL_COUNT', 'hr', 's2hr', 's8hr', 's24hr', 'n_edrk',
       'edrk', 's2edrk', 's8edrk', 's24edrk', 'srr', 'dfa', 'cosen', 'lds',
       'af', 'AF']

lower = [ 0.00000000e+00,  0.00000000e+00,  0.00000000e+00,  0.00000000e+00,
       -5.03298611e+01,  0.00000000e+00,  0.00000000e+00,  0.00000000e+00,
        0.00000000e+00,  1.00000000e+01,  0.00000000e+00,  0.00000000e+00,
        8.50000000e+01,  0.00000000e+00,  0.00000000e+00,  3.50000000e+01,
        1.30000000e+00,  1.90000000e+01,  6.00000000e+00,  6.00000000e+00,
        2.00000000e+00,  4.80000000e+00,  8.30000000e+01,  7.00000000e+00,
        3.00000000e-01,  4.90000000e+01,  2.20000000e+00,  2.00000000e-01,
        7.00000000e-01,  7.90000000e+01,  2.00000000e+01,  1.65000000e+01,
        9.00000000e-01,  1.00000000e+01,  1.90000000e+00,  8.00000000e-01,
        1.19000000e+02,  1.00000000e-01,  3.60000000e+00,  2.00000000e-02,
        1.20000000e-01,  3.00000000e+01, -7.62808303e-02, -7.62808303e-02,
       -7.62808303e-02,  0.00000000e+00,  4.68750236e+00, -1.90728029e-02,
       -1.90728029e-02, -1.90728029e-02,  1.06648029e-03, -9.69343118e-01,
       -3.23661607e+00,  0.00000000e+00,  0.00000000e+00,  0.00000000e+00] #lowerbound

upper = [1.22000000e+02, 1.04000000e+02, 1.00000000e+00, 4.00000000e+00,
       8.77861111e+01, 1.00000000e+00, 1.00000000e+00, 1.00000000e+00,
       1.00000000e+00, 1.50000000e+01, 7.00000000e+00, 4.90000000e+01,
       1.00000000e+02, 2.60000000e+02, 3.82000000e+02, 4.05000000e+01,
       5.00000000e+00, 3.86000000e+02, 3.56000000e+02, 2.42000000e+02,
       1.11000000e+02, 1.10000000e+01, 1.32000000e+02, 4.00000000e+01,
       1.00000000e+01, 4.60000000e+02, 2.02000000e+01, 3.40000000e+00,
       3.40000000e+00, 9.98000000e+01, 1.40000000e+02, 6.76000000e+01,
       8.00000000e+00, 6.62000000e+02, 8.30000000e+00, 5.00000000e+00,
       1.51000000e+02, 9.00000000e+00, 9.70000000e+00, 2.35000000e+01,
       2.60000000e+01, 3.00000000e+02, 6.86283741e-02, 6.86283741e-02,
       6.86283741e-02, 1.00000000e+00, 5.43110090e+01, 1.69365926e-02,
       1.69365926e-02, 1.69365926e-02, 6.05001092e-01, 2.22452357e+00,
       8.51720869e-01, 4.49814800e+00, 1.00000000e+00, 1.00000000e+00] # upperbound

l = Learning(logging.INFO, "Data/ICUData/133.txt", "Data/ICUData/133labels.txt", "Data/ICUData/time.txt", variables, lower, upper)


#start learning
generation = l.run()

#save rules and scores to file
ruleScores = generation.finalFormulaScoresToString(100)
with open("1ruleScores.txt", 'w') as filehandle:
    for r in ruleScores:
        filehandle.write('%s\n' % r)

#save rules themselves
rules = generation.finalFormulasToString(100)

with open("1rules.txt", 'w') as filehandle:
    for r in rules:
        filehandle.write('%s\n' % r)



#Patient IDs who have both true and false y vals
trueList = [133, 187, 206, 282, 295, 307, 348, 414, 427, 461, 488, 498, 558, 586, 611, 624, 627, 648, 752, 782, 785, 791, 793, 806, 808, 833, 853, 854, 872, 910, 918, 948, 951, 958, 1007, 1047, 1152, 1180, 1219, 1243, 1308, 1314, 1318, 1320, 1367, 1411, 1447, 1508, 1541, 1593, 1612, 1654, 1671, 1683, 1709, 1710, 1779, 1801, 1818, 1826, 1830, 1838, 1894, 1901, 1913, 1916, 1922, 1936, 1984, 2005, 2009, 2024, 2040, 2047, 2084, 2131, 2132, 2168, 2201, 2256, 2282, 2284, 2321, 2336, 2342, 2355, 2456, 2489, 2525, 2555, 2558, 2618, 2647, 2650, 2703, 2709, 2738, 2748, 2751, 2806, 2817, 2827, 2840, 2856, 2857, 2894, 2905, 2914, 2923, 2928, 2981, 2995, 2996, 3001, 3040, 3053, 3066, 3091, 3139, 3157, 3196, 3198, 3248, 3261, 3293, 3307, 3310, 3326, 3354, 3358, 3360, 3447, 3466, 3473, 3483, 3505, 3511, 3531, 3544, 3590, 3598, 3664, 3667, 3706, 3714, 3719, 3745, 3750, 3760, 3804, 3895, 3906, 3960, 3970, 3973, 3986, 4034, 4045, 4067, 4071, 4082, 4110, 4125, 4128, 4138, 4174, 4183, 4189, 4227, 4234, 4257, 4291, 4306, 4318, 4320, 4325, 4336, 4347, 4351, 4418, 4475, 4489, 4512, 4529, 4534, 4546, 4573, 4682, 4749, 4771, 4788, 4791, 4796, 4804, 4824, 4858, 4869, 4905, 4925, 4972, 4984, 4985, 4986, 5010, 5042, 5043, 5044, 5072, 5093, 5101, 5145, 5174, 5217, 5239, 5270, 5285, 5298, 5379, 5408, 5416, 5431, 5460, 5492, 5549, 5552, 5563, 5565, 5587, 5594, 5596, 5600, 5618, 5646, 5659, 5671, 5702, 5731, 5740, 5754, 5762, 5810, 5878, 5886, 5889, 5909, 5920, 5929, 5942, 5959, 5976, 5997, 6008, 6027, 6044, 6063, 6070, 6075, 6087, 6132, 6168, 6190, 6191, 6208, 6211, 6217, 6297, 6332, 6347, 6379, 6433, 6444, 6445, 6448, 6457, 6458, 6459, 6463, 6513, 6516, 6540, 6572, 6583, 6618, 6626, 6636, 6656, 6683, 6699, 6723, 6740, 6746, 6757, 6797, 6841, 6849, 6866, 6888, 6893, 6912, 6930, 6940, 6964, 7019, 7029, 7071, 7077, 7078, 7089, 7130, 7145, 7189, 7199, 7217, 7222, 7224, 7283, 7291, 7306, 7316, 7392, 7393, 7434, 7459, 7500, 7516, 7530, 7618, 7631, 7646, 7662, 7692, 7695, 7710, 7712, 7723, 7726, 7746, 7771, 7816, 7822, 7850, 7868, 7911, 7923, 7941, 7964, 7969, 7984, 7993, 8024, 8035, 8046, 8056, 8058, 8059, 8060, 8066]