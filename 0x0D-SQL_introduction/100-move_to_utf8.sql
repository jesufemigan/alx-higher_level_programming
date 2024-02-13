-- converts database to utf-8 format
ALTER DATABASE hbtn_0c_0 CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
ALTER TABLE hbtn_0c_0.first_table CONVERT TO CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
ALTER TABLE hbtn_0c_0.first_table DROP COLUMN `name`;
ALTER TABLE hbtn_0c_0.first_table ADD COLUMN `name` VARCHAR(256) COLLATE utf8mb4_unicode_ci;
