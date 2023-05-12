--Find the number of sellers whose rating is higher than 1000.
--result: 3130, should be: 3130
SELECT COUNT(DISTINCT userID)
FROM User, Item
WHERE Item.sellerID = userID and CAST(rating AS INT) > 1000;