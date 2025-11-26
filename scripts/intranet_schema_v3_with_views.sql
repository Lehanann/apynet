

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
