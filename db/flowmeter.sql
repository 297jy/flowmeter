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

 Date: 19/03/2020 23:44:07
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
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_bin ROW_FORMAT = Dynamic;

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
) ENGINE = InnoDB AUTO_INCREMENT = 141 CHARACTER SET = utf8 COLLATE = utf8_bin ROW_FORMAT = Dynamic;

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
INSERT INTO `auth_permission` VALUES (129, 'Can add configure', 33, 'add_configure');
INSERT INTO `auth_permission` VALUES (130, 'Can change configure', 33, 'change_configure');
INSERT INTO `auth_permission` VALUES (131, 'Can delete configure', 33, 'delete_configure');
INSERT INTO `auth_permission` VALUES (132, 'Can view configure', 33, 'view_configure');
INSERT INTO `auth_permission` VALUES (133, 'Can add flag', 34, 'add_flag');
INSERT INTO `auth_permission` VALUES (134, 'Can change flag', 34, 'change_flag');
INSERT INTO `auth_permission` VALUES (135, 'Can delete flag', 34, 'delete_flag');
INSERT INTO `auth_permission` VALUES (136, 'Can view flag', 34, 'view_flag');
INSERT INTO `auth_permission` VALUES (137, 'Can add system log', 35, 'add_systemlog');
INSERT INTO `auth_permission` VALUES (138, 'Can change system log', 35, 'change_systemlog');
INSERT INTO `auth_permission` VALUES (139, 'Can delete system log', 35, 'delete_systemlog');
INSERT INTO `auth_permission` VALUES (140, 'Can view system log', 35, 'view_systemlog');

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
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_bin ROW_FORMAT = Dynamic;

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
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_bin ROW_FORMAT = Dynamic;

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
) ENGINE = InnoDB AUTO_INCREMENT = 36 CHARACTER SET = utf8 COLLATE = utf8_bin ROW_FORMAT = Dynamic;

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
INSERT INTO `django_content_type` VALUES (33, 'flowmeter', 'configure');
INSERT INTO `django_content_type` VALUES (31, 'flowmeter', 'controlregister');
INSERT INTO `django_content_type` VALUES (18, 'flowmeter', 'datafield');
INSERT INTO `django_content_type` VALUES (9, 'flowmeter', 'dataframeformat');
INSERT INTO `django_content_type` VALUES (10, 'flowmeter', 'dtu');
INSERT INTO `django_content_type` VALUES (17, 'flowmeter', 'dturegion');
INSERT INTO `django_content_type` VALUES (34, 'flowmeter', 'flag');
INSERT INTO `django_content_type` VALUES (29, 'flowmeter', 'loginlog');
INSERT INTO `django_content_type` VALUES (16, 'flowmeter', 'meter');
INSERT INTO `django_content_type` VALUES (32, 'flowmeter', 'meterstate');
INSERT INTO `django_content_type` VALUES (15, 'flowmeter', 'navigationbar');
INSERT INTO `django_content_type` VALUES (28, 'flowmeter', 'oprlog');
INSERT INTO `django_content_type` VALUES (14, 'flowmeter', 'protocol');
INSERT INTO `django_content_type` VALUES (11, 'flowmeter', 'role');
INSERT INTO `django_content_type` VALUES (13, 'flowmeter', 'roleauth');
INSERT INTO `django_content_type` VALUES (35, 'flowmeter', 'systemlog');
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
) ENGINE = InnoDB AUTO_INCREMENT = 63 CHARACTER SET = utf8 COLLATE = utf8_bin ROW_FORMAT = Dynamic;

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
INSERT INTO `django_migrations` VALUES (38, 'flowmeter', '0020_auto_20200220_1150', '2020-02-20 11:50:32.104873');
INSERT INTO `django_migrations` VALUES (39, 'flowmeter', '0021_auto_20200221_1135', '2020-02-21 11:35:26.031685');
INSERT INTO `django_migrations` VALUES (40, 'flowmeter', '0022_auto_20200221_1150', '2020-02-21 11:50:11.521907');
INSERT INTO `django_migrations` VALUES (41, 'flowmeter', '0023_auto_20200221_1157', '2020-02-21 11:57:08.291731');
INSERT INTO `django_migrations` VALUES (42, 'flowmeter', '0024_meterstate_sensor_state', '2020-02-21 16:35:29.589011');
INSERT INTO `django_migrations` VALUES (43, 'flowmeter', '0025_auto_20200221_1812', '2020-02-21 18:12:22.412733');
INSERT INTO `django_migrations` VALUES (44, 'flowmeter', '0026_auto_20200221_1831', '2020-02-21 18:31:31.977634');
INSERT INTO `django_migrations` VALUES (45, 'flowmeter', '0027_auto_20200222_1426', '2020-02-22 14:26:08.248165');
INSERT INTO `django_migrations` VALUES (46, 'flowmeter', '0028_auto_20200223_1423', '2020-02-23 14:23:30.313387');
INSERT INTO `django_migrations` VALUES (47, 'flowmeter', '0029_auto_20200223_2350', '2020-02-23 23:50:50.325953');
INSERT INTO `django_migrations` VALUES (48, 'flowmeter', '0030_auto_20200224_1521', '2020-02-24 15:21:41.100991');
INSERT INTO `django_migrations` VALUES (49, 'flowmeter', '0031_auto_20200311_1120', '2020-03-11 11:20:54.080368');
INSERT INTO `django_migrations` VALUES (50, 'flowmeter', '0032_valve_valve_dtu', '2020-03-11 11:22:18.811341');
INSERT INTO `django_migrations` VALUES (51, 'flowmeter', '0033_remove_meter_valve', '2020-03-11 19:19:39.461964');
INSERT INTO `django_migrations` VALUES (52, 'flowmeter', '0034_role_label', '2020-03-12 17:38:38.155463');
INSERT INTO `django_migrations` VALUES (53, 'flowmeter', '0035_configure', '2020-03-13 20:30:39.930716');
INSERT INTO `django_migrations` VALUES (54, 'flowmeter', '0036_flag', '2020-03-13 20:50:07.621041');
INSERT INTO `django_migrations` VALUES (55, 'flowmeter', '0037_auto_20200313_2053', '2020-03-13 20:53:24.881165');
INSERT INTO `django_migrations` VALUES (56, 'flowmeter', '0038_auto_20200314_1251', '2020-03-14 12:51:51.673398');
INSERT INTO `django_migrations` VALUES (57, 'flowmeter', '0039_oprlog_val', '2020-03-16 13:18:00.149826');
INSERT INTO `django_migrations` VALUES (58, 'flowmeter', '0040_remove_meterstate_online_state', '2020-03-16 14:40:11.418374');
INSERT INTO `django_migrations` VALUES (59, 'flowmeter', '0041_auto_20200317_1807', '2020-03-17 18:07:40.198417');
INSERT INTO `django_migrations` VALUES (60, 'flowmeter', '0042_auto_20200319_1729', '2020-03-19 17:29:42.893913');
INSERT INTO `django_migrations` VALUES (61, 'flowmeter', '0043_auto_20200319_1734', '2020-03-19 17:34:52.438862');
INSERT INTO `django_migrations` VALUES (62, 'flowmeter', '0044_remove_alarmlog_opr_user', '2020-03-19 20:44:48.188759');

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
INSERT INTO `django_session` VALUES ('201oh4w0wafq4fp1nmqq1mw4v7bzbvy7', 'NTc0ZTQ2ODZmYjA3ODNiMTQzMDI3YmZiNTQwYmQxNDFiNWE4YjA2ODp7InVzZXIiOnsiaWQiOjIsIm5hbWUiOiJcdTk2NDhcdTRmMWZcdTVmM2EiLCJwaG9uZSI6IjEzODUwNTkyMDg2IiwiZW1haWwiOiIxMzQ3NzA0MjYyQHFxLmNvbSIsInN0YXRlIjoiZW5hYmxlIiwicmVtYXJrIjoiIiwiYWN0aW9ucyI6WyJxdWVyeV9hZG1pbiIsInF1ZXJ5X2NvbnRyb2xfcmVnaXN0ZXIiLCJ1cGRhdGVfY29udHJvbF9yZWdpc3RlciIsInF1ZXJ5X2RhdGFfZmllbGQiLCJ1cGRhdGVfZGF0YV9maWVsZCIsInF1ZXJ5X21hbnVmYWN0dXJlciIsImNyZWF0ZV9hZG1pbiIsImVkaXRfYWRtaW4iLCJjcmVhdGVfbWFudWZhY3R1cmVyIiwiZWRpdF9tYW51ZmFjdHVyZXIiLCJzd2l0Y2hfYWRtaW5fc3RhdGUiLCJzd2l0Y2hfbWFudWZhY3R1cmVyX3N0YXRlIiwiZGVsX2JhdGNoX2FkbWluIiwiZGVsX2JhdGNoX21hbnVmYWN0dXJlciIsImltcG9ydF9hZG1pbiIsImltcG9ydF9tYW51ZmFjdHVyZXIiLCJleHBvcnRfYWRtaW4iLCJleHBvcnRfbWFudWZhY3R1cmVyIiwicXVlcnlfZHR1X3JlZ2lvbiIsInF1ZXJ5X21hbl9yZWdpb24iLCJhZGRfZHR1X3JlZ2lvbiIsImRlbF9iYXRjaF9kdHVfcmVnaW9uIiwidXBkYXRlX2R0dV9yZWdpb24iLCJxdWVyeV9kdHVfdXNlciIsInF1ZXJ5X2R0dV91c2VyX2J5X21hbl9pZCIsImVkaXRfZHR1X3VzZXIiLCJkZWxfYmF0Y2hfZHR1X3VzZXIiLCJjcmVhdGVfZHR1X3VzZXIiLCJjcmVhdGVfZHR1X3VzZXIiLCJpbXBvcnRfZHR1X3VzZXIiLCJleHBvcnRfZHR1X3VzZXIiLCJxdWVyeV9zZXR0aW5nIiwic3dpdGNoX2R0dV91c2VyX3N0YXRlIiwicXVlcnlfZHR1IiwicXVlcnlfZHR1X2J5X3VzZXJfaWQiLCJhZGRfZHR1IiwidXBkYXRlX2R0dSIsImRlbF9iYXRjaF9kdHUiLCJxdWVyeV9tZXRlciIsInF1ZXJ5X3N0YXRlIiwiYWRkX21ldGVyIiwidXBkYXRlX21ldGVyIiwiZGVsX2JhdGNoX21ldGVyIiwicXVlcnlfcm9sZSIsImVkaXRfcm9sZSIsImVkaXRfcm9sZV9hdXRoIl0sInJvbGUiOiJhZG1pbiJ9fQ==', '2020-03-26 22:38:54.438765');

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
  PRIMARY KEY (`id`) USING BTREE,
  INDEX `flowmeter_alarmlog_meter_id_a826c25e_fk_flowmeter_meter_id`(`meter_id`) USING BTREE,
  CONSTRAINT `flowmeter_alarmlog_meter_id_a826c25e_fk_flowmeter_meter_id` FOREIGN KEY (`meter_id`) REFERENCES `flowmeter_meter` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
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
) ENGINE = InnoDB AUTO_INCREMENT = 63 CHARACTER SET = utf8 COLLATE = utf8_bin ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of flowmeter_auth
-- ----------------------------
INSERT INTO `flowmeter_auth` VALUES (1, '查询管理员', 'query_admin', ' ', 1);
INSERT INTO `flowmeter_auth` VALUES (2, '查询控制寄存器定义', 'query_control_register', NULL, 2);
INSERT INTO `flowmeter_auth` VALUES (3, '编辑控制寄存器定义', 'update_control_register', NULL, 2);
INSERT INTO `flowmeter_auth` VALUES (4, '查询数据帧格式定义', 'query_data_field', NULL, 2);
INSERT INTO `flowmeter_auth` VALUES (5, '编辑数据帧格式定义', 'update_data_field', NULL, 2);
INSERT INTO `flowmeter_auth` VALUES (6, '查询供气商', 'query_manufacturer', NULL, 3);
INSERT INTO `flowmeter_auth` VALUES (7, '创建管理员账号', 'create_admin', NULL, 1);
INSERT INTO `flowmeter_auth` VALUES (8, '编辑管理员', 'edit_admin', NULL, 1);
INSERT INTO `flowmeter_auth` VALUES (9, '创建供气商账号', 'create_manufacturer', NULL, 3);
INSERT INTO `flowmeter_auth` VALUES (10, '编辑供气商', 'edit_manufacturer', NULL, 3);
INSERT INTO `flowmeter_auth` VALUES (11, '切换管理员账号状态', 'switch_admin_state', NULL, 1);
INSERT INTO `flowmeter_auth` VALUES (12, '切换供气商账号状态', 'switch_manufacturer_state', NULL, 3);
INSERT INTO `flowmeter_auth` VALUES (13, '批量删除管理员', 'del_batch_admin', NULL, 1);
INSERT INTO `flowmeter_auth` VALUES (14, '批量删除供气商', 'del_batch_manufacturer', NULL, 3);
INSERT INTO `flowmeter_auth` VALUES (15, '导入管理员', 'import_admin', NULL, 1);
INSERT INTO `flowmeter_auth` VALUES (16, '导入供气商', 'import_manufacturer', NULL, 3);
INSERT INTO `flowmeter_auth` VALUES (17, '导出管理员', 'export_admin', NULL, 1);
INSERT INTO `flowmeter_auth` VALUES (18, '导出供气商', 'export_manufacturer', NULL, 3);
INSERT INTO `flowmeter_auth` VALUES (19, '查询DTU区间', 'query_dtu_region;query_man_region', NULL, 4);
INSERT INTO `flowmeter_auth` VALUES (20, '增加DTU区间', 'add_dtu_region', NULL, 4);
INSERT INTO `flowmeter_auth` VALUES (21, '删除DTU区间', 'del_batch_dtu_region', NULL, 4);
INSERT INTO `flowmeter_auth` VALUES (22, '编辑DTU区间', 'update_dtu_region', NULL, 4);
INSERT INTO `flowmeter_auth` VALUES (23, '查询DTU用户', 'query_dtu_user;query_dtu_user_by_man_id', NULL, 5);
INSERT INTO `flowmeter_auth` VALUES (24, '编辑DTU用户', 'edit_dtu_user', NULL, 5);
INSERT INTO `flowmeter_auth` VALUES (25, '批量删除DTU用户', 'del_batch_dtu_user', NULL, 5);
INSERT INTO `flowmeter_auth` VALUES (26, '添加DTU用户', 'create_dtu_user', NULL, 5);
INSERT INTO `flowmeter_auth` VALUES (27, '添加DTU用户', 'create_dtu_user', NULL, 5);
INSERT INTO `flowmeter_auth` VALUES (28, '导入DTU用户', 'import_dtu_user', NULL, 5);
INSERT INTO `flowmeter_auth` VALUES (29, '导出DTU用户', 'export_dtu_user', NULL, 5);
INSERT INTO `flowmeter_auth` VALUES (30, '查看系统设置', 'query_setting', NULL, 2);
INSERT INTO `flowmeter_auth` VALUES (31, '切换DTU用户账号状态', 'switch_dtu_user_state', NULL, 5);
INSERT INTO `flowmeter_auth` VALUES (32, '查询DTU列表', 'query_dtu;query_dtu_by_user_id', NULL, 6);
INSERT INTO `flowmeter_auth` VALUES (33, '添加DTU', 'add_dtu', NULL, 6);
INSERT INTO `flowmeter_auth` VALUES (34, '编辑DTU', 'update_dtu', NULL, 6);
INSERT INTO `flowmeter_auth` VALUES (35, '删除DTU', 'del_batch_dtu', NULL, 6);
INSERT INTO `flowmeter_auth` VALUES (36, '查询仪表', 'query_meter;query_state', NULL, 7);
INSERT INTO `flowmeter_auth` VALUES (37, '添加仪表', 'add_meter', NULL, 7);
INSERT INTO `flowmeter_auth` VALUES (38, '编辑仪表', 'update_meter', NULL, 7);
INSERT INTO `flowmeter_auth` VALUES (39, '批量删除仪表', 'del_batch_meter', NULL, 7);
INSERT INTO `flowmeter_auth` VALUES (40, '查询角色', 'query_role', NULL, 8);
INSERT INTO `flowmeter_auth` VALUES (41, '编辑角色信息', 'edit_role', NULL, 8);
INSERT INTO `flowmeter_auth` VALUES (42, '编辑角色权限', 'edit_role_auth', NULL, 8);
INSERT INTO `flowmeter_auth` VALUES (43, '更改阀门状态', 'update_valve_state', NULL, 9);
INSERT INTO `flowmeter_auth` VALUES (44, '更改预充值状态', 'update_recharge_state', NULL, 9);
INSERT INTO `flowmeter_auth` VALUES (45, '更改流量系数', 'update_flow_ratio', NULL, 9);
INSERT INTO `flowmeter_auth` VALUES (46, '查询仪表', 'query_meter_data', NULL, 9);
INSERT INTO `flowmeter_auth` VALUES (47, '重启仪表', 'reset_meter', NULL, 9);
INSERT INTO `flowmeter_auth` VALUES (48, '充值仪表', 'recharge_meter', NULL, 9);
INSERT INTO `flowmeter_auth` VALUES (49, '删除操作日志', 'del_opr_log', NULL, 10);
INSERT INTO `flowmeter_auth` VALUES (50, '查询操作日志', 'query_opr_log', NULL, 10);
INSERT INTO `flowmeter_auth` VALUES (51, '删除系统日志', 'del_system_log', NULL, 10);
INSERT INTO `flowmeter_auth` VALUES (52, '查询系统日志', 'query_system_log', NULL, 10);
INSERT INTO `flowmeter_auth` VALUES (53, '删除警报日志', 'del_alarm_log', NULL, 10);
INSERT INTO `flowmeter_auth` VALUES (54, '查询警报日志', 'query_alarm_log', NULL, 10);
INSERT INTO `flowmeter_auth` VALUES (55, '删除警报日志', 'del_alarm_log', NULL, 10);
INSERT INTO `flowmeter_auth` VALUES (56, '导出操作日志', 'export_alarm_log', NULL, 10);
INSERT INTO `flowmeter_auth` VALUES (57, '导出系统日志', 'export_system_log', NULL, 10);
INSERT INTO `flowmeter_auth` VALUES (58, '导出警报日志', 'export_alarm_log', NULL, 10);
INSERT INTO `flowmeter_auth` VALUES (59, '修改阀门控制器物理地址', 'update_valve_address', NULL, 7);
INSERT INTO `flowmeter_auth` VALUES (60, '修改阀门控制器DTU', 'update_valve_dtu', NULL, 7);
INSERT INTO `flowmeter_auth` VALUES (61, '查询系统设置', 'query_configure', NULL, 2);
INSERT INTO `flowmeter_auth` VALUES (62, '编辑系统设置', 'update_configure', NULL, 2);

-- ----------------------------
-- Table structure for flowmeter_authcategory
-- ----------------------------
DROP TABLE IF EXISTS `flowmeter_authcategory`;
CREATE TABLE `flowmeter_authcategory`  (
  `id` int(0) NOT NULL AUTO_INCREMENT,
  `name` varchar(64) CHARACTER SET utf8 COLLATE utf8_bin NOT NULL,
  `remark` varchar(256) CHARACTER SET utf8 COLLATE utf8_bin DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 12 CHARACTER SET = utf8 COLLATE = utf8_bin ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of flowmeter_authcategory
-- ----------------------------
INSERT INTO `flowmeter_authcategory` VALUES (1, '管理员管理', '');
INSERT INTO `flowmeter_authcategory` VALUES (2, '系统管理', NULL);
INSERT INTO `flowmeter_authcategory` VALUES (3, '供气商管理', NULL);
INSERT INTO `flowmeter_authcategory` VALUES (4, 'DTU区间管理', NULL);
INSERT INTO `flowmeter_authcategory` VALUES (5, 'DTU用户管理', NULL);
INSERT INTO `flowmeter_authcategory` VALUES (6, 'DTU管理', NULL);
INSERT INTO `flowmeter_authcategory` VALUES (7, '仪表管理', NULL);
INSERT INTO `flowmeter_authcategory` VALUES (8, '角色管理', NULL);
INSERT INTO `flowmeter_authcategory` VALUES (9, '仪表远程操作管理', NULL);
INSERT INTO `flowmeter_authcategory` VALUES (10, '日志管理', NULL);

-- ----------------------------
-- Table structure for flowmeter_configure
-- ----------------------------
DROP TABLE IF EXISTS `flowmeter_configure`;
CREATE TABLE `flowmeter_configure`  (
  `id` int(0) NOT NULL AUTO_INCREMENT,
  `name` varchar(128) CHARACTER SET utf8 COLLATE utf8_bin NOT NULL,
  `val` varchar(256) CHARACTER SET utf8 COLLATE utf8_bin NOT NULL,
  `label` varchar(128) CHARACTER SET utf8 COLLATE utf8_bin NOT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 2 CHARACTER SET = utf8 COLLATE = utf8_bin ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of flowmeter_configure
-- ----------------------------
INSERT INTO `flowmeter_configure` VALUES (1, 'unexecuted_opr_check_time', '5', '检查未执行操作的时间间隔');

-- ----------------------------
-- Table structure for flowmeter_controlregister
-- ----------------------------
DROP TABLE IF EXISTS `flowmeter_controlregister`;
CREATE TABLE `flowmeter_controlregister`  (
  `id` int(0) NOT NULL AUTO_INCREMENT,
  `name` varchar(128) CHARACTER SET utf8 COLLATE utf8_bin NOT NULL,
  `field_val` int(0) NOT NULL,
  `const_data` int(0) DEFAULT NULL,
  `remark` varchar(256) CHARACTER SET utf8 COLLATE utf8_bin NOT NULL,
  `opr_type` varchar(64) CHARACTER SET utf8 COLLATE utf8_bin NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `opr_type`(`opr_type`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 9 CHARACTER SET = utf8 COLLATE = utf8_bin ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of flowmeter_controlregister
-- ----------------------------
INSERT INTO `flowmeter_controlregister` VALUES (1, '设置通信地址', 38400, NULL, ' test111', 'set_meter_address');
INSERT INTO `flowmeter_controlregister` VALUES (2, '增加可用气量', 38401, NULL, ' test 111111', 'recharge');
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
) ENGINE = InnoDB AUTO_INCREMENT = 13 CHARACTER SET = utf8 COLLATE = utf8_bin ROW_FORMAT = Dynamic;

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
  `user_id` int(0) DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `flowmeter_dtu_dtu_no_09e8e0cf_uniq`(`dtu_no`) USING BTREE,
  INDEX `flowmeter_dtu_region_id_2c8e3b9c_fk_flowmeter_dturegion_id`(`region_id`) USING BTREE,
  INDEX `flowmeter_dtu_user_id_7a23c210_fk_flowmeter_user_id`(`user_id`) USING BTREE,
  CONSTRAINT `flowmeter_dtu_region_id_2c8e3b9c_fk_flowmeter_dturegion_id` FOREIGN KEY (`region_id`) REFERENCES `flowmeter_dturegion` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `flowmeter_dtu_user_id_7a23c210_fk_flowmeter_user_id` FOREIGN KEY (`user_id`) REFERENCES `flowmeter_user` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 18 CHARACTER SET = utf8 COLLATE = utf8_bin ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of flowmeter_dtu
-- ----------------------------
INSERT INTO `flowmeter_dtu` VALUES (14, 'testsdfsdfsdfdsf   test', 14, 0, 15);
INSERT INTO `flowmeter_dtu` VALUES (15, 'testsdfsfdsfsdfdsf  test', 16, 100, 15);
INSERT INTO `flowmeter_dtu` VALUES (16, 'test', 14, 1, 15);
INSERT INTO `flowmeter_dtu` VALUES (17, 'test', 17, 220, 15);

-- ----------------------------
-- Table structure for flowmeter_dturegion
-- ----------------------------
DROP TABLE IF EXISTS `flowmeter_dturegion`;
CREATE TABLE `flowmeter_dturegion`  (
  `id` int(0) NOT NULL AUTO_INCREMENT,
  `left` int(0) NOT NULL,
  `right` int(0) NOT NULL,
  `manufacturer_id` int(0) NOT NULL,
  `used_num` int(0) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  INDEX `flowmeter_dturegion_manufacturer_id_ad32ad37`(`manufacturer_id`) USING BTREE,
  CONSTRAINT `flowmeter_dturegion_manufacturer_id_ad32ad37_fk_flowmeter` FOREIGN KEY (`manufacturer_id`) REFERENCES `flowmeter_user` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 18 CHARACTER SET = utf8 COLLATE = utf8_bin ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of flowmeter_dturegion
-- ----------------------------
INSERT INTO `flowmeter_dturegion` VALUES (14, 0, 99, 9, 2);
INSERT INTO `flowmeter_dturegion` VALUES (16, 100, 219, 9, 1);
INSERT INTO `flowmeter_dturegion` VALUES (17, 220, 220, 9, 1);

-- ----------------------------
-- Table structure for flowmeter_flag
-- ----------------------------
DROP TABLE IF EXISTS `flowmeter_flag`;
CREATE TABLE `flowmeter_flag`  (
  `id` int(0) NOT NULL AUTO_INCREMENT,
  `name` varchar(128) CHARACTER SET utf8 COLLATE utf8_bin NOT NULL,
  `val` varchar(256) CHARACTER SET utf8 COLLATE utf8_bin NOT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 4 CHARACTER SET = utf8 COLLATE = utf8_bin ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of flowmeter_flag
-- ----------------------------
INSERT INTO `flowmeter_flag` VALUES (1, 'admin_version', '15');
INSERT INTO `flowmeter_flag` VALUES (2, 'dtu_user_version', '1');
INSERT INTO `flowmeter_flag` VALUES (3, 'manufacturer_version', '1');

-- ----------------------------
-- Table structure for flowmeter_meter
-- ----------------------------
DROP TABLE IF EXISTS `flowmeter_meter`;
CREATE TABLE `flowmeter_meter`  (
  `id` int(0) NOT NULL AUTO_INCREMENT,
  `address` int(0) NOT NULL,
  `last_update_time` datetime(6) DEFAULT NULL,
  `surplus_gas` double DEFAULT NULL,
  `surplus_gas_limits` double DEFAULT NULL,
  `flow_ratio` double DEFAULT NULL,
  `flow_rate` double DEFAULT NULL,
  `total_flow` double DEFAULT NULL,
  `temperature` double DEFAULT NULL,
  `power` double DEFAULT NULL,
  `version` double DEFAULT NULL,
  `remark` varchar(256) CHARACTER SET utf8 COLLATE utf8_bin DEFAULT NULL,
  `dtu_id` int(0) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `flowmeter_meter_dtu_id_address_82f69c16_uniq`(`dtu_id`, `address`) USING BTREE,
  CONSTRAINT `flowmeter_meter_dtu_id_584ecca7_fk_flowmeter_dtu_id` FOREIGN KEY (`dtu_id`) REFERENCES `flowmeter_dtu` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 13 CHARACTER SET = utf8 COLLATE = utf8_bin ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of flowmeter_meter
-- ----------------------------
INSERT INTO `flowmeter_meter` VALUES (11, 1, '2020-03-18 21:33:02.777854', -1, 1.2, -1, -1, -1, -1, -1, -1, 'test', 14);
INSERT INTO `flowmeter_meter` VALUES (12, 2, '2020-03-19 17:19:06.691427', -1, 2.2, -1, -1, -1, -1, -1, -1, '', 14);

-- ----------------------------
-- Table structure for flowmeter_meterstate
-- ----------------------------
DROP TABLE IF EXISTS `flowmeter_meterstate`;
CREATE TABLE `flowmeter_meterstate`  (
  `id` int(0) NOT NULL AUTO_INCREMENT,
  `valve_state` int(0) NOT NULL,
  `recharge_state` int(0) NOT NULL,
  `battery_pressure_state` int(0) NOT NULL,
  `valve_error_flag` int(0) NOT NULL,
  `owe_state` int(0) NOT NULL,
  `sensor_state` int(0) NOT NULL,
  `meter_id` int(0) DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `meter_id`(`meter_id`) USING BTREE,
  CONSTRAINT `flowmeter_meterstate_meter_id_44db7d81_fk_flowmeter_meter_id` FOREIGN KEY (`meter_id`) REFERENCES `flowmeter_meter` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 13 CHARACTER SET = utf8 COLLATE = utf8_bin ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of flowmeter_meterstate
-- ----------------------------
INSERT INTO `flowmeter_meterstate` VALUES (11, 1, 1, -1, -1, -1, -1, 11);
INSERT INTO `flowmeter_meterstate` VALUES (12, 1, 1, -1, -1, -1, -1, 12);

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
) ENGINE = InnoDB AUTO_INCREMENT = 13 CHARACTER SET = utf8 COLLATE = utf8_bin ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of flowmeter_navigationbar
-- ----------------------------
INSERT INTO `flowmeter_navigationbar` VALUES (1, 'xe6b8', '管理员列表', -1, 1, '/admin/view/', 1);
INSERT INTO `flowmeter_navigationbar` VALUES (2, 'xe6b8', '系统管理', -1, 8, '', NULL);
INSERT INTO `flowmeter_navigationbar` VALUES (3, 'xe6b8', '控制寄存器定义', 2, 1, '/system/register/', 2);
INSERT INTO `flowmeter_navigationbar` VALUES (4, 'xe6b8', '数据帧格式定义', 2, 2, '/system/frame/', 4);
INSERT INTO `flowmeter_navigationbar` VALUES (5, 'xe6b8', '供气商列表', -1, 2, '/manufacturer/view/', 6);
INSERT INTO `flowmeter_navigationbar` VALUES (6, 'xe6b8', 'DTU区间列表', -1, 4, '/dtu_region/view/', 19);
INSERT INTO `flowmeter_navigationbar` VALUES (7, 'xe6b8', 'DTU用户列表', -1, 3, '/dtu_user/view/', 24);
INSERT INTO `flowmeter_navigationbar` VALUES (8, 'xe6b8', 'DTU列表', -1, 5, '/dtu/view/', 32);
INSERT INTO `flowmeter_navigationbar` VALUES (9, 'xe6b8', '仪表列表', -1, 6, '/meter/view/', 36);
INSERT INTO `flowmeter_navigationbar` VALUES (10, 'xe6b8', '角色管理', -1, 4, '/role/view/', 40);
INSERT INTO `flowmeter_navigationbar` VALUES (11, 'xe6b8', '日志管理', -1, 7, '', NULL);
INSERT INTO `flowmeter_navigationbar` VALUES (12, 'xe6b8', '操作日志管理', 11, 1, '/log/opr/view/', 50);
INSERT INTO `flowmeter_navigationbar` VALUES (13, 'xe6b8', '系统日志管理', 11, 2, '/log/system/view/', 52);
INSERT INTO `flowmeter_navigationbar` VALUES (14, 'xe6b8', '警报日志管理', 11, 3, '/log/alarm/view/', 54);
INSERT INTO `flowmeter_navigationbar` VALUES (15, 'xe6b8', '系统设置', 2, 3, '/system/configure/', 2);

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
  `val` varchar(256) CHARACTER SET utf8 COLLATE utf8_bin NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  INDEX `flowmeter_oprlog_opr_user_id_414a4755_fk_flowmeter_user_id`(`opr_user_id`) USING BTREE,
  INDEX `flowmeter_oprlog_meter_id_382107dd_fk_flowmeter_meter_id`(`meter_id`) USING BTREE,
  CONSTRAINT `flowmeter_oprlog_meter_id_382107dd_fk_flowmeter_meter_id` FOREIGN KEY (`meter_id`) REFERENCES `flowmeter_meter` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `flowmeter_oprlog_opr_user_id_414a4755_fk_flowmeter_user_id` FOREIGN KEY (`opr_user_id`) REFERENCES `flowmeter_user` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 47 CHARACTER SET = utf8 COLLATE = utf8_bin ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of flowmeter_oprlog
-- ----------------------------
INSERT INTO `flowmeter_oprlog` VALUES (42, '2020-03-19 16:39:16.253721', 'wait', 'open_valve', 2, 12, '');
INSERT INTO `flowmeter_oprlog` VALUES (43, '2020-03-19 16:39:17.416780', 'success', 'open_recharge', 2, 12, '');
INSERT INTO `flowmeter_oprlog` VALUES (44, '2020-03-19 16:43:16.124581', 'wait', 'open_valve', 2, 12, '');
INSERT INTO `flowmeter_oprlog` VALUES (45, '2020-03-19 17:10:01.278637', 'wait', 'open_valve', 2, 12, '');
INSERT INTO `flowmeter_oprlog` VALUES (46, '2020-03-19 17:18:46.275831', 'success', 'open_valve', 2, 12, '');

-- ----------------------------
-- Table structure for flowmeter_role
-- ----------------------------
DROP TABLE IF EXISTS `flowmeter_role`;
CREATE TABLE `flowmeter_role`  (
  `name` varchar(128) CHARACTER SET utf8 COLLATE utf8_bin NOT NULL,
  `remark` varchar(256) CHARACTER SET utf8 COLLATE utf8_bin DEFAULT NULL,
  `label` varchar(128) CHARACTER SET utf8 COLLATE utf8_bin NOT NULL,
  PRIMARY KEY (`name`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_bin ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of flowmeter_role
-- ----------------------------
INSERT INTO `flowmeter_role` VALUES ('admin', 'test', '管理员');
INSERT INTO `flowmeter_role` VALUES ('dtu_user', '！~！！！', 'DTU用户');
INSERT INTO `flowmeter_role` VALUES ('manufacturer', 'sdfsf', '供气商');

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
) ENGINE = InnoDB AUTO_INCREMENT = 726 CHARACTER SET = utf8 COLLATE = utf8_bin ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of flowmeter_roleauth
-- ----------------------------
INSERT INTO `flowmeter_roleauth` VALUES (787, 1, 'admin');
INSERT INTO `flowmeter_roleauth` VALUES (788, 2, 'admin');
INSERT INTO `flowmeter_roleauth` VALUES (789, 3, 'admin');
INSERT INTO `flowmeter_roleauth` VALUES (790, 4, 'admin');
INSERT INTO `flowmeter_roleauth` VALUES (791, 5, 'admin');
INSERT INTO `flowmeter_roleauth` VALUES (792, 6, 'admin');
INSERT INTO `flowmeter_roleauth` VALUES (793, 7, 'admin');
INSERT INTO `flowmeter_roleauth` VALUES (794, 8, 'admin');
INSERT INTO `flowmeter_roleauth` VALUES (795, 9, 'admin');
INSERT INTO `flowmeter_roleauth` VALUES (796, 10, 'admin');
INSERT INTO `flowmeter_roleauth` VALUES (797, 11, 'admin');
INSERT INTO `flowmeter_roleauth` VALUES (798, 12, 'admin');
INSERT INTO `flowmeter_roleauth` VALUES (799, 13, 'admin');
INSERT INTO `flowmeter_roleauth` VALUES (800, 14, 'admin');
INSERT INTO `flowmeter_roleauth` VALUES (801, 15, 'admin');
INSERT INTO `flowmeter_roleauth` VALUES (802, 16, 'admin');
INSERT INTO `flowmeter_roleauth` VALUES (803, 17, 'admin');
INSERT INTO `flowmeter_roleauth` VALUES (804, 18, 'admin');
INSERT INTO `flowmeter_roleauth` VALUES (805, 19, 'admin');
INSERT INTO `flowmeter_roleauth` VALUES (806, 20, 'admin');
INSERT INTO `flowmeter_roleauth` VALUES (807, 21, 'admin');
INSERT INTO `flowmeter_roleauth` VALUES (808, 22, 'admin');
INSERT INTO `flowmeter_roleauth` VALUES (809, 23, 'admin');
INSERT INTO `flowmeter_roleauth` VALUES (810, 24, 'admin');
INSERT INTO `flowmeter_roleauth` VALUES (811, 25, 'admin');
INSERT INTO `flowmeter_roleauth` VALUES (812, 26, 'admin');
INSERT INTO `flowmeter_roleauth` VALUES (813, 27, 'admin');
INSERT INTO `flowmeter_roleauth` VALUES (814, 28, 'admin');
INSERT INTO `flowmeter_roleauth` VALUES (815, 29, 'admin');
INSERT INTO `flowmeter_roleauth` VALUES (816, 30, 'admin');
INSERT INTO `flowmeter_roleauth` VALUES (817, 31, 'admin');
INSERT INTO `flowmeter_roleauth` VALUES (818, 32, 'admin');
INSERT INTO `flowmeter_roleauth` VALUES (819, 33, 'admin');
INSERT INTO `flowmeter_roleauth` VALUES (820, 34, 'admin');
INSERT INTO `flowmeter_roleauth` VALUES (821, 35, 'admin');
INSERT INTO `flowmeter_roleauth` VALUES (822, 36, 'admin');
INSERT INTO `flowmeter_roleauth` VALUES (823, 37, 'admin');
INSERT INTO `flowmeter_roleauth` VALUES (824, 38, 'admin');
INSERT INTO `flowmeter_roleauth` VALUES (825, 39, 'admin');
INSERT INTO `flowmeter_roleauth` VALUES (826, 40, 'admin');
INSERT INTO `flowmeter_roleauth` VALUES (827, 41, 'admin');
INSERT INTO `flowmeter_roleauth` VALUES (828, 42, 'admin');
INSERT INTO `flowmeter_roleauth` VALUES (829, 43, 'admin');
INSERT INTO `flowmeter_roleauth` VALUES (830, 44, 'admin');
INSERT INTO `flowmeter_roleauth` VALUES (831, 45, 'admin');
INSERT INTO `flowmeter_roleauth` VALUES (832, 46, 'admin');
INSERT INTO `flowmeter_roleauth` VALUES (833, 47, 'admin');
INSERT INTO `flowmeter_roleauth` VALUES (834, 48, 'admin');
INSERT INTO `flowmeter_roleauth` VALUES (835, 49, 'admin');
INSERT INTO `flowmeter_roleauth` VALUES (836, 50, 'admin');
INSERT INTO `flowmeter_roleauth` VALUES (837, 51, 'admin');
INSERT INTO `flowmeter_roleauth` VALUES (838, 52, 'admin');
INSERT INTO `flowmeter_roleauth` VALUES (839, 53, 'admin');
INSERT INTO `flowmeter_roleauth` VALUES (840, 54, 'admin');
INSERT INTO `flowmeter_roleauth` VALUES (841, 55, 'admin');
INSERT INTO `flowmeter_roleauth` VALUES (842, 56, 'admin');
INSERT INTO `flowmeter_roleauth` VALUES (843, 57, 'admin');
INSERT INTO `flowmeter_roleauth` VALUES (844, 58, 'admin');
INSERT INTO `flowmeter_roleauth` VALUES (845, 59, 'admin');
INSERT INTO `flowmeter_roleauth` VALUES (846, 60, 'admin');
INSERT INTO `flowmeter_roleauth` VALUES (847, 61, 'admin');
INSERT INTO `flowmeter_roleauth` VALUES (848, 62, 'admin');

-- ----------------------------
-- Table structure for flowmeter_systemlog
-- ----------------------------
DROP TABLE IF EXISTS `flowmeter_systemlog`;
CREATE TABLE `flowmeter_systemlog`  (
  `id` int(0) NOT NULL AUTO_INCREMENT,
  `opr_time` datetime(6) NOT NULL,
  `action_type` varchar(256) CHARACTER SET utf8 COLLATE utf8_bin NOT NULL,
  `state` varchar(16) CHARACTER SET utf8 COLLATE utf8_bin NOT NULL,
  `opr_user_id` int(0) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  INDEX `flowmeter_systemlog_opr_user_id_b12aa62a_fk_flowmeter_user_id`(`opr_user_id`) USING BTREE,
  CONSTRAINT `flowmeter_systemlog_opr_user_id_b12aa62a_fk_flowmeter_user_id` FOREIGN KEY (`opr_user_id`) REFERENCES `flowmeter_user` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8 COLLATE = utf8_bin ROW_FORMAT = Dynamic;

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
) ENGINE = InnoDB AUTO_INCREMENT = 16 CHARACTER SET = utf8 COLLATE = utf8_bin ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of flowmeter_user
-- ----------------------------
INSERT INTO `flowmeter_user` VALUES (1, 'test1', 'e4e5d1c9bf848d039fcf8afdb38ec6cb', '11111111111', '2@qq.com', '2020-02-26 17:04:40.000000', 'enable', ' ', 'admin');
INSERT INTO `flowmeter_user` VALUES (2, '陈伟强', 'e4e5d1c9bf848d039fcf8afdb38ec6cb', '13850592086', '1347704262@qq.com', '2020-02-14 17:09:58.900227', 'enable', '', 'admin');
INSERT INTO `flowmeter_user` VALUES (9, '供气商1', 'e4e5d1c9bf848d039fcf8afdb38ec6cb', '13850592081', '111@qq.com', '2020-02-24 15:28:33.706380', 'enable', 'test111', 'manufacturer');
INSERT INTO `flowmeter_user` VALUES (10, '供气商2', 'e4e5d1c9bf848d039fcf8afdb38ec6cb', '13850592082', '121@qq.com', '2020-02-24 17:30:27.532084', 'enable', 'test111', 'manufacturer');
INSERT INTO `flowmeter_user` VALUES (11, '供气商3', 'e4e5d1c9bf848d039fcf8afdb38ec6cb', '13850592087', '13477042611@qq.com', '2020-02-25 16:29:09.801093', 'enable', '', 'manufacturer');
INSERT INTO `flowmeter_user` VALUES (12, '供气商4', 'e4e5d1c9bf848d039fcf8afdb38ec6cb', '13850599098', '1333@qq.com', '2020-02-25 16:29:34.215352', 'enable', '', 'manufacturer');
INSERT INTO `flowmeter_user` VALUES (13, '供气商5', 'e4e5d1c9bf848d039fcf8afdb38ec6cb', '13003950222', '211@qq.com', '2020-02-25 16:30:54.408364', 'enable', '', 'manufacturer');
INSERT INTO `flowmeter_user` VALUES (15, 'test', 'e4e5d1c9bf848d039fcf8afdb38ec6cb', '13850592083', '13444@qq.com', '2020-03-10 22:12:47.616825', 'enable', 'test', 'dtu_user');

-- ----------------------------
-- Table structure for flowmeter_valve
-- ----------------------------
DROP TABLE IF EXISTS `flowmeter_valve`;
CREATE TABLE `flowmeter_valve`  (
  `id` int(0) NOT NULL AUTO_INCREMENT,
  `address` int(0) DEFAULT NULL,
  `dtu_id` int(0) DEFAULT NULL,
  `valve_dtu_id` int(0) DEFAULT NULL,
  `meter_id` int(0) DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `meter_id`(`meter_id`) USING BTREE,
  UNIQUE INDEX `flowmeter_valve_dtu_id_address_e15e2602_uniq`(`dtu_id`, `address`) USING BTREE,
  INDEX `flowmeter_valve_valve_dtu_id_f690f97a_fk_flowmeter_dtu_id`(`valve_dtu_id`) USING BTREE,
  INDEX `flowmeter_valve_dtu_id_51252e3a`(`dtu_id`) USING BTREE,
  CONSTRAINT `flowmeter_valve_meter_id_f5ca6c64_fk_flowmeter_meter_id` FOREIGN KEY (`meter_id`) REFERENCES `flowmeter_meter` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `flowmeter_valve_valve_dtu_id_f690f97a_fk_flowmeter_dtu_id` FOREIGN KEY (`valve_dtu_id`) REFERENCES `flowmeter_dtu` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 11 CHARACTER SET = utf8 COLLATE = utf8_bin ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of flowmeter_valve
-- ----------------------------
INSERT INTO `flowmeter_valve` VALUES (9, 1, 14, NULL, 11);
INSERT INTO `flowmeter_valve` VALUES (10, 3, 14, NULL, 12);

SET FOREIGN_KEY_CHECKS = 1;
