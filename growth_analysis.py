'''
Day 10 — Ultimate Freelance Mini-Project

Scenario:

You are a freelance growth analyst for a SaaS company. You have 4 matrices representing 6 products over 4 weeks:

website_visits → daily visits per product

ad_spend → advertising spend per product

signups → number of signups per product

cancellations → number of cancellations per product

Steps:

Generate random integers:

website_visits: 500–5000

ad_spend: 1000–10000

signups: 50–500

cancellations: 0–50

Normalize all matrices column-wise

Compute NetGrowthScore = (signups - cancellations) * website_visits / ad_spend (broadcasting)

Compute WeightedScore = NetGrowthScore * normalized signups

Identify top 25% products and bottom 25% products using percentiles → mark 1 and 0, -1 otherwise

Compute:

Row-wise total score → overall product performance

Column-wise average → weekly performance trend

Maximum and minimum scores in the final matrix

Print products that consistently perform above the average score

'''
import numpy as np
#Decalaration of matrices
rng=np.random.default_rng()
website_visits=rng.integers(500,5000,size=(6,4))
ad_spend=rng.integers(1000,10000,size=(6,4))
signups=rng.integers(50,500,size=(6,4))
cancellations=rng.integers(0,50,size=(6,4))

#Normalizing all matrices

def NormalizeColumnWise(mat):
    denominator=np.max(mat,axis=0)-np.min(mat,axis=0)
    denominator[denominator==0]=1
    return (mat-np.min(mat,axis=0)[None,:])/(denominator)[None,:]

Normalize_wv=NormalizeColumnWise(website_visits)
Normalize_as=NormalizeColumnWise(ad_spend)
Normalize_su=NormalizeColumnWise(signups)
Normalize_cc=NormalizeColumnWise(cancellations)

#Printing all matrices
print(f"{''*50} ALL MATRICES ")
print(f"{' '*50}WebsiteVisits \n {website_visits} ")
print(f"{' '*50}ad spend \n {ad_spend} ")
print(f"{' '*50}signups \n {signups} ")
print(f"{' '*50}cancellations \n {cancellations} ")
#NORMALIZE MATRICES
print('='*100)
print(f'{'='*30}NORMALIZE MATRICES {'='*30}')
print(f"{' '*50}WebsiteVisits \n {Normalize_wv} ")
print(f"{' '*50}ad spend \n {Normalize_as} ")
print(f"{' '*50}signups \n {Normalize_su} ")
print(f"{' '*50}cancellations \n {Normalize_cc} ")


#NETGROWTHSCORE
NETGROWTHSCORE=(signups-cancellations)*(website_visits/ad_spend)

print(f'{'='*30}NETGROWTHSCORE MATRICES {'='*30}')
print(f"{' '*50}NETGROWTHSCORE \n {NETGROWTHSCORE} ")

#WeightedScore
WeightedScore=NETGROWTHSCORE*Normalize_su
print(f'{'='*30}WeightedScore MATRICES {'='*30}')
print(f"{' '*50}WeightedScore \n {WeightedScore} ")

#top 25% and bottom 25%
flag=np.full((6,4),-1)
top=np.percentile(WeightedScore,75,axis=1) # value from which 75% is less
bottom=np.percentile(WeightedScore,25,axis=1) # value from which 20% is less
flag[WeightedScore>=top[:,None]]=1 #mark value 1 which is higher than or equal to the value who has 75% lower than it 
flag[WeightedScore<=bottom[:,None]]=0 #mark value 0 which is lower than or equal to the value who has 20%  lower than it
print(f'{'='*30} top and bottom Products {'='*30}')
print(f"{' '*50}Top and Bottom \n {flag} ")

#Row wise Total Score
print('='*100)
print(f' {''*50} Product overall Performance')
print(f" {np.sum(WeightedScore,axis=1)}")
#Column-wise average → weekly performance trend
print('='*100)
print(f' {''*50} Product overall Performance')
print(f" {np.mean(WeightedScore,axis=0)}")

#Maximum and minimum scores in the final matrix

print('='*100)
print(f' {''*50} Max and Min Scores ')
print(f" Max: {np.max(WeightedScore)} , Min {np.min(WeightedScore)}")

#Print products that consistently perform above the average score

avgScore=np.mean(WeightedScore,axis=1)
print('='*100)
print(f' {''*50} Product above average')
print(f" {WeightedScore[WeightedScore>avgScore[:,None]]}")
