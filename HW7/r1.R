df <- read.csv('C:\\Users\\АЛЕНА\\Desktop\\GitHubFiles\\PythonWoks\\HW7\\mlbootcamp5_train.csv', sep =';')
head(df)

#Сколько мужчин и женщин представлено в этом наборе данных? 
table(df$gender)

#Кто в среднем реже указывает, что употребляет алкоголь – мужчины или женщины?
mean(df[df['gender'] == 1, 'alco'])
mean(df[df['gender'] == 2, 'alco'])

#Во сколько раз(округленно)процент курящих мужчин больше, чем процент курящих женщин?
round((mean(df[df['gender'] == 1, 'smoke'])*100)/(mean(df[df['gender'] == 2, 'smoke'])))

#На сколько месяцев отличаются медианные значения возраста курящих и некурящих?
(median(df[df['smoke'] == 0, 'age']) - median(df[df['smoke'] == 1, 'age']))/30

#Создайте новый признак age_years – возраст в годах, округлив до целых (round).

#Интересуют 2 подвыборки курящих мужчин возраста от 60 до 64 лет включительно: 
#первая с ap_hi строго меньше 120 мм рт.ст. и холестерином – 4 ммоль/л, а вторая –
#с ap_hi от 160 (включительно) до 180 мм рт.ст. (не включительно) и холестерином – 8 ммоль/л.
#Во сколько раз отличаются доли больных людей в этих двух подвыборках?
age_years <- round(df$age/365)
df <- cbind(df, age_years)
df2 <- subset(df, smoke == 1 & gender == 2 & age_years >= 60 & age_years <= 64)
gr1 <- subset(df2, ap_hi < 120)
gr2 <- subset(df2, ap_hi >= 160 & ap_hi < 180)
round(mean(gr2[gr2['cholesterol'] == 3, 'cardio'])/ mean(gr1[gr1['cholesterol'] == 1, 'cardio']))

#Постройте новый признак – BMI (Body Mass Index).

#Медианный BMI по выборке превышает норму?
bmi <- df$weight/(df$height/100)^2
df <- cbind(df, bmi)
median(df['bmi'])

#У женщин в среднем BMI ниже, чем у мужчин?
mean(df[df['gender'] == 1, 'bmi'])
mean(df[df['gender'] == 2, 'bmi'])

#У здоровых в среднем BMI выше, чем у больных?
mean(df[df['cardio'] == 1, 'bmi'])
mean(df[df['cardio'] == 0, 'bmi'])

#В сегменте здоровых и непьющих мужчин в среднем BMI ближе к норме, 
#чем в сегменте здоровых и непьющих женщин?
healthy <-  subset(df, cardio == 0 & alco == 0)
mean(healthy[healthy['gender'] == 1, 'bmi'])
mean(healthy[healthy['gender'] == 2, 'bmi'])

#Отфильтруйте следующие сегменты пациентов (считаем это ошибками в данных)
#Сколько процентов данных (округленно, round) мы выбросили?
filtered_df <- subset(df, ap_hi < ap_lo | height < quantile(df$height, 0.025) |
height > quantile(df$height, 0.975) | weight < quantile(df$weight, 0.025) |
weight > quantile(df$weight, 0.975))
round(length(filtered_df)/length(df)*10)