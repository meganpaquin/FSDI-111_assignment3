
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

INSERT INTO data_type (
    name,
    summary,
    description
) VALUES (
    "Strings",
    "Used for letters and words",
    "A collection of alphabets, words, or characters"
);

INSERT INTO data_type (
    name,
    summary,
    description
) VALUES (
    "Lists",
    "An ordered sequence of elements",
    "A changeable and ordered sequence of elements. A way to hold data defined by [] brackets."
);

INSERT INTO data_type (
    name,
    summary,
    description
) VALUES (
    "Dictionaries",
    "A collection of key-value pairs",
    "A collection of data defined in key-value pairs. Where keys cannot be repeated but values can be repeated. Defined by {} brackets."
);

INSERT INTO data_type (
    name,
    summary,
    description
) VALUES (
    "Tuples",
    "Single variables collected together",
    "A collection of single variables stored in one variable. It is ordered and unchanegable and declared with () brackets."
);

UPDATE data_type SET description = "A floating point number. Used to represent real numbers and is written with a decimal point to divide fractional parts." WHERE id=2;

UPDATE data_type SET description = "A built in data type that can either be true (1) or false (0)." WHERE id=3;
