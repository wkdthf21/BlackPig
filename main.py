import classifier.AbuseClassifier as aClif

clif = aClif('sports_model/sports.model', 'sports_model/lb.pickle')
result = clif.isAbuse('input/boxing1.mp4')

print ('----------result-----------')
print (result)
