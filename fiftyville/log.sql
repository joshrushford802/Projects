-- Find names of all potential suspects
SELECT name FROM people;

-- Read the crime report
SELECT description FROM crime_scene_reports WHERE year IS 2021 AND month IS "7" AND day IS 28 AND street IS "Humphrey Street";

-- Find the interviews of the crime
SELECT transcript FROM interviews WHERE year IS 2021 AND month IS "7" AND day IS 28;

-- Look at atm withdrawl logs on the street the interviewee mentioned and on that particular day
SELECT amount FROM atm_transactions WHERE year IS 2021 AND month IS "7" AND day IS 28 AND atm_location IS "Leggett Street";

-- Look at the bakery's security cameras
SELECT activity FROM bakery_security_logs WHERE year IS 2021 AND month IS "7" AND day IS 28 AND hour is 10 AND minute BETWEEN 15 AND 25 ;

-- Set a time frame based on police reports of when the theif might've left the bakery and be caught on security camera
SELECT activity FROM bakery_security_logs WHERE year IS 2021 AND month IS "7" AND day IS 28 AND hour IS 10 AND minute BETWEEN 15 and 25;

-- Look at license plates that left the bakery
SELECT license_plate FROM bakery_security_logs WHERE year IS 2021 AND month IS "7" AND day IS 28 AND hour IS 10 AND minute BETWEEN 15 and 25;

-- Look at names associated with licnse plates
SELECT name FROM people WHERE license_plate IS "license_plate";

-- Name of suspects based on the license plates:
-- Vanessa
-- Bruce
-- Barry
-- Luca
-- Iman
-- Diana
-- Kelsey
-- Sofia

-- Look at calls made in that timeframe
SELECT receiver FROM phone_calls WHERE year IS 2021 AND month IS "7" AND day IS 28 AND duration < 60;

-- Phone numbers gathered
-- (996) 555-8899
-- (892) 555-8872
-- (375) 555-8161
-- (717) 555-1342
-- (676) 555-6554
-- (725) 555-3243
-- (910) 555-3251
-- (066) 555-9701
-- (704) 555-2131

-- Match phone numbers with suspect names
SELECT name FROM people WHERE phone_number IS "phone_number";

-- Phone number owners
-- Jack
-- Larry
-- Robin
-- Melissa
-- James
-- Philip
-- Jacqueline
-- Doris
-- Anna

-- Get bank account numbers of all withdraws on Legget Street on day of robbery
SELECT account_number
FROM atm_transactions
WHERE year
IS 2021
AND month
IS "7"
AND day
IS 28
AND atm_location
IS "Leggett Street"
AND transaction_type
IS "withdraw";

-- Bank account numbers
-- 28500762
-- 28296815
-- 76054385
-- 49610011
-- 16153065
-- 25506511
-- 81061156
-- 26013199

-- Match bank account numbers with names
SELECT name FROM people WHERE id = (SELECT person_id from bank_accounts WHERE account_number IS 'account_number')

-- Owners of bank accounts
-- Luca
-- Kenny
-- Taylor
-- Bruce
-- Brooke
-- Iman
-- Benista
-- Diana

-- New suspect list:
-- Luca - Passport#: 8496433585; Flight_ids: 11 36 48
-- Bruce - Passport#: 5773159633; Flight_ids: 36
-- Iman - Passport#: 7049073643; Flight_ids: 26
-- Diana - Passport#: 3592750733; Flight_ids: 18 24 54

-- Get passport number of all suspects
SELECT passport_number FROM people WHERE name IS "name";

-- Get flight ids
SELECT flight_id FROM passengers WHERE passport_number IS 'passport_number';

-- Match flight ids with flights
SELECT id FROM flights WHERE origin_airport_id =
(SELECT id FROM airports WHERE city IS "Fiftyville") AND  year IS 2021 AND month IS '7' AND day IS 29;

-- Updated suspect list:
-- Diana
-- Bruce
-- Luca

-- Get airport id of Fiftyville
SELECT id FROM airports WHERE city IS "Fiftyville"
-- id: 8

-- Get airport id of destination airport
SELECT destination_airport_id FROM flights WHERE origin_airport_id IS '8' AND id IS '18';

-- 6
-- 4

-- Get name of destination airport
SELECT city FROM airports WHERE id = (SELECT id FROM flights WHERE destination_airport_id IS '8');

-- Paris
-- New York City