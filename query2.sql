--Find the number of users from New York (i.e., users whose location is the string "New York").
--result: 80, should be: 80
SELECT Count(userID) FROM User
WHERE location = "New York";