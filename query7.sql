--Find the number of categories that include at least one item with a bid of more than $100.
--result: 150, should be 150
SELECT COUNT(DISTINCT category_id)
FROM Category_Item as c, Bids as b
WHERE c.itemID = b.itemID and b.amount > 100;