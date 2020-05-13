CREATE TABLE vessel (
    Id SERIAL PRIMARY KEY, -- ИДЕНТИФИКАТОР 
    Name text NOT NULL, -- НАЗВАНИЕ (выражается строковыми данными)
    Port text NOT NULL, -- ПОРТ ПРИПИСКИ  (выражается строковыми данными)
    Exemption integer NOT NULL, CHECK (Exemption >=0 ) -- ЛЬГОТА (выражается числовыми данными, не может быть < 0)
);
CREATE TABLE places ( -- МЕСТА ПОГРУЗКИ
    Id SERIAL PRIMARY KEY, -- ИДЕНТИФИКАТОР 
    Pier text NOT NULL, -- ПРИЧАЛ (выражается строковыми данными)
    Port text NOT NULL, -- ПОРТ (выражается строковыми данными)
    Allocation integer NOT NULL, CHECK (Allocation >= 0) -- ОТЧИСЛЕНИЯ НА ПОГРУЗКУ (выражается числовыми данными, не может быть < 0)
);

CREATE TABLE cargo ( -- ГРУЗ
    Id SERIAL PRIMARY KEY, -- ИДЕНТИФИКАТОР 
    Name text NOT NULL, -- НАЗВАНИЕ (выражается строковыми данными)
    Port text NOT NULL, -- ПОРТ СКЛАДИРОВАНИЯ (выражается строковыми данными)
    Price integer NOT NULL, CHECK (Price >= 0), -- СТОИМОСТЬ, РУБ (выражается числовыми данными, не может быть < 0)
	Amount integer NOT NULL, CHECK (Amount > 0) -- МАКС. КОЛ-ВО (выражается числовыми данными, не может быть <= 0)
);

CREATE TABLE shipment ( -- ПОГРУЗКА
    Register SERIAL PRIMARY KEY, -- НОМЕР ВЕДОМОСТИ
    Weekday text NOT NULL, -- ДАТА (выражается строковыми данными)
    Vessel integer NOT NULL, CHECK (Vessel > 0), -- СУДНО (выражается числовыми данными, не может быть <= 0)
    Place integer NOT NULL CHECK (Place > 0), -- МЕСТО ПОГРУЗКИ (выражается числовыми данными, не может быть <= 0)
	Cargo integer NOT NULL, CHECK (Cargo > 0), -- ГРУЗ (выражается числовыми данными, не может быть <= 0)
	Amount integer NOT NULL, CHECK (Amount > 0), -- КОЛ-ВО (выражается числовыми данными, не может быть <= 0)
	Price integer NOT NULL -- СТОИМОСТЬ, РУБ (выражается числовыми данными)
)
