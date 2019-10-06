import classifier.AbuseClassifier as aClif

clif = aClif.AbuseClassifier('sports_model/sports.model', 'sports_model/lb.pickle')
result = clif.isAbusedChild('input/boxing1.mp4')

print ('----------result-----------')
print (result)
