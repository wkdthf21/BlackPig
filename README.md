<h2>2019 Open SW Í∞úÎ∞ú???Ä??- ?ôÎ? Í∞êÏ? CCTV</h2>

<h4> 1. Import </h4>
'''python
from classifier.AbuseClassifier import AbuseClassifier
from sendmail.sendmail import send_warning
'''

<h4> 2. Useage </h4>
'''python
clif = AbuseClassifier('MODEL PATH', 'LB PATH')
abused_spicious_time = clif.isAbusedChild('VIDEO PATH')

if abused_spicious_time is not empty:
    send_warning("YOUR GMAIL ID", "YOUR GMAIL PW", "TO_EMAIL", abused_spicious_time)
'''