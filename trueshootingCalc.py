# NBA True Shooting %
# True Shooting % is used to
# Formula for TS%: TS% = PTS / (2 * TSA)

pts = float(input('\nEnter Player\'s Points: '))
fga = float(input('Enter Player\'s Field Goal Attempts: '))
fta = float(input('Enter Player\'s Free Throw Attempts: '))
tsa = fga+0.44*fta
ts_percentage = pts/(2*tsa)*100

print('\nPoints: ', pts)
print('Field Goal Attempts: ', fga)
print('Free Throw Attempts: ', fta)
print('True Shooting Attempts: ', tsa)
print('The Player\'s True Shooting Percentage is '+str(ts_percentage)+'%.\n')
