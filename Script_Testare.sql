--AFISARE NUME JUCATOR, ANTRENOR PRINCIPAL SI NUMELE ECHIPEI DIN CARE FAC PARTE--
SELECT nume_jucator, nume_echipa, antrenor_principal FROM jucator_de_fotbal, echipa_de_club 
	WHERE jucator_de_fotbal.id_club = echipa_de_club.id_club;

--AFISARE NUME JUCATOR, NUME SELECTIONER SI NATIONALA REPREZENTATA(CONVOCAT SI NU ESTE RETRAS)--
SELECT nume_jucator, jucator_de_fotbal.tara as tara, nume_selectioner FROM jucator_de_fotbal, echipa_nationala
	WHERE jucator_de_fotbal.tara = echipa_nationala.tara 
        AND jucator_de_fotbal.convocare = 'convocat' AND jucator_de_fotbal.retras = 'nu' ;
		
--AFISARE NUME JUCATOR SI PALMARES JUCATOR(TROFEU + ANUL CASTIGARII)--
SELECT nume_jucator, trofee.nume_competitie, anul_trofeului FROM jucator_de_fotbal, trofee, palmares, directionare
	WHERE trofee.trofee_ID = directionare.trofee_trofee_ID AND palmares.Palmares_ID = directionare.palmares_palmares_id
            AND jucator_de_fotbal.id_player = palmares.id_player;
			
--AFISARE NUME JUCATOR, ACTIV SAU RETRAS, CONVOCAT SAU NECONVOCAT, ECHIPA DE CLUB, TARA SI CONTINENTUL SI NUMARUL DE GOLURI MARCATE--
SELECT jucator_de_fotbal.nume_jucator, jucator_de_fotbal.retras, jucator_de_fotbal.convocare, echipa_de_club.nume_echipa, jucator_de_fotbal.tara, grupe_nationale.continent, jucator_de_fotbal.numar_goluri
	FROM jucator_de_fotbal, echipa_de_club, grupe_nationale, echipa_nationala 
		WHERE jucator_de_fotbal.id_club = echipa_de_club.id_club AND jucator_de_fotbal.tara = echipa_nationala.tara
			AND echipa_nationala.grupe_nationale_ID = grupe_nationale.grupe_nationale_ID; 
			
--AFISARE NUME JUCATOR, ACTIVI, CONVOCATI CARE JOACA IN ROMANIA, ECHIPA DE CLUB SI NUMARUL DE GOLURI MARCATE FOLOSIN SUBINTEROGARE--
SELECT jucator_de_fotbal.nume_jucator, jucator_de_fotbal.retras, jucator_de_fotbal.convocare, echipa_de_club.nume_echipa, jucator_de_fotbal.tara, jucator_de_fotbal.numar_goluri
	FROM jucator_de_fotbal, echipa_de_club, liga_de_fotbal 
		WHERE jucator_de_fotbal.id_club = echipa_de_club.id_club AND jucator_de_fotbal.tara = liga_de_fotbal.tara
			AND echipa_de_club.id_liga = (SELECT id_liga FROM liga_de_fotbal WHERE tara = 'ROMANIA')
				AND  jucator_de_fotbal.convocare = 'convocat' AND jucator_de_fotbal.retras = 'nu';
				
--AFISARE NUME JUCATOR, ACTIVI, CONVOCATI CARE JOACA NU JOACA IN ROMANIA SI SPANIA, ECHIPA DE CLUB SI NUMARUL DE GOLURI MARCATE FOLOSIN SUBINTEROGARE--			
SELECT jucator_de_fotbal.nume_jucator, jucator_de_fotbal.retras, jucator_de_fotbal.convocare, echipa_de_club.nume_echipa, jucator_de_fotbal.numar_goluri
	FROM jucator_de_fotbal, echipa_de_club, liga_de_fotbal 
		WHERE jucator_de_fotbal.id_club = echipa_de_club.id_club AND jucator_de_fotbal.tara = liga_de_fotbal.tara
			AND echipa_de_club.id_liga NOT IN((SELECT id_liga FROM liga_de_fotbal WHERE tara = 'SPAIN'), (SELECT id_liga FROM liga_de_fotbal WHERE tara = 'ROMANIA'))
				AND  jucator_de_fotbal.convocare = 'convocat' AND jucator_de_fotbal.retras = 'nu';

--ATACANTII CARE AU SUB 70 DE GOLURI SI SUNT RETRASI DIN ACTIVITATE NU VOR FI CONVOCATI(ABSTRACTIE DE COLOANA CONVOCARE)--
SELECT jucator_de_fotbal.nume_jucator, jucator_de_fotbal.pozitie, jucator_de_fotbal.numar_goluri, jucator_de_fotbal.retras, jucator_de_fotbal.convocare
	FROM jucator_de_fotbal WHERE jucator_de_fotbal.pozitie = 'atacant' AND jucator_de_fotbal.numar_goluri > 70
		AND jucator_de_fotbal.retras = 'nu';

--MARIREA NUMARULUI DE JUCATORI CONVOCATI PENTRU NATIONALELE DIN EUROPA FOLOSIND SI SUBINTEROGARE--
UPDATE echipa_nationala SET numar_jucatori_convocati = numar_jucatori_convocati + 1 
	WHERE echipa_nationala.grupe_nationale_ID IN ((SELECT grupe_nationale_ID FROM grupe_nationale WHERE continent = 'Europa'));
	
--AFISAREA NUMARULUI TOTAL DE GOLURI MARCATE DE JUCATORII CONVOCATI LA NATIONALA ROMANIEI--
SELECT echipa_nationala.tara, SUM(jucator_de_fotbal.numar_goluri) AS "NUMAR TOTAL DE GOLURI" FROM echipa_nationala, jucator_de_fotbal
	WHERE jucator_de_fotbal.convocare = 'convocat' AND jucator_de_fotbal.retras = 'nu' 
		AND echipa_nationala.nume_selectioner = 'Mirel Radoi' GROUP BY echipa_nationala.tara;
		
--AFISAREA NUMARULUI TOTAL DE JUCATORI CONVOCATI DE PE FIECARE POZITIE LA NATIONALA ROMANIEI--
SELECT jucator_de_fotbal.pozitie, COUNT(jucator_de_fotbal.pozitie) AS "Total jucatori" FROM echipa_nationala, jucator_de_fotbal
	WHERE jucator_de_fotbal.convocare = 'convocat' AND jucator_de_fotbal.retras = 'nu' 
		AND echipa_nationala.nume_selectioner = 'Mirel Radoi' GROUP BY jucator_de_fotbal.pozitie;

--ERORI DATE DE CONSTRANGERI--	
--MODIFICARE NUMAR DE JUCATORI CONVOCATI CU +5 PENTRU NATIONALELE DIN EUROPA => valorea returnata ar fi mai mare decat valoarea maxima impusa	
UPDATE echipa_nationala set numar_jucatori_convocati = numar_jucatori_convocati + 5 
	WHERE echipa_nationala.grupe_nationale_ID IN ((SELECT grupe_nationale_ID FROM grupe_nationale WHERE continent = 'Europa'));
	
--INSERT JUCATOR DE FOTBAL -> GENERARE EROARE PENTRU UNICITATEA PRIMARY KEY-ULUI--
INSERT INTO jucator_de_fotbal VALUES(3, 'Andrei Cristea', TO_DATE('15-05-1984', ' DD-MM-YYYY'), 179, 70, 'atacant',
		156, 450, 72, 'neconvocat', 'nu', NULL,
		(SELECT id_club FROM echipa_de_club WHERE nume_echipa = 'Steaua Bucuresti'),
		(SELECT tara FROM echipa_nationala WHERE nume_selectioner = 'Mirel Radoi'),
		(SELECT id_liga FROM liga_de_fotbal WHERE tara = 'ROMANIA'));
		-- id-ul 3 este deja asignat unui jucator --
		
--INSERT ECHIPA DE CLUB -> GENERARE EROARE PENTRU UNICITATEA NUMELUI ECHIPEI--
INSERT INTO echipa_de_club VALUES(NULL, 'Steaua Bucuresti', 'POPRICANI', 32, 'Augusto Dinu', 
		(SELECT id_liga FROM liga_de_fotbal WHERE tara = 'ROMANIA'));
		-- numele Steaua Bucuresti este deja asignat unei echipe --

--INSERT JUCATOR DE FOTBAL -> GENERARE EROARE PENTRU UNICITATEA NUME + CONVOCARE + RETRAS--
INSERT INTO jucator_de_fotbal VALUES(NULL, 'Stefan Radu', TO_DATE('22-10-1986', ' DD-MM-YYYY'), 183, 70, 'fundas',
		7, 403, 26, 'convocat', 'nu', 'Capitan',
		(SELECT id_club FROM echipa_de_club WHERE nume_echipa = 'FC Barcelona'),
		(SELECT tara FROM echipa_nationala WHERE nume_selectioner = 'Mirel Radoi'),
		(SELECT id_liga FROM liga_de_fotbal WHERE tara = 'SPAIN'));
		-- numele de Stefan Radu exista o data si este convocat si activ--
		
--INSERT COMPETITIE -> GENERARE EROARE PENTRU DEPASIREA NUMARULUI DE CARACTERE DISPONIBIL SI UTILIZAREA UNOR CARACTERE SPECIALE
INSERT INTO competitie VALUES('CUPA ROMANIEI LIGA 1, LIGA A 2-A  SI LIGA A 3-A', 'Echipe de club', 5, 1,
		(SELECT numar_liga FROM liga_de_fotbal WHERE tara = 'ROMANIA'),
		(SELECT grupe_nationale_id FROM grupe_nationale WHERE continent = 'Europa'),
		(SELECT id_liga FROM liga_de_fotbal WHERE tara = 'ROMANIA'));
		-- CARACTERE SPECIALE: -   ,   --
		
--INSERT TROFEE -> GENERARE EROARE PENTRU INCALCAREA CONDITIEI individuale > 0--
INSERT INTO trofee VALUES(-2, 3, 
            (SELECT nume_competitie FROM competitie WHERE id_liga = 3), NULL, 2018);
			
--INSERT JUCATOR DE FOTBAL -> GENERARE EROARE ALTA VALOARE PENTRU COLOANA RETRAS DECAT CELE IMPUSE--
INSERT INTO jucator_de_fotbal VALUES(NULL, 'Andrei Cristea', TO_DATE('15-05-1984', ' DD-MM-YYYY'), 179, 70, 'atacant',
		156, 450, 72, 'neconvocat', 'IS', NULL,
		(SELECT id_club FROM echipa_de_club WHERE nume_echipa = 'Steaua Bucuresti'),
		(SELECT tara FROM echipa_nationala WHERE nume_selectioner = 'Mirel Radoi'),
		(SELECT id_liga FROM liga_de_fotbal WHERE tara = 'ROMANIA'));
		-- disponibil doar 'da' sau 'nu' --

--INSERT ECHIPA DE CLUB -> GENERARE EROARE PENTRU UTILIZAREA CIFRELOR INTR UN NUME--
INSERT INTO echipa_de_club VALUES(NULL, 'ASC PASCANI 2020', 'POPRICANI', 32, 'Augusto Dinu123', 
		(SELECT id_liga FROM liga_de_fotbal WHERE tara = 'ROMANIA'));
		-- numele Steaua Bucuresti este deja asignat unei echipe --

--INSERT JUCATOR DE FOTBAL -> GENERARE EROARE PENTRU DATA NASTERII
INSERT INTO jucator_de_fotbal VALUES(NULL, 'Stefan Radu', TO_DATE('22-10-2021', ' DD-MM-YYYY'), 183, 70, 'fundas',
		7, 403, 26, 'neconvocat', 'nu', 'Capitan',
		(SELECT id_club FROM echipa_de_club WHERE nume_echipa = 'FC Barcelona'),
		(SELECT tara FROM echipa_nationala WHERE nume_selectioner = 'Mirel Radoi'),
		(SELECT id_liga FROM liga_de_fotbal WHERE tara = 'SPAIN'));
		-- data nasterii este din 'viitor'--		
