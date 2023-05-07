SELECT season, COUNT(SEASON)
FROM results
GROUP BY season
HAVING COUNT(season) != 380
ORDER BY season;
#Check for anamolous data
#1 Season of incomplete data

DELETE
FROM results
WHERE season = '2021-22';
#Remove column