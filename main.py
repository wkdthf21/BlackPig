from classifier.AbuseClassifier import AbuseClassifier
from sendmail.sendmail import send_warning

clif = AbuseClassifier('model_path', 'lb_path')
result = clif.isAbusedChild('video_path')

send_warning("rlaehdwn1026@gmail.com", "YOUR PASSWORD",  "tyg04308@naver.com", result)

print ("Finish")
