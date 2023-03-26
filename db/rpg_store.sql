DROP TABLE IF EXISTS item_adv;
DROP TABLE IF EXISTS adventurers;
DROP TABLE IF EXISTS items;

CREATE TABLE items (
    id SERIAL PRIMARY KEY,
    type VARCHAR(255),
    name VARCHAR(255),
    rarity VARCHAR(255),
    image VARCHAR(255),
    value INT
);

CREATE TABLE adventurers (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255)
);

CREATE TABLE item_adv (
    id SERIAL PRIMARY KEY,
    adventurer_id INT NOT NULL REFERENCES adventurers(id) ON DELETE CASCADE,
    loot_id INT NOT NULL REFERENCES items(id) ON DELETE CASCADE,
    review TEXT
);

INSERT INTO items (type, name, rarity,image, value) VALUES ('helmet', 'rusty helmet', NULL, 'axe.png', NULL);
INSERT INTO items (type, name, rarity,image, value) VALUES ('sword', 'dirty dagger', NULL, 'axe.png', NULL);
INSERT INTO items (type, name, rarity,image, value) VALUES ('tunic', 'worn tunic', NULL, 'axe.png',NULL);
INSERT INTO items (type, name, rarity,image, value) VALUES ('lamp', 'dusty lamp', NULL, 'axe.png', NULL);
INSERT INTO items (type, name, rarity,image, value) VALUES ('helmet', 'cracked helmet', NULL, 'axe.png', NULL);
INSERT INTO items (type, name, rarity,image, value) VALUES ('belt', 'tired belt', NULL, 'axe.png', NULL);
INSERT INTO items (type, name, rarity,image, value) VALUES ('axe', 'brittle axe', NULL, 'axe.png', NULL);
INSERT INTO items (type, name, rarity,image, value) VALUES ('Sword', 'Sword of the Greats ','rare', 'axe.png', 1000);
INSERT INTO items (type, name, rarity,image, value) VALUES ('Axe', 'Oh Dear Axe', 'common', 'axe.png', 500);
INSERT INTO items (type, name, rarity,image, value) VALUES ('Greaves', 'Jimmy Greavous', 'ultra', 'axe.png', 5000);
INSERT INTO items (type, name, rarity,image, value) VALUES ('Helmet', 'Helm of Oblivion', 'ultra', 'axe.png', 10000);
INSERT INTO items (type, name, rarity,image, value) VALUES ('Bow', 'BOW','common', 'axe.png', 500);
INSERT INTO items (type, name, rarity,image, value) VALUES ('Crossbow', 'Vampire Slayer', 'rare', 'axe.png', 2500);
INSERT INTO items (type, name, rarity,image, value) VALUES ('Tunic', 'NIce Tunic', 'common', 'axe.png', 800);
INSERT INTO items (type, name, rarity,image, value) VALUES ('Battle Axe', 'Thorkill', 'ultra', 'axe.png', 8000);


-- INSERT INTO items (type, name, rarity, value)
-- VALUES (
--     'Helmet', 'The Helmet of Bravery', 
--     CASE floor(random() * 3) 
--         WHEN 0 THEN 'Common'
--         WHEN 1 THEN 'Rare'
--         ELSE 'Ultra'
--     END,
--     floor(random() * 10000) + 100
-- );


INSERT INTO adventurers (name) VALUES ('Thorfin');
INSERT INTO adventurers (name) VALUES ('Thorkell');
INSERT INTO adventurers (name) VALUES ('Thor');
INSERT INTO item_adv(adventurer_id, loot_id) VALUES (1,1);
INSERT INTO item_adv(adventurer_id, loot_id) VALUES (2,1);
INSERT INTO item_adv(adventurer_id, loot_id) VALUES (1,2);

-- SELECT adventurers.* FROM adventurers INNER JOIN item_adv ON item_adv.adventurer_id = adventurers.id WHERE item_adv.loot_id = 1
-- This query tells me the number of adventurers that own ID 1 in this case a rusty helmet.