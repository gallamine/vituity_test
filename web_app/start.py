from flask import Flask
from flask import request, render_template, make_response
import gzip
import json
import pickle 
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.metrics import roc_auc_score
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import RandomizedSearchCV
from sklearn.decomposition import PCA
from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import chi2
from sklearn.metrics import classification_report

from sklearn.metrics import roc_curve
from sklearn.metrics import roc_auc_score
app = Flask(__name__)

def _predict_bad_event(features):
	with gzip.open('model.pkl.gzip', 'rb') as f:
		model = pickle.load(f)
	return list(model.predict_proba([features])[0])

@app.route("/predict")
def predict():

	chestpain = request.args.get('chestpain', default = 0.0, type = float)		# All checkboxes default to 0.0
	hxofCABG = request.args.get('hxofCABG', default = 0.0, type = float)
	mbp = request.args.get('mbp', default = 148.0, type = float)
	hxofMI = request.args.get('hxofMI', default = 0.0, type = float)
	hxofCig_non_smoker = request.args.get('hxofCig_non-smoker', default = 1.0, type = float)
	hxofPTCA = request.args.get('hxofPTCA', default = 0.0, type = float)
	age = request.args.get('age', default = 60.0, type = float)
	pctMphr = request.args.get('pctMphr', default = 73.0, type = float)
	hxofCig_heavy = request.args.get('hxofCig_heavy', default = 0.0, type = float)
	restwma = request.args.get('restwma', default = 0.0, type = float)
	hxofDM = request.args.get('hxofDM', default = 0.0, type = float)
	dobdose = request.args.get('dobdose', default = 20.0, type = float)
	hxofCig_moderate = request.args.get('hxofCig_moderate', default = 0.0, type = float)
	dpmaxdo = request.args.get('dpmaxdo', default = 17316.0, type = float)
	maxhr = request.args.get('maxhr', default = 117.0, type = float)
	sbp = request.args.get('sbp', default = 148.0, type = float)
	baseEF = request.args.get('baseEF', default = 64.0, type = float)
	pkhr = request.args.get('pkhr', default = 117.0, type = float)
	hxofHT = request.args.get('hxofHT', default = 0.0, type = float)
	basebp = request.args.get('basebp', default = 9792.0, type = float)
	posSE = request.args.get('posSE', default = 0.0, type = float)
	bhr = request.args.get('bhr', default = 72.0, type = float)

	gender = request.args.get('gender', default = "female")
	if gender == "female":
		gender_female = 1.0
		gender_male = 0.0
	else:

		gender_female = 0.0
		gender_male = 1.0

	hxoCig = request.args.get('hxoCig', default = "non-smoker")
	if hxoCig == "non-smoker":
		hxofCig_non_smoker = 1.0
		hxofCig_moderate = 0.0
		hxofCig_heavy = 0.0
	elif hxoCig == "moderate":
		hxofCig_non_smoker = 0.0
		hxofCig_moderate = 1.0
		hxofCig_heavy = 0.0
	elif hxoCig == "heavy":
		hxofCig_non_smoker = 0.0
		hxofCig_moderate = 0.0
		hxofCig_heavy = 1.0
	else:
		return "Invalid smoking value. Should be 'non-smoker','modeate',or'heavy'"

	ecg = request.args.get('ecg', default = "normal")
	if ecg == "normal":
		ecg_normal = 1.0
		ecg_equivocal  = 0.0	
		ecg_MI = 0.0	
	elif ecg == "equivocal":
		ecg_normal = 0.0
		ecg_equivocal  = 1.0	
		ecg_MI = 0.0
	elif ecg == "MI":
		ecg_normal = 0.0
		ecg_equivocal  = 0.0	
		ecg_MI = 1.0
	else:
		return "Invalid ECG value. Should be 'normal','equivocal', or 'MI'"		


	basedp = bhr * basebp
	dp = pkhr * sbp


	features = [chestpain, 
				hxofCABG, 
				mbp, 
				hxofMI, 
				gender_male, 
				hxofCig_non_smoker, 
				hxofPTCA,
				age, 
				dp, 
				pctMphr, 
				hxofCig_heavy,
				restwma, 
				ecg_equivocal, 
				hxofDM, 
				ecg_normal, 
				dobdose,
				hxofCig_moderate, 
				dpmaxdo,
				basebp, 
				maxhr,
				sbp,
				baseEF, 
				pkhr, 
				hxofHT, 
				ecg_MI, 
				basedp, 
				posSE, 
				bhr, 
				gender_female]

	print(f"Features: {features}")

	return f"{_predict_bad_event(features)[1]}"

@app.route("/")
def start():
	#width = request.args.get('width', default = 20, type = int)
	#height = request.args.get('height', default = 26, type = int)
	#difficulty = request.args.get('difficulty', default=1.0, type =float)

	return render_template('index.html')


