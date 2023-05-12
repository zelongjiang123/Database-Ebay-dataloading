--Find the ID(s) of auction(s) with the highest current price.
--result: 1046871451 should be 1046871451
SELECT itemID FROM Item
WHERE currently in (
    SELECT MAX(currently) FROM Item
) 