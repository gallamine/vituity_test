Recruit Sample Problem

Background - You have been handed a dataset from your hospital.  Below are the column descriptions.

PatientIdentifier 	unique patient id
bhr					basal heart rate
basebp				basal blood pressure
basedp				basal double product (= bhr x basebp)
pkhr				peak heart rate
sbp					systolic blood pressure
dp					double product (= pkhr x sbp)
maxhr				maximum heart rate
pctMphr  			% of maximum predicted heart rate achieved
mbp					maximum blood pressure
age					age
gender				gender
ecg					echocardiogram was positive
baseef				baseline cardiac ejection fraction (a measure of the heart's pumping efficiency)
chestpain			experienced chest pain
restwma				cardiologist sees wall motion anomoly on echocardiogram 
posse				stress echocardiogram was positive 
hxofht				patient history of hypertension 
hxofdm				patient history of diabetes 
hxofcig				patient history of smoking 
hxofmi				patient history of heart attack 
hxofptca			patient history of angioplasty 
hxofcabg			patient history of bypass surgery 
any.event			Outcome variable, defined as "death or newmi or newptca or newcabg".  If any of these variables is positive then "any.event" is also positive
death				Outcome variable, patient dies after Encounter 
newmi				Outcome variable, new myocardial infarction, or heart attack 
newptca				Outcome variable, recent angioplasty 
newcabg				Outcome variable, recent bypass surgery

Problem statement - Your goal is to build a model to estimate the likelihood a given patient will have a bad outcome in the future (any.event = 1).  

Reporting - We would like you to prepare a 5-7 minute presentation on your findings.  

