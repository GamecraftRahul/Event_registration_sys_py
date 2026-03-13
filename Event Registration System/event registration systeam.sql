-- ============================================================
-- EVENT REGISTRATION SYSTEM DATABASE
-- ============================================================

-- 1. Create Database
CREATE DATABASE IF NOT EXISTS event_system;

-- 2. Select Database
USE event_system;

-- 3. Create Table
CREATE TABLE IF NOT EXISTS participants (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(150) NOT NULL,
    phone VARCHAR(20) NOT NULL,
    event_name VARCHAR(150) NOT NULL,
    reg_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- 4. Insert Sample Data
INSERT INTO participants (name, email, phone, event_name) VALUES
('Rahul Verma', 'rahul.verma@example.com', '9876543210', 'Tech Expo 2025'),
('Priya Sharma', 'priya.sharma@example.com', '9123456780', 'Startup Meetup'),
('Aman Singh', 'aman.singh@example.com', '9988776655', 'AI Workshop'),
('Sneha Patil', 'sneha.patil@example.com', '9001122334', 'Developer Summit'),
('Rohan Mehta', 'rohan.mehta@example.com', '7890456123', 'Digital Marketing Bootcamp');
