#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#modifica index y xquery
import tensorflow as tf
import numpy as np


dic_workclass = {

    "Private": 0,
    "Self-emp-not-inc": 1,
    'Self-emp-inc': 2,
    "Federal-gov": 3,
    "Local-gov": 4,
    "State-gov": 5,
    "Without-pay": 6,
    "Never-worked": 7,
    "?": -1

}

dic_education = {

    "Bachelors": 0,
    "Some-college": 1,
    "11th": 2,
    "HS-grad": 3,
    "Prof-school": 4,
    "Assoc-acdm": 5,
    "Assoc-voc": 6,
    "9th": 7,
    "7th-8th": 8,
    "12th": 9,
    "Masters": 10,
    "1st-4th": 11,
    "10th": 12,
    "Doctorate": 13,
    "5th-6th": 14,
    "Preschool": 15,
    "?": -1

}

dic_marital_status = {

    "Married-civ-spouse": 0,
    "Divorced": 1,
    "Never-married": 2,
    "Separated": 3,
    "Widowed": 4,
    "Married-spouse-absent": 5,
    "Married-AF-spouse": 6,
    "?": -1

}

dic_occupation = {

    "Tech-support": 0,
    "Craft-repair": 1,
    "Other-service": 2,
    "Sales": 3,
    "Exec-managerial": 4,
    "Prof-specialty": 5,
    "Handlers-cleaners": 6,
    "Machine-op-inspct": 7,
    "Adm-clerical": 8,
    "Farming-fishing": 9,
    "Transport-moving": 10,
    "Priv-house-serv": 11,
    "Protective-serv": 12,
    "Armed-Forces": 13,
    "?": -1

}

dic_relationship = {

    "Wife": 0,
    "Own-child": 1,
    "Husband": 2,
    "Not-in-family": 3,
    "Other-relative": 4,
    "Unmarried": 5,
    "?": -1

}

dic_race = {

    'White': 0,
    "Asian-Pac-Islander": 1,
    "Amer-Indian-Eskimo": 2,
    "Other": 3,
    "Black": 4,
    "?": -1

}

dic_sex = {

    "Female": 0,
    "Male": 1,
    "?": -1

}

dic_native_country = {

    "United-States": 0,
    "Cambodia": 1,
    "England": 2,
    "Puerto-Rico": 3,
    "Canada": 4,
    "Germany": 5,
    "Outlying-US(Guam-USVI-etc)": 6,
    "India": 7,
    "Japan": 8,
    "Greece": 9,
    "South": 10,
    "China": 11,
    "Cuba": 12,
    "Iran": 13,
    "Honduras": 14,
    "Philippines": 15,
    "Italy": 16,
    "Poland": 17,
    "Jamaica": 18,
    "Vietnam": 19,
    "Mexico": 20,
    "Portugal": 21,
    "Ireland": 22,
    "France": 23,
    "Dominican-Republic": 24,
    "Laos": 25,
    "Ecuador": 26,
    "Taiwan": 27,
    "Haiti": 28,
    "Columbia": 29,
    "Hungary": 30,
    "Guatemala": 31,
    "Nicaragua": 32,
    "Scotland": 33,
    "Thailand": 34,
    "Yugoslavia": 35,
    "El-Salvador": 36,
    "Trinadad&Tobago": 37,
    "Peru": 38,
    "Hong": 39,
    "Holand-Netherlands": 40,
    "?": -1

}


dic_50 = {
    "<=50K\n": 0, "<=50K.\n":0, "<=50K":0,"<=50K.":0,
    ">50K\n": 1,">50K.\n":1, ">50K":1,">50K.":1,
    "?": -1
}

print('Ingrese el número asociado al atributo que quiere predecir:')
j = 0
for i in ('edad', 'tipo de trabajo', 'nivel de educación', 'grado de educación','estatus marital', 
'ocupación', 'situación sentimental', 'raza', 'sexo', 'ganancias de capital','pérdidas de capital', 
'horas de trabajo semanal', 'país de origen', 'gana más o menos de $$50K'):
    print("\t"+str(j)+":\t"+i) 
    j = j + 1
del j
index = int(input())

modelPath = 'modelos/modelo{}'.format(index)
model = tf.keras.models.load_model(modelPath)

print('Ingrese una lista con los valores de los otros atributos')
"""
x_query = input()
x_query = x_query[1:len(x_query)-1]
x_query = x_query.split(',')
x_query = [int(i) for i in x_query]
print(x_query)
"""
i = input()
i = i.split(', ')
i[1] = dic_workclass[i[1]]
i[3] = dic_education[i[3]]
i[5] = dic_marital_status[i[5]]
i[6] = dic_occupation[i[6]]
i[7] = dic_relationship[i[7]]
i[8] = dic_race[i[8]]
i[9] = dic_sex[i[9]]
i[13] = dic_native_country[i[13]]
i[14] = dic_50[i[14]]
del i[2]
del i[index]
i = [int(j) for j in i]
x_query = i

meanstdFile = open(modelPath+"/mean_std.txt", "r")
x_mean = float(meanstdFile.readline())
x_std = float(meanstdFile.readline())
meanstdFile.close()

epsilon = 1e-10

x_test = []
for i in range(13):
	x_query[i] = (x_query[i] - x_mean)/(x_std + epsilon)
x_test.append(x_query)

model.summary()
pred1 = model.predict(x_test)
pred = np.argmax( pred1[0])
pred = pred - 1
print(pred1)
listaDics = [0, dic_workclass, dic_education, 0, dic_marital_status, dic_occupation, dic_relationship, dic_race, dic_sex, 0, 0, 0, dic_native_country, dic_50]
if index in  (1, 2, 4, 5, 6, 7, 8, 12, 13):
    d= listaDics[index]
    for k in d.keys():
        if pred == d[k]:
            pred = k
print('predicción: '+str(pred))
respQuery = open('respQuery.txt','w')
respQuery.write('predicción: '+str(pred))
respQuery.close()
