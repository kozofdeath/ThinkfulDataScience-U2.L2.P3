import collections
import pandas as pd
from scipy import stats
import matplotlib.pyplot as plt

loansData = pd.read_csv('https://github.com/Thinkful-Ed/curric-data-001-data-sets/raw/master/loans/loansData.csv');
loansData.dropna(inplace=True)
freq = collections.Counter(loansData['Open.CREDIT.Lines']);
print freq;
print 'Number of unique entries: ', len(freq.keys())
print freq[2.0];

#this creates a figure
#call close when done if calling multiple figures to clear memory
#figure instance is returned and will be passed to new_figure_manager in the backends
plt.figure()

#the kwargs are plotted in x vs. y
plt.bar(freq.keys(), freq.values(), width=1)

#will display all figures when running in ipython
plt.show();

#calculates a one way chi square test; returns chi-squared test statistic and p value for this statistic
#if f_obs is just given, it assumed that the expected frquencies is equal to the mean of the observed frequencies
#in this example, this values are being compared to their mean value (assuming they all have the same mean)
#now the goodness of fit test is being applied to see if it is probable that this data distribution could result from a uniform population value
chi, p = stats.chisquare(freq.values())
print chi, p

#as p is less than our .05, we can reject that this distribution happened by chance
