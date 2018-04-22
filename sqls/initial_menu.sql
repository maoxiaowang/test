-- Run these SQL in your environment to initialize database TEST.

USE ecloud;
INSERT INTO dashboard_menu (name, display_name) VALUES ('dashboard', 'Dashboard');
INSERT INTO dashboard_menu (name, display_name) VALUES ('compute', 'Compute');
INSERT INTO dashboard_menu (name, display_name) VALUES ('storage', 'Storage');
INSERT INTO dashboard_menu (name, display_name) VALUES ('network', 'Network');
INSERT INTO dashboard_menu (name, display_name) VALUES ('user', 'User');

INSERT INTO dashboard_sub_menu(name, display_name, menu_id) VALUES ('server', 'Server', 2);
INSERT INTO dashboard_sub_menu(name, display_name, menu_id) VALUES ('host', 'Host', 2);
INSERT INTO dashboard_sub_menu(name, display_name, menu_id) VALUES ('snapshot', 'Snapshot', 2);
INSERT INTO dashboard_sub_menu(name, display_name, menu_id) VALUES ('image', 'Image', 2);
INSERT INTO dashboard_sub_menu(name, display_name, menu_id) VALUES ('backup', 'Backup', 2);
INSERT INTO dashboard_sub_menu(name, display_name, menu_id) VALUES ('storage', 'Storage', 3);
INSERT INTO dashboard_sub_menu(name, display_name, menu_id) VALUES ('volume', 'Volume', 3);
INSERT INTO dashboard_sub_menu(name, display_name, menu_id) VALUES ('network', 'Network', 4);