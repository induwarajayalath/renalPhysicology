# bowmanCapsule
# proximalConvolutedTubule
# thickportionDescendingLoopOfHenle
# thinDescendingLoopOfHenle
# thinAscendingLoopOfHenle
# thickAscendingLoopOfHenle
# distalConvolutedTubule
# collectingTubule
# collectingDuct

# substances = glucose, Na, K, Cl, Ca, Mg, PO4, NH4, urea, water, H, creatinine, AA, HCO3

# glucose = input('Enter the inital glucose amount in mmol/min - ')
# Na = input('Enter the inital Na amount in mmol/min - ')
# K = input('Enter the inital K amount in mmol/min - ')
# Cl = input('Enter the inital Cl amount in mmol/min - ')
# Ca = input('Enter the inital Ca amount in mmol/min - ')
# Mg = input('Enter the inital Mg amount in mmol/min - ')
# PO4 = input('Enter the inital PO4 amount in mmol/min - ')
# NH4 = input('Enter the inital NH4 amount in mmol/min - ')
# urea = input('Enter the inital urea amount in mmol/min - ')
# water = input('Enter the inital water amount in mmol/min - ')
# H = input('Enter the inital H amount in mmol/min - ')
# creatinine = input('Enter the inital creatinine amount in mmol/min - ')
# AA = input('Enter the inital AA amount in mmol/min - ')
# HCO3 = input('Enter the inital HCO3 amount in mmol/min - ')


segmentReabsorbtion = { 
				'bowmanCapsule' : [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
				'proximalConvolutedTubule' : [100, 65, 65, 5, 5, 5, 5, 5, 5, 20, 5, 90, 5, 5], 
				'thickportionDescendingLoopOfHenle' : [0, 0, 0, 0, 0, 0, 0, 0, 0, 25, 0, 0, 0, 0], 
				# 'thinDescendingLoopOfHenle'
				# 'thinAscendingLoopOfHenle'
				# 'thickAscendingLoopOfHenle'
				# 'distalConvolutedTubule'
				# 'collectingTubule'
				# 'collectingDuct'
			}

segmentSecretion = { 
				'bowmanCapsule' : [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
				'proximalConvolutedTubule' 
				'thickportionDescendingLoopOfHenle'
				'thinDescendingLoopOfHenle'
				'thinAscendingLoopOfHenle'
				'thickAscendingLoopOfHenle'
				'distalConvolutedTubule'
				'collectingTubule'
				'collectingDuct'
			}			


# print(segmentsDic['bowmanCapsule'][0])

# for x in segmentReabsorbtion:
# 	# print (i+' '+segmentsDic[i])
# 	# print(x,':',segmentsDic[x])
# 	print ("segment "+x)
# 	for y in segmentsDic[x]:
# 		print (y)
# 	print ("end of segment\n")


# Template to print
# print('bowmanCapsule :  Reabsorbtion - 12 mmol/min \t Secretion - 20 mmol/min \n')



