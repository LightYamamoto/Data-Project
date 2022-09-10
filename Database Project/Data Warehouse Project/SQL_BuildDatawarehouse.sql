CREATE DATABASE DEP302_ASM1
GO
USE DEP302_ASM1
GO
CREATE TABLE Pet_DIM (
    Pet_ID INT PRIMARY KEY NOT NULL,
    Type VARCHAR(3) NOT NULL,
    Name NVARCHAR(255) NULL,
    Age INT NOT NULL,
    Gender VARCHAR(6) NOT NULL,
    MaturitySize VARCHAR(13) NOT NULL,
    FurLength VARCHAR(13) NOT NULL,
    Description NVARCHAR(2000) NULL,
)
GO
CREATE TABLE Color_DIM (
Color_ID INT PRIMARY KEY NOT NULL IDENTITY(1,1),
Color1 VARCHAR(255) NOT NULL,
Color2 VARCHAR(255) NULL,
Color3 VARCHAR(255) NULL)
GO
CREATE TABLE Breed_DIM (
Breed_ID INT PRIMARY KEY NOT NULL IDENTITY(1,1),
Breed1 VARCHAR(255) NOT NULL,
Breed2 VARCHAR(255) NULL
)
GO
CREATE TABLE Health_DIM (
Health_ID INT PRIMARY KEY NOT NULL IDENTITY(1,1),
Health VARCHAR(14) NOT NULL,
Vaccinated  VARCHAR(8) NOT NULL,
Dewormed VARCHAR(8)  NOT NULL,
Sterilized VARCHAR(8) NOT NULL
)
GO
CREATE TABLE Sale_DIM (
Sale_ID INT PRIMARY KEY NOT NULL IDENTITY(1,1),
Quantity INT NOT NULL,
Fee  INT NOT NULL,
State VARCHAR(255)  NOT NULL,
RescuerID INT NOT NULL
)
GO
CREATE TABLE Transaction_FACT(
Pet_ID INT  NOT NULL,
Color_ID INT NOT NULL,
Breed_ID INT NOT NULL,
Health_ID INT NOT NULL,
Sale_ID INT NOT NULL,
FOREIGN KEY(Pet_ID) REFERENCES Pet_DIM(Pet_ID),
FOREIGN KEY(Color_ID) REFERENCES Color_DIM(Color_ID),
FOREIGN KEY(Breed_ID) REFERENCES Breed_DIM(Breed_ID),
FOREIGN KEY(Health_ID) REFERENCES Health_DIM(Health_ID),
FOREIGN KEY(Sale_ID) REFERENCES Sale_DIM(Sale_ID)
)
-- Các truy vấn nghiệp vụ 
--1.	Những vật nuôi nào đã được tiêm vaccine
select * from Transaction_FACT  JOIN Pet_DIM
	ON Pet_DIM.Pet_ID = Transaction_FACT.Pet_ID
	JOIN Health_DIM
	ON Transaction_FACT.Health_ID = Health_DIM.Health_ID
	WHERE Vaccinated = 'Yes'

--2.Liệt kê những vật nuôi có phí chuyển giao là 0 (Nhận nuôi không mất phí)
-- Chỉ liệt kê các trường P.Pet_ID,Type,Gender,Fee,State,Description
SELECT P.Pet_ID,Type,Gender,Fee,State,Description FROM Transaction_FACT  T 
JOIN Sale_DIM  S 
ON T.Sale_ID = S.Sale_ID
JOIN Pet_DIM  P 
ON P.Pet_ID = T.Pet_ID
WHERE Fee = 0



--Có bao nhiêu vật nuôi ở một bang?
SELECT State,COUNT(*) AS PET_COUNT FROM Transaction_FACT  T 
JOIN Sale_DIM  S 
ON T.Sale_ID = S.Sale_ID
JOIN Pet_DIM  P 
ON P.Pet_ID = T.Pet_ID
GROUP BY State 