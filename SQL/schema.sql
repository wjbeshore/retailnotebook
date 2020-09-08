CREATE TABLE stores
    (
        ceres_id VARCHAR(20) NOT NULL,
        banner VARCHAR(100),
        street VARCHAR(50),
        city VARCHAR(50),
        state VARCHAR(50),
        PRIMARY KEY(ceres_id)
    );
    
 CREATE TABLE donation
    (
        donation_id INTEGER AUTO_INCREMENT PRIMARY KEY,
        ceres_id VARCHAR(20) NOT NULL,
        month VARCHAR(20),
        mix INT, 
        dairy INT,
        produce INT,
        meat INT,
        nonfood INT,
        FOREIGN KEY(ceres_id) REFERENCES stores(ceres_id)
    );

    CREATE TABLE agencies
    (
        agency_id VARCHAR(20) NOT NULL,
        name VARCHAR(20),
        contact VARCHAR(20),
        email VARCHAR(20),
        phone VARCHAR(20),
        store_id VARCHAR(20),
        FOREIGN KEY(store_id) REFERENCES stores(ceres_id),
        PRIMARY KEY(agency_id)
    );
    
CREATE TABLE notes
    (
        ceres_id VARCHAR(20) NOT NULL,
        name VARCHAR(20),
        day VARCHAR(20),
        content VARCHAR(200),
        FOREIGN KEY(ceres_id) REFERENCES stores(ceres_id)
    );    