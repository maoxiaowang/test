-- Run these SQL in your environment to initialize database TEST.

USE ecloud;
INSERT INTO dashboard_menu (id, name, display_name) VALUES (1, 'dashboard', 'Dashboard');
INSERT INTO dashboard_menu (id, name, display_name) VALUES (2, 'compute', 'Compute');
INSERT INTO dashboard_menu (id, name, display_name) VALUES (3, 'storage', 'Storage');
INSERT INTO dashboard_menu (id, name, display_name) VALUES (4, 'network', 'Network');
INSERT INTO dashboard_menu (id, name, display_name) VALUES (5, 'identity', 'Identity');

INSERT INTO dashboard_sub_menu(name, display_name, menu_id) VALUES ('server', 'Server', 2);
INSERT INTO dashboard_sub_menu(name, display_name, menu_id) VALUES ('host', 'Host', 2);
INSERT INTO dashboard_sub_menu(name, display_name, menu_id) VALUES ('snapshot', 'Snapshot', 2);
INSERT INTO dashboard_sub_menu(name, display_name, menu_id) VALUES ('image', 'Image', 2);
INSERT INTO dashboard_sub_menu(name, display_name, menu_id) VALUES ('backup', 'Backup', 2);
INSERT INTO dashboard_sub_menu(name, display_name, menu_id) VALUES ('storage', 'Storage', 3);
INSERT INTO dashboard_sub_menu(name, display_name, menu_id) VALUES ('volume', 'Volume', 3);
INSERT INTO dashboard_sub_menu(name, display_name, menu_id) VALUES ('network', 'Network', 4);
INSERT INTO dashboard_sub_menu(name, display_name, menu_id) VALUES ('user', 'User', 5);
INSERT INTO dashboard_sub_menu(name, display_name, menu_id) VALUES ('group', 'Group', 5);
INSERT INTO dashboard_sub_menu(name, display_name, menu_id) VALUES ('permission', 'Permission', 5);