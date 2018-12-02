import pandas as pd
import numpy as np

#=============== PARAMETERS AND ASSUMPTIONS ===============
#----------------------------------------------------------
#Assume XYZ Private Equity LLP purchases A.Target & Co for 5.0x FTM EBITDA at the end of Year 0
#The debt-to-equity ratio for the aquisition will be 60:40
#Assume avg interest on debt to be 10%
#ABS expects to reach $100m in sales revenue with EBITDA margin of 40% in Year 1
#Revenue is expected to increase 10% y-o-y
#EBITDA margins are expected to remain flat over the investment
#Capital expenditures are expected to be 15% of sales
#Operating working capital is expected to increase $5 million per year
#Depreciation is assumed to be $20 million per year
#Constant tax rate of 40% is assumed
#XYZ will exit after Year 5 at the same EBITDA multiple at entry (5.0x FTM EBITDA)
#Assume all debt paydown occurs at the moment of sale

#Function to print the income statement
def printIncomeStatement(salesRevenue,EBITDA,DandA,EBIT,interest,EBT,taxes,EBTta):
	try:
		#Create list of column labels and insert a row label at the start of each list
		labels = ['','Year 1','Year 2','Year 3','Year 4','Year 5','Year 6']
		row1 = ['Sales Revenue'] + salesRevenue
		row2 = ['EBITDA'] + EBITDA
		row3 = ['Less: D&A'] + DandA
		row4 = ['EBIT'] + EBIT
		row5 = ['Less: Interest'] + interest
		row6 = ['EBT'] + EBT
		row7 = ['Less: Tax'] + taxes
		row8 = ['EBT (Tax-Effected)'] + EBTta
		arr = np.array([labels,row1,row2,row3,row4,row5,row6,row7,row8])
		incomeStatement = pd.DataFrame(data=arr[1:,1:],index=arr[1:,0],columns=arr[0,1:])
		print('==================== INCOME STATEMENT ====================\n')
		print(incomeStatement)
	except Exception as e:
		print('Printing Income Statement:'+str(e))

def printFCFStatement(EBTta,DandA,CapEx,dNWC,FCF,cumFCF):
	try:
		labels = ['','Year 1','Year 2','Year 3','Year 4','Year 5','Year 6']
		rowA = ['EBT (Tax-Effected)'] + EBTta
		rowB = ['Plus: D&A'] + DandA
		rowC = ['Less: Capital Expenditures'] + CapEx + ['']
		rowD = ['Less: Increase in NWC'] + dNWC + ['']
		rowE = ['Free Cash Flow (FCF)'] + FCF + ['']
		rowF = ['Cumulative FCF'] + cumFCF + ['']
		arr = np.array([labels,rowA,rowB,rowC,rowD,rowE,rowF])
		FCFStatement = pd.DataFrame(data=arr[1:,1:],index=arr[1:,0],columns=arr[0,1:])
		print('==================== FCF STATEMENT ====================\n')
		print(FCFStatement)
	except Exception as e:
		print('Printing FCF Statement:'+str(e))

#Define the assumptions in variables
EBITDAx = 5.0 								#EBITDA multiple: 5.0x
debtFundingpc = 0.6							#debt-to-equity ratio: 60:40
equityFundingpc = 0.4
r = 0.1 									#interest rate: 10%
salesRevenue = []
salesRevenue.append(100) 					#add year 1 sales revenue: 100m
EBITDAmargin = 0.4 							#EBITDA margin: 40%
g = 0.1										#Growth rate of sales: 10%
DandA = [20]*6								#yearly depreciation and amortization: $20m
tax = 0.4 									#tax rate: 40%
dNWC = [5]*5

#Step 1: Calculate the purchase price of A.Target & Co

purchasePx = EBITDAx * EBITDAmargin * salesRevenue[0]

#Step 2: Calculate the debt and equity funding figures for this purchase price

debt   = debtFundingpc   * purchasePx
equity = equityFundingpc * purchasePx

#Step 3: Build the income statement

for i in range(5):
	salesRevenue.append(round(salesRevenue[i]*(1+g),3))			#Populate sales revenue list, increaseing 10% y-o-y

EBITDA = [round(i*EBITDAmargin,3) for i in salesRevenue]		#Create list of yearly EBITDA
EBIT   = [v-DandA[i] for i,v in enumerate(EBITDA)]				#Less D&A
interest = [r*debt]*6
EBT    = [round(v-interest[i],3) for i,v in enumerate(EBIT)]					#Less interest
taxes  = [round(i*tax,3) for i in EBT]
EBTta  = [round(v-taxes[i],3) for i,v in enumerate(EBT)]						#Less taxes

printIncomeStatement(salesRevenue,EBITDA,DandA,EBIT,interest,EBT,taxes,EBTta)

#Step 4: Calculate cumulative levered FCF

CapEx = [round(i*3/20,3) for i in salesRevenue[:-1]]

FCF = [round(v+DandA[i]-CapEx[i]-dNWC[i],3) for i,v in enumerate(EBTta[:-1])]

cumFCF = np.cumsum(FCF).tolist()

printFCFStatement(EBTta,DandA,CapEx,dNWC,FCF,cumFCF)

#Step 6: Calculate a



 























