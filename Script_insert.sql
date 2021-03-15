
--INSERT TABELA GRUPE_NATIONALE--

INSERT INTO grupe_nationale VALUES(NULL, 52, 'Europa');
INSERT INTO grupe_nationale VALUES(NULL, 40, 'Asia');
INSERT INTO grupe_nationale VALUES(NULL, 20, 'America');
INSERT INTO grupe_nationale VALUES(NULL, 56, 'Africa');
INSERT INTO grupe_nationale VALUES(NULL, 12, 'Oceania_si_Australia');
INSERT INTO grupe_nationale VALUES(NULL,  0, 'Nu este nationala' );

--INSERT TABELA ECHIPA_NATIONALA--

INSERT INTO echipa_nationala VALUES('ROMANIA', 31, 'Mirel Radoi', 
		(SELECT grupe_nationale_id FROM grupe_nationale WHERE continent = 'Europa'));
INSERT INTO echipa_nationala VALUES('FRANCE', 31, 'Didier Deschamps', 
		(SELECT grupe_nationale_id FROM grupe_nationale WHERE continent = 'Europa'));
INSERT INTO echipa_nationala VALUES('SPAIN', 31, 'Luis Enrique', 
		(SELECT grupe_nationale_id FROM grupe_nationale WHERE continent = 'Europa'));
INSERT INTO echipa_nationala VALUES('GERMANY', 31, 'Joachim Low', 
		(SELECT grupe_nationale_id FROM grupe_nationale WHERE continent = 'Europa'));
INSERT INTO echipa_nationala VALUES('ENGLAND', 31, 'Gareth Southgate', 
		(SELECT grupe_nationale_id FROM grupe_nationale WHERE continent = 'Europa'));
		
INSERT INTO echipa_nationala VALUES('EGIPT', 31, 'Hossam El Badry', 
		(SELECT grupe_nationale_id FROM grupe_nationale WHERE continent = 'Asia'));
INSERT INTO echipa_nationala VALUES('INDIA', 31, 'Igor Stimac', 
		(SELECT grupe_nationale_id FROM grupe_nationale WHERE continent = 'Asia'));
INSERT INTO echipa_nationala VALUES('JAPAN', 31, 'Hajime Moriyasu', 
		(SELECT grupe_nationale_id FROM grupe_nationale WHERE continent = 'Asia'));
INSERT INTO echipa_nationala VALUES('CHINA', 31, 'Marcello Lippi', 
		(SELECT grupe_nationale_id FROM grupe_nationale WHERE continent = 'Asia'));		
INSERT INTO echipa_nationala VALUES('SOUTH KOREA', 31, 'Paulo Bento', 
		(SELECT grupe_nationale_id FROM grupe_nationale WHERE continent = 'Asia'));

INSERT INTO echipa_nationala VALUES('BRAZIL', 31, 'Leonardo Bacchi', 
		(SELECT grupe_nationale_id FROM grupe_nationale WHERE continent = 'America'));
INSERT INTO echipa_nationala VALUES('ARGENTINA', 31, 'Lionel Scaloni', 
		(SELECT grupe_nationale_id FROM grupe_nationale WHERE continent = 'America'));
INSERT INTO echipa_nationala VALUES('CHILE', 31, 'Reinaldo Rueda', 
		(SELECT grupe_nationale_id FROM grupe_nationale WHERE continent = 'America'));
INSERT INTO echipa_nationala VALUES('CANADA', 31, 'John Herdman', 
		(SELECT grupe_nationale_id FROM grupe_nationale WHERE continent = 'America'));
INSERT INTO echipa_nationala VALUES('MEXIC', 31, 'Gerardo Martino', 
		(SELECT grupe_nationale_id FROM grupe_nationale WHERE continent = 'America'));

INSERT INTO echipa_nationala VALUES('CAMEROON', 31, 'Silva Oliveira', 
		(SELECT grupe_nationale_id FROM grupe_nationale WHERE continent = 'Africa'));
INSERT INTO echipa_nationala VALUES('SENEGAL', 31, 'Aliou Cisse', 
		(SELECT grupe_nationale_id FROM grupe_nationale WHERE continent = 'Africa'));
INSERT INTO echipa_nationala VALUES('GHANA', 31, 'Charles Akonnor', 
		(SELECT grupe_nationale_id FROM grupe_nationale WHERE continent = 'Africa'));
INSERT INTO echipa_nationala VALUES('IVORY COAST', 31, 'Patrice Beaumelle', 
		(SELECT grupe_nationale_id FROM grupe_nationale WHERE continent = 'Africa'));
INSERT INTO echipa_nationala VALUES('NIGERIA', 31, 'Gernot Rohr', 
		(SELECT grupe_nationale_id FROM grupe_nationale WHERE continent = 'Africa'));
		
INSERT INTO echipa_nationala VALUES('AUSTRALIA', 31, 'Graham Arnold', 
		(SELECT grupe_nationale_id FROM grupe_nationale WHERE continent = 'Oceania_si_Australia'));
INSERT INTO echipa_nationala VALUES('NEW ZEALAND', 31, 'Danny Hay', 
		(SELECT grupe_nationale_id FROM grupe_nationale WHERE continent = 'Oceania_si_Australia'));
INSERT INTO echipa_nationala VALUES('FIJI', 31, 'Flemming Serritslev', 
		(SELECT grupe_nationale_id FROM grupe_nationale WHERE continent = 'Oceania_si_Australia'));
		
--INSERT TABELA LIGA_DE_FOTBAL--

INSERT INTO liga_de_fotbal VALUES(NULL, 'Liga 1', 16, 2,
        (SELECT distinct tara FROM echipa_nationala WHERE nume_selectioner = 'Mirel Radoi'));
INSERT INTO liga_de_fotbal VALUES(NULL, 'Liga 1', 18, 3,
        (SELECT distinct tara FROM echipa_nationala WHERE nume_selectioner = 'Didier Deschamps'));
INSERT INTO liga_de_fotbal VALUES(NULL, 'Liga 1', 18, 3,
        (SELECT distinct tara FROM echipa_nationala WHERE nume_selectioner = 'Luis Enrique'));
INSERT INTO liga_de_fotbal VALUES(NULL, 'Liga 1', 18, 2,
        (SELECT distinct tara FROM echipa_nationala WHERE nume_selectioner = 'Joachim Low'));
INSERT INTO liga_de_fotbal VALUES(NULL, 'Liga 1', 18, 3,
        (SELECT distinct tara FROM echipa_nationala WHERE nume_selectioner = 'Gareth Southgate'));

INSERT INTO liga_de_fotbal VALUES(NULL, 'Liga 1', 16, 2,
        (SELECT distinct tara FROM echipa_nationala WHERE nume_selectioner = 'Hossam El Badry'));
INSERT INTO liga_de_fotbal VALUES(NULL, 'Liga 1', 18, 2,
        (SELECT distinct tara FROM echipa_nationala WHERE nume_selectioner = 'Igor Stimac'));
INSERT INTO liga_de_fotbal VALUES(NULL, 'Liga 1', 18, 2,
        (SELECT distinct tara FROM echipa_nationala WHERE nume_selectioner = 'Hajime Moriyasu'));
INSERT INTO liga_de_fotbal VALUES(NULL, 'Liga 1', 18, 2,
        (SELECT distinct tara FROM echipa_nationala WHERE nume_selectioner = 'Marcello Lippi'));
INSERT INTO liga_de_fotbal VALUES(NULL, 'Liga 1', 18, 2,
        (SELECT distinct tara FROM echipa_nationala WHERE nume_selectioner = 'Paulo Bento'));
		
INSERT INTO liga_de_fotbal VALUES(NULL, 'Liga 1', 16, 2,
        (SELECT distinct tara FROM echipa_nationala WHERE nume_selectioner = 'Silva Oliveira'));
INSERT INTO liga_de_fotbal VALUES(NULL, 'Liga 1', 20, 2,
        (SELECT distinct tara FROM echipa_nationala WHERE nume_selectioner = 'Aliou Cisse'));
INSERT INTO liga_de_fotbal VALUES(NULL, 'Liga 1', 18, 2,
        (SELECT distinct tara FROM echipa_nationala WHERE nume_selectioner = 'Charles Akonnor'));
INSERT INTO liga_de_fotbal VALUES(NULL, 'Liga 1', 16, 2,
        (SELECT distinct tara FROM echipa_nationala WHERE nume_selectioner = 'Patrice Beaumelle'));
INSERT INTO liga_de_fotbal VALUES(NULL, 'Liga 1', 18, 2,
        (SELECT distinct tara FROM echipa_nationala WHERE nume_selectioner = 'Gernot Rohr'));

INSERT INTO liga_de_fotbal VALUES(NULL, 'Liga 1', 18, 2,
        (SELECT distinct tara FROM echipa_nationala WHERE nume_selectioner = 'Leonardo Bacchi'));
INSERT INTO liga_de_fotbal VALUES(NULL, 'Liga 1', 20, 2,
        (SELECT distinct tara FROM echipa_nationala WHERE nume_selectioner = 'Lionel Scaloni'));
INSERT INTO liga_de_fotbal VALUES(NULL, 'Liga 1', 16, 2,
        (SELECT distinct tara FROM echipa_nationala WHERE nume_selectioner = 'Reinaldo Rueda'));
INSERT INTO liga_de_fotbal VALUES(NULL, 'Liga 1', 16, 2,
        (SELECT distinct tara FROM echipa_nationala WHERE nume_selectioner = 'John Herdman'));
INSERT INTO liga_de_fotbal VALUES(NULL, 'Liga 1', 16, 2,
        (SELECT distinct tara FROM echipa_nationala WHERE nume_selectioner = 'Gerardo Martino'));
		
INSERT INTO liga_de_fotbal VALUES(NULL, 'Liga 1', 16, 2,
        (SELECT distinct tara FROM echipa_nationala WHERE nume_selectioner = 'Graham Arnold'));
INSERT INTO liga_de_fotbal VALUES(NULL, 'Liga 1', 16, 2,
        (SELECT distinct tara FROM echipa_nationala WHERE nume_selectioner = 'Danny Hay'));
INSERT INTO liga_de_fotbal VALUES(NULL, 'Liga 1', 16, 2,
        (SELECT distinct tara FROM echipa_nationala WHERE nume_selectioner = 'Flemming Serritslev'));
		
INSERT INTO liga_de_fotbal VALUES(NULL, 'Liga 1', 16, 1,
        (SELECT distinct continent FROM grupe_nationale WHERE numar_echipe_nationale = 52));
INSERT INTO liga_de_fotbal VALUES(NULL, 'Liga 1', 16, 1,
        (SELECT distinct continent FROM grupe_nationale WHERE numar_echipe_nationale = 40));
INSERT INTO liga_de_fotbal VALUES(NULL, 'Liga 1', 16, 1,
        (SELECT distinct continent FROM grupe_nationale WHERE numar_echipe_nationale = 56));
		
--INSERT ECHIPA DE CLUB--

INSERT INTO echipa_de_club VALUES(NULL, 'Steaua Bucuresti', 'Bucuresti', 30, 'Toni Petrea', 
		(SELECT id_liga FROM liga_de_fotbal WHERE tara = 'ROMANIA'));
INSERT INTO echipa_de_club VALUES(NULL, 'Dinamo Bucuresti', 'Bucuresti', 30, 'Cosmin Contra', 
		(SELECT id_liga FROM liga_de_fotbal WHERE tara = 'ROMANIA'));
INSERT INTO echipa_de_club VALUES(NULL, 'CFR Cluj 1907', 'Cluj', 30, 'Dan Petrescu', 
		(SELECT id_liga FROM liga_de_fotbal WHERE tara = 'ROMANIA'));
INSERT INTO echipa_de_club VALUES(NULL, 'Poli Iasi', 'Iasi', 30, 'Daniel Pancu', 
		(SELECT id_liga FROM liga_de_fotbal WHERE tara = 'ROMANIA'));
INSERT INTO echipa_de_club VALUES(NULL, 'Univ Craiova', 'Craiova', 30, 'Cornel Papura', 
		(SELECT id_liga FROM liga_de_fotbal WHERE tara = 'ROMANIA'));
INSERT INTO echipa_de_club VALUES(NULL, 'FC Botosani', 'Botosani', 30, 'Marius Croitoru', 
		(SELECT id_liga FROM liga_de_fotbal WHERE tara = 'ROMANIA'));
INSERT INTO echipa_de_club VALUES(NULL, 'Viitorul Constanta', 'Constanta', 30, 'Gheorghe Hagi', 
		(SELECT id_liga FROM liga_de_fotbal WHERE tara = 'ROMANIA'));
INSERT INTO echipa_de_club VALUES(NULL, 'Astra Giurgiu', 'Giurgiu', 30, 'Eugen Neagoe', 
		(SELECT id_liga FROM liga_de_fotbal WHERE tara = 'ROMANIA'));
		
INSERT INTO echipa_de_club VALUES(NULL, 'Paris Saint Germain FC', 'Paris', 32, 'Thomas Tuchel', 
		(SELECT id_liga FROM liga_de_fotbal WHERE tara = 'FRANCE'));
INSERT INTO echipa_de_club VALUES(NULL, 'Lille OSC', 'Lille', 32, 'Christophe Galtier', 
		(SELECT id_liga FROM liga_de_fotbal WHERE tara = 'FRANCE'));
INSERT INTO echipa_de_club VALUES(NULL, 'Olympique Lyonnais', 'Lyon', 32, 'Rudi Garcia', 
		(SELECT id_liga FROM liga_de_fotbal WHERE tara = 'FRANCE'));
INSERT INTO echipa_de_club VALUES(NULL, 'AS Monaco FC', 'Monaco', 32, 'Niko Kovac', 
		(SELECT id_liga FROM liga_de_fotbal WHERE tara = 'FRANCE'));
INSERT INTO echipa_de_club VALUES(NULL, 'Olympique de Marseille', 'Marsilia', 32, ' Andre Villas Boas', 
		(SELECT id_liga FROM liga_de_fotbal WHERE tara = 'FRANCE'));
INSERT INTO echipa_de_club VALUES(NULL, 'FC Girondins de Bordeaux', 'Bordeaux', 32, 'Jean Louis Gasset', 
		(SELECT id_liga FROM liga_de_fotbal WHERE tara = 'FRANCE'));
INSERT INTO echipa_de_club VALUES(NULL, 'AS Saint Etienne', 'Etienne', 32, 'Claude Puel', 
		(SELECT id_liga FROM liga_de_fotbal WHERE tara = 'FRANCE'));
INSERT INTO echipa_de_club VALUES(NULL, 'Football Club de Nantes', 'Nantes', 32, 'Christian Gourcuff', 
		(SELECT id_liga FROM liga_de_fotbal WHERE tara = 'FRANCE'));
		
INSERT INTO echipa_de_club VALUES(NULL, 'FC Barcelona', 'Barcelona', 31, 'Ronald Koeman', 
		(SELECT id_liga FROM liga_de_fotbal WHERE tara = 'SPAIN'));
INSERT INTO echipa_de_club VALUES(NULL, 'Real Madrid', 'Madrid', 31, 'Zinedine Zidane', 
		(SELECT id_liga FROM liga_de_fotbal WHERE tara = 'SPAIN'));
INSERT INTO echipa_de_club VALUES(NULL, 'Atletico Madrid', 'Madrid', 31, 'Diego Simeone', 
		(SELECT id_liga FROM liga_de_fotbal WHERE tara = 'SPAIN'));
INSERT INTO echipa_de_club VALUES(NULL, 'Real Sociedad', 'San Sebastian', 31, 'Imanol Alguacil', 
		(SELECT id_liga FROM liga_de_fotbal WHERE tara = 'SPAIN'));
INSERT INTO echipa_de_club VALUES(NULL, 'Sevilla FC', 'Sevilla', 31, 'Julen Lopetegui', 
		(SELECT id_liga FROM liga_de_fotbal WHERE tara = 'SPAIN'));
INSERT INTO echipa_de_club VALUES(NULL, 'Villarreal CF', 'Villarreal', 31, 'Unai Emery', 
		(SELECT id_liga FROM liga_de_fotbal WHERE tara = 'SPAIN'));
INSERT INTO echipa_de_club VALUES(NULL, 'Valencia CF', 'Valencia', 31, 'Javi Gracia', 
		(SELECT id_liga FROM liga_de_fotbal WHERE tara = 'SPAIN'));
INSERT INTO echipa_de_club VALUES(NULL, 'Athletic Bilbao', 'Bilbao', 31, 'Gaizka Garitano', 
		(SELECT id_liga FROM liga_de_fotbal WHERE tara = 'SPAIN'));
		
INSERT INTO echipa_de_club VALUES(NULL, 'FC Bayern Munchen', 'Munchen', 30, 'Hans Dieter Flick', 
		(SELECT id_liga FROM liga_de_fotbal WHERE tara = 'GERMANY'));
INSERT INTO echipa_de_club VALUES(NULL, 'Borussia Dortmund', 'Dortmund', 30, 'Lucien Favre', 
		(SELECT id_liga FROM liga_de_fotbal WHERE tara = 'GERMANY'));
INSERT INTO echipa_de_club VALUES(NULL, 'Bayer 04 Leverkusen', 'Leverkusen', 30, 'Peter Bosz', 
		(SELECT id_liga FROM liga_de_fotbal WHERE tara = 'GERMANY'));
INSERT INTO echipa_de_club VALUES(NULL, 'RB Leipzig', 'Leipzig', 30, 'Julian Nagelsmann', 
		(SELECT id_liga FROM liga_de_fotbal WHERE tara = 'GERMANY'));
INSERT INTO echipa_de_club VALUES(NULL, 'FC Schalke 04', 'Gelsenkirchen', 30, 'Manuel Baum', 
		(SELECT id_liga FROM liga_de_fotbal WHERE tara = 'GERMANY'));
INSERT INTO echipa_de_club VALUES(NULL, 'Borussia Monchengladbach', 'Monchengladbach', 30, 'Marco Rose', 
		(SELECT id_liga FROM liga_de_fotbal WHERE tara = 'GERMANY'));
INSERT INTO echipa_de_club VALUES(NULL, 'Hertha Berlin', 'Berlin', 30, 'Bruno Labbadia', 
		(SELECT id_liga FROM liga_de_fotbal WHERE tara = 'GERMANY'));
INSERT INTO echipa_de_club VALUES(NULL, 'VfB Stuttgart', 'Stuttgart', 30, 'Pellegrino Matarazzo', 
		(SELECT id_liga FROM liga_de_fotbal WHERE tara = 'GERMANY'));
		
INSERT INTO echipa_de_club VALUES(NULL, 'Liverpool FC', 'Liverpool', 34, 'Jurgen Klopp', 
		(SELECT id_liga FROM liga_de_fotbal WHERE tara = 'ENGLAND'));
INSERT INTO echipa_de_club VALUES(NULL, 'Manchester City FC', 'Manchester', 34, 'Josep Guardiola', 
		(SELECT id_liga FROM liga_de_fotbal WHERE tara = 'ENGLAND'));
INSERT INTO echipa_de_club VALUES(NULL, 'Manchester United FC', 'Manchester', 34, 'Ole Gunnar Solskjaer', 
		(SELECT id_liga FROM liga_de_fotbal WHERE tara = 'ENGLAND'));
INSERT INTO echipa_de_club VALUES(NULL, 'Chelsea FC', 'Londra', 34, 'Frank Lampard', 
		(SELECT id_liga FROM liga_de_fotbal WHERE tara = 'ENGLAND'));
INSERT INTO echipa_de_club VALUES(NULL, 'Arsenal FC', 'Londra', 34, 'Mikel Arteta', 
		(SELECT id_liga FROM liga_de_fotbal WHERE tara = 'ENGLAND'));
INSERT INTO echipa_de_club VALUES(NULL, 'Tottenham Hotspur FC', 'Tottenham', 34, 'Jose Mourinho', 
		(SELECT id_liga FROM liga_de_fotbal WHERE tara = 'ENGLAND'));
INSERT INTO echipa_de_club VALUES(NULL, 'Leicester City FC', 'Leicester', 34, 'Brendan Rodgers', 
		(SELECT id_liga FROM liga_de_fotbal WHERE tara = 'ENGLAND'));
INSERT INTO echipa_de_club VALUES(NULL, 'Everton FC', 'Liverpool', 34, 'Carlo Ancelotti', 
		(SELECT id_liga FROM liga_de_fotbal WHERE tara = 'ENGLAND'));
		
INSERT INTO echipa_de_club VALUES(NULL, 'Al Ahly SC', 'Cairo', 28, 'Pitso Mosimane', 
		(SELECT id_liga FROM liga_de_fotbal WHERE tara = 'EGIPT'));
		
INSERT INTO echipa_de_club VALUES(NULL, 'UMS de Loum', 'Loum', 28, 'Fabricio Goncalves Mendes', 
		(SELECT id_liga FROM liga_de_fotbal WHERE tara = 'CAMEROON'));
		
INSERT INTO echipa_de_club VALUES(NULL, 'Clube de Flamengo', 'Rio de Janeiro', 29, 'RogErio Ceni', 
		(SELECT id_liga FROM liga_de_fotbal WHERE tara = 'BRAZIL'));
		
INSERT INTO echipa_de_club VALUES(NULL, 'Sydney Football Club', 'Sydney', 30, 'Steve Corica', 
		(SELECT id_liga FROM liga_de_fotbal WHERE tara = 'AUSTRALIA'));
		
--INSERT COMPETITIE--

INSERT INTO competitie VALUES('CAMPIONAT ROMANIA', 'Echipe de club', 5, 1,
		(SELECT numar_liga FROM liga_de_fotbal WHERE tara = 'ROMANIA'),
		(SELECT grupe_nationale_id FROM grupe_nationale WHERE continent = 'Europa'),
		(SELECT id_liga FROM liga_de_fotbal WHERE tara = 'ROMANIA')); 

INSERT INTO competitie VALUES('CAMPIONAT FRANCE', 'Echipe de club', 5, 1,
		(SELECT numar_liga FROM liga_de_fotbal WHERE tara = 'FRANCE'),
		(SELECT grupe_nationale_id FROM grupe_nationale WHERE continent = 'Europa'),
		(SELECT id_liga FROM liga_de_fotbal WHERE tara = 'FRANCE'));

INSERT INTO competitie VALUES('CAMPIONAT GERMANY', 'Echipe de club', 5, 1,
		(SELECT numar_liga FROM liga_de_fotbal WHERE tara = 'GERMANY'),
		(SELECT grupe_nationale_id FROM grupe_nationale WHERE continent = 'Europa'),
		(SELECT id_liga FROM liga_de_fotbal WHERE tara = 'GERMANY'));
		
INSERT INTO competitie VALUES('CAMPIONAT SPAIN', 'Echipe de club', 5, 1,
		(SELECT numar_liga FROM liga_de_fotbal WHERE tara = 'SPAIN'),
		(SELECT grupe_nationale_id FROM grupe_nationale WHERE continent = 'Europa'),
		(SELECT id_liga FROM liga_de_fotbal WHERE tara = 'SPAIN'));
		
INSERT INTO competitie VALUES('CAMPIONAT ENGLAND', 'Echipe de club', 5, 1,
		(SELECT numar_liga FROM liga_de_fotbal WHERE tara = 'ENGLAND'),
		(SELECT grupe_nationale_id FROM grupe_nationale WHERE continent = 'Europa'),
		(SELECT id_liga FROM liga_de_fotbal WHERE tara = 'ENGLAND'));
		
INSERT INTO competitie VALUES('CAMPIONAT EGIPT', 'Echipe de club', 5, 1,
		(SELECT numar_liga FROM liga_de_fotbal WHERE tara = 'EGIPT'),
		(SELECT grupe_nationale_id FROM grupe_nationale WHERE continent = 'Asia'),
		(SELECT id_liga FROM liga_de_fotbal WHERE tara = 'EGIPT'));
		
INSERT INTO competitie VALUES('CAMPIONAT CAMEROON', 'Echipe de club', 5, 1,
		(SELECT numar_liga FROM liga_de_fotbal WHERE tara = 'CAMEROON'),
		(SELECT grupe_nationale_id FROM grupe_nationale WHERE continent = 'Africa'),
		(SELECT id_liga FROM liga_de_fotbal WHERE tara = 'CAMEROON'));
		
INSERT INTO competitie VALUES('CAMPIONAT BRAZIL', 'Echipe de club', 5, 1,
		(SELECT numar_liga FROM liga_de_fotbal WHERE tara = 'BRAZIL'),
		(SELECT grupe_nationale_id FROM grupe_nationale WHERE continent = 'America'),
		(SELECT id_liga FROM liga_de_fotbal WHERE tara = 'BRAZIL'));
		
INSERT INTO competitie VALUES('CAMPIONAT AUSTRALIA', 'Echipe de club', 5, 1,
		(SELECT numar_liga FROM liga_de_fotbal WHERE tara = 'AUSTRALIA'),
		(SELECT grupe_nationale_id FROM grupe_nationale WHERE continent = 'Oceania_si_Australia'),
		(SELECT id_liga FROM liga_de_fotbal WHERE tara = 'AUSTRALIA'));
		
INSERT INTO competitie VALUES('CAMPIONAT EUROPEAN', 'Echipe nationale', 5, 1, NULL,
		(SELECT grupe_nationale_id FROM grupe_nationale WHERE continent = 'Europa'),
		(SELECT id_liga FROM liga_de_fotbal WHERE tara = 'Europa'));
		
INSERT INTO competitie VALUES('CAMPIONAT ASIATIC', 'Echipe nationale', 5, 1, NULL,
		(SELECT grupe_nationale_id FROM grupe_nationale WHERE continent = 'Asia'),
		(SELECT id_liga FROM liga_de_fotbal WHERE tara = 'Asia'));

--INSERT JUCATOR_DE_FOTBAL--

--PORTAR--

INSERT INTO jucator_de_fotbal VALUES(NULL, 'Ciprian Tatarusanu', TO_DATE('09-02-1986', ' DD-MM-YYYY'), 198, 90, 'portar',
		0, 354, 1, 'convocat', 'nu', 'reflexe bune',
		(SELECT id_club FROM echipa_de_club WHERE nume_echipa = 'Steaua Bucuresti'),
		(SELECT tara FROM echipa_nationala WHERE nume_selectioner = 'Mirel Radoi'),
		(SELECT id_liga FROM liga_de_fotbal WHERE tara = 'ROMANIA'));
INSERT INTO jucator_de_fotbal VALUES(NULL, 'David Lazar', TO_DATE('08-08-1991', ' DD-MM-YYYY'), 184, 85, 'portar',
		0, 96, 91, 'convocat', 'nu', NULL,
		(SELECT id_club FROM echipa_de_club WHERE nume_echipa = 'Astra Giurgiu'),
		(SELECT tara FROM echipa_nationala WHERE nume_selectioner = 'Mirel Radoi'),
		(SELECT id_liga FROM liga_de_fotbal WHERE tara = 'ROMANIA'));
INSERT INTO jucator_de_fotbal VALUES(NULL, 'Cristian Balgradean', TO_DATE('21-03-1988', ' DD-MM-YYYY'), 187, 86, 'portar',
		0, 282, 34, 'convocat', 'nu', NULL,
		(SELECT id_club FROM echipa_de_club WHERE nume_echipa = 'CFR Cluj 1907'),
		(SELECT tara FROM echipa_nationala WHERE nume_selectioner = 'Mirel Radoi'),
		(SELECT id_liga FROM liga_de_fotbal WHERE tara = 'ROMANIA'));
INSERT INTO jucator_de_fotbal VALUES(NULL, 'Andrei Vlad', TO_DATE('15-04-1999', ' DD-MM-YYYY'), 190, 75, 'portar',
		0, 54, 99, 'neconvocat', 'nu', NULL,
		(SELECT id_club FROM echipa_de_club WHERE nume_echipa = 'Steaua Bucuresti'),
		(SELECT tara FROM echipa_nationala WHERE nume_selectioner = 'Mirel Radoi'),
		(SELECT id_liga FROM liga_de_fotbal WHERE tara = 'ROMANIA'));
INSERT INTO jucator_de_fotbal VALUES(NULL, 'Helmuth Duckadam', TO_DATE('01-04-1959', ' DD-MM-YYYY'), 193, 80, 'portar',
		0, 140, 59, 'neconvocat', 'da', 'Eroul Sevilla',
		(SELECT id_club FROM echipa_de_club WHERE nume_echipa = 'Steaua Bucuresti'),
		(SELECT tara FROM echipa_nationala WHERE nume_selectioner = 'Mirel Radoi'),
		(SELECT id_liga FROM liga_de_fotbal WHERE tara = 'ROMANIA'));
		
--FUNDAS--

INSERT INTO jucator_de_fotbal VALUES(NULL, 'Valentin Cretu', TO_DATE('02-01-1989', ' DD-MM-YYYY'), 176, 71, 'fundas',
		2, 286, 2, 'convocat', 'nu', 'Sprinter',
		(SELECT id_club FROM echipa_de_club WHERE nume_echipa = 'Steaua Bucuresti'),
		(SELECT tara FROM echipa_nationala WHERE nume_selectioner = 'Mirel Radoi'),
		(SELECT id_liga FROM liga_de_fotbal WHERE tara = 'ROMANIA'));
INSERT INTO jucator_de_fotbal VALUES(NULL, 'Cristi Manea', TO_DATE('09-08-1997', ' DD-MM-YYYY'), 183, 72, 'fundas',
		4, 174, 4, 'convocat', 'nu', NULL,
		(SELECT id_club FROM echipa_de_club WHERE nume_echipa = 'CFR Cluj 1907'),
		(SELECT tara FROM echipa_nationala WHERE nume_selectioner = 'Mirel Radoi'),
		(SELECT id_liga FROM liga_de_fotbal WHERE tara = 'ROMANIA'));
INSERT INTO jucator_de_fotbal VALUES(NULL, 'Stefan Radu', TO_DATE('22-10-1986', ' DD-MM-YYYY'), 183, 70, 'fundas',
		7, 403, 26, 'convocat', 'nu', 'Capitan',
		(SELECT id_club FROM echipa_de_club WHERE nume_echipa = 'FC Barcelona'),
		(SELECT tara FROM echipa_nationala WHERE nume_selectioner = 'Mirel Radoi'),
		(SELECT id_liga FROM liga_de_fotbal WHERE tara = 'SPAIN'));
INSERT INTO jucator_de_fotbal VALUES(NULL, 'Vlad Chiriches', TO_DATE('14-11-1989', ' DD-MM-YYYY'), 184, 72, 'fundas',
		10, 282, 21, 'convocat', 'nu', 'Solid Player',
		(SELECT id_club FROM echipa_de_club WHERE nume_echipa = 'RB Leipzig'),
		(SELECT tara FROM echipa_nationala WHERE nume_selectioner = 'Mirel Radoi'),
		(SELECT id_liga FROM liga_de_fotbal WHERE tara = 'GERMANY'));
INSERT INTO jucator_de_fotbal VALUES(NULL, 'Cosmin Frasinescu', TO_DATE('10-02-1985', ' DD-MM-YYYY'), 187, 79, 'fundas',
		13, 425, 23, 'convocat', 'nu', 'Power Header',
		(SELECT id_club FROM echipa_de_club WHERE nume_echipa = 'Poli Iasi'),
		(SELECT tara FROM echipa_nationala WHERE nume_selectioner = 'Mirel Radoi'),
		(SELECT id_liga FROM liga_de_fotbal WHERE tara = 'ROMANIA'));
INSERT INTO jucator_de_fotbal VALUES(NULL, 'Bogdan Tiru', TO_DATE('15-03-1994', ' DD-MM-YYYY'), 185, 79, 'fundas',
		10, 210, 25, 'convocat', 'nu', 'Penalty Taker',
		(SELECT id_club FROM echipa_de_club WHERE nume_echipa = 'Viitorul Constanta'),
		(SELECT tara FROM echipa_nationala WHERE nume_selectioner = 'Mirel Radoi'),
		(SELECT id_liga FROM liga_de_fotbal WHERE tara = 'ROMANIA'));
INSERT INTO jucator_de_fotbal VALUES(NULL, 'Mihai Bordeianu', TO_DATE('18-11-1991', ' DD-MM-YYYY'), 175, 73, 'fundas',
		6, 127, 6, 'convocat', 'nu', 'Capitan',
		(SELECT id_club FROM echipa_de_club WHERE nume_echipa = 'CFR Cluj 1907'),
		(SELECT tara FROM echipa_nationala WHERE nume_selectioner = 'Mirel Radoi'),
		(SELECT id_liga FROM liga_de_fotbal WHERE tara = 'ROMANIA'));
INSERT INTO jucator_de_fotbal VALUES(NULL, 'Mario Camora', TO_DATE('10-11-1986', ' DD-MM-YYYY'), 178, 73, 'fundas',
		15, 390, 45, 'convocat', 'nu', 'Sprinter',
		(SELECT id_club FROM echipa_de_club WHERE nume_echipa = 'CFR Cluj 1907'),
		(SELECT tara FROM echipa_nationala WHERE nume_selectioner = 'Mirel Radoi'),
		(SELECT id_liga FROM liga_de_fotbal WHERE tara = 'ROMANIA'));
INSERT INTO jucator_de_fotbal VALUES(NULL, 'Nicusor Bancu', TO_DATE('18-09-1992', ' DD-MM-YYYY'), 182, 72, 'fundas',
		6, 270, 11, 'convocat', 'nu', NULL,
		(SELECT id_club FROM echipa_de_club WHERE nume_echipa = 'Chelsea FC'),
		(SELECT tara FROM echipa_nationala WHERE nume_selectioner = 'Mirel Radoi'),
		(SELECT id_liga FROM liga_de_fotbal WHERE tara = 'ENGLAND'));
INSERT INTO jucator_de_fotbal VALUES(NULL, 'Florin Stefan', TO_DATE('09-05-1996', ' DD-MM-YYYY'), 183, 73, 'fundas',
		13, 161, 96, 'convocat', 'nu', 'Free Kicker',
		(SELECT id_club FROM echipa_de_club WHERE nume_echipa = 'Clube de Flamengo'),
		(SELECT tara FROM echipa_nationala WHERE nume_selectioner = 'Mirel Radoi'),
		(SELECT id_liga FROM liga_de_fotbal WHERE tara = 'BRAZIL'));
INSERT INTO jucator_de_fotbal VALUES(NULL, 'Mihai Balasa', TO_DATE('14-01-1995', ' DD-MM-YYYY'), 186, 75, 'fundas',
		10, 220, 95, 'neconvocat', 'nu', NULL,
		(SELECT id_club FROM echipa_de_club WHERE nume_echipa = 'UMS de Loum'),
		(SELECT tara FROM echipa_nationala WHERE nume_selectioner = 'Mirel Radoi'),
		(SELECT id_liga FROM liga_de_fotbal WHERE tara = 'CAMEROON'));
INSERT INTO jucator_de_fotbal VALUES(NULL, 'Marius Mihalache', TO_DATE('14-12-1984', ' DD-MM-YYYY'), 184, 78, 'fundas',
		15, 301, 92, 'neconvocat', 'nu', NULL,
		(SELECT id_club FROM echipa_de_club WHERE nume_echipa = 'Sydney Football Club'),
		(SELECT tara FROM echipa_nationala WHERE nume_selectioner = 'Mirel Radoi'),
		(SELECT id_liga FROM liga_de_fotbal WHERE tara = 'AUSTRALIA'));
INSERT INTO jucator_de_fotbal VALUES(NULL, 'Michael Klein', TO_DATE('10-10-1959', ' DD-MM-YYYY'), 177, 72, 'fundas',
		44, 504, 91, 'neconvocat', 'da', 'MVP',
		(SELECT id_club FROM echipa_de_club WHERE nume_echipa = 'Dinamo Bucuresti'),
		(SELECT tara FROM echipa_nationala WHERE nume_selectioner = 'Mirel Radoi'),
		(SELECT id_liga FROM liga_de_fotbal WHERE tara = 'ROMANIA'));
		
--MIJLOCAS--

INSERT INTO jucator_de_fotbal VALUES(NULL, 'Nicusor Stanciu', TO_DATE('07-06-1993', ' DD-MM-YYYY'), 170, 70, 'mijlocas',
		67, 347, 7, 'convocat', 'nu', 'Play-maker',
		(SELECT id_club FROM echipa_de_club WHERE nume_echipa = 'Real Madrid'),
		(SELECT tara FROM echipa_nationala WHERE nume_selectioner = 'Mirel Radoi'),
		(SELECT id_liga FROM liga_de_fotbal WHERE tara = 'SPAIN'));
INSERT INTO jucator_de_fotbal VALUES(NULL, 'Darius Olaru', TO_DATE('03-03-1998', ' DD-MM-YYYY'), 176, 71, 'mijlocas',
		17, 250, 27, 'convocat', 'nu', 'Play-maker',
		(SELECT id_club FROM echipa_de_club WHERE nume_echipa = 'Steaua Bucuresti'),
		(SELECT tara FROM echipa_nationala WHERE nume_selectioner = 'Mirel Radoi'),
		(SELECT id_liga FROM liga_de_fotbal WHERE tara = 'ROMANIA'));
INSERT INTO jucator_de_fotbal VALUES(NULL, 'Florin Tanase', TO_DATE('03-03-1998', ' DD-MM-YYYY'), 185, 72, 'mijlocas',
		66, 224, 12, 'convocat', 'nu', 'Penalty Taker',
		(SELECT id_club FROM echipa_de_club WHERE nume_echipa = 'Steaua Bucuresti'),
		(SELECT tara FROM echipa_nationala WHERE nume_selectioner = 'Mirel Radoi'),
		(SELECT id_liga FROM liga_de_fotbal WHERE tara = 'ROMANIA'));
INSERT INTO jucator_de_fotbal VALUES(NULL, 'Dennis Man', TO_DATE('26-08-1998', ' DD-MM-YYYY'), 183, 74, 'mijlocas',
		64, 161, 8, 'convocat', 'nu', 'Finisher',
		(SELECT id_club FROM echipa_de_club WHERE nume_echipa = 'FC Barcelona'),
		(SELECT tara FROM echipa_nationala WHERE nume_selectioner = 'Mirel Radoi'),
		(SELECT id_liga FROM liga_de_fotbal WHERE tara = 'SPAIN'));
INSERT INTO jucator_de_fotbal VALUES(NULL, 'Florinel Coman', TO_DATE('10-04-1998', ' DD-MM-YYYY'), 182, 71, 'mijlocas',
		68, 162, 15, 'convocat', 'nu', 'Dribbler',
		(SELECT id_club FROM echipa_de_club WHERE nume_echipa = 'Borussia Dortmund'),
		(SELECT tara FROM echipa_nationala WHERE nume_selectioner = 'Mirel Radoi'),
		(SELECT id_liga FROM liga_de_fotbal WHERE tara = 'GERMANY'));
INSERT INTO jucator_de_fotbal VALUES(NULL, 'Alexandru Cretu', TO_DATE('03-03-1998', ' DD-MM-YYYY'), 190, 76, 'mijlocas',
		10, 249, 29, 'convocat', 'nu', 'Leadership',
		(SELECT id_club FROM echipa_de_club WHERE nume_echipa = 'AS Monaco FC'),
		(SELECT tara FROM echipa_nationala WHERE nume_selectioner = 'Mirel Radoi'),
		(SELECT id_liga FROM liga_de_fotbal WHERE tara = 'FRANCE'));
INSERT INTO jucator_de_fotbal VALUES(NULL, 'Dan Nistor', TO_DATE('06-05-1988', ' DD-MM-YYYY'), 172, 70, 'mijlocas',
		35, 290, 16, 'convocat', 'nu', 'Penalty Taker',
		(SELECT id_club FROM echipa_de_club WHERE nume_echipa = 'Univ Craiova'),
		(SELECT tara FROM echipa_nationala WHERE nume_selectioner = 'Mirel Radoi'),
		(SELECT id_liga FROM liga_de_fotbal WHERE tara = 'ROMANIA'));
INSERT INTO jucator_de_fotbal VALUES(NULL, 'Ianis Hagi', TO_DATE('22-10-1998', ' DD-MM-YYYY'), 182, 71, 'mijlocas',
		40, 170, 10, 'convocat', 'nu', 'Dribbler',
		(SELECT id_club FROM echipa_de_club WHERE nume_echipa = 'Manchester City FC'),
		(SELECT tara FROM echipa_nationala WHERE nume_selectioner = 'Mirel Radoi'),
		(SELECT id_liga FROM liga_de_fotbal WHERE tara = 'ENGLAND'));
INSERT INTO jucator_de_fotbal VALUES(NULL, 'Razvan Marin', TO_DATE('23-05-1996', ' DD-MM-YYYY'), 178, 73, 'mijlocas',
		29, 210, 20, 'convocat', 'nu', 'Solid Player',
		(SELECT id_club FROM echipa_de_club WHERE nume_echipa = 'Tottenham Hotspur FC'),
		(SELECT tara FROM echipa_nationala WHERE nume_selectioner = 'Mirel Radoi'),
		(SELECT id_liga FROM liga_de_fotbal WHERE tara = 'ENGLAND'));
INSERT INTO jucator_de_fotbal VALUES(NULL, 'Eric Bicfalvi', TO_DATE('05-02-1988', ' DD-MM-YYYY'), 187, 76, 'mijlocas',
		80, 366, 55, 'convocat', 'nu', 'MVP',
		(SELECT id_club FROM echipa_de_club WHERE nume_echipa = 'Paris Saint Germain FC'),
		(SELECT tara FROM echipa_nationala WHERE nume_selectioner = 'Mirel Radoi'),
		(SELECT id_liga FROM liga_de_fotbal WHERE tara = 'FRANCE'));
INSERT INTO jucator_de_fotbal VALUES(NULL, 'Paul Anton', TO_DATE('10-05-1991', ' DD-MM-YYYY'), 182, 78, 'mijlocas',
		29, 310, 51, 'neconvocat', 'nu', null,
		(SELECT id_club FROM echipa_de_club WHERE nume_echipa = 'Dinamo Bucuresti'),
		(SELECT tara FROM echipa_nationala WHERE nume_selectioner = 'Mirel Radoi'),
		(SELECT id_liga FROM liga_de_fotbal WHERE tara = 'ROMANIA'));
INSERT INTO jucator_de_fotbal VALUES(NULL, 'Olimpiu Morutan', TO_DATE('25-04-1991', ' DD-MM-YYYY'), 172, 71, 'mijlocas',
		14, 120, 52, 'neconvocat', 'nu', null,
		(SELECT id_club FROM echipa_de_club WHERE nume_echipa = 'Steaua Bucuresti'),
		(SELECT tara FROM echipa_nationala WHERE nume_selectioner = 'Mirel Radoi'),
		(SELECT id_liga FROM liga_de_fotbal WHERE tara = 'ROMANIA'));
INSERT INTO jucator_de_fotbal VALUES(NULL, 'Gheorghe Hagi', TO_DATE('10-05-1991', ' DD-MM-YYYY'), 182, 78, 'mijlocas',
		272, 740, 10, 'neconvocat', 'da', 'The Best',
		(SELECT id_club FROM echipa_de_club WHERE nume_echipa = 'FC Barcelona'),
		(SELECT tara FROM echipa_nationala WHERE nume_selectioner = 'Mirel Radoi'),
		(SELECT id_liga FROM liga_de_fotbal WHERE tara = 'SPAIN'));
		
--ATACANT--

INSERT INTO jucator_de_fotbal VALUES(NULL, 'Denis Alibec', TO_DATE('05-01-1991', ' DD-MM-YYYY'), 187, 84, 'atacant',
		72, 268, 77, 'convocat', 'nu', 'Solid Player',
		(SELECT id_club FROM echipa_de_club WHERE nume_echipa = 'Astra Giurgiu'),
		(SELECT tara FROM echipa_nationala WHERE nume_selectioner = 'Mirel Radoi'),
		(SELECT id_liga FROM liga_de_fotbal WHERE tara = 'ROMANIA'));
INSERT INTO jucator_de_fotbal VALUES(NULL, 'Florin Andone', TO_DATE('11-04-1993', ' DD-MM-YYYY'), 180, 78, 'atacant',
		77, 275, 85, 'convocat', 'nu', 'Finisher',
		(SELECT id_club FROM echipa_de_club WHERE nume_echipa = 'Arsenal FC'),
		(SELECT tara FROM echipa_nationala WHERE nume_selectioner = 'Mirel Radoi'),
		(SELECT id_liga FROM liga_de_fotbal WHERE tara = 'ENGLAND'));
INSERT INTO jucator_de_fotbal VALUES(NULL, 'George Puscas', TO_DATE('08-04-1996', ' DD-MM-YYYY'), 188, 80, 'atacant',
		80, 213, 47, 'convocat', 'nu', 'Power Header',
		(SELECT id_club FROM echipa_de_club WHERE nume_echipa = 'Manchester United FC'),
		(SELECT tara FROM echipa_nationala WHERE nume_selectioner = 'Mirel Radoi'),
		(SELECT id_liga FROM liga_de_fotbal WHERE tara = 'ENGLAND'));
INSERT INTO jucator_de_fotbal VALUES(NULL, 'Claudiu Keseru', TO_DATE('02-12-1986', ' DD-MM-YYYY'), 178, 78, 'atacant',
		250, 550, 28, 'convocat', 'nu', 'Finsiher',
		(SELECT id_club FROM echipa_de_club WHERE nume_echipa = 'Lille OSC'),
		(SELECT tara FROM echipa_nationala WHERE nume_selectioner = 'Mirel Radoi'),
		(SELECT id_liga FROM liga_de_fotbal WHERE tara = 'FRANCE'));
INSERT INTO jucator_de_fotbal VALUES(NULL, 'Bogdan Stancu', TO_DATE('28-06-1987', ' DD-MM-YYYY'), 182, 78, 'atacant',
		153, 467, 60, 'convocat', 'nu', 'Solid Player',
		(SELECT id_club FROM echipa_de_club WHERE nume_echipa = 'Real Sociedad'),
		(SELECT tara FROM echipa_nationala WHERE nume_selectioner = 'Mirel Radoi'),
		(SELECT id_liga FROM liga_de_fotbal WHERE tara = 'SPAIN'));
INSERT INTO jucator_de_fotbal VALUES(NULL, 'Adrian Petre', TO_DATE('11-02-1998', ' DD-MM-YYYY'), 188, 80, 'atacant',
		61, 140, 67, 'neconvocat', 'nu', NULL,
		(SELECT id_club FROM echipa_de_club WHERE nume_echipa = 'Steaua Bucuresti'),
		(SELECT tara FROM echipa_nationala WHERE nume_selectioner = 'Mirel Radoi'),
		(SELECT id_liga FROM liga_de_fotbal WHERE tara = 'ROMANIA'));
INSERT INTO jucator_de_fotbal VALUES(NULL, 'Marius Lacatus', TO_DATE('05-04-1964', ' DD-MM-YYYY'), 181, 76, 'atacant',
		126, 580, 7, 'neconvocat', 'da', 'MVP',
		(SELECT id_club FROM echipa_de_club WHERE nume_echipa = 'Steaua Bucuresti'),
		(SELECT tara FROM echipa_nationala WHERE nume_selectioner = 'Mirel Radoi'),
		(SELECT id_liga FROM liga_de_fotbal WHERE tara = 'ROMANIA'));



--INSERT PALMARES--

INSERT INTO palmares VALUES(10, 4,
			(SELECT id_player FROM jucator_de_fotbal WHERE nume_jucator = 'Ciprian Tatarusanu'), NULL);
INSERT INTO palmares VALUES(20, 10,
			(SELECT id_player FROM jucator_de_fotbal WHERE nume_jucator = 'Stefan Radu'), NULL);
INSERT INTO palmares VALUES(15, 8,
			(SELECT id_player FROM jucator_de_fotbal WHERE nume_jucator = 'Eric Bicfalvi'), NULL);
INSERT INTO palmares VALUES(25, 15,
			(SELECT id_player FROM jucator_de_fotbal WHERE nume_jucator = 'Claudiu Keseru'), NULL);
INSERT INTO palmares VALUES(45, 20,
			(SELECT id_player FROM jucator_de_fotbal WHERE nume_jucator = 'Gheorghe Hagi'), NULL);
INSERT INTO palmares VALUES(4, 3,
			(SELECT id_player FROM jucator_de_fotbal WHERE nume_jucator = 'Paul Anton'), NULL);

--INSERT TROFEE--

INSERT INTO trofee VALUES(5, 1, 
            (SELECT nume_competitie FROM competitie WHERE id_liga = 1), NULL, 2019);

INSERT INTO trofee VALUES(5, 1, 
            (SELECT nume_competitie FROM competitie WHERE id_liga = 1), NULL, 2018);

INSERT INTO trofee VALUES(5, 1, 
            (SELECT nume_competitie FROM competitie WHERE id_liga = 1), NULL, 2017);

INSERT INTO trofee VALUES(5, 1, 
            (SELECT nume_competitie FROM competitie WHERE id_liga = 2), NULL, 2019);

INSERT INTO trofee VALUES(5, 1, 
            (SELECT nume_competitie FROM competitie WHERE id_liga = 2), NULL, 2018);

INSERT INTO trofee VALUES(5, 1, 
            (SELECT nume_competitie FROM competitie WHERE id_liga = 2), NULL, 2017);
INSERT INTO trofee VALUES(5, 1, 
            (SELECT nume_competitie FROM competitie WHERE id_liga = 3), NULL, 2019);

INSERT INTO trofee VALUES(5, 1, 
            (SELECT nume_competitie FROM competitie WHERE id_liga = 3), NULL, 2018);

INSERT INTO trofee VALUES(5, 1, 
            (SELECT nume_competitie FROM competitie WHERE id_liga = 3), NULL, 2017);
INSERT INTO trofee VALUES(5, 1, 
            (SELECT nume_competitie FROM competitie WHERE id_liga = 4), NULL, 2019);

INSERT INTO trofee VALUES(5, 1, 
            (SELECT nume_competitie FROM competitie WHERE id_liga = 4), NULL, 2018);

INSERT INTO trofee VALUES(5, 1, 
            (SELECT nume_competitie FROM competitie WHERE id_liga = 4), NULL, 2017);
INSERT INTO trofee VALUES(5, 1, 
            (SELECT nume_competitie FROM competitie WHERE id_liga = 5), NULL, 2019);

INSERT INTO trofee VALUES(5, 1, 
            (SELECT nume_competitie FROM competitie WHERE id_liga = 5), NULL, 2018);

INSERT INTO trofee VALUES(5, 1, 
            (SELECT nume_competitie FROM competitie WHERE id_liga = 5), NULL, 2017);


--INSERT M-N DIRECTIONARE--

INSERT INTO Directionare VALUES ((SELECT Palmares_ID FROM Palmares WHERE id_player = 1),
			(SELECT Trofee_ID FROM trofee WHERE nume_competitie = 'CAMPIONAT ROMANIA' 
					AND anul_trofeului = 2019));
INSERT INTO Directionare VALUES ((SELECT Palmares_ID FROM Palmares WHERE id_player = 1),
			(SELECT Trofee_ID FROM trofee WHERE nume_competitie = 'CAMPIONAT ROMANIA' 
					AND anul_trofeului = 2018));
INSERT INTO Directionare VALUES ((SELECT Palmares_ID FROM Palmares WHERE id_player = 1),
			(SELECT Trofee_ID FROM trofee WHERE nume_competitie = 'CAMPIONAT ROMANIA' 
					AND anul_trofeului = 2017));
INSERT INTO Directionare VALUES ((SELECT Palmares_ID FROM Palmares WHERE id_player = 8),
			(SELECT Trofee_ID FROM trofee WHERE nume_competitie = 'CAMPIONAT SPAIN' 
					AND anul_trofeului = 2019));
INSERT INTO Directionare VALUES ((SELECT Palmares_ID FROM Palmares WHERE id_player = 8),
			(SELECT Trofee_ID FROM trofee WHERE nume_competitie = 'CAMPIONAT SPAIN' 
					AND anul_trofeului = 2018));
INSERT INTO Directionare VALUES ((SELECT Palmares_ID FROM Palmares WHERE id_player = 8),
			(SELECT Trofee_ID FROM trofee WHERE nume_competitie = 'CAMPIONAT SPAIN' 
					AND anul_trofeului = 2017));
INSERT INTO Directionare VALUES ((SELECT Palmares_ID FROM Palmares WHERE id_player = 28),
			(SELECT Trofee_ID FROM trofee WHERE nume_competitie = 'CAMPIONAT FRANCE' 
					AND anul_trofeului = 2019));
INSERT INTO Directionare VALUES ((SELECT Palmares_ID FROM Palmares WHERE id_player = 28),
			(SELECT Trofee_ID FROM trofee WHERE nume_competitie = 'CAMPIONAT FRANCE' 
					AND anul_trofeului = 2018));
INSERT INTO Directionare VALUES ((SELECT Palmares_ID FROM Palmares WHERE id_player = 28),
			(SELECT Trofee_ID FROM trofee WHERE nume_competitie = 'CAMPIONAT FRANCE' 
					AND anul_trofeului = 2017));					


		




		
		
