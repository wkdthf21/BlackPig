<h2>2019 Open SW 개발자 대회 - 학대 감지 CCTV</h2>

<h4> 1. Import </h4>
<pre>
from classifier.AbuseClassifier import AbuseClassifier
from sendmail.sendmail import send_warning
</pre>

<h4> 2. Useage </h4>
<pre>
clif = AbuseClassifier('MODEL PATH', 'LB PATH')
abused_spicious_time = clif.isAbusedChild('VIDEO PATH')

if abused_spicious_time is not empty:
    send_warning("YOUR GMAIL ID", "YOUR GMAIL PW", "TO_EMAIL", abused_spicious_time)
</pre>

