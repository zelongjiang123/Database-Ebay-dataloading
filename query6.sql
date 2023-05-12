--Find the number of users who are both sellers and bidders.
--result: 6717, should be: 6717
SELECT COUNT(DISTINCT userID)
FROM User
WHERE userID in (SELECT bidderID FROM Bids)
and userID in (SELECT sellerID FROM Item);