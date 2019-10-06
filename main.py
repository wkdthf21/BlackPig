#import classifier.AbuseClassifier as aClif
from sendmail.sendmail import send_warning

#clif = aClif.AbuseClassifier('sports_model/sports.model', 'sports_model/lb.pickle')
#result = clif.isAbusedChild('input/boxing1.mp4')

test = {1: [52752.70003, 54421.03333], 2: [59459.4, 64197.4666], 3: [79512.76666, 81781.7]}
send_warning("rlaehdwn1026@gmail.com", "YOUR PASSWORD",  "tyg04308@naver.com", test)

#print ('----------result-----------')
#print (result)
