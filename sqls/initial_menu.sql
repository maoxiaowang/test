### Run these SQL in your environment to initialize database TEST.

USE ecloud;
INSERT INTO dashboard_menu (name, display_name) VALUES ('dashboard', 'Dashboard');
INSERT INTO dashboard_menu (name, display_name) VALUES ('compute', 'Compute');
INSERT INTO dashboard_menu (name, display_name) VALUES ('storage', 'Storage');
INSERT INTO dashboard_menu (name, display_name) VALUES ('network', 'Network');
INSERT INTO dashboard_menu (name, display_name) VALUES ('user', 'User');

INSERT INTO dashboard_sub_menu(name, display_name, region_id) VALUES ('server', 'Server', 'compute');
INSERT INTO dashboard_sub_menu(name, display_name, region_id) VALUES ('host', 'Host', 'compute');
INSERT INTO dashboard_sub_menu(name, display_name, region_id) VALUES ('snapshot', 'Snapshot', 'compute');
INSERT INTO dashboard_sub_menu(name, display_name, region_id) VALUES ('image', 'Image', 'compute');
INSERT INTO dashboard_sub_menu(name, display_name, region_id) VALUES ('backup', 'Backup', 'compute');
INSERT INTO dashboard_sub_menu(name, display_name, region_id) VALUES ('storage', 'Storage', 'storage');
INSERT INTO dashboard_sub_menu(name, display_name, region_id) VALUES ('volume', 'Volume', 'storage');
INSERT INTO dashboard_sub_menu(name, display_name, region_id) VALUES ('network', 'Network', 'network');