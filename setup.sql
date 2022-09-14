
-- CREATE a new table called data_type
CREATE TABLE data_type (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR(45),
    summary VARCHAR(512),
    description TEXT
);

-- INSERT 3 records so our table has data to work with
INSERT INTO data_type (
    name,
    summary,
    description
) VALUES (
    "Integers",
    "Integer values",
    "A data type that stores integer values"
);

INSERT INTO data_type (
    name,
    summary,
    description
) VALUES (
    "Float",
    "Floating point values",
    "A data type that allows us to store multiple values after the decimal point"
);

INSERT INTO data_type (
    name,
    summary,
    description
) VALUES (
    "Booleans",
    "True or false values",
    "A data type that is either true or false"
);