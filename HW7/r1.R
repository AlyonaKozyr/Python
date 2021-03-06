df <- read.csv('C:\\Users\\�����\\Desktop\\GitHubFiles\\PythonWoks\\HW7\\mlbootcamp5_train.csv', sep =';')
head(df)

#������� ������ � ������ ������������ � ���� ������ ������? 
table(df$gender)

#��� � ������� ���� ���������, ��� ����������� �������� � ������� ��� �������?
mean(df[df['gender'] == 1, 'alco'])
mean(df[df['gender'] == 2, 'alco'])

#�� ������� ���(����������)������� ������� ������ ������, ��� ������� ������� ������?
round((mean(df[df['gender'] == 1, 'smoke'])*100)/(mean(df[df['gender'] == 2, 'smoke'])))

#�� ������� ������� ���������� ��������� �������� �������� ������� � ���������?
(median(df[df['smoke'] == 0, 'age']) - median(df[df['smoke'] == 1, 'age']))/30

#�������� ����� ������� age_years � ������� � �����, �������� �� ����� (round).

#���������� 2 ���������� ������� ������ �������� �� 60 �� 64 ��� ������������: 
#������ � ap_hi ������ ������ 120 �� ��.��. � ������������ � 4 �����/�, � ������ �
#� ap_hi �� 160 (������������) �� 180 �� ��.��. (�� ������������) � ������������ � 8 �����/�.
#�� ������� ��� ���������� ���� ������� ����� � ���� ���� �����������?
age_years <- round(df$age/365)
df <- cbind(df, age_years)
df2 <- subset(df, smoke == 1 & gender == 2 & age_years >= 60 & age_years <= 64)
gr1 <- subset(df2, ap_hi < 120)
gr2 <- subset(df2, ap_hi >= 160 & ap_hi < 180)
round(mean(gr2[gr2['cholesterol'] == 3, 'cardio'])/ mean(gr1[gr1['cholesterol'] == 1, 'cardio']))

#��������� ����� ������� � BMI (Body Mass Index).

#��������� BMI �� ������� ��������� �����?
bmi <- df$weight/(df$height/100)^2
df <- cbind(df, bmi)
median(df['bmi'])

#� ������ � ������� BMI ����, ��� � ������?
mean(df[df['gender'] == 1, 'bmi'])
mean(df[df['gender'] == 2, 'bmi'])

#� �������� � ������� BMI ����, ��� � �������?
mean(df[df['cardio'] == 1, 'bmi'])
mean(df[df['cardio'] == 0, 'bmi'])

#� �������� �������� � �������� ������ � ������� BMI ����� � �����, 
#��� � �������� �������� � �������� ������?
healthy <-  subset(df, cardio == 0 & alco == 0)
mean(healthy[healthy['gender'] == 1, 'bmi'])
mean(healthy[healthy['gender'] == 2, 'bmi'])

#������������ ��������� �������� ��������� (������� ��� �������� � ������)
#������� ��������� ������ (����������, round) �� ���������?
filtered_df <- subset(df, ap_hi < ap_lo | height < quantile(df$height, 0.025) |
height > quantile(df$height, 0.975) | weight < quantile(df$weight, 0.025) |
weight > quantile(df$weight, 0.975))
round(length(filtered_df)/length(df)*10)