--Find the number of auctions belonging to exactly four categories.
--result:      should be: 8365

SELECT Count(itemID) as "count"
FROM (
    SELECT itemID 
    FROM Category_Item
    GROUP BY itemID
    HAVING COUNT(category_id) = 4
) as temp;
