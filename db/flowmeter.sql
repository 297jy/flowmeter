/*
 Navicat Premium Data Transfer

 Source Server         : test
 Source Server Type    : MySQL
 Source Server Version : 80019
 Source Host           : localhost:3306
 Source Schema         : flowmeter

 Target Server Type    : MySQL
 Target Server Version : 80019
 File Encoding         : 65001

 Date: 18/02/2020 18:24:07
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for auth_group
-- ----------------------------
DROP TABLE IF EXISTS `auth_group`;
CREATE TABLE `auth_group`  (
  `id` int(0) NOT NULL AUTO_INCREMENT,
  `name` varchar(150) CHARACTER SET utf8 COLLATE utf8_bin NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `name`(`name`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_bin ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for auth_group_permissions
-- ----------------------------
DROP TABLE IF EXISTS `auth_group_permissions`;
CREATE TABLE `auth_group_permissions`  (
  `id` int(0) NOT NULL AUTO_INCREMENT,
  `group_id` int(0) NOT NULL,
  `permission_id` int(0) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `auth_group_permissions_group_id_permission_id_0cd325b0_uniq`(`group_id`, `permission_id`) USING BTREE,
  INDEX `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm`(`permission_id`) USING BTREE,
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8 COLLATE = utf8_bin ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for auth_permission
-- ----------------------------
DROP TABLE IF EXISTS `auth_permission`;
CREATE TABLE `auth_permission`  (
  `id` int(0) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) CHARACTER SET utf8 COLLATE utf8_bin NOT NULL,
  `content_type_id` int(0) NOT NULL,
  `codename` varchar(100) CHARACTER SET utf8 COLLATE utf8_bin NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `auth_permission_content_type_id_codename_01ab375a_uniq`(`content_type_id`, `codename`) USING BTREE,
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 125 CHARACTER SET = utf8 COLLATE = utf8_bin ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of auth_permission
-- ----------------------------
INSERT INTO `auth_permission` VALUES (1, 'Can add log entry', 1, 'add_logentry');
INSERT INTO `auth_permission` VALUES (2, 'Can change log entry', 1, 'change_logentry');
INSERT INTO `auth_permission` VALUES (3, 'Can delete log entry', 1, 'delete_logentry');
INSERT INTO `auth_permission` VALUES (4, 'Can view log entry', 1, 'view_logentry');
INSERT INTO `auth_permission` VALUES (5, 'Can add permission', 2, 'add_permission');
INSERT INTO `auth_permission` VALUES (6, 'Can change permission', 2, 'change_permission');
INSERT INTO `auth_permission` VALUES (7, 'Can delete permission', 2, 'delete_permission');
INSERT INTO `auth_permission` VALUES (8, 'Can view permission', 2, 'view_permission');
INSERT INTO `auth_permission` VALUES (9, 'Can add group', 3, 'add_group');
INSERT INTO `auth_permission` VALUES (10, 'Can change group', 3, 'change_group');
INSERT INTO `auth_permission` VALUES (11, 'Can delete group', 3, 'delete_group');
INSERT INTO `auth_permission` VALUES (12, 'Can view group', 3, 'view_group');
INSERT INTO `auth_permission` VALUES (13, 'Can add user', 4, 'add_user');
INSERT INTO `auth_permission` VALUES (14, 'Can change user', 4, 'change_user');
INSERT INTO `auth_permission` VALUES (15, 'Can delete user', 4, 'delete_user');
INSERT INTO `auth_permission` VALUES (16, 'Can view user', 4, 'view_user');
INSERT INTO `auth_permission` VALUES (17, 'Can add content type', 5, 'add_contenttype');
INSERT INTO `auth_permission` VALUES (18, 'Can change content type', 5, 'change_contenttype');
INSERT INTO `auth_permission` VALUES (19, 'Can delete content type', 5, 'delete_contenttype');
INSERT INTO `auth_permission` VALUES (20, 'Can view content type', 5, 'view_contenttype');
INSERT INTO `auth_permission` VALUES (21, 'Can add session', 6, 'add_session');
INSERT INTO `auth_permission` VALUES (22, 'Can change session', 6, 'change_session');
INSERT INTO `auth_permission` VALUES (23, 'Can delete session', 6, 'delete_session');
INSERT INTO `auth_permission` VALUES (24, 'Can view session', 6, 'view_session');
INSERT INTO `auth_permission` VALUES (25, 'Can add auth', 7, 'add_auth');
INSERT INTO `auth_permission` VALUES (26, 'Can change auth', 7, 'change_auth');
INSERT INTO `auth_permission` VALUES (27, 'Can delete auth', 7, 'delete_auth');
INSERT INTO `auth_permission` VALUES (28, 'Can view auth', 7, 'view_auth');
INSERT INTO `auth_permission` VALUES (29, 'Can add auth category', 8, 'add_authcategory');
INSERT INTO `auth_permission` VALUES (30, 'Can change auth category', 8, 'change_authcategory');
INSERT INTO `auth_permission` VALUES (31, 'Can delete auth category', 8, 'delete_authcategory');
INSERT INTO `auth_permission` VALUES (32, 'Can view auth category', 8, 'view_authcategory');
INSERT INTO `auth_permission` VALUES (33, 'Can add data frame format', 9, 'add_dataframeformat');
INSERT INTO `auth_permission` VALUES (34, 'Can change data frame format', 9, 'change_dataframeformat');
INSERT INTO `auth_permission` VALUES (35, 'Can delete data frame format', 9, 'delete_dataframeformat');
INSERT INTO `auth_permission` VALUES (36, 'Can view data frame format', 9, 'view_dataframeformat');
INSERT INTO `auth_permission` VALUES (37, 'Can add dtu', 10, 'add_dtu');
INSERT INTO `auth_permission` VALUES (38, 'Can change dtu', 10, 'change_dtu');
INSERT INTO `auth_permission` VALUES (39, 'Can delete dtu', 10, 'delete_dtu');
INSERT INTO `auth_permission` VALUES (40, 'Can view dtu', 10, 'view_dtu');
INSERT INTO `auth_permission` VALUES (41, 'Can add role', 11, 'add_role');
INSERT INTO `auth_permission` VALUES (42, 'Can change role', 11, 'change_role');
INSERT INTO `auth_permission` VALUES (43, 'Can delete role', 11, 'delete_role');
INSERT INTO `auth_permission` VALUES (44, 'Can view role', 11, 'view_role');
INSERT INTO `auth_permission` VALUES (45, 'Can add user', 12, 'add_user');
INSERT INTO `auth_permission` VALUES (46, 'Can change user', 12, 'change_user');
INSERT INTO `auth_permission` VALUES (47, 'Can delete user', 12, 'delete_user');
INSERT INTO `auth_permission` VALUES (48, 'Can view user', 12, 'view_user');
INSERT INTO `auth_permission` VALUES (49, 'Can add role auth', 13, 'add_roleauth');
INSERT INTO `auth_permission` VALUES (50, 'Can change role auth', 13, 'change_roleauth');
INSERT INTO `auth_permission` VALUES (51, 'Can delete role auth', 13, 'delete_roleauth');
INSERT INTO `auth_permission` VALUES (52, 'Can view role auth', 13, 'view_roleauth');
INSERT INTO `auth_permission` VALUES (53, 'Can add protocol', 14, 'add_protocol');
INSERT INTO `auth_permission` VALUES (54, 'Can change protocol', 14, 'change_protocol');
INSERT INTO `auth_permission` VALUES (55, 'Can delete protocol', 14, 'delete_protocol');
INSERT INTO `auth_permission` VALUES (56, 'Can view protocol', 14, 'view_protocol');
INSERT INTO `auth_permission` VALUES (57, 'Can add navigation bar', 15, 'add_navigationbar');
INSERT INTO `auth_permission` VALUES (58, 'Can change navigation bar', 15, 'change_navigationbar');
INSERT INTO `auth_permission` VALUES (59, 'Can delete navigation bar', 15, 'delete_navigationbar');
INSERT INTO `auth_permission` VALUES (60, 'Can view navigation bar', 15, 'view_navigationbar');
INSERT INTO `auth_permission` VALUES (61, 'Can add meter', 16, 'add_meter');
INSERT INTO `auth_permission` VALUES (62, 'Can change meter', 16, 'change_meter');
INSERT INTO `auth_permission` VALUES (63, 'Can delete meter', 16, 'delete_meter');
INSERT INTO `auth_permission` VALUES (64, 'Can view meter', 16, 'view_meter');
INSERT INTO `auth_permission` VALUES (65, 'Can add dtu region', 17, 'add_dturegion');
INSERT INTO `auth_permission` VALUES (66, 'Can change dtu region', 17, 'change_dturegion');
INSERT INTO `auth_permission` VALUES (67, 'Can delete dtu region', 17, 'delete_dturegion');
INSERT INTO `auth_permission` VALUES (68, 'Can view dtu region', 17, 'view_dturegion');
INSERT INTO `auth_permission` VALUES (69, 'Can add data field', 18, 'add_datafield');
INSERT INTO `auth_permission` VALUES (70, 'Can change data field', 18, 'change_datafield');
INSERT INTO `auth_permission` VALUES (71, 'Can delete data field', 18, 'delete_datafield');
INSERT INTO `auth_permission` VALUES (72, 'Can view data field', 18, 'view_datafield');
INSERT INTO `auth_permission` VALUES (73, 'Can add interval', 19, 'add_intervalschedule');
INSERT INTO `auth_permission` VALUES (74, 'Can change interval', 19, 'change_intervalschedule');
INSERT INTO `auth_permission` VALUES (75, 'Can delete interval', 19, 'delete_intervalschedule');
INSERT INTO `auth_permission` VALUES (76, 'Can view interval', 19, 'view_intervalschedule');
INSERT INTO `auth_permission` VALUES (77, 'Can add crontab', 20, 'add_crontabschedule');
INSERT INTO `auth_permission` VALUES (78, 'Can change crontab', 20, 'change_crontabschedule');
INSERT INTO `auth_permission` VALUES (79, 'Can delete crontab', 20, 'delete_crontabschedule');
INSERT INTO `auth_permission` VALUES (80, 'Can view crontab', 20, 'view_crontabschedule');
INSERT INTO `auth_permission` VALUES (81, 'Can add periodic task', 21, 'add_periodictask');
INSERT INTO `auth_permission` VALUES (82, 'Can change periodic task', 21, 'change_periodictask');
INSERT INTO `auth_permission` VALUES (83, 'Can delete periodic task', 21, 'delete_periodictask');
INSERT INTO `auth_permission` VALUES (84, 'Can view periodic task', 21, 'view_periodictask');
INSERT INTO `auth_permission` VALUES (85, 'Can add periodic tasks', 22, 'add_periodictasks');
INSERT INTO `auth_permission` VALUES (86, 'Can change periodic tasks', 22, 'change_periodictasks');
INSERT INTO `auth_permission` VALUES (87, 'Can delete periodic tasks', 22, 'delete_periodictasks');
INSERT INTO `auth_permission` VALUES (88, 'Can view periodic tasks', 22, 'view_periodictasks');
INSERT INTO `auth_permission` VALUES (89, 'Can add task state', 23, 'add_taskmeta');
INSERT INTO `auth_permission` VALUES (90, 'Can change task state', 23, 'change_taskmeta');
INSERT INTO `auth_permission` VALUES (91, 'Can delete task state', 23, 'delete_taskmeta');
INSERT INTO `auth_permission` VALUES (92, 'Can view task state', 23, 'view_taskmeta');
INSERT INTO `auth_permission` VALUES (93, 'Can add saved group result', 24, 'add_tasksetmeta');
INSERT INTO `auth_permission` VALUES (94, 'Can change saved group result', 24, 'change_tasksetmeta');
INSERT INTO `auth_permission` VALUES (95, 'Can delete saved group result', 24, 'delete_tasksetmeta');
INSERT INTO `auth_permission` VALUES (96, 'Can view saved group result', 24, 'view_tasksetmeta');
INSERT INTO `auth_permission` VALUES (97, 'Can add task', 25, 'add_taskstate');
INSERT INTO `auth_permission` VALUES (98, 'Can change task', 25, 'change_taskstate');
INSERT INTO `auth_permission` VALUES (99, 'Can delete task', 25, 'delete_taskstate');
INSERT INTO `auth_permission` VALUES (100, 'Can view task', 25, 'view_taskstate');
INSERT INTO `auth_permission` VALUES (101, 'Can add worker', 26, 'add_workerstate');
INSERT INTO `auth_permission` VALUES (102, 'Can change worker', 26, 'change_workerstate');
INSERT INTO `auth_permission` VALUES (103, 'Can delete worker', 26, 'delete_workerstate');
INSERT INTO `auth_permission` VALUES (104, 'Can view worker', 26, 'view_workerstate');
INSERT INTO `auth_permission` VALUES (105, 'Can add alarm log', 27, 'add_alarmlog');
INSERT INTO `auth_permission` VALUES (106, 'Can change alarm log', 27, 'change_alarmlog');
INSERT INTO `auth_permission` VALUES (107, 'Can delete alarm log', 27, 'delete_alarmlog');
INSERT INTO `auth_permission` VALUES (108, 'Can view alarm log', 27, 'view_alarmlog');
INSERT INTO `auth_permission` VALUES (109, 'Can add opr log', 28, 'add_oprlog');
INSERT INTO `auth_permission` VALUES (110, 'Can change opr log', 28, 'change_oprlog');
INSERT INTO `auth_permission` VALUES (111, 'Can delete opr log', 28, 'delete_oprlog');
INSERT INTO `auth_permission` VALUES (112, 'Can view opr log', 28, 'view_oprlog');
INSERT INTO `auth_permission` VALUES (113, 'Can add login log', 29, 'add_loginlog');
INSERT INTO `auth_permission` VALUES (114, 'Can change login log', 29, 'change_loginlog');
INSERT INTO `auth_permission` VALUES (115, 'Can delete login log', 29, 'delete_loginlog');
INSERT INTO `auth_permission` VALUES (116, 'Can view login log', 29, 'view_loginlog');
INSERT INTO `auth_permission` VALUES (117, 'Can add valve', 30, 'add_valve');
INSERT INTO `auth_permission` VALUES (118, 'Can change valve', 30, 'change_valve');
INSERT INTO `auth_permission` VALUES (119, 'Can delete valve', 30, 'delete_valve');
INSERT INTO `auth_permission` VALUES (120, 'Can view valve', 30, 'view_valve');
INSERT INTO `auth_permission` VALUES (121, 'Can add control register', 31, 'add_controlregister');
INSERT INTO `auth_permission` VALUES (122, 'Can change control register', 31, 'change_controlregister');
INSERT INTO `auth_permission` VALUES (123, 'Can delete control register', 31, 'delete_controlregister');
INSERT INTO `auth_permission` VALUES (124, 'Can view control register', 31, 'view_controlregister');
INSERT INTO `auth_permission` VALUES (125, 'Can add meter state', 32, 'add_meterstate');
INSERT INTO `auth_permission` VALUES (126, 'Can change meter state', 32, 'change_meterstate');
INSERT INTO `auth_permission` VALUES (127, 'Can delete meter state', 32, 'delete_meterstate');
INSERT INTO `auth_permission` VALUES (128, 'Can view meter state', 32, 'view_meterstate');

-- ----------------------------
-- Table structure for auth_user
-- ----------------------------
DROP TABLE IF EXISTS `auth_user`;
CREATE TABLE `auth_user`  (
  `id` int(0) NOT NULL AUTO_INCREMENT,
  `password` varchar(128) CHARACTER SET utf8 COLLATE utf8_bin NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) CHARACTER SET utf8 COLLATE utf8_bin NOT NULL,
  `first_name` varchar(30) CHARACTER SET utf8 COLLATE utf8_bin NOT NULL,
  `last_name` varchar(150) CHARACTER SET utf8 COLLATE utf8_bin NOT NULL,
  `email` varchar(254) CHARACTER SET utf8 COLLATE utf8_bin NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `username`(`username`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_bin ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for auth_user_groups
-- ----------------------------
DROP TABLE IF EXISTS `auth_user_groups`;
CREATE TABLE `auth_user_groups`  (
  `id` int(0) NOT NULL AUTO_INCREMENT,
  `user_id` int(0) NOT NULL,
  `group_id` int(0) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `auth_user_groups_user_id_group_id_94350c0c_uniq`(`user_id`, `group_id`) USING BTREE,
  INDEX `auth_user_groups_group_id_97559544_fk_auth_group_id`(`group_id`) USING BTREE,
  CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_bin ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for auth_user_user_permissions
-- ----------------------------
DROP TABLE IF EXISTS `auth_user_user_permissions`;
CREATE TABLE `auth_user_user_permissions`  (
  `id` int(0) NOT NULL AUTO_INCREMENT,
  `user_id` int(0) NOT NULL,
  `permission_id` int(0) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq`(`user_id`, `permission_id`) USING BTREE,
  INDEX `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm`(`permission_id`) USING BTREE,
  CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8 COLLATE = utf8_bin ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for celery_taskmeta
-- ----------------------------
DROP TABLE IF EXISTS `celery_taskmeta`;
CREATE TABLE `celery_taskmeta`  (
  `id` int(0) NOT NULL AUTO_INCREMENT,
  `task_id` varchar(255) CHARACTER SET utf8 COLLATE utf8_bin NOT NULL,
  `status` varchar(50) CHARACTER SET utf8 COLLATE utf8_bin NOT NULL,
  `result` longtext CHARACTER SET utf8 COLLATE utf8_bin,
  `date_done` datetime(6) NOT NULL,
  `traceback` longtext CHARACTER SET utf8 COLLATE utf8_bin,
  `hidden` tinyint(1) NOT NULL,
  `meta` longtext CHARACTER SET utf8 COLLATE utf8_bin,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `task_id`(`task_id`) USING BTREE,
  INDEX `celery_taskmeta_hidden_23fd02dc`(`hidden`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_bin ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for celery_tasksetmeta
-- ----------------------------
DROP TABLE IF EXISTS `celery_tasksetmeta`;
CREATE TABLE `celery_tasksetmeta`  (
  `id` int(0) NOT NULL AUTO_INCREMENT,
  `taskset_id` varchar(255) CHARACTER SET utf8 COLLATE utf8_bin NOT NULL,
  `result` longtext CHARACTER SET utf8 COLLATE utf8_bin NOT NULL,
  `date_done` datetime(6) NOT NULL,
  `hidden` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `taskset_id`(`taskset_id`) USING BTREE,
  INDEX `celery_tasksetmeta_hidden_593cfc24`(`hidden`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_bin ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for django_admin_log
-- ----------------------------
DROP TABLE IF EXISTS `django_admin_log`;
CREATE TABLE `django_admin_log`  (
  `id` int(0) NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext CHARACTER SET utf8 COLLATE utf8_bin,
  `object_repr` varchar(200) CHARACTER SET utf8 COLLATE utf8_bin NOT NULL,
  `action_flag` smallint unsigned NOT NULL,
  `change_message` longtext CHARACTER SET utf8 COLLATE utf8_bin NOT NULL,
  `content_type_id` int(0) DEFAULT NULL,
  `user_id` int(0) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  INDEX `django_admin_log_content_type_id_c4bce8eb_fk_django_co`(`content_type_id`) USING BTREE,
  INDEX `django_admin_log_user_id_c564eba6_fk_auth_user_id`(`user_id`) USING BTREE,
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8 COLLATE = utf8_bin ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for django_content_type
-- ----------------------------
DROP TABLE IF EXISTS `django_content_type`;
CREATE TABLE `django_content_type`  (
  `id` int(0) NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) CHARACTER SET utf8 COLLATE utf8_bin NOT NULL,
  `model` varchar(100) CHARACTER SET utf8 COLLATE utf8_bin NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `django_content_type_app_label_model_76bd3d3b_uniq`(`app_label`, `model`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 32 CHARACTER SET = utf8 COLLATE = utf8_bin ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of django_content_type
-- ----------------------------
INSERT INTO `django_content_type` VALUES (1, 'admin', 'logentry');
INSERT INTO `django_content_type` VALUES (3, 'auth', 'group');
INSERT INTO `django_content_type` VALUES (2, 'auth', 'permission');
INSERT INTO `django_content_type` VALUES (4, 'auth', 'user');
INSERT INTO `django_content_type` VALUES (5, 'contenttypes', 'contenttype');
INSERT INTO `django_content_type` VALUES (20, 'djcelery', 'crontabschedule');
INSERT INTO `django_content_type` VALUES (19, 'djcelery', 'intervalschedule');
INSERT INTO `django_content_type` VALUES (21, 'djcelery', 'periodictask');
INSERT INTO `django_content_type` VALUES (22, 'djcelery', 'periodictasks');
INSERT INTO `django_content_type` VALUES (23, 'djcelery', 'taskmeta');
INSERT INTO `django_content_type` VALUES (24, 'djcelery', 'tasksetmeta');
INSERT INTO `django_content_type` VALUES (25, 'djcelery', 'taskstate');
INSERT INTO `django_content_type` VALUES (26, 'djcelery', 'workerstate');
INSERT INTO `django_content_type` VALUES (27, 'flowmeter', 'alarmlog');
INSERT INTO `django_content_type` VALUES (7, 'flowmeter', 'auth');
INSERT INTO `django_content_type` VALUES (8, 'flowmeter', 'authcategory');
INSERT INTO `django_content_type` VALUES (31, 'flowmeter', 'controlregister');
INSERT INTO `django_content_type` VALUES (18, 'flowmeter', 'datafield');
INSERT INTO `django_content_type` VALUES (9, 'flowmeter', 'dataframeformat');
INSERT INTO `django_content_type` VALUES (10, 'flowmeter', 'dtu');
INSERT INTO `django_content_type` VALUES (17, 'flowmeter', 'dturegion');
INSERT INTO `django_content_type` VALUES (29, 'flowmeter', 'loginlog');
INSERT INTO `django_content_type` VALUES (16, 'flowmeter', 'meter');
INSERT INTO `django_content_type` VALUES (32, 'flowmeter', 'meterstate');
INSERT INTO `django_content_type` VALUES (15, 'flowmeter', 'navigationbar');
INSERT INTO `django_content_type` VALUES (28, 'flowmeter', 'oprlog');
INSERT INTO `django_content_type` VALUES (14, 'flowmeter', 'protocol');
INSERT INTO `django_content_type` VALUES (11, 'flowmeter', 'role');
INSERT INTO `django_content_type` VALUES (13, 'flowmeter', 'roleauth');
INSERT INTO `django_content_type` VALUES (12, 'flowmeter', 'user');
INSERT INTO `django_content_type` VALUES (30, 'flowmeter', 'valve');
INSERT INTO `django_content_type` VALUES (6, 'sessions', 'session');

-- ----------------------------
-- Table structure for django_migrations
-- ----------------------------
DROP TABLE IF EXISTS `django_migrations`;
CREATE TABLE `django_migrations`  (
  `id` int(0) NOT NULL AUTO_INCREMENT,
  `app` varchar(255) CHARACTER SET utf8 COLLATE utf8_bin NOT NULL,
  `name` varchar(255) CHARACTER SET utf8 COLLATE utf8_bin NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 35 CHARACTER SET = utf8 COLLATE = utf8_bin ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of django_migrations
-- ----------------------------
INSERT INTO `django_migrations` VALUES (1, 'contenttypes', '0001_initial', '2020-02-14 17:00:39.227105');
INSERT INTO `django_migrations` VALUES (2, 'auth', '0001_initial', '2020-02-14 17:00:39.373238');
INSERT INTO `django_migrations` VALUES (3, 'admin', '0001_initial', '2020-02-14 17:00:39.795623');
INSERT INTO `django_migrations` VALUES (4, 'admin', '0002_logentry_remove_auto_add', '2020-02-14 17:00:39.914732');
INSERT INTO `django_migrations` VALUES (5, 'admin', '0003_logentry_add_action_flag_choices', '2020-02-14 17:00:39.927743');
INSERT INTO `django_migrations` VALUES (6, 'contenttypes', '0002_remove_content_type_name', '2020-02-14 17:00:40.025832');
INSERT INTO `django_migrations` VALUES (7, 'auth', '0002_alter_permission_name_max_length', '2020-02-14 17:00:40.080882');
INSERT INTO `django_migrations` VALUES (8, 'auth', '0003_alter_user_email_max_length', '2020-02-14 17:00:40.139936');
INSERT INTO `django_migrations` VALUES (9, 'auth', '0004_alter_user_username_opts', '2020-02-14 17:00:40.148944');
INSERT INTO `django_migrations` VALUES (10, 'auth', '0005_alter_user_last_login_null', '2020-02-14 17:00:40.199991');
INSERT INTO `django_migrations` VALUES (11, 'auth', '0006_require_contenttypes_0002', '2020-02-14 17:00:40.202994');
INSERT INTO `django_migrations` VALUES (12, 'auth', '0007_alter_validators_add_error_messages', '2020-02-14 17:00:40.212002');
INSERT INTO `django_migrations` VALUES (13, 'auth', '0008_alter_user_username_max_length', '2020-02-14 17:00:40.270055');
INSERT INTO `django_migrations` VALUES (14, 'auth', '0009_alter_user_last_name_max_length', '2020-02-14 17:00:40.351129');
INSERT INTO `django_migrations` VALUES (15, 'auth', '0010_alter_group_name_max_length', '2020-02-14 17:00:40.402175');
INSERT INTO `django_migrations` VALUES (16, 'auth', '0011_update_proxy_permissions', '2020-02-14 17:00:40.411183');
INSERT INTO `django_migrations` VALUES (17, 'flowmeter', '0001_initial', '2020-02-14 17:00:40.851585');
INSERT INTO `django_migrations` VALUES (18, 'sessions', '0001_initial', '2020-02-14 17:00:41.259956');
INSERT INTO `django_migrations` VALUES (19, 'djcelery', '0001_initial', '2020-02-15 15:01:00.824696');
INSERT INTO `django_migrations` VALUES (20, 'flowmeter', '0002_meter_user', '2020-02-16 20:56:07.405837');
INSERT INTO `django_migrations` VALUES (21, 'flowmeter', '0003_alarmlog_loginlog_oprlog', '2020-02-16 20:56:07.556975');
INSERT INTO `django_migrations` VALUES (22, 'flowmeter', '0004_auto_20200216_2108', '2020-02-16 21:08:16.237744');
INSERT INTO `django_migrations` VALUES (23, 'flowmeter', '0005_auto_20200216_2128', '2020-02-16 21:28:42.543914');
INSERT INTO `django_migrations` VALUES (24, 'flowmeter', '0006_auto_20200216_2130', '2020-02-16 21:30:13.904192');
INSERT INTO `django_migrations` VALUES (25, 'flowmeter', '0007_remove_alarmlog_state', '2020-02-16 21:41:26.760024');
INSERT INTO `django_migrations` VALUES (26, 'flowmeter', '0008_remove_alarmlog_meter_user', '2020-02-16 21:44:08.771277');
INSERT INTO `django_migrations` VALUES (27, 'flowmeter', '0009_auto_20200216_2219', '2020-02-16 22:19:29.782274');
INSERT INTO `django_migrations` VALUES (28, 'flowmeter', '0010_auto_20200216_2239', '2020-02-16 22:39:15.973008');
INSERT INTO `django_migrations` VALUES (29, 'flowmeter', '0011_auto_20200217_1742', '2020-02-17 17:42:57.579217');
INSERT INTO `django_migrations` VALUES (30, 'flowmeter', '0012_auto_20200217_1843', '2020-02-17 18:44:05.400811');
INSERT INTO `django_migrations` VALUES (31, 'flowmeter', '0013_delete_protocol', '2020-02-17 20:30:36.828978');
INSERT INTO `django_migrations` VALUES (32, 'flowmeter', '0014_controlregister', '2020-02-17 20:49:07.013013');
INSERT INTO `django_migrations` VALUES (33, 'flowmeter', '0015_auto_20200217_2105', '2020-02-17 21:05:29.734949');
INSERT INTO `django_migrations` VALUES (34, 'flowmeter', '0016_controlregister_opr_type', '2020-02-18 16:53:52.881794');
INSERT INTO `django_migrations` VALUES (35, 'flowmeter', '0017_auto_20200218_1656', '2020-02-18 16:56:21.642925');
INSERT INTO `django_migrations` VALUES (36, 'flowmeter', '0018_datafield_field_name', '2020-02-18 17:02:03.878104');
INSERT INTO `django_migrations` VALUES (37, 'flowmeter', '0019_auto_20200218_1749', '2020-02-18 17:49:20.208251');

-- ----------------------------
-- Table structure for django_session
-- ----------------------------
DROP TABLE IF EXISTS `django_session`;
CREATE TABLE `django_session`  (
  `session_key` varchar(40) CHARACTER SET utf8 COLLATE utf8_bin NOT NULL,
  `session_data` longtext CHARACTER SET utf8 COLLATE utf8_bin NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`) USING BTREE,
  INDEX `django_session_expire_date_a5c62663`(`expire_date`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_bin ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of django_session
-- ----------------------------
INSERT INTO `django_session` VALUES ('201oh4w0wafq4fp1nmqq1mw4v7bzbvy7', 'NWI5OWY0NzBiNjc5NzVjNjVjN2NiMzJiMWRiZmExNzU2YWE2NWY5MDp7InVzZXIiOnsiaWQiOjIsIm5hbWUiOiJcdTk2NDhcdTRmMWZcdTVmM2EiLCJwaG9uZSI6IjEzODUwNTkyMDg2IiwiZW1haWwiOiIxMzQ3NzA0MjYyQHFxLmNvbSIsInN0YXRlIjoiZW5hYmxlIiwicmVtYXJrIjoiIiwiYWN0aW9ucyI6WyJxdWVyeV9hZG1pbiIsInF1ZXJ5X2NvbnRyb2xfcmVnaXN0ZXIiLCJ1cGRhdGVfY29udHJvbF9yZWdpc3RlciIsInF1ZXJ5X2RhdGFfZmllbGQiLCJ1cGRhdGVfZGF0YV9maWVsZCJdfX0=', '2020-03-03 18:14:46.043982');

-- ----------------------------
-- Table structure for djcelery_crontabschedule
-- ----------------------------
DROP TABLE IF EXISTS `djcelery_crontabschedule`;
CREATE TABLE `djcelery_crontabschedule`  (
  `id` int(0) NOT NULL AUTO_INCREMENT,
  `minute` varchar(64) CHARACTER SET utf8 COLLATE utf8_bin NOT NULL,
  `hour` varchar(64) CHARACTER SET utf8 COLLATE utf8_bin NOT NULL,
  `day_of_week` varchar(64) CHARACTER SET utf8 COLLATE utf8_bin NOT NULL,
  `day_of_month` varchar(64) CHARACTER SET utf8 COLLATE utf8_bin NOT NULL,
  `month_of_year` varchar(64) CHARACTER SET utf8 COLLATE utf8_bin NOT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_bin ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for djcelery_intervalschedule
-- ----------------------------
DROP TABLE IF EXISTS `djcelery_intervalschedule`;
CREATE TABLE `djcelery_intervalschedule`  (
  `id` int(0) NOT NULL AUTO_INCREMENT,
  `every` int(0) NOT NULL,
  `period` varchar(24) CHARACTER SET utf8 COLLATE utf8_bin NOT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_bin ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for djcelery_periodictask
-- ----------------------------
DROP TABLE IF EXISTS `djcelery_periodictask`;
CREATE TABLE `djcelery_periodictask`  (
  `id` int(0) NOT NULL AUTO_INCREMENT,
  `name` varchar(200) CHARACTER SET utf8 COLLATE utf8_bin NOT NULL,
  `task` varchar(200) CHARACTER SET utf8 COLLATE utf8_bin NOT NULL,
  `args` longtext CHARACTER SET utf8 COLLATE utf8_bin NOT NULL,
  `kwargs` longtext CHARACTER SET utf8 COLLATE utf8_bin NOT NULL,
  `queue` varchar(200) CHARACTER SET utf8 COLLATE utf8_bin DEFAULT NULL,
  `exchange` varchar(200) CHARACTER SET utf8 COLLATE utf8_bin DEFAULT NULL,
  `routing_key` varchar(200) CHARACTER SET utf8 COLLATE utf8_bin DEFAULT NULL,
  `expires` datetime(6) DEFAULT NULL,
  `enabled` tinyint(1) NOT NULL,
  `last_run_at` datetime(6) DEFAULT NULL,
  `total_run_count` int unsigned NOT NULL,
  `date_changed` datetime(6) NOT NULL,
  `description` longtext CHARACTER SET utf8 COLLATE utf8_bin NOT NULL,
  `crontab_id` int(0) DEFAULT NULL,
  `interval_id` int(0) DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `name`(`name`) USING BTREE,
  INDEX `djcelery_periodictas_crontab_id_75609bab_fk_djcelery_`(`crontab_id`) USING BTREE,
  INDEX `djcelery_periodictas_interval_id_b426ab02_fk_djcelery_`(`interval_id`) USING BTREE,
  CONSTRAINT `djcelery_periodictas_crontab_id_75609bab_fk_djcelery_` FOREIGN KEY (`crontab_id`) REFERENCES `djcelery_crontabschedule` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `djcelery_periodictas_interval_id_b426ab02_fk_djcelery_` FOREIGN KEY (`interval_id`) REFERENCES `djcelery_intervalschedule` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_bin ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for djcelery_periodictasks
-- ----------------------------
DROP TABLE IF EXISTS `djcelery_periodictasks`;
CREATE TABLE `djcelery_periodictasks`  (
  `ident` smallint(0) NOT NULL,
  `last_update` datetime(6) NOT NULL,
  PRIMARY KEY (`ident`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_bin ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for djcelery_taskstate
-- ----------------------------
DROP TABLE IF EXISTS `djcelery_taskstate`;
CREATE TABLE `djcelery_taskstate`  (
  `id` int(0) NOT NULL AUTO_INCREMENT,
  `state` varchar(64) CHARACTER SET utf8 COLLATE utf8_bin NOT NULL,
  `task_id` varchar(36) CHARACTER SET utf8 COLLATE utf8_bin NOT NULL,
  `name` varchar(200) CHARACTER SET utf8 COLLATE utf8_bin DEFAULT NULL,
  `tstamp` datetime(6) NOT NULL,
  `args` longtext CHARACTER SET utf8 COLLATE utf8_bin,
  `kwargs` longtext CHARACTER SET utf8 COLLATE utf8_bin,
  `eta` datetime(6) DEFAULT NULL,
  `expires` datetime(6) DEFAULT NULL,
  `result` longtext CHARACTER SET utf8 COLLATE utf8_bin,
  `traceback` longtext CHARACTER SET utf8 COLLATE utf8_bin,
  `runtime` double DEFAULT NULL,
  `retries` int(0) NOT NULL,
  `hidden` tinyint(1) NOT NULL,
  `worker_id` int(0) DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `task_id`(`task_id`) USING BTREE,
  INDEX `djcelery_taskstate_worker_id_f7f57a05_fk_djcelery_workerstate_id`(`worker_id`) USING BTREE,
  INDEX `djcelery_taskstate_state_53543be4`(`state`) USING BTREE,
  INDEX `djcelery_taskstate_name_8af9eded`(`name`) USING BTREE,
  INDEX `djcelery_taskstate_tstamp_4c3f93a1`(`tstamp`) USING BTREE,
  INDEX `djcelery_taskstate_hidden_c3905e57`(`hidden`) USING BTREE,
  CONSTRAINT `djcelery_taskstate_worker_id_f7f57a05_fk_djcelery_workerstate_id` FOREIGN KEY (`worker_id`) REFERENCES `djcelery_workerstate` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_bin ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for djcelery_workerstate
-- ----------------------------
DROP TABLE IF EXISTS `djcelery_workerstate`;
CREATE TABLE `djcelery_workerstate`  (
  `id` int(0) NOT NULL AUTO_INCREMENT,
  `hostname` varchar(255) CHARACTER SET utf8 COLLATE utf8_bin NOT NULL,
  `last_heartbeat` datetime(6) DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `hostname`(`hostname`) USING BTREE,
  INDEX `djcelery_workerstate_last_heartbeat_4539b544`(`last_heartbeat`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_bin ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for flowmeter_alarmlog
-- ----------------------------
DROP TABLE IF EXISTS `flowmeter_alarmlog`;
CREATE TABLE `flowmeter_alarmlog`  (
  `id` int(0) NOT NULL AUTO_INCREMENT,
  `opr_time` datetime(6) NOT NULL,
  `alarm_type` varchar(64) CHARACTER SET utf8 COLLATE utf8_bin NOT NULL,
  `meter_id` int(0) NOT NULL,
  `opr_user_id` int(0) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  INDEX `flowmeter_alarmlog_meter_id_a826c25e_fk_flowmeter_meter_id`(`meter_id`) USING BTREE,
  INDEX `flowmeter_alarmlog_opr_user_id_9c965e30_fk_flowmeter_user_id`(`opr_user_id`) USING BTREE,
  CONSTRAINT `flowmeter_alarmlog_meter_id_a826c25e_fk_flowmeter_meter_id` FOREIGN KEY (`meter_id`) REFERENCES `flowmeter_meter` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `flowmeter_alarmlog_opr_user_id_9c965e30_fk_flowmeter_user_id` FOREIGN KEY (`opr_user_id`) REFERENCES `flowmeter_user` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8 COLLATE = utf8_bin ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for flowmeter_auth
-- ----------------------------
DROP TABLE IF EXISTS `flowmeter_auth`;
CREATE TABLE `flowmeter_auth`  (
  `id` int(0) NOT NULL AUTO_INCREMENT,
  `name` varchar(128) CHARACTER SET utf8 COLLATE utf8_bin NOT NULL,
  `permission_action` varchar(256) CHARACTER SET utf8 COLLATE utf8_bin NOT NULL,
  `remark` varchar(256) CHARACTER SET utf8 COLLATE utf8_bin DEFAULT NULL,
  `category_id` int(0) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  INDEX `flowmeter_auth_category_id_8f7a78fc_fk_flowmeter_authcategory_id`(`category_id`) USING BTREE,
  CONSTRAINT `flowmeter_auth_category_id_8f7a78fc_fk_flowmeter_authcategory_id` FOREIGN KEY (`category_id`) REFERENCES `flowmeter_authcategory` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 4 CHARACTER SET = utf8 COLLATE = utf8_bin ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of flowmeter_auth
-- ----------------------------
INSERT INTO `flowmeter_auth` VALUES (1, '查询管理员', 'query_admin', ' ', 1);
INSERT INTO `flowmeter_auth` VALUES (2, '查询控制寄存器定义', 'query_control_register', NULL, 2);
INSERT INTO `flowmeter_auth` VALUES (3, '编辑控制寄存器定义', 'update_control_register', NULL, 2);
INSERT INTO `flowmeter_auth` VALUES (4, '查询数据帧格式定义', 'query_data_field', NULL, 2);
INSERT INTO `flowmeter_auth` VALUES (5, '编辑数据帧格式定义', 'update_data_field', NULL, 2);

-- ----------------------------
-- Table structure for flowmeter_authcategory
-- ----------------------------
DROP TABLE IF EXISTS `flowmeter_authcategory`;
CREATE TABLE `flowmeter_authcategory`  (
  `id` int(0) NOT NULL AUTO_INCREMENT,
  `name` varchar(64) CHARACTER SET utf8 COLLATE utf8_bin NOT NULL,
  `remark` varchar(256) CHARACTER SET utf8 COLLATE utf8_bin DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 3 CHARACTER SET = utf8 COLLATE = utf8_bin ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of flowmeter_authcategory
-- ----------------------------
INSERT INTO `flowmeter_authcategory` VALUES (1, '管理员管理', '');
INSERT INTO `flowmeter_authcategory` VALUES (2, '系统设置', NULL);

-- ----------------------------
-- Table structure for flowmeter_controlregister
-- ----------------------------
DROP TABLE IF EXISTS `flowmeter_controlregister`;
CREATE TABLE `flowmeter_controlregister`  (
  `id` int(0) NOT NULL AUTO_INCREMENT,
  `name` varchar(128) CHARACTER SET utf8 COLLATE utf8_bin NOT NULL,
  `address` int(0) NOT NULL,
  `const_data` int(0) DEFAULT NULL,
  `remark` varchar(256) CHARACTER SET utf8 COLLATE utf8_bin NOT NULL,
  `opr_type` varchar(64) CHARACTER SET utf8 COLLATE utf8_bin NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `opr_type`(`opr_type`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_bin ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of flowmeter_controlregister
-- ----------------------------
INSERT INTO `flowmeter_controlregister` VALUES (1, '设置通信地址', 38400, NULL, ' test111', 'set_meter_address');
INSERT INTO `flowmeter_controlregister` VALUES (2, '增加可用气量', 38401, NULL, ' test', 'recharge');
INSERT INTO `flowmeter_controlregister` VALUES (3, '设置流量系数', 38402, NULL, ' test', 'set_flow_ratio');
INSERT INTO `flowmeter_controlregister` VALUES (4, '阀门开', 38403, 29712, ' test', 'open_valve');
INSERT INTO `flowmeter_controlregister` VALUES (5, '阀门关', 38404, 29712, ' test', 'close_valve');
INSERT INTO `flowmeter_controlregister` VALUES (6, '预充值功能开', 38405, 29712, ' test', 'open_recharge');
INSERT INTO `flowmeter_controlregister` VALUES (7, '预充值功能关', 38405, 35823, ' test', 'close_recharge');
INSERT INTO `flowmeter_controlregister` VALUES (8, '表复位重启', 38416, 29712, 'testtestttt', 'reset');

-- ----------------------------
-- Table structure for flowmeter_datafield
-- ----------------------------
DROP TABLE IF EXISTS `flowmeter_datafield`;
CREATE TABLE `flowmeter_datafield`  (
  `id` int(0) NOT NULL AUTO_INCREMENT,
  `name` varchar(128) CHARACTER SET utf8 COLLATE utf8_bin NOT NULL,
  `begin_address` int(0) NOT NULL,
  `end_address` int(0) NOT NULL,
  `field_name` varchar(128) CHARACTER SET utf8 COLLATE utf8_bin NOT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8 COLLATE = utf8_bin ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of flowmeter_datafield
-- ----------------------------
INSERT INTO `flowmeter_datafield` VALUES (1, '设备地址', 0, 0, 'address');
INSERT INTO `flowmeter_datafield` VALUES (2, '功能码', 1, 1, 'opr_code');
INSERT INTO `flowmeter_datafield` VALUES (3, '字节数量', 2, 2, 'byte_num');
INSERT INTO `flowmeter_datafield` VALUES (4, '瞬时流量', 3, 6, 'flow_rate');
INSERT INTO `flowmeter_datafield` VALUES (5, '累计流量整数部分', 7, 10, 'flow_total_int');
INSERT INTO `flowmeter_datafield` VALUES (6, '累计流量小数部分', 11, 14, 'flow_total_float');
INSERT INTO `flowmeter_datafield` VALUES (7, '剩余气量', 15, 16, 'surplus_gas');
INSERT INTO `flowmeter_datafield` VALUES (8, '版本号', 21, 21, 'version');
INSERT INTO `flowmeter_datafield` VALUES (9, '设备状态字', 23, 24, 'meter_state');
INSERT INTO `flowmeter_datafield` VALUES (10, '电池电压', 25, 26, 'power');
INSERT INTO `flowmeter_datafield` VALUES (11, '温度', 27, 28, 'temperature');
INSERT INTO `flowmeter_datafield` VALUES (12, '流量系数', 29, 30, 'flow_ratio');

-- ----------------------------
-- Table structure for flowmeter_dataframeformat
-- ----------------------------
DROP TABLE IF EXISTS `flowmeter_dataframeformat`;
CREATE TABLE `flowmeter_dataframeformat`  (
  `id` int(0) NOT NULL AUTO_INCREMENT,
  `name` varchar(128) CHARACTER SET utf8 COLLATE utf8_bin NOT NULL,
  `remark` varchar(256) CHARACTER SET utf8 COLLATE utf8_bin NOT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_bin ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for flowmeter_dtu
-- ----------------------------
DROP TABLE IF EXISTS `flowmeter_dtu`;
CREATE TABLE `flowmeter_dtu`  (
  `id` int(0) NOT NULL AUTO_INCREMENT,
  `remark` varchar(256) CHARACTER SET utf8 COLLATE utf8_bin NOT NULL,
  `region_id` int(0) NOT NULL,
  `dtu_no` int(0) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  INDEX `flowmeter_dtu_region_id_2c8e3b9c_fk_flowmeter_dturegion_id`(`region_id`) USING BTREE,
  CONSTRAINT `flowmeter_dtu_region_id_2c8e3b9c_fk_flowmeter_dturegion_id` FOREIGN KEY (`region_id`) REFERENCES `flowmeter_dturegion` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8 COLLATE = utf8_bin ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for flowmeter_dturegion
-- ----------------------------
DROP TABLE IF EXISTS `flowmeter_dturegion`;
CREATE TABLE `flowmeter_dturegion`  (
  `id` int(0) NOT NULL AUTO_INCREMENT,
  `left` int(0) NOT NULL,
  `right` int(0) NOT NULL,
  `manufacturer_id` int(0) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  INDEX `flowmeter_dturegion_manufacturer_id_ad32ad37_fk_flowmeter`(`manufacturer_id`) USING BTREE,
  CONSTRAINT `flowmeter_dturegion_manufacturer_id_ad32ad37_fk_flowmeter` FOREIGN KEY (`manufacturer_id`) REFERENCES `flowmeter_user` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8 COLLATE = utf8_bin ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for flowmeter_loginlog
-- ----------------------------
DROP TABLE IF EXISTS `flowmeter_loginlog`;
CREATE TABLE `flowmeter_loginlog`  (
  `id` int(0) NOT NULL AUTO_INCREMENT,
  `opr_time` datetime(6) NOT NULL,
  `state` varchar(16) CHARACTER SET utf8 COLLATE utf8_bin NOT NULL,
  `opr_user_id` int(0) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  INDEX `flowmeter_loginlog_opr_user_id_dcc6dc03_fk_flowmeter_user_id`(`opr_user_id`) USING BTREE,
  CONSTRAINT `flowmeter_loginlog_opr_user_id_dcc6dc03_fk_flowmeter_user_id` FOREIGN KEY (`opr_user_id`) REFERENCES `flowmeter_user` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8 COLLATE = utf8_bin ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for flowmeter_meter
-- ----------------------------
DROP TABLE IF EXISTS `flowmeter_meter`;
CREATE TABLE `flowmeter_meter`  (
  `id` int(0) NOT NULL AUTO_INCREMENT,
  `address` int(0) NOT NULL,
  `last_update_time` datetime(6) NOT NULL,
  `surplus_gas` double NOT NULL,
  `surplus_gas_limits` double NOT NULL,
  `flow_ratio` double NOT NULL,
  `state_id` int(0) NOT NULL,
  `flow_rate` double NOT NULL,
  `total_flow` double NOT NULL,
  `temperature` double NOT NULL,
  `power` double NOT NULL,
  `version` double NOT NULL,
  `remark` varchar(256) CHARACTER SET utf8 COLLATE utf8_bin NOT NULL,
  `dtu_id` int(0) NOT NULL,
  `user_id` int(0) NOT NULL,
  `valve_id` int(0) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `flowmeter_meter_valve_id_e8435585_uniq`(`valve_id`) USING BTREE,
  UNIQUE INDEX `flowmeter_meter_state_id_08f3b8c6_uniq`(`state_id`) USING BTREE,
  INDEX `flowmeter_meter_dtu_id_584ecca7_fk_flowmeter_dtu_id`(`dtu_id`) USING BTREE,
  INDEX `flowmeter_meter_user_id_f08fd909_fk_flowmeter_user_id`(`user_id`) USING BTREE,
  CONSTRAINT `flowmeter_meter_dtu_id_584ecca7_fk_flowmeter_dtu_id` FOREIGN KEY (`dtu_id`) REFERENCES `flowmeter_dtu` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `flowmeter_meter_state_id_08f3b8c6_fk_flowmeter_meterstate_id` FOREIGN KEY (`state_id`) REFERENCES `flowmeter_meterstate` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `flowmeter_meter_user_id_f08fd909_fk_flowmeter_user_id` FOREIGN KEY (`user_id`) REFERENCES `flowmeter_user` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `flowmeter_meter_valve_id_e8435585_fk_flowmeter_valve_id` FOREIGN KEY (`valve_id`) REFERENCES `flowmeter_valve` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8 COLLATE = utf8_bin ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for flowmeter_meterstate
-- ----------------------------
DROP TABLE IF EXISTS `flowmeter_meterstate`;
CREATE TABLE `flowmeter_meterstate`  (
  `id` int(0) NOT NULL AUTO_INCREMENT,
  `valve_state` varchar(8) CHARACTER SET utf8 COLLATE utf8_bin NOT NULL,
  `recharge_state` varchar(8) CHARACTER SET utf8 COLLATE utf8_bin NOT NULL,
  `battery_pressure_state` varchar(8) CHARACTER SET utf8 COLLATE utf8_bin NOT NULL,
  `valve_error_flag` int(0) NOT NULL,
  `owe_state` int(0) NOT NULL,
  `sensor_error_flag` int(0) NOT NULL,
  `state` varchar(8) CHARACTER SET utf8 COLLATE utf8_bin NOT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_bin ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for flowmeter_navigationbar
-- ----------------------------
DROP TABLE IF EXISTS `flowmeter_navigationbar`;
CREATE TABLE `flowmeter_navigationbar`  (
  `id` int(0) NOT NULL AUTO_INCREMENT,
  `icon` varchar(32) CHARACTER SET utf8 COLLATE utf8_bin NOT NULL,
  `name` varchar(64) CHARACTER SET utf8 COLLATE utf8_bin NOT NULL,
  `fid` int(0) NOT NULL,
  `order` int(0) NOT NULL,
  `url` varchar(128) CHARACTER SET utf8 COLLATE utf8_bin NOT NULL,
  `auth_id` int(0) DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  INDEX `flowmeter_navigationbar_auth_id_a595869c_fk_flowmeter_auth_id`(`auth_id`) USING BTREE,
  CONSTRAINT `flowmeter_navigationbar_auth_id_a595869c_fk_flowmeter_auth_id` FOREIGN KEY (`auth_id`) REFERENCES `flowmeter_auth` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 4 CHARACTER SET = utf8 COLLATE = utf8_bin ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of flowmeter_navigationbar
-- ----------------------------
INSERT INTO `flowmeter_navigationbar` VALUES (1, 'xe6b8', '管理员列表', -1, 1, '/admin/view/', 1);
INSERT INTO `flowmeter_navigationbar` VALUES (2, 'xe6b8', '系统设置', -1, 2, '', NULL);
INSERT INTO `flowmeter_navigationbar` VALUES (3, 'xe6b8', '控制寄存器定义', 2, 1, '/system/register/', 2);
INSERT INTO `flowmeter_navigationbar` VALUES (4, 'xe6b8', '数据帧格式定义', 2, 2, '/system/frame/', 4);

-- ----------------------------
-- Table structure for flowmeter_oprlog
-- ----------------------------
DROP TABLE IF EXISTS `flowmeter_oprlog`;
CREATE TABLE `flowmeter_oprlog`  (
  `id` int(0) NOT NULL AUTO_INCREMENT,
  `opr_time` datetime(6) NOT NULL,
  `state` varchar(16) CHARACTER SET utf8 COLLATE utf8_bin NOT NULL,
  `opr_type` varchar(64) CHARACTER SET utf8 COLLATE utf8_bin NOT NULL,
  `opr_user_id` int(0) NOT NULL,
  `meter_id` int(0) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  INDEX `flowmeter_oprlog_opr_user_id_414a4755_fk_flowmeter_user_id`(`opr_user_id`) USING BTREE,
  INDEX `flowmeter_oprlog_meter_id_382107dd_fk_flowmeter_meter_id`(`meter_id`) USING BTREE,
  CONSTRAINT `flowmeter_oprlog_meter_id_382107dd_fk_flowmeter_meter_id` FOREIGN KEY (`meter_id`) REFERENCES `flowmeter_meter` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `flowmeter_oprlog_opr_user_id_414a4755_fk_flowmeter_user_id` FOREIGN KEY (`opr_user_id`) REFERENCES `flowmeter_user` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8 COLLATE = utf8_bin ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for flowmeter_role
-- ----------------------------
DROP TABLE IF EXISTS `flowmeter_role`;
CREATE TABLE `flowmeter_role`  (
  `name` varchar(128) CHARACTER SET utf8 COLLATE utf8_bin NOT NULL,
  `remark` varchar(256) CHARACTER SET utf8 COLLATE utf8_bin DEFAULT NULL,
  PRIMARY KEY (`name`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_bin ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of flowmeter_role
-- ----------------------------
INSERT INTO `flowmeter_role` VALUES ('admin', NULL);

-- ----------------------------
-- Table structure for flowmeter_roleauth
-- ----------------------------
DROP TABLE IF EXISTS `flowmeter_roleauth`;
CREATE TABLE `flowmeter_roleauth`  (
  `id` int(0) NOT NULL AUTO_INCREMENT,
  `auth_id` int(0) NOT NULL,
  `role_id` varchar(128) CHARACTER SET utf8 COLLATE utf8_bin NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  INDEX `flowmeter_roleauth_auth_id_076ea1f3_fk_flowmeter_auth_id`(`auth_id`) USING BTREE,
  INDEX `flowmeter_roleauth_role_id_dc772944_fk_flowmeter_role_name`(`role_id`) USING BTREE,
  CONSTRAINT `flowmeter_roleauth_auth_id_076ea1f3_fk_flowmeter_auth_id` FOREIGN KEY (`auth_id`) REFERENCES `flowmeter_auth` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `flowmeter_roleauth_role_id_dc772944_fk_flowmeter_role_name` FOREIGN KEY (`role_id`) REFERENCES `flowmeter_role` (`name`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 4 CHARACTER SET = utf8 COLLATE = utf8_bin ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of flowmeter_roleauth
-- ----------------------------
INSERT INTO `flowmeter_roleauth` VALUES (1, 1, 'admin');
INSERT INTO `flowmeter_roleauth` VALUES (2, 2, 'admin');
INSERT INTO `flowmeter_roleauth` VALUES (3, 3, 'admin');
INSERT INTO `flowmeter_roleauth` VALUES (4, 4, 'admin');
INSERT INTO `flowmeter_roleauth` VALUES (5, 5, 'admin');

-- ----------------------------
-- Table structure for flowmeter_user
-- ----------------------------
DROP TABLE IF EXISTS `flowmeter_user`;
CREATE TABLE `flowmeter_user`  (
  `id` int(0) NOT NULL AUTO_INCREMENT,
  `name` varchar(128) CHARACTER SET utf8 COLLATE utf8_bin NOT NULL,
  `password` varchar(128) CHARACTER SET utf8 COLLATE utf8_bin NOT NULL,
  `phone` varchar(11) CHARACTER SET utf8 COLLATE utf8_bin NOT NULL,
  `email` varchar(254) CHARACTER SET utf8 COLLATE utf8_bin NOT NULL,
  `create_time` datetime(6) NOT NULL,
  `state` varchar(16) CHARACTER SET utf8 COLLATE utf8_bin NOT NULL,
  `remark` varchar(256) CHARACTER SET utf8 COLLATE utf8_bin NOT NULL,
  `role_id` varchar(128) CHARACTER SET utf8 COLLATE utf8_bin NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `flowmeter_user_email_abc66f6c_uniq`(`email`) USING BTREE,
  UNIQUE INDEX `flowmeter_user_phone_0c31bcc5_uniq`(`phone`) USING BTREE,
  INDEX `flowmeter_user_role_id_0a219bb5_fk_flowmeter_role_name`(`role_id`) USING BTREE,
  CONSTRAINT `flowmeter_user_role_id_0a219bb5_fk_flowmeter_role_name` FOREIGN KEY (`role_id`) REFERENCES `flowmeter_role` (`name`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 3 CHARACTER SET = utf8 COLLATE = utf8_bin ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of flowmeter_user
-- ----------------------------
INSERT INTO `flowmeter_user` VALUES (1, 'test', '111111', '11111111111', '2@qq.com', '2020-02-26 17:04:40.000000', 'enable', ' ', 'admin');
INSERT INTO `flowmeter_user` VALUES (2, '陈伟强', 'e4e5d1c9bf848d039fcf8afdb38ec6cb', '13850592086', '1347704262@qq.com', '2020-02-14 17:09:58.900227', 'enable', '', 'admin');

-- ----------------------------
-- Table structure for flowmeter_valve
-- ----------------------------
DROP TABLE IF EXISTS `flowmeter_valve`;
CREATE TABLE `flowmeter_valve`  (
  `id` int(0) NOT NULL AUTO_INCREMENT,
  `valve_type` varchar(16) CHARACTER SET utf8 COLLATE utf8_bin NOT NULL,
  `address` int(0) DEFAULT NULL,
  `dtu_id` int(0) DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  INDEX `flowmeter_valve_dtu_id_51252e3a_fk_flowmeter_dtu_id`(`dtu_id`) USING BTREE,
  CONSTRAINT `flowmeter_valve_dtu_id_51252e3a_fk_flowmeter_dtu_id` FOREIGN KEY (`dtu_id`) REFERENCES `flowmeter_dtu` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8 COLLATE = utf8_bin ROW_FORMAT = Dynamic;

SET FOREIGN_KEY_CHECKS = 1;
