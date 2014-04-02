#Players
bryce_year1 = {"year": "2012", "team": "Washington Nationals", "type": "hitter", "games": "139", "pa": "597", "avg": ".270", "obp": ".340", "slg": ".477", "hr": "22", "rbi": "59", "player_id": "3" }
bryce_year2 = {"year": "2013", "team": "Washington Nationals", "type": "hitter", "games": "118", "pa": "497", "avg": ".274", "obp": ".368", "slg": ".486", "hr": "20", "rbi": "58", "player_id": "3"}
bryce_player = { "name": "Bryce Harper", "number": "34", "position": "OF", "number": "34",  "social": "@Bharper3407" ,"bats": "R", "throws": "L", "height": "74", "weight": "230", "school": "College of Southern Nevada"}
bryce_image = "http://mlb.com/images/players/525x330/547180.jpg"
bryce_years = [bryce_year1, bryce_year2]

yu_year1 = {"year": "2012", "team": "TEX", "type": "pitcher", "games": "29", "wins": "16", "losses": "9", "era": "3.90", "gs": "29", "s": "0", "whip": "1.280", "ip": "191.1"}
yu_year2 = { "year": "2013", "team": "TEX", "type": "pitcher", "games": "32", "wins": "13", "losses": "9", "era": "2.83", "gs": "32", "s": "0", "whip": "1.073", "ip": "209.2"}
yu_image = "http://mlb.com/images/players/525x330/506433.jpg"
yu_player = { "name": "Yu Darvish", "number": "11", "position": "P", "number": "11", "social": "@faridyu" ,"bats": "R", "throws": "R", "height": "6'5", "weight": "225", "school": "Sendai, Japan", "years": [yu_year1, yu_year2] }
yu_years = [yu_year1, yu_year2]

mike_year1 = {"id": "7", "year": "2011", "team": "Los Angeles Angels of Anaheim", "type": "hitter", "games": "40", "pa": "135", "avg": ".220", "obp": ".281", "slg": ".390", "hr": "5", "rbi": "16", "player_id": "10"}
mike_year2 = {"id": "8", "year": "2012", "team": "Los Angeles Angels of Anaheim", "type": "hitter", "games": "139", "pa": "639", "avg": ".326", "obp": ".399", "slg": ".564", "hr": "30", "rbi": "83", "player_id": "10"}
mike_year3 = {"id": "9", "year": "2013", "team": "Los Angeles Angels of Anaheim", "type": "hitter", "games": "157", "pa": "716", "avg": ".323", "obp": ".432", "slg": ".557", "hr": "27", "rbi": "97", "player_id": "10"}
mike_image = "http://mlb.com/images/players/525x330/545361.jpg"
mike_player = { "id": "10", "name": "Mike Trout", "number": "27", "position": "OF", "number": "27", "social": "@Trouty20" ,"bats": "R", "throws": "R", "height": "6'2", "weight": "230", "school": "Millville Senior HS, Millville, NJ" }
mike_years = [mike_year1, mike_year2, mike_year3]

bryce = dict(player=bryce_player, image=bryce_image, years=bryce_years)
mike = dict(player=mike_player, image=mike_image, years=mike_years)
yu = dict(player=yu_player, image=yu_image, years=yu_years)

# Leave out yu because we don't have a Texas team in the DB
players = [bryce, mike]