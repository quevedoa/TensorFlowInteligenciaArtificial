#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# =============== PROCESA DATOS

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
    "<=50K\n": 0, "<=50K.\n":0,
    ">50K\n": 1,">50K.\n":1,
    "?": -1
}

import csv
arr = []

readfile = open('datos/adult_data.txt', "r")

for line in readfile:
    Type = line.split(", ")
    arr.append(Type)

arr = arr[:len(arr)-1]
for i in arr:
	i[1] = dic_workclass[i[1]]
	i[3] = dic_education[i[3]]
	i[5] = dic_marital_status[i[5]]
	i[6] = dic_occupation[i[6]]
	i[7] = dic_relationship[i[7]]
	i[8] = dic_race[i[8]]
	i[9] = dic_sex[i[9]]
	i[13] = dic_native_country[i[13]]
	i[14] = dic_50[i[14]]

for i in arr:
    del i[2]

arr = [list(map(int,i)) for i in arr]



# Conjunto de prueba
arr_pruebas = []

readfile = open('datos/adult_test.txt', "r")

for line in readfile:
	Type = line.split(", ")
	arr_pruebas.append(Type)

arr_pruebas = arr_pruebas[0:len(arr_pruebas)-1]

for i in arr_pruebas:
	i[1] = dic_workclass[i[1]]
	i[3] = dic_education[i[3]]
	i[5] = dic_marital_status[i[5]]
	i[6] = dic_occupation[i[6]]
	i[7] = dic_relationship[i[7]]
	i[8] = dic_race[i[8]]
	i[9] = dic_sex[i[9]]
	i[13] = dic_native_country[i[13]]
	i[14] = dic_50[i[14]]

for i in arr_pruebas:
    del i[2]

arr_pruebas = [list(map(int,i)) for i in arr_pruebas]

# atributo que se desea clasificar (0-13)
accuracies = []
for n in range(14):
	x_train= [e.copy() for e in arr]
	x_test = [e.copy() for e in arr_pruebas]
	
	y_train = [i[n] for i in arr]
	for i in x_train:
		del i[n]

	y_test = [i[n] for i in arr_pruebas]
	for i in x_test:
		del i[n]
	num_categorias = np.max(y_train) +2
	
	#=========== 
		#==== les sumo uno para que el -1 sea la primera categoría
	# asociada a la casilla 0
	#print(y_train)
	for i in range(len(y_train)):
		y_train[i] = y_train[i] + 1
	for i in range(len(y_test)):
		y_test[i] = y_test[i] + 1
	print(y_test)

	#========= convertir a onehot 
	from tensorflow.keras.utils import to_categorical
	y_train_encoded = to_categorical(y_train, num_classes = num_categorias)
	y_test_encoded = to_categorical(y_test, num_classes = num_categorias)
	
	#======= normalizar datos
	x_mean = np.mean(x_train)
	x_std = np.std(x_train)
	epsilon = 1e-10

	x_train_norm = (x_train - x_mean)/(x_std + epsilon)
	x_test_norm = (x_test - x_mean)/(x_std + epsilon)


	#crear el modelo
	#all layers will be dense
	from tensorflow.keras.models import Sequential
	from tensorflow.keras.layers import Dense

	model = Sequential([
    Dense(128, activation = 'relu', input_shape=(len(x_train_norm[0]),)),
    Dense(200, activation = 'relu'),
    Dense(num_categorias, activation = 'softmax')
	])

	#compilar el modelo
	model.compile(
	optimizer = 'sgd',
	loss = 'categorical_crossentropy',
    	metrics=['accuracy']
	)
	model.summary()

	#entrenarlo
	#epochs is the number of times each train example is going to be iterated
	model.fit(x_train_norm, y_train_encoded,epochs = 3)

	#evaluarlo
	loss, accuracy = model.evaluate(x_test_norm, y_test_encoded)
	print('Test set accuracy:', accuracy*100)
	accuracies.append(accuracy*100)

	model_path = "modelos/modelo{}".format(n)
	model.save(model_path)

	meanStdFile = open(model_path+"/mean_std.txt", "w")
	meanStdFile.write(str(x_mean)+"\n")
	meanStdFile.write(str(x_std))
	meanStdFile.close()
	
	accFile = open(model_path+"/accuracy.txt", "w")
	accFile.write(str(accuracy))
	accFile.close()
generalAccuracy = open("modelos/accuracies.txt", "w")
for i in accuracies:
	generalAccuracy.write(str(i)+"\n")
generalAccuracy.close()
