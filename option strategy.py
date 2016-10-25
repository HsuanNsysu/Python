import numpy as np
k=9300
premium_call=159
premium_put=82
Interval=500
St=np.arange(k-Interval,k+Interval)


payoff_longcall=np.maximum(St-k,0)-premium_call
payoff_longput=np.maximum(k-St,0)-premium_put
payoff_strategy=payoff_longcall+payoff_longput
zeroline=St-St
kpoint=k-k

import matplotlib.pyplot as pic
pic.plot(St,payoff_longcall,'c--',label='lon call')
pic.plot(St,payoff_longput,'y--',label='long put')
pic.plot(St,payoff_strategy,'r',linewidth=3,label='profit')
pic.plot(St,zeroline,'--')
pic.xlabel("St")
pic.ylabel("payoff")
pic.title("Option Strategy : long straddle")
pic.legend(bbox_to_anchor=(1,1.025),loc='upper left',shadow=True,fancybox=True)
pic.plot([9300],[-241],'ko')
pic.plot([9300],[0],'ko')
pic.text(9450,-200,'max loss=-241',fontsize=13)
pic.text(9300,25,'K',fontsize=15)
