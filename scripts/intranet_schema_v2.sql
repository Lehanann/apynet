-- ==========================================
-- SCHEMA INTRANET - Version 2
-- Avec gestion automatique des timestamps et jeu de données initial
-- ==========================================

CREATE SCHEMA IF NOT EXISTS intranet;
SET search_path TO intranet;

-- ==========================================
-- ENUMS
-- ==========================================
CREATE TYPE gender_enum AS ENUM ('m','f','x');
CREATE TYPE step_result_enum AS ENUM ('pending','accepted','rejected');
CREATE TYPE step_name_enum AS ENUM ('telephone1','interview1','interview2','interview3');
CREATE TYPE structure_type_enum AS ENUM ('department','service');

-- ==========================================
-- TABLES
-- ==========================================
CREATE TABLE corporates (
    id_corporate SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL UNIQUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE companies (
    id_company SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    corporate_id INT NOT NULL,
    UNIQUE(name, corporate_id),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (corporate_id) REFERENCES corporates(id_corporate)
);

CREATE TABLE sites (
    id_site SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    address TEXT,
    company_id INT NOT NULL,
    UNIQUE(name, company_id),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (company_id) REFERENCES companies(id_company)
);

CREATE TABLE meeting_rooms (
    id_meeting_room SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    site_id INT NOT NULL,
    UNIQUE(name, site_id),
    FOREIGN KEY (site_id) REFERENCES sites(id_site)
);

CREATE TABLE departments (
    id_department SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    company_id INT NOT NULL,
    UNIQUE(name, company_id),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (company_id) REFERENCES companies(id_company)
);

CREATE TABLE services (
    id_service SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    department_id INT NOT NULL,
    UNIQUE(name, department_id),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (department_id) REFERENCES departments(id_department)
);

CREATE TABLE professions (
    id_profession SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    default_account_allowed BOOLEAN DEFAULT FALSE,
    default_material_allowed BOOLEAN DEFAULT FALSE,
    default_material JSONB,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE positions (
    id_position SERIAL PRIMARY KEY,
    name VARCHAR(50) NOT NULL UNIQUE,
    description TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE employees (
    id_employee SERIAL PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    birth_date DATE CHECK (birth_date <= CURRENT_DATE),
    gender gender_enum NOT NULL DEFAULT 'x',
    address VARCHAR(255),
    personal_email VARCHAR(100) UNIQUE,
    personal_phone VARCHAR(20) CHECK (personal_phone ~ '^[0-9+ ]*$'),
    social_security_number VARCHAR(30) UNIQUE,
    emergency_contact_name VARCHAR(100),
    emergency_contact_phone VARCHAR(20),
    spouse_name VARCHAR(100),
    spouse_phone VARCHAR(20),
    profession_id INT NOT NULL,
    position_id INT NOT NULL,
    service_id INT,
    department_id INT,
    company_id INT NOT NULL,
    hire_date DATE DEFAULT CURRENT_DATE,
    leave_date DATE,
    archived BOOLEAN DEFAULT FALSE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (profession_id) REFERENCES professions(id_profession),
    FOREIGN KEY (position_id) REFERENCES positions(id_position),
    FOREIGN KEY (service_id) REFERENCES services(id_service),
    FOREIGN KEY (department_id) REFERENCES departments(id_department),
    FOREIGN KEY (company_id) REFERENCES companies(id_company)
);

CREATE TABLE user_accounts (
    id_user SERIAL PRIMARY KEY,
    username VARCHAR(50) NOT NULL UNIQUE,
    password VARCHAR(255) NOT NULL,
    work_email VARCHAR(100) UNIQUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    last_login TIMESTAMP,
    employee_id INT NOT NULL UNIQUE,
    FOREIGN KEY (employee_id) REFERENCES employees(id_employee)
);

CREATE TABLE system_roles (
    id_system_role SERIAL PRIMARY KEY,
    name VARCHAR(50) NOT NULL UNIQUE,
    description TEXT,
    permission_level SMALLINT NOT NULL DEFAULT 1 CHECK (permission_level >= 1),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE user_roles (
    user_id INT NOT NULL,
    system_role_id INT NOT NULL,
    PRIMARY KEY (user_id, system_role_id),
    FOREIGN KEY (user_id) REFERENCES user_accounts(id_user) ON DELETE CASCADE,
    FOREIGN KEY (system_role_id) REFERENCES system_roles(id_system_role) ON DELETE CASCADE
);

CREATE TABLE materials (
    id_material SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    type VARCHAR(50) NOT NULL,
    description TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE user_materials (
    user_id INT NOT NULL,
    material_id INT NOT NULL,
    assigned_date DATE DEFAULT CURRENT_DATE,
    return_date DATE,
    PRIMARY KEY(user_id, material_id),
    FOREIGN KEY (user_id) REFERENCES user_accounts(id_user),
    FOREIGN KEY (material_id) REFERENCES materials(id_material)
);

CREATE TABLE phone_numbers (
    id_phone SERIAL PRIMARY KEY,
    internal_number VARCHAR(4) UNIQUE,
    external_number VARCHAR(15),
    active BOOLEAN NOT NULL DEFAULT TRUE
);

CREATE TABLE phone_assignments ( 
    id_assignment SERIAL PRIMARY KEY, 
    phone_id INT NOT NULL UNIQUE, 
    assigned_type VARCHAR(30) NOT NULL, 
    assigned_id INT NOT NULL, 
    FOREIGN KEY (phone_id) REFERENCES phone_numbers(id_phone), 
    CHECK (
        assigned_type IN ('employee', 'service', 'meeting_room')
    )
);

CREATE TABLE candidates (
    id_candidate SERIAL PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    email VARCHAR(100),
    phone VARCHAR(20),
    archived BOOLEAN DEFAULT FALSE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE candidate_steps (
    id_step SERIAL PRIMARY KEY,
    candidate_id INT NOT NULL,
    step_name step_name_enum NOT NULL,
    result step_result_enum DEFAULT 'pending',
    step_date DATE DEFAULT CURRENT_DATE,
    FOREIGN KEY (candidate_id) REFERENCES candidates(id_candidate)
);

CREATE TABLE logs (
    id_log SERIAL PRIMARY KEY,
    user_id INT,
    action VARCHAR(255),
    table_name VARCHAR(100),
    record_id INT,
    action_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    ip_address VARCHAR(50),
    additional_info JSONB,
    FOREIGN KEY (user_id) REFERENCES user_accounts(id_user)
);

-- ==========================================
-- TRIGGERS POUR AUTOMATISER updated_at
-- ==========================================
CREATE OR REPLACE FUNCTION set_updated_at()
RETURNS TRIGGER AS $$
BEGIN
  NEW.updated_at = CURRENT_TIMESTAMP;
  RETURN NEW;
END;
$$ LANGUAGE plpgsql;

DO $$
DECLARE
    t TEXT;
BEGIN
    FOR t IN 
        SELECT unnest(ARRAY[
            'corporates','companies','departments','services',
            'professions','positions','employees',
            'user_accounts','system_roles','materials','candidates'
        ])
    LOOP
        EXECUTE format(
            'CREATE TRIGGER trg_update_timestamp_%I BEFORE UPDATE ON %I FOR EACH ROW EXECUTE FUNCTION set_updated_at();',
            t, t
        );
    END LOOP;
END $$;

-- ==========================================
-- JEU DE DONNÉES EXEMPLE
-- ==========================================
INSERT INTO corporates (name) VALUES ('prismaflex international');

INSERT INTO companies (name, corporate_id) VALUES 
('prismaflex france', 1),
('prismatronic', 1),
('fpi affiches', 1);
INSERT INTO sites (name, address, company_id) VALUES
("La Bourrie", "309 rte de Lyon, 69610 Haute-Rivoire", 1),
("Les Prébendes", "rte de Lyon, 69610 Haute-Rivoire",2),
("Wissous",NULL,1);

INSERT INTO meeting_rooms (name, site_id)
VALUES ('Salle Neptune', 1);

INSERT INTO departments (name, company_id) VALUES
('sytèmes d information', 1),
('ressources humaines', 1),
('direction',1),
('commercial',1),
('administratif et finance',1),
('production',1);

INSERT INTO services (name, department_id) VALUES
('développement', 1),
('it et infrastructure', 1),
('recrutement', 2),
('gestion des paies',2),
('achats', 3),
('commercial',4),
('adv',4),
('compatabilité',5),
('controle de gestion',5),
('impression', 6),
('confection',6),
('prepress',6);

INSERT INTO professions (name, default_account_allowed, default_material_allowed)
VALUES 
('technicien systemes et reseaux', TRUE, TRUE),
('développeur', TRUE, TRUE),
('responsable rh', TRUE, TRUE);

INSERT INTO positions (name)
VALUES ('employe'), ('responsable'), ('directeur');

INSERT INTO employees 
(first_name, last_name, birth_date, gender, personal_email, profession_id, position_id, service_id, department_id, company_id)
VALUES
('jean', 'dupont', '1990-02-14', 'm', 'jean.dupont@example.com', 2, 1, 1, 1, 1),
('sophie', 'martin', '1988-11-03', 'f', 'sophie.martin@example.com', 3, 2, 3, 2, 1),
('paul', 'durand', '1995-07-09', 'm', 'paul.durand@example.com', 1, 1, 2, 1, 1);

INSERT INTO system_roles (name, description, permission_level)
VALUES 
('admin', 'acces complet à toutes les sections', 5),
('rh', 'acces a la gestion rh', 3),
('user', 'acces standard', 1);

INSERT INTO user_accounts (username, password, work_email, employee_id)
VALUES
('jdupont', 'hashed_password1', 'jean.dupont@alpha.com', 1),
('smartin', 'hashed_password2', 'sophie.martin@alpha.com', 2),
('pdurand', 'hashed_password3', 'paul.durand@alpha.com', 3);

INSERT INTO user_roles (user_id, system_role_id) VALUES
(1, 1),
(2, 2),
(3, 3);

INSERT INTO materials (name, type, description)
VALUES
('Laptop Dell', 'Ordinateur', 'PC portable professionnel'),
('iPhone 13', 'Smartphone', 'Téléphone professionnel'),
('Casque Logitech', 'Accessoire', 'Casque audio');

INSERT INTO user_materials (user_id, material_id)
VALUES (1, 1), (1, 2), (3, 3);

INSERT INTO phone_numbers (internal_number, external_number) VALUES
('1001', '+33123456701'),
('1002', '+33123456702'),
('1003', '+33123456703'),
('2001', '+33123456801'),
('3001', '+33123456901');

INSERT INTO phone_assignments (phone_id, assigned_type, assigned_id)
VALUES
(1, 'employee', 1), -- Jean Dupont
(2, 'employee', 2); -- Sophie Martin

INSERT INTO phone_assignments (phone_id, assigned_type, assigned_id)
VALUES
(4, 'service', 2); -- Service "it et infrastructure"

INSERT INTO candidates (first_name, last_name, email, phone)
VALUES
('claire', 'lemoine', 'claire.lemoine@example.com', '+33612345678'),
('lucas', 'bernard', 'lucas.bernard@example.com', '+33698765432');

INSERT INTO candidate_steps (candidate_id, step_name, result)
VALUES
(1, 'telephone1', 'accepted'),
(1, 'interview1', 'pending'),
(2, 'telephone1', 'pending');


-- ==========================================
-- VUES POUR LES RESPONSABLES ET DIRECTEURS
-- ==========================================

-- Vue : responsables de départements
CREATE OR REPLACE VIEW intranet.v_department_responsibles AS
SELECT
    d.id_department,
    d.name AS department_name,
    c.name AS company_name,
    g.name AS corporate_name,
    e.id_employee,
    e.first_name,
    e.last_name,
    ua.work_email,
    e.personal_phone,
    p.name AS profession_name,
    pos.name AS position_name,
    e.hire_date
FROM intranet.employees e
JOIN intranet.departments d ON e.department_id = d.id_department
JOIN intranet.companies c ON d.company_id = c.id_company
JOIN intranet.corporates g ON c.corporate_id = g.id_corporate
JOIN intranet.professions p ON e.profession_id = p.id_profession
JOIN intranet.positions pos ON e.position_id = pos.id_position
LEFT JOIN intranet.user_accounts ua ON e.id_employee = ua.employee_id
WHERE pos.name IN ('responsable', 'directeur')
ORDER BY g.name, c.name, d.name;

-- Vue : responsables de services
CREATE OR REPLACE VIEW intranet.v_service_responsibles AS
SELECT
    s.id_service,
    s.name AS service_name,
    d.name AS department_name,
    c.name AS company_name,
    g.name AS corporate_name,
    e.id_employee,
    e.first_name,
    e.last_name,
    ua.work_email,
    e.personal_phone,
    p.name AS profession_name,
    pos.name AS position_name,
    e.hire_date
FROM intranet.employees e
JOIN intranet.services s ON e.service_id = s.id_service
JOIN intranet.departments d ON s.department_id = d.id_department
JOIN intranet.companies c ON d.company_id = c.id_company
JOIN intranet.corporates g ON c.corporate_id = g.id_corporate
JOIN intranet.professions p ON e.profession_id = p.id_profession
JOIN intranet.positions pos ON e.position_id = pos.id_position
LEFT JOIN intranet.user_accounts ua ON e.id_employee = ua.employee_id
WHERE pos.name IN ('responsable', 'directeur')
ORDER BY g.name, c.name, d.name, s.name;

-- Vue combinée : responsables des départements et services
CREATE OR REPLACE VIEW intranet.v_structure_responsibles AS
SELECT
    'department'::TEXT AS structure_type,
    d.id_department AS structure_id,
    d.name AS structure_name,
    c.name AS company_name,
    g.name AS corporate_name,
    e.id_employee,
    e.first_name,
    e.last_name,
    ua.work_email,
    e.personal_phone,
    p.name AS profession_name,
    pos.name AS position_name,
    e.hire_date
FROM intranet.employees e
JOIN intranet.departments d ON e.department_id = d.id_department
JOIN intranet.companies c ON d.company_id = c.id_company
JOIN intranet.corporates g ON c.corporate_id = g.id_corporate
JOIN intranet.professions p ON e.profession_id = p.id_profession
JOIN intranet.positions pos ON e.position_id = pos.id_position
LEFT JOIN intranet.user_accounts ua ON e.id_employee = ua.employee_id
WHERE pos.name IN ('responsable', 'directeur')

UNION ALL

SELECT
    'service'::TEXT AS structure_type,
    s.id_service AS structure_id,
    s.name AS structure_name,
    c.name AS company_name,
    g.name AS corporate_name,
    e.id_employee,
    e.first_name,
    e.last_name,
    ua.work_email,
    e.personal_phone,
    p.name AS profession_name,
    pos.name AS position_name,
    e.hire_date
FROM intranet.employees e
JOIN intranet.services s ON e.service_id = s.id_service
JOIN intranet.departments d ON s.department_id = d.id_department
JOIN intranet.companies c ON d.company_id = c.id_company
JOIN intranet.corporates g ON c.corporate_id = g.id_corporate
JOIN intranet.professions p ON e.profession_id = p.id_profession
JOIN intranet.positions pos ON e.position_id = pos.id_position
LEFT JOIN intranet.user_accounts ua ON e.id_employee = ua.employee_id
WHERE pos.name IN ('responsable', 'directeur');
