drop table if exists User;
create table User (
    userID varchar(255) NOT NULL,
    rating int,
    location varchar(255),
    country varchar(255),
    Primary Key (userID)
);

drop table if exists Item;
create table Item (
    itemID varchar(255) NOT NULL Primary Key,
    name varchar(255) NOT NULL,
    currently float NOT NULL,
    buy_Price float,
    first_Bid float NOT NULL,
    number_of_Bids int NOT NULL,
    started date,
    ends date,
    sellerID varchar(255),
    description varchar(255),
    FOREIGN KEY (SellerID) REFERENCES User(userID)
);

drop table if exists Category;
create table Category (
    id int Primary KEY, 
    name varchar(255) NOT NULL
);

drop table if exists Category_Item;
create table Category_Item (
    category_id int,
    itemID varchar(255),
    FOREIGN KEY (itemID) REFERENCES Item(itemID),
    FOREIGN KEY (category_id) REFERENCES Category(id)
);

drop table if exists Bids;
create table Bids (
    bidderID varchar(255),
    itemID varchar(255),
    amount float,
    time date,
    FOREIGN KEY (itemID) REFERENCES Item(itemID),
    FOREIGN KEY (bidderID) REFERENCES User(userID)
);