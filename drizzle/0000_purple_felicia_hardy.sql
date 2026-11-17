CREATE TABLE `cms_content_items` (
	`id` int AUTO_INCREMENT NOT NULL,
	`slug` varchar(190) NOT NULL,
	`title` varchar(220) NOT NULL,
	`contentType` enum('white-paper','newsletter','funding-opportunity','thought-leadership') NOT NULL,
	`status` enum('draft','published') NOT NULL DEFAULT 'draft',
	`excerpt` text,
	`body` text,
	`coverImageUrl` text,
	`createdByUserId` int,
	`updatedByUserId` int,
	`publishedAt` timestamp,
	`createdAt` timestamp NOT NULL DEFAULT (now()),
	`updatedAt` timestamp NOT NULL DEFAULT (now()) ON UPDATE CURRENT_TIMESTAMP,
	CONSTRAINT `cms_content_items_id` PRIMARY KEY(`id`),
	CONSTRAINT `cms_content_items_slug_unique` UNIQUE(`slug`)
);
--> statement-breakpoint
CREATE TABLE `cms_users` (
	`id` int AUTO_INCREMENT NOT NULL,
	`email` varchar(320) NOT NULL,
	`name` varchar(160) NOT NULL,
	`passwordHash` varchar(255) NOT NULL,
	`role` enum('admin','editor') NOT NULL DEFAULT 'admin',
	`isActive` int NOT NULL DEFAULT 1,
	`createdAt` timestamp NOT NULL DEFAULT (now()),
	`updatedAt` timestamp NOT NULL DEFAULT (now()) ON UPDATE CURRENT_TIMESTAMP,
	`lastSignedIn` timestamp,
	CONSTRAINT `cms_users_id` PRIMARY KEY(`id`),
	CONSTRAINT `cms_users_email_unique` UNIQUE(`email`)
);
--> statement-breakpoint
CREATE TABLE `users` (
	`id` int AUTO_INCREMENT NOT NULL,
	`openId` varchar(64) NOT NULL,
	`name` text,
	`email` varchar(320),
	`loginMethod` varchar(64),
	`role` enum('user','admin') NOT NULL DEFAULT 'user',
	`createdAt` timestamp NOT NULL DEFAULT (now()),
	`updatedAt` timestamp NOT NULL DEFAULT (now()) ON UPDATE CURRENT_TIMESTAMP,
	`lastSignedIn` timestamp NOT NULL DEFAULT (now()),
	CONSTRAINT `users_id` PRIMARY KEY(`id`),
	CONSTRAINT `users_openId_unique` UNIQUE(`openId`)
);
