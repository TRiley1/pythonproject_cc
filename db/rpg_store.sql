DROP TABLE IF EXISTS adventurers;
DROP TABLE IF EXISTS items;

CREATE TABLE items (
    id SERIAL PRIMARY KEY,
    type VARCHAR(255),
    name VARCHAR(255),
    rarity VARCHAR(255),
    value INT
);

CREATE TABLE adventurers (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    loot_id INT NOT NULL REFERENCES items(id)
);

INSERT INTO items (type, name, rarity, value) VALUES ('helmet', 'rusty helmet', NULL, NULL);
INSERT INTO adventurers (name, loot_id) VALUES ('Thorfin', 1);