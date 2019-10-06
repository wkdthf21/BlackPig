from classifier.AbuseClassifier import AbuseClassifier
from sendmail.sendmail import send_warning

clif = AbuseClassifier('model_path', 'lb_path')
result = clif.isAbusedChild('video_path')

if send_warning("rlaehdwn1026@gmail.com", "YOUR PASSWORD",  "tyg04308@naver.com", result):
    print ("Send Successful!")
else:
    print ("Mail not Send!")

print ("Finish")
