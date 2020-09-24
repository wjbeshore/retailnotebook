
    
 CREATE TABLE donation
    (
        donation_id INTEGER AUTO_INCREMENT PRIMARY KEY,
        ceres_id VARCHAR(20) NOT NULL,
        month DATE,
        mix INT, 
        dairy INT,
        produce INT,
        meat INT,
        nonfood INT
    );